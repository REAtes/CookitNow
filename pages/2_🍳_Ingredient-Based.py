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

st.set_page_config(page_title="Malzemeye Göre Tarifler  | GastroMiuul", page_icon="🍳")


# ---- Main Screen  ---- #


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


lottie_coding2 = load_lottieurl("https://lottie.host/cc7f103d-8c61-410d-b2c3-dd12baca3c5e/NSfWO4QLy3.json")
st.write('# Tell Us What You Have, We\'ll Tell You What to Make!')

col1, col2, col3 = st.columns((1, 4, 1))
with col2:
    st_lottie(lottie_coding2)
st.subheader('Be Proud of Preventing Product Waste!')

#seçim yapılacak malzeme listesinin tamamı

ingredients = ["chicken", "beef", "pork", "lamb", "turkey", "duck", "veal", "bacon", "ham", "sausage"
         "salmon", "tuna", "shrimp", "lobster", "crab", "cod", "mackerel", "trout", "oyster", "clam"
         "tomato", "onion", "garlic", "bell pepper", "broccoli", "carrot", "spinach",
         "lettuce", "cabbage", "mushroom", "green beans", "peas", "corn", "zucchini",
         "eggplant", "cucumber", "celery", "kale", "brussels sprouts", "cauliflower",
         "asparagus", "beet", "radish", "leek"
         "apple", "banana", "orange", "strawberry", "blueberry", "raspberry", "kiwi",
         "mango", "pineapple", "grape", "watermelon", "peach", "pear", "plum", "pomegranate",
         "fig", "lemon", "lime", "cherry", "blackberry"
         "rice", "pasta", "potato", "bread", "quinoa", "oats", "barley", "cornmeal",
         "whole wheat", "rye", "buckwheat", "couscous"
         "milk", "cream", "yogurt", "cheese", "butter", "ghee", "almond milk",
         "soy milk", "oat milk", "cashew milk", "feta", "parmesan", "cheddar"
         "almond", "walnut", "cashew", "peanut", "sesame seed", "sunflower seed",
         "pumpkin seed", "chia seed", "flaxseed", "pecan", "macadamia", "hazelnut"
         "pepper", "salt", "sugar", "cinnamon", "chili", "rosemary", "basil",
         "oregano", "parsley", "cilantro", "thyme", "curry powder", "ginger",
         "turmeric", "coriander", "cumin", "paprika", "cardamom", "cloves", "nutmeg", "saffron"
         "olive oil", "soy sauce", "vinegar", "honey", "maple syrup", "sesame oil",
         "coconut oil", "mustard", "ketchup", "mayonnaise", "hot sauce", "peanut butter",
         "wasabi", "teriyaki sauce", "BBQ sauce", "salsa"
         "tea", "coffee", "wine", "beer", "soda", "juice"
         "black beans", "lentils", "chickpeas", "green lentils", "red kidney beans",
         "white beans", "soybeans", "mung beans", "peanuts", "fava beans", "lima beans"
         "tofu", "tempeh", "seitan", "edamame", "textured vegetable protein", "soy chunks",
         "chocolate", "vanilla", "gelatin", "marshmallow", "caramel", "cookie",
         "cake", "brownie", "pie", "ice cream"]
with st.container():
    st.write("Now, can you please type the ingredients you have? What products do you have?")
    inputs = st.multiselect('', ingredients, placeholder="type here")

#aşağıdaki ufak liste de kullanılabilir.

    #st.multiselect('',
    #           [
