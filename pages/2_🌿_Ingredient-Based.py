import xml.sax
import xml.sax.saxutils
import pandas as pd
import numpy as np
import streamlit as st
import requests
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
from streamlit_extras.metric_cards import style_metric_cards
from streamlit_extras.stylable_container import stylable_container
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from googleapiclient.discovery import build



st.set_page_config(page_title="Ingredient-Based  | GastroMiuul", page_icon="🌿")


@st.cache_data  # 👈 Add the caching decorator
def load_data(url):
    df = pd.read_csv(url)
    return df


# ---- Data ---- #
df = load_data("C:/Users/remre/OneDrive/Belgeler/GitHub/test/GastroMiuul/datasets/ib4.csv")
# df[df["NAME"].str.contains('SPICY SWEET ')]
# df[df["NAME"] == "VEGETARIAN SWEDISH MEATBALLS"]
# df = df.loc[df["NAME"] != "SPICY SWEET ONION RINGS"]
# df = df.loc[df["NAME"] != "TOTALLY TEMPESTUOUS TATER TOTS"]
# df = df.loc[df["NAME"] != "VEGETARIAN SWEDISH MEATBALLS"]


pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1500)
df = df.applymap(lambda x: str(x).lower())
df.columns = [col.lower() for col in df.columns]

ingredients = ["chicken", "beef", "pork", "lamb", "turkey", "duck", "veal", "bacon", "ham", "sausage",
               "salmon", "tuna", "shrimp", "lobster", "crab", "cod", "mackerel", "trout", "oyster", "clam",
               "tomato", "onion", "garlic", "bell pepper", "broccoli", "carrot", "spinach",
               "lettuce", "cabbage", "mushroom", "green beans", "peas", "corn", "zucchini",
               "eggplant", "cucumber", "celery", "kale", "brussels sprouts", "cauliflower",
               "asparagus", "beet", "radish", "leek",
               "apple", "banana", "orange", "strawberry", "blueberry", "raspberry", "kiwi",
               "mango", "pineapple", "grape", "watermelon", "peach", "pear", "plum", "pomegranate",
               "fig", "lemon", "lime", "cherry", "blackberry",
               "rice", "pasta", "potato", "bread", "quinoa", "oats", "barley", "cornmeal",
               "whole wheat", "rye", "buckwheat", "couscous",
               "milk", "cream", "yogurt", "cheese", "butter", "ghee", "almond milk",
               "soy milk", "oat milk", "cashew milk", "feta", "parmesan", "cheddar",
               "almond", "walnut", "cashew", "peanut", "sesame seed", "sunflower seed",
               "pumpkin seed", "chia seed", "flaxseed", "pecan", "macadamia", "hazelnut",
               "pepper", "salt", "sugar", "cinnamon", "chili", "rosemary", "basil",
               "oregano", "parsley", "cilantro", "thyme", "curry powder", "ginger",
               "turmeric", "coriander", "cumin", "paprika", "cardamom", "cloves", "nutmeg", "saffron",
               "olive oil", "soy sauce", "vinegar", "honey", "maple syrup", "sesame oil",
               "coconut oil", "mustard", "ketchup", "mayonnaise", "hot sauce", "peanut butter",
               "wasabi", "teriyaki sauce", "BBQ sauce", "salsa",
               "tea", "coffee", "wine", "beer", "soda", "juice",
               "black beans", "lentils", "chickpeas", "green lentils", "red kidney beans",
               "white beans", "soybeans", "mung beans", "peanuts", "fava beans", "lima beans",
               "tofu", "tempeh", "seitan", "edamame", "textured vegetable protein", "soy chunks",
               "chocolate", "vanilla", "gelatin", "marshmallow", "caramel", "cookie",
               "cake", "brownie", "pie", "ice cream"]
sorted_ingredients = sorted(ingredients)


