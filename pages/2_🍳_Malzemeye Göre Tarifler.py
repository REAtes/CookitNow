import pandas as pd
import numpy as np
import streamlit as st
import requests
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
from streamlit_extras.metric_cards import style_metric_cards
from streamlit_extras.stylable_container import stylable_container


st.set_page_config(page_title="Malzemeye Göre Tarifler  | GastroMiuul", page_icon="🍳")


# ---- Main Screen  ---- #

@st.cache_data
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
    st.multiselect('', ingredients, placeholder="type here")

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
    st.button('**Give Recommendation**')

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