#         "chicken", "beef", "pork", "lamb", "turkey", "duck", "veal", "bacon", "ham", "sausage"
#         "salmon", "tuna", "shrimp", "lobster", "crab", "cod", "mackerel", "trout", "oyster", "clam"
#         "tomato", "onion", "garlic", "bell pepper", "broccoli", "carrot", "spinach",
#         "lettuce", "cabbage", "mushroom", "green beans", "peas", "corn", "zucchini",
#         "eggplant", "cucumber", "celery", "kale", "brussels sprouts", "cauliflower",
#         "asparagus", "beet", "radish", "leek"
#         "apple", "banana", "orange", "strawberry", "blueberry", "raspberry", "kiwi",
#         "mango", "pineapple", "grape", "watermelon", "peach", "pear", "plum", "pomegranate",
#         "fig", "lemon", "lime", "cherry", "blackberry"
#         "rice", "pasta", "potato", "bread", "quinoa", "oats", "barley", "cornmeal",
#         "whole wheat", "rye", "buckwheat", "couscous"
#         "milk", "cream", "yogurt", "cheese", "butter", "ghee", "almond milk",
#         "soy milk", "oat milk", "cashew milk", "feta", "parmesan", "cheddar"
#         "almond", "walnut", "cashew", "peanut", "sesame seed", "sunflower seed",
#         "pumpkin seed", "chia seed", "flaxseed", "pecan", "macadamia", "hazelnut"
#         "pepper", "salt", "sugar", "cinnamon", "chili", "rosemary", "basil",
#         "oregano", "parsley", "cilantro", "thyme", "curry powder", "ginger",
#         "turmeric", "coriander", "cumin", "paprika", "cardamom", "cloves", "nutmeg", "saffron"
#         "olive oil", "soy sauce", "vinegar", "honey", "maple syrup", "sesame oil",
#         "coconut oil", "mustard", "ketchup", "mayonnaise", "hot sauce", "peanut butter",
#         "wasabi", "teriyaki sauce", "BBQ sauce", "salsa"
#         "tea", "coffee", "wine", "beer", "soda", "juice"
#         "black beans", "lentils", "chickpeas", "green lentils", "red kidney beans",
#         "white beans", "soybeans", "mung beans", "peanuts", "fava beans", "lima beans"
#         "tofu", "tempeh", "seitan", "edamame", "textured vegetable protein", "soy chunks",
#         "chocolate", "vanilla", "gelatin", "marshmallow", "caramel", "cookie",
#         "cake", "brownie", "pie", "ice cream"]
#
#
# print(ingredients)
    #            ])
    #["Domates", "Soğan", "Sarımsak", "Biber", "Tavuk", "Kırmızı Et", "Pirinç", "Makarna", "Patates",
     #"Havuç", "Ispanak", "Brokoli", "Bezelye", "Mantar", "Kabak", "Kırmızı Mercimek", "Nohut", "Yoğurt",
    #"Peynir", "Zeytin", "Zeytinyağı", "Tereyağı", "Süt", "Un", "Yumurta", "Maydanoz", "Dereotu", "Nane",
    # "Kekik", "Tarçın", "Zencefil", "Kırmızı Pul Biber", "Kekik", "Krema", "Limon", "Limon Suyu", "Elma",
    # "Armut", "Çilek", "Üzüm", "Portakal", "Muz", "Ananas", "Avokado", "Karpuz", "Kavun", "Badem",
    # "Ceviz", "Fındık", "Susam", "Ayçiçek Yağı", "Bal", "Tahin", "Hardal", "Mayonez", "Ketçap", "Salça",
    # "Balık", "Karides", "Midye", "Kalamar", "Tavuk Göğsü", "Pastirma", "Salam", "Sucuk", "Sosis",
    # "Zeytin Ezmesi", "Süzme Yoğurt", "Kıvırcık", "Roka", "Lahana", "Karnabahar", "Turşu", "Salatalık",
    # "Kırmızı Lahana", "Beyaz Lahana", "Brokoli", "Kabak", "Brüksel Lahanası", "Patlıcan", "Enginar",
    # "Bamya", "Kırmızı Biber", "Acı Biber", "Enginar", "Mısır", "Bezelye", "Yeşil Fasulye", "Kuşkonmaz",
    # "Sarımsak", "Kereviz", "Havuç", "Patates", "Taze Soğan", "Roka", "Marul", "Semizotu", "Dereotu",
    # "Taze Nane", "Kıvırcık Maydanoz", "Ruşeym", "Quinoa", "Kinoa", "Bulgur", "Couscous"
    # ]

df = pd.read_csv("recipes_with_search.csv")
df = df.applymap(lambda x: str(x).lower())
df.columns = [col.lower() for col in df.columns]
main_cols = ['name', 'ingredients', 'ingredients_raw_str', 'steps', 'calories',
              "because_of_allergen", 'carbon_emission', 'tags', 'search_terms']
df = df[main_cols]