def food_recipes_recommender_only(dataframe, colname, inputs):
    # girilen liste içindeki ürünlerin olduğu tarifleri getirir.
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(dataframe[colname])
    # girilen input için matrix
    input_tfidf = tfidf.transform(inputs)
    # iki matris için benzerlik hesabı
    cosine_sim = cosine_similarity(tfidf_matrix, input_tfidf)
    # cosine sim ndarray veriyor bunu df yapalım.
    cosine_sim_df = pd.DataFrame(cosine_sim, columns=inputs)
    #  malzemenin de bulunduğu tarifleri seçtiğinden emin ol.
    cosine_sim_df = cosine_sim_df[~(cosine_sim_df == 0).any(axis=1)]

    # girilen malzeme sayısı kadar sütun var, her satırın toplamı bize skor verecek
    row_sum = np.sum(cosine_sim_df, axis=1)
    row_sum_dataframe = pd.DataFrame(row_sum, columns=["scores"])
    # score'u yüksek ilk 5 indexi seç
    top_5_index = row_sum_dataframe.sort_values("scores", ascending=False)[0:5].index
    recommended_recipes = dataframe.iloc[top_5_index].sort_values("calories")
    return recommended_recipes, cosine_sim_df


def food_recipes_recommender(dataframe, colname, inputs):
    # tfidf puanı yüksekliğine göre, bazen girilen malzemelerden birinin
    # veya bir kaçının olmadığı yemeği de önerebilir.
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(dataframe[colname])
    # girilen input için matrix
    input_tfidf = tfidf.transform(inputs)
    # iki matris için benzerlik hesabı
    cosine_sim = cosine_similarity(tfidf_matrix, input_tfidf)

    # girilen malzeme sayısı kadar sütun var, her satırın toplamı bize skor verecek
    row_sum = np.sum(cosine_sim, axis=1)
    row_sum_dataframe = pd.DataFrame(row_sum, columns=["scores"])
    # score'u yüksek ilk 5 indexi seç
    top_5_index = row_sum_dataframe.sort_values("scores", ascending=False)[0:5].index
    recommended_recipes = dataframe.iloc[top_5_index].sort_values("calories")
    return recommended_recipes, cosine_sim



def format_word(word_or_phrase):
    if ' ' in word_or_phrase:
        # Kelime öbeği içeriyorsa, kelimeler arasına artı işareti ekle
        formatted_word = '+'.join(word_or_phrase.split())
    else:
        # Tek bir kelimeyse, aynı kelimeyi döndür
        formatted_word = word_or_phrase
    return formatted_word


# görseller için fonk ve api idleri
def google_image_search(query, api_key, cse_id, num=1):
   service = build("customsearch", "v1", developerKey=api_key)
   res = service.cse().list(q=query, cx=cse_id, searchType='image', num=num).execute()
   return res['items'][0]['link']

# api_key =  # get your own api_key if you want to show the recipes pictures
# cse_id =  # get your own cse_id if you want to show the recipes pictures


# ---- Main Screen ---- #


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


lottie_coding2 = load_lottieurl("https://lottie.host/cc7f103d-8c61-410d-b2c3-dd12baca3c5e/NSfWO4QLy3.json")
st.write("# Be Proud of Preventing Product Waste!")

col1, col2, col3 = st.columns((1, 4, 1))
with col2:
    st_lottie(lottie_coding2)

st.subheader("Share your ingredients, and let us inspire you with recipes tailored just for you!")
st.write("Now, can you please type the ingredients that you really want to use? What products do you have?")

secenek = ["NO", "YES"]
kesin_kullanilmali_y_n = st.radio("If you have products that you **absolutely want to use** or **products that are close to their expiration date**, please click on '**YES**' option and enter those items in the first box.", secenek)

# input1 = ["beef", "carrot", "onion", "potato"]

