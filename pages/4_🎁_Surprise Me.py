import pandas as pd
import numpy as np
import streamlit as st
import requests
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
from streamlit_extras.metric_cards import style_metric_cards
from streamlit_extras.switch_page_button import switch_page
from streamlit_card import card
from streamlit_extras.stylable_container import stylable_container

from googleapiclient.discovery import build
import random

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 300)
pd.set_option('display.max_rows', None)

st.set_page_config(page_title="Surprise Me | GastroMiuul", page_icon="🎁")


# ---- Main Screen  ---- #
#import streamlit as st

#on = st.toggle('Activate feature')

#if on:
#    st.write('Feature activated!')
@st.cache_data
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding4 = load_lottieurl("https://lottie.host/68d7a267-b8e5-4784-af12-ebc654174f85/KvYLzoHX4M.json")

st.write('# Surprise!')
col1, col2, col3 = st.columns((1,2,1))
with col2:
    st_lottie(lottie_coding4)

#bu sayfa için surprise me adında bir csv yaptım. içinde sadece aşağıda kullandığımız
#kolan isimleri var.
df_surprise = pd.read_csv("surprise_me.csv")
#lowercase = lambda x: str(x).lower()
df_surprise = df_surprise.applymap(lambda x: str(x).lower())
df_surprise.columns = [col.lower() for col in df_surprise.columns]
#df.rename(lowercase, axis='columns', inplace=True)
df_surprise.drop("unnamed: 0", axis=1, inplace=True)
#df.dropna(inplace=True)
df_surprise.head()


name = df_surprise["name"].tolist()
ingredients = df_surprise["ingredients_raw_str"].tolist()
steps = df_surprise["steps"].tolist()
allergen = df_surprise["because_of_allergen"].tolist()
calories = df_surprise["calories"].tolist()
carbon = df_surprise["carbon_emission"].tolist()
def google_image_search(query, api_key, cse_id, num=1):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=query, cx=cse_id, searchType='image', num=num).execute()
    return res['items'][0]['link']

api_key = "AIzaSyDld5RyAGvlO3KNzHLP3R2CCZV_Uz8cYbg"
cse_id = "c42eb241a8bb244c0"

for a in random.sample(range(0, len(df_surprise)), 5): #range kısmı df'e göre değişecek
    st.subheader(name[a].title())
    #image_url1 = google_image_search(name[a], api_key, cse_id)
    #print(image_url1)
    #st.image(image_url1, caption=name[a], use_column_width="auto")
    tab1, tab2, tab3 , tab4 = st.tabs(["Ingredients", "Cooking Steps", "Calori & Carbon Footprint", "Allergen"])
    with tab1:
        st.write(ingredients[a])
    with tab2:
        st.write(steps[a])
    with tab3:
        st.write(f"Calories: {calories[a]} cal")
        st.write(f"Carbon Emission: {carbon[a]} gr")
    with tab4:
        st.write(allergen[a].title())
    #st.write("---")

#şu aşağıdaki uzun işi yukarıdaki iki satır kod yapıyor.

#name_list = df["title"].tolist()
#query1 = random.choice(name_list)
#st.title(query1.upper())

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
#image_url = google_image_search(query, api_key, cse_id)
#print(image_url)

#image_url1 = google_image_search(query1, api_key, cse_id)
#print(image_url1)
#st.image(image_url1, caption=query1)

#malz1 = df[(df["title"] == query1)]["ingredients"].tolist()
#st.header("Ingredients")
#malz1[0]

#info1 = df[(df["title"] == query1)]["instructions"].tolist()
#st.header("Instructions")
#info1[0]
#st.write("---")


#query2 = random.choice(name_list)
#st.title(query2.upper())

#image_url2 = google_image_search(query2, api_key, cse_id)
#print(image_url2)
#st.image(image_url2, caption=query2)

#malz2 = df[(df["title"] == query2)]["ingredients"].tolist()
#st.header("Ingredients")
#malz2[0]

#info2 = df[(df["title"] == query2)]["instructions"].tolist()
#st.header("Instructions")
#info2[0]
#st.write("---")

#query3 = random.choice(name_list)
#st.title(query3.upper())

#image_url3 = google_image_search(query3, api_key, cse_id)
#print(image_url3)
#st.image(image_url3, caption=query3)

#malz3 = df[(df["title"] == query3)]["ingredients"].tolist()
#st.header("Ingredients")
#malz3[0]

#info3 = df[(df["title"] == query3)]["instructions"].tolist()
#st.header("Instructions")
#info3[0]
#st.write("---")

#query4 = random.choice(name_list)
#st.title(query4.upper())

#image_url4 = google_image_search(query4, api_key, cse_id)
#print(image_url4)
#st.image(image_url4, caption=query4)

#malz4 = df[(df["title"] == query4)]["ingredients"].tolist()
#st.header("Ingredients")
#malz4[0]

#info4 = df[(df["title"] == query4)]["instructions"].tolist()
#st.header("Instructions")
#info4[0]
#st.write("---")

#query5 = random.choice(name_list)
#st.title(query5.upper())

#image_url5 = google_image_search(query5, api_key, cse_id)
#print(image_url5)
#st.image(image_url5, caption=query5)

#malz5 = df[(df["title"] == query5)]["ingredients"].tolist()
#st.header("Ingredients")
#malz5[0]

#info5 = df[(df["title"] == query5)]["instructions"].tolist()
#st.header("Instructions")
#info5[0]
#st.write("---")
