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

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


st.set_page_config(page_title="Ingredient-Based  | GastroMiuul", page_icon="🍳")


@st.cache_data  # 👈 Add the caching decorator
def load_data(url):
    df = pd.read_csv(url)
    return df


# ---- Data ---- #
df = load_data("C:/Users/remre/OneDrive/Belgeler/GitHub/test/GastroMiuul/datasets/ib.csv")
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


def search_item(query):
    driver = webdriver.Chrome()
    # driver.get("https://www.a101kapida.com/")  # çalıştı = by="id", value="searchbar"
    driver.get("https://www.carrefoursa.com/")  # çalıştı = by="id", value="js-site-search-input"

    search_box = driver.find_element(by="id", value="js-site-search-input")
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)

    # Tarayıcıyı kapatmadan önce kullanıcının onayını bekliyoruz
    input(f"{query} aranıyor...")
    driver.quit()


# görseller için fonk ve api idleri
# def google_image_search(query, api_key, cse_id, num=1):
#    service = build("customsearch", "v1", developerKey=api_key)
#    res = service.cse().list(q=query, cx=cse_id, searchType='image', num=num).execute()
#    return res['items'][0]['link']

# api_key = "AIzaSyDld5RyAGvlO3KNzHLP3R2CCZV_Uz8cYbg"
# cse_id = "c42eb241a8bb244c0"

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

secenek = ["No", "Yes"]
kesin_kullanilmali_y_n = st.radio("Kesinlikle bu malzemeyi kullanmam gerekiyor diyorsan YES seçeneğini seç", secenek)

input1 = ["beef", "garlic", "onion"]

if kesin_kullanilmali_y_n == "No":
    input1 = st.multiselect('', sorted_ingredients, placeholder="Kesinlikle kullanman gereken ürünler", key=1)

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

            for a in range(0, 5):
                st.subheader(f':red[{name[a].capitalize()}]')
                # image_url1 = google_image_search(name[a], api_key, cse_id)
                # print(image_url1)
                # st.image(image_url1, caption=name[a], use_column_width="auto")
                tab1, tab2, tab3, tab4 = st.tabs(["Calori & Carbon Footprint & Allergen",
                                                  "Ingredients",
                                                  "Cooking Steps",
                                                  "Missing Ingredients"])
                with tab1:
                    col1, col2 = st.columns((0.3, 5))
                    with col1:
                        st.image("Görseller_Streamlit/icons/calori1.jpg")
                    with col2:
                        st.write(f"Calori: {calories[a]}")
                    col1, col2 = st.columns((0.3, 5))
                    with col1:
                        st.image("Görseller_Streamlit/icons/carbon_footprint.jpg")
                    with col2:
                        st.write(f"Carbon Footprint: {carbon[a]}")
                    col1, col2 = st.columns((0.3, 5))
                    with col1:
                        st.image("Görseller_Streamlit/icons/allergen1.jpg")
                    with col2:
                        st.write(f"Allergen Item: {allergen[a]}")
                with tab2:
                    st.write(ingredients[a].lower().capitalize())
                with tab3:
                    st.write(steps[a].capitalize())
                with tab4:
                    st.write(missing_ingredients[a])
                st.write("##")

len(eksik_malzeme)

eksik_malzeme.iloc[4][i]

for liste in eksik_malzeme:
    for i in liste:
        driver = webdriver.Chrome()
        driver.get(f"https://www.amazon.de/s?k={eksik_malzeme.iloc[0][0]}")


url = "https://www.amazon.de/s?k={eksik_malzeme.iloc[0][0]}"
st.write("[eksik_malzeme.iloc[0][0]](%s)" % url)


else:
    input1 = st.multiselect('', sorted_ingredients, placeholder="Kesinlikle kullanman gereken ürünler", key=1)
    input2 = st.multiselect('', sorted_ingredients, placeholder="Bu ürün olsa da olur, olmasa da", key=2)

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
            name = recommended_recipes2["name"].tolist()
            ingredients = recommended_recipes2["ingredients_raw_str"].tolist()
            steps = recommended_recipes2["steps"].tolist()
            allergen = recommended_recipes2["because_of_allergen"].tolist()
            calories = recommended_recipes2["calories"].tolist()
            carbon = recommended_recipes2["carbon_emission"].tolist()
            recommended_recipes2['missing ingredients'] = recommended_recipes2['ingredients']. \
                apply(lambda x: [ingredient for ingredient in x.split(', ') if ingredient not in input1])
            missing_ingredients = recommended_recipes2['missing ingredients'] = recommended_recipes2[
                'missing ingredients'].apply(
                lambda x: ', '.join(x)).tolist()

            for a in range(0, 5):
                st.subheader(f':red[{name[a].capitalize()}]')
                # image_url1 = google_image_search(name[a], api_key, cse_id)
                # print(image_url1)
                # st.image(image_url1, caption=name[a], use_column_width="auto")
                tab1, tab2, tab3, tab4 = st.tabs(["Calori & Carbon Footprint & Allergen",
                                                  "Ingredients",
                                                  "Cooking Steps",
                                                  "Missing Ingredients"])
                with tab1:
                    col1, col2 = st.columns((0.3, 5))
                    with col1:
                        st.image("Görseller_Streamlit/icons/calori1.jpg")
                    with col2:
                        st.write(f"Calori: {calories[a]}")
                    col1, col2 = st.columns((0.3, 5))
                    with col1:
                        st.image("Görseller_Streamlit/icons/carbon_footprint.jpg")
                    with col2:
                        st.write(f"Carbon Footprint: {carbon[a]}")
                    col1, col2 = st.columns((0.3, 5))
                    with col1:
                        st.image("Görseller_Streamlit/icons/allergen1.jpg")
                    with col2:
                        st.write(f"Allergen Item: {allergen[a]}")
                with tab2:
                    st.write(ingredients[a].lower().capitalize())
                with tab3:
                    st.write(steps[a].capitalize())
                with tab4:
                    st.write(missing_ingredients[a])
                st.write("##")