if kesin_kullanilmali_y_n == "NO":
    input1 = st.multiselect('', sorted_ingredients, placeholder="Please type here what you have...", key=1)
    st.write("##")
    with stylable_container(
            key="white_button",
            css_styles=
            """
            button {background-color: #FFFFFF;
            color: #FFBC42;
            border-radius: 5px;
            }""",
    ):
        recommendation_button = st.button('**Show Me Recipes**')
        if recommendation_button:
            recommended_recipes1, cosine_sim_df1 = food_recipes_recommender_only(df, "ingredients", input1)

            # (BS) Onerilen yemekleri begenenelerin begendigi diger yemekler icin id de ekledim
            id = recommended_recipes1["id"].tolist()

            name = recommended_recipes1["name"].tolist()
            ingredients = recommended_recipes1["ingredients_raw_str"].tolist()
            steps = recommended_recipes1["steps"].tolist()
            allergen = recommended_recipes1["because_of_allergen"].tolist()
            calories = recommended_recipes1["calories"].tolist()
            carbon = recommended_recipes1["carbon_emission"].tolist()
            recommended_recipes1['missing ingredients'] = recommended_recipes1['ingredients']. \
                apply(lambda x: [ingredient for ingredient in x.split(', ') if ingredient not in input1])
            missing_ingredients = recommended_recipes1['missing ingredients'] = \
                recommended_recipes1['missing ingredients'].apply(
                    lambda x: ', '.join(x)).tolist()
            eksik_malzeme = recommended_recipes1['ingredients']. \
                apply(lambda x: [ingredient for ingredient in x.split(', ') if ingredient not in input1])

            # (BS) Bu uc satirin amaci search_terms degiskeninin icindeki gozlemlerin tipini listeye ekleyip
            # ardindan search_terms listesindeki eleman sayisini (num_search_terms) bulmaktir. Yeni degisken urettik
            import ast
            df['search_terms'] = df['search_terms'].apply(lambda x: ast.literal_eval(x))
            df["num_search_terms"] = df["search_terms"].apply(lambda x: len(x))

            # (BS) bu satir ile search_term_id listesi olusturduk boylece bu liste ile asagida benzer urunler
            # karsilastirmasi yapacagiz
            search_term_id = recommended_recipes1["search_term_id"].tolist()

            for a in range(0, 5):
                st.subheader(f':red[{name[a].upper()}]')
                # if you have "api_key, cse_id" you can type them here:
                # image_url1 = google_image_search(name[a], api_key, cse_id)
                # print(image_url1)
                # st.image(image_url1, caption=name[a], use_column_width="auto")
                tab1, tab2, tab3, tab4 = st.tabs(["Details", "Ingredients", "Recipe", "Missing Ingredients"])
                with tab1:
                    col1, col2 = st.columns((0.3, 5))
                    with col1:
                        st.image("Görseller_Streamlit/icons/calori1.jpg")
                    with col2:
                        st.write(f"**Calories**: {calories[a]}")
                    col1, col2 = st.columns((0.3, 5))
                    with col1:
                        st.image("Görseller_Streamlit/icons/carbon_footprint.jpg")
                    with col2:
                        st.write(f"**Carbon Footprint**: {carbon[a]}")
                    col1, col2 = st.columns((0.3, 5))
                    with col1:
                        st.image("Görseller_Streamlit/icons/allergen1.jpg")
                    with col2:
                        st.write(f"**Allergens**: {allergen[a].capitalize()}")
                with tab2:
                    st.write(ingredients[a].lower().capitalize())
                with tab3:
                    st.write(steps[a].capitalize())
                with tab4:
                    st.write(f"**Missing Ingredients**: {missing_ingredients[a].capitalize()}")
                    eksik_malzeme_listesi = eksik_malzeme.iloc[a]
                    with st.expander("**👇 Click and Buy The Missing Ingredients**"):
                        mal, link = st.columns((0.5, 4))
                        with mal:
                            for malzeme in eksik_malzeme_listesi:
                                url = f"https://www.amazon.de/s?k={format_word(malzeme)}"
                                st.write("[Buy Now](%s)" % url)
                        with link:
                            for malzeme in eksik_malzeme_listesi:
                                malzeme_buyuk = malzeme.capitalize()
                                st.write(malzeme_buyuk)
                st.write("##")

                # (BS) bu bolume bir streamlit infosu eklendi. Burada eger onerilen yemegin baska yemeklerle
                # search_term benzerligi varsa gosterilecektir. Onerilen bu urunu begenen kullanicilar bu yemegi de
                # begendi mantigi

                # (BS) Onerilen tarif ile search_term_id no su ayni olan, icerisindeki search_terms sayisi (num_search_terms)
                # 2 den buyuk olan ve yemegin id numarasi oneri sisteminin id numarasindan farkli olan butun yemekleri
                # filtreledik
                filtered_df = df[(df["search_term_id"] == search_term_id[a])
                                 & (df["num_search_terms"] > 2)
                                 & (df["id"] != id[a])]

                # (BS) filtered_df icerisinden rasgele bir urun secilecegi icin random i import ettik
                import random

                # (BS) Rastgele bir satır seçin
                if len(filtered_df) >= 1:
                    random_index = random.randint(0, len(filtered_df) - 1)
                    selected_row = filtered_df.iloc[[random_index]]
                else:
                    selected_row = pd.DataFrame
                # (BS) Bu blokta info tanimlandi ve bir expander ile eger varsa onerilen yemegi sevenlerin diger
                # inceledigi tarifleri listeledik
                if not selected_row.empty:
                    st.info(f'Those who enjoyed this dish also liked the **_{selected_row["name"].iloc[0].capitalize()}_** dish.')
                    with st.expander("Click for The Recipe"):
                        st.subheader(f':red[{selected_row["name"].iloc[0].upper()}]')
                        tab1, tab2, tab3 = st.tabs(["Details", "Ingredients", "Recipe"])
                        with tab1:
                            col1, col2 = st.columns((0.3, 5))
                            with col1:
                                st.image("Görseller_Streamlit/icons/calori1.jpg")
                            with col2:
                                st.write(f'**Calories**: {selected_row["calories"].iloc[0].capitalize()}')
                            col1, col2 = st.columns((0.3, 5))
                            with col1:
                                st.image("Görseller_Streamlit/icons/carbon_footprint.jpg")
                            with col2:
                                st.write(f'**Carbon Footprint**: {selected_row["carbon_emission"].iloc[0].capitalize()}')
                            col1, col2 = st.columns((0.3, 5))
                            with col1:
                                st.image("Görseller_Streamlit/icons/allergen1.jpg")
                            with col2:
                                st.write(f'**Allergens**: {selected_row["because_of_allergen"].iloc[0].capitalize()}')
                        with tab2:
                            st.write(selected_row["ingredients_raw_str"].iloc[0].capitalize().replace('[', '').replace(']','').replace('"', ''))
                        with tab3:
                            st.write(selected_row["steps"].iloc[0].capitalize().replace('[', '').replace(']', '').replace('"', '').replace("'", '').replace(',', ''))
                        st.write("##")
                    selected_row = selected_row.iloc[0:0]