def food_recipes_recommender(dataframe, colname, inputs):
    #df içinde nan yazanları boş değerle değiştirir
    dataframe[colname] = dataframe[colname].fillna('')
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(dataframe[colname])
    #girilen input için matrix
    input_tfidf = tfidf.transform(inputs)
    #iki matris için benzerlik hesabı
    cosine_sim = cosine_similarity(tfidf_matrix, input_tfidf)
    #cosine sim ndarray veriyor bunu df yapalım.
    cosine_sim_df = pd.DataFrame(cosine_sim, columns=inputs)
    #her malzemenin de bulunduğu tarifleri seçtiğinden emin ol.
    cosine_sim_df = cosine_sim_df[~(cosine_sim_df == 0).any(axis=1)]

    #girilen malzeme sayısı kadar sütun var, her satırın toplamı bize skor verecek
    row_sum = np.sum(cosine_sim_df, axis=1)
    row_sum_dataframe = pd.DataFrame(row_sum, columns=["scores"])
    #score'u yüksek ilk 5 indexi seç
    top_5_index = row_sum_dataframe.sort_values("scores", ascending=False)[0:5].index
    recommended_recipes = dataframe.iloc[top_5_index]#.sort_values("calories")
    return recommended_recipes, cosine_sim_df

#def google_image_search(query, api_key, cse_id, num=1):
#    service = build("customsearch", "v1", developerKey=api_key)
#    res = service.cse().list(q=query, cx=cse_id, searchType='image', num=num).execute()
#    return res['items'][0]['link']

#api_key = "AIzaSyDld5RyAGvlO3KNzHLP3R2CCZV_Uz8cYbg"
#cse_id = "c42eb241a8bb244c0"

with stylable_container(
                            key="white_button",
                            css_styles="""
                                    button {
                                        background-color: #FFFFFF;
                                        color: #FFBC42;
                                        border-radius: 5px;
                                    }
                                    """,
                    ):
    recommendation_button = st.button('**Give Recommendation**')

if recommendation_button:
    recommended_recipes, cosine_sim_df = food_recipes_recommender(df, "ingredients", inputs)

    name = recommended_recipes["name"].tolist()
    ingredients = recommended_recipes["ingredients_raw_str"].tolist()
    steps = recommended_recipes["steps"].tolist()
    allergen = recommended_recipes["because_of_allergen"].tolist()
    calories = recommended_recipes["calories"].tolist()
    carbon = recommended_recipes["carbon_emission"].tolist()
    col1, col2, col3 = st.columns((1, 3, 1))
    with col2:
        for a in range(0,5):
            st.subheader(name[a].title())
            #image_url1 = google_image_search(name[a], api_key, cse_id)
            #print(image_url1)
            #st.image(image_url1, caption=name[a], use_column_width="auto")
            tab1, tab2, tab3 = st.tabs(["Ingredients", "Cooking Steps", "Calori & Carbon Footprint & Allergen"])
            with tab1:
                st.write(ingredients[a])
            with tab2:
                st.write(steps[a])
            with tab3:
                col1, col2 = st.columns((0.3, 5))
                with col1:
                    st.image("GastroMiuul/Görseller_Streamlit/calori1.jpg")
                with col2:
                    st.write(f"Calori: {calories[a]} cal")
                col1, col2 = st.columns((0.3, 5))
                with col1:
                    st.image("GastroMiuul/Görseller_Streamlit/carbon_footprint.jpg")
                with col2:
                    st.write(f"Carbon Footprint: {carbon[a]} gr")
                col1, col2 = st.columns((0.3, 5))
                with col1:
                    st.image("GastroMiuul/Görseller_Streamlit/allergen1.jpg")
                with col2:
                    st.write(f"Allergen Item: {allergen[a]}")


#------Görsel ekleme------#
#from googleapiclient.discovery import build
#def google_image_search(query, api_key, cse_id, num=1):
#    service = build("customsearch", "v1", developerKey=api_key)
#    res = service.cse().list(q=query, cx=cse_id, searchType='image', num=num).execute()
#    return res['items'][0]['link']

# Google search için api ve cse id'lerim.
#api_key = "AIzaSyDld5RyAGvlO3KNzHLP3R2CCZV_Uz8cYbg"
#cse_id = "c42eb241a8bb244c0"
#buraya seçilen yemeğin ismi gelecek
#query = "kuru fasülye"
#Fonksiyon görselin url'sini çekiyor..
#image_url1 = google_image_search(query1, api_key, cse_id)
#print(image_url1)
