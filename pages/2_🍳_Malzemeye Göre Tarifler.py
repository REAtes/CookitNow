import pandas as pd
import numpy as np
import streamlit as st
import requests
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
from streamlit_extras.metric_cards import style_metric_cards

st.set_page_config(page_title="Malzemeye Göre Tarifler  | GastroMiuul", page_icon="🍳")


# ---- Main Screen  ---- #


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


lottie_coding2 = load_lottieurl("https://lottie.host/cc7f103d-8c61-410d-b2c3-dd12baca3c5e/NSfWO4QLy3.json")
st.write('# Elindeki Malzemeyi Söyle, Sana Ne Yapacağını Söyleyelim!')

col1, col2, col3 = st.columns((1,4,1))
with col2:
    st_lottie(lottie_coding2)
st.subheader('Ürün israfının önüne geçtiğin için kendinle gurur duymalısın!')
#seçim yapılacak malzeme listesinin tamamı
df_ingredients = pd.read_csv("ingredients.csv")
ingredients = df_ingredients["ingredients"].tolist()

with st.container():
    st.write(
        """
        Şimdi bize elindeki malzemeler hakkında bilgi verir misin, hangi ürünler var?
        """)
    st.multiselect('', ingredients)


#aşağıdaki ufak liste de kullanılabilir.

    #st.multiselect('',
    #           ["Tomato", "Onion", "Garlic", "Pepper", "Chicken", "Red Meat", "Rice", "Pasta", "Potato",
    #            "Carrot", "Spinach", "Broccoli", "Peas", "Mushroom", "Zucchini", "Red Lentil", "Chickpea", "Yogurt",
    #            "Cheese", "Olive", "Olive Oil", "Butter", "Milk", "Flour", "Egg", "Parsley", "Dill", "Mint",
    #            "Cinnamon", "Ginger", "Red Pepper Flakes", "Thyme", "Cream", "Lemon", "Lemon Juice", "Apple",
    #            "Pear", "Strawberry", "Grape", "Orange", "Banana", "Pineapple", "Avocado", "Watermelon", "Melon", "Almond",
    #            "Walnut", "Hazelnut", "Sesame", "Sunflower Oil", "Honey", "Tahini", "Mustard", "Mayonnaise", "Ketchup", "Tomato Paste",
    #            "Fish", "Shrimp", "Mussel", "Squid", "Chicken Breast", "Pastrami", "Salami", "Sausage", "Frankfurter",
    #            "Olive Paste", "Strained Yogurt", "Lettuce", "Rocket", "Cabbage", "Cauliflower", "Pickle", "Cucumber",
    #            "Red Cabbage", "White Cabbage", "Broccoli", "Zucchini", "Brussels Sprouts", "Eggplant", "Artichoke",
    #            "Okra", "Red Pepper", "Hot Pepper", "Corn", "Peas", "Green Bean", "Asparagus",
    #            "Garlic", "Celery", "Carrot", "Potato", "Green Onion", "Rocket", "Lettuce", "Purslane", "Dill",
    #            "Fresh Mint", "Curled Parsley", "Wheat Germ", "Quinoa", "Bulgur", "Couscous"
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

st.button('Gelsin Tarifler')

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