else:
    input1 = st.multiselect('', sorted_ingredients, placeholder="The products you definitely want to use", key=1)
    input2 = st.multiselect('', sorted_ingredients, placeholder="Other ingredients", key=2)
    st.write("##")
    with stylable_container(
            key="white_button",
            css_styles=
            """
            button {background-color: #FFFFFF;
            color: #FFBC42;
            border-radius: 5px;
            }""",
    ):
        recommendation_button = st.button('**Show Me Recipes**')
        if recommendation_button:
            df_filtered = df[df['ingredients'].apply(lambda item: all(key in item for key in input1))]
            recommended_recipes2, cosine_sim2 = food_recipes_recommender_only(df_filtered, "ingredients", input2)
            # (BS)
            id = recommended_recipes2["id"].tolist()

            name = recommended_recipes2["name"].tolist()
            ingredients = recommended_recipes2["ingredients_raw_str"].tolist()
            steps = recommended_recipes2["steps"].tolist()
            allergen = recommended_recipes2["because_of_allergen"].tolist()
            calories = recommended_recipes2["calories"].tolist()
            carbon = recommended_recipes2["carbon_emission"].tolist()
            input3 = input1 + input2
            recommended_recipes2['missing ingredients'] = recommended_recipes2['ingredients']. \
                apply(lambda x: [ingredient for ingredient in x.split(', ') if ingredient not in input3])
            missing_ingredients = recommended_recipes2['missing ingredients'] = recommended_recipes2[
                'missing ingredients'].apply(
                lambda x: ', '.join(x)).tolist()
            eksik_malzeme = recommended_recipes2['ingredients']. \
                apply(lambda x: [ingredient for ingredient in x.split(', ') if ingredient not in input3])

            # (BS)
            import ast
            df['search_terms'] = df['search_terms'].apply(lambda x: ast.literal_eval(x))
            df["num_search_terms"] = df["search_terms"].apply(lambda x: len(x))

            # (BS)
            search_term_id = recommended_recipes2["search_term_id"].tolist()

            for a in range(0, 5):
                st.subheader(f':red[{name[a].upper()}]')

                # if you have "api_key, cse_id" you can type them here:
                # image_url1 = google_image_search(name[a], api_key, cse_id)
                # print(image_url1)
                # st.image(image_url1, caption=name[a], use_column_width="auto")
                tab1, tab2, tab3, tab4 = st.tabs(["Details", "Ingredients", "Recipe", "Missing Ingredients"])
                with tab1:
                    col1, col2 = st.columns((0.3, 5))
                    with col1:
                        st.image("Görseller_Streamlit/icons/calori1.jpg")
                    with col2:
                        st.write(f"**Calories**: {calories[a]}")
                    col1, col2 = st.columns((0.3, 5))
                    with col1:
                        st.image("Görseller_Streamlit/icons/carbon_footprint.jpg")
                    with col2:
                        st.write(f"**Carbon Footprint**: {carbon[a]}")
                    col1, col2 = st.columns((0.3, 5))
                    with col1:
                        st.image("Görseller_Streamlit/icons/allergen1.jpg")
                    with col2:
                        st.write(f"**Allergens**: {allergen[a].capitalize()}")
                with tab2:
                    st.write(ingredients[a].lower().capitalize())
                with tab3:
                    st.write(steps[a].capitalize())
                with tab4:
                    st.write(f"**Missing Ingredients**: {missing_ingredients[a].capitalize()}")
                    eksik_malzeme_listesi = eksik_malzeme.iloc[a]
                    with st.expander("**👇 Click and Buy The Missing Ingredients**"):
                        mal, link = st.columns((0.5, 4))
                        with mal:
                            for malzeme in eksik_malzeme_listesi:
                                url = f"https://www.amazon.de/s?k={format_word(malzeme)}"
                                st.write("[Buy Now](%s)" % url)
                        with link:
                            for malzeme in eksik_malzeme_listesi:
                                malzeme_buyuk = malzeme.capitalize()
                                st.write(malzeme_buyuk)
                st.write("##")



                # (BS)
                filtered_df = df[(df["search_term_id"] == search_term_id[a])
                                 & (df["num_search_terms"] > 2)
                                 & (df["id"] != id[a])]

                import random

                # Rastgele bir satır seçin
                if len(filtered_df) >= 1:
                    random_index = random.randint(0, len(filtered_df) - 1)
                    selected_row = filtered_df.iloc[[random_index]]
                else:
                    selected_row = pd.DataFrame
                # pd.isna(selected_row["name"].iloc[0])
                if not selected_row.empty:
                    st.info(
                        f'Those who enjoyed this dish also liked the **_{selected_row["name"].iloc[0].capitalize()}_** dish.')
                    with st.expander("Click for The Recipe"):
                        st.subheader(f':red[{selected_row["name"].iloc[0].upper()}]')
                        tab1, tab2, tab3 = st.tabs(
                            ["Details", "Ingredients", "Recipe"])
                        with tab1:
                            col1, col2 = st.columns((0.3, 5))
                            with col1:
                                st.image('Görseller_Streamlit/icons/calori1.jpg')
                            with col2:
                                st.write(f'**Calories**: {selected_row["calories"].iloc[0].capitalize()}')
                            col1, col2 = st.columns((0.3, 5))
                            with col1:
                                st.image("Görseller_Streamlit/icons/carbon_footprint.jpg")
                            with col2:
                                st.write(f'**Carbon Footprint**: {selected_row["carbon_emission"].iloc[0].capitalize()}')
                            col1, col2 = st.columns((0.3, 5))
                            with col1:
                                st.image("Görseller_Streamlit/icons/allergen1.jpg")
                            with col2:
                                st.write(f'**Allergens**: {selected_row["because_of_allergen"].iloc[0].capitalize()}')
                        with tab2:
                            st.write(
                                selected_row["ingredients_raw_str"].iloc[0].capitalize().replace('[', '').replace(']',
                                                                                                                  '').replace(
                                    '"', ''))
                        with tab3:
                            st.write(
                                selected_row["steps"].iloc[0].capitalize().replace('[', '').replace(']', '').replace(
                                    '"',
                                    '').replace(
                                    "'", '').replace(',', ''))
                        st.write("##")
                    selected_row = selected_row.iloc[0:0]