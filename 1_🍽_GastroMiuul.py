import pandas as pd
import numpy as np
import streamlit as st
import requests
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.metric_cards import style_metric_cards


st.set_page_config(page_title="GastroMiuul - Daha Sürdürülebilir Dünya İçin", page_icon="🍽")

# ---- Load Data ----



@st.cache_data  # 👈 Add the caching decorator
def load_data(url, page):
    df = pd.read_excel(url, sheet_name=page)
    return df


df = load_data("C:/Users/remre/PycharmProjects/Tarif_Olusturucu/GastroMiuul/datasets/dataframe.xlsx", "Raw_Data")
lowercase = lambda x: str(x).lower()
df.rename(lowercase, axis='columns', inplace=True)
pd.set_option('display.max_columns', None)
# pd.set_option('display.max_rows', 500)
pd.set_option('display.width', 1500)



# ---- Main Page Gif ----
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()



# ---- Header Section ----
lottie_coding = load_lottieurl("https://lottie.host/53a4d2ce-e9fd-48e7-bd10-688f975eb3c5/imx9F1N56R.json")



with st.container():
    col1, col2, col3 = st.columns((1, 4, 1))
    with col2:
        st.write('# Gastr🍽Miuul')
        st_lottie(lottie_coding)
    st.write('## Mutfak Maceran Başlıyor!')


st.write(
    "Mutfakta `sürdürülebilir` bir yaklaşımla hem doğayı korumaya hem de yiyecek israfını önlemeye hazır mısın?")

st.write("İster elindeki malzemeye göre ister diğer tariflere göz at ve mutfak maceranı başlat!")

with st.container():
    sol_col, sag_col = st.columns(2)
    with sol_col:
        malzemeye_gore = st.button("Elimdeki Malzemeye Göre")
        if malzemeye_gore:
            switch_page("Malzemeye Göre Tarifler")
    with sag_col:
        diger = st.button("Diğer Tariflere Göz At")
        if diger:
            switch_page("Diğer Tarifler")

# ---- Numbers ----
df["tatli"] = df["search_terms"].apply(lambda search_terms: 1 if "cake" in search_terms.lower() or
                                                                 "cookie" in search_terms.lower() or
                                                                 "dessert" in search_terms.lower() or
                                                                 "pudding" in search_terms.lower() else 0)
df["tatli"].sum()

df["tavuk"] = df["search_terms"].apply(lambda search_terms: 1 if "chicken" in search_terms.lower() else 0)
df["tavuk"].sum()

df["dana"] = df["search_terms"].apply(lambda search_terms: 1 if "beef" in search_terms.lower() else 0)
df["dana"].sum()

df["içecek"] = df["search_terms"].apply(lambda search_terms: 1 if "drink" in search_terms.lower() else 0)
df["içecek"].sum()

df["denizden"] = df["search_terms"].apply(lambda search_terms: 1 if "fish" in search_terms.lower() or
                                                                    "seafood" in search_terms.lower() or
                                                                    "shrimp" in search_terms.lower() else 0)
df["denizden"].sum()

df["kuzu"] = df["search_terms"].apply(lambda search_terms: 1 if "lamb" in search_terms.lower() else 0)
df["kuzu"].sum()

df["noodles"] = df["search_terms"].apply(lambda search_terms: 1 if "noodles" in search_terms.lower() else 0)
df["noodles"].sum()

df["pasta"] = df["search_terms"].apply(lambda search_terms: 1 if "pasta" in search_terms.lower() else 0)
df["pasta"].sum()

df["pie"] = df["search_terms"].apply(lambda search_terms: 1 if "pie" in search_terms.lower() else 0)
df["pie"].sum()

df["pizza"] = df["search_terms"].apply(lambda search_terms: 1 if "pizza" in search_terms.lower() else 0)
df["pizza"].sum()

df["pork"] = df["search_terms"].apply(lambda search_terms: 1 if "pork" in search_terms.lower() else 0)
df["pork"].sum()

df["quick"] = df["search_terms"].apply(lambda search_terms: 1 if "quick" in search_terms.lower() else 0)
df["quick"].sum()

df["rice"] = df["search_terms"].apply(lambda search_terms: 1 if "rice" in search_terms.lower() else 0)
df["rice"].sum()

df["salad"] = df["search_terms"].apply(lambda search_terms: 1 if "salad" in search_terms.lower() else 0)
df["salad"].sum()

df["sandwich"] = df["search_terms"].apply(lambda search_terms: 1 if "sandwich" in search_terms.lower() else 0)
df["sandwich"].sum()

df["soup"] = df["search_terms"].apply(lambda search_terms: 1 if "soup" in search_terms.lower() else 0)
df["soup"].sum()

df["vegan"] = df["search_terms"].apply(lambda search_terms: 1 if "vegan" in search_terms.lower() else 0)
df["vegan"].sum()

df["vegetarian"] = df["search_terms"].apply(lambda search_terms: 1 if "vegetarian" in search_terms.lower() else 0)
df["vegetarian"].sum()

df["diet"] = df["search_terms"].apply(lambda search_terms: 1 if "atkins" in search_terms.lower() or
                                                                 "carb-free" in search_terms.lower() or
                                                                 "dairy-free" in search_terms.lower() or
                                                                 "diet" in search_terms.lower() or
                                                                 "low-fat" in search_terms.lower() or
                                                                 "low-sodium" in search_terms.lower() or
                                                                 "low-sugar" in search_terms.lower() or
                                                                 "noflour" in search_terms.lower() or
                                                                 "salt-free" in search_terms.lower() or
                                                                 "sodium-free" in search_terms.lower() or
                                                                 "sugar-free" in search_terms.lower() or
                                                                 "lowfat" in search_terms.lower() or
                                                                 "low-carb" in search_terms.lower() or
                                                                 "low-calorie" in search_terms.lower() or
                                                                 "light" in search_terms.lower() or
                                                                 "lactose-free" in search_terms.lower() or
                                                                 "healthy" in search_terms.lower() or
                                                                 "grain-free" in search_terms.lower() or
                                                                 "gluten-free" in search_terms.lower() or
                                                                 "flour-less" in search_terms.lower() or
                                                                 "flourless" in search_terms.lower() or
                                                                 "sugarless" in search_terms.lower() or
                                                                 "diabetic" in search_terms.lower() else 0)
df["diet"].sum()


st.write("---")
st.write("## Menümüzde Neler Var?")

col1, col2, col3, col4 = st.columns(4)
col1.metric(label="Recipes 🧄", value=df.shape[0])
col2.metric(label="Desserts 🍰", value=df["tatli"].sum())
col3.metric(label="Chicken Recipes 🍗", value=df["tavuk"].sum())
col4.metric(label="Lamb Recipes 🍖", value=df["kuzu"].sum())
col2.metric(label="Beef Recipes 🥩", value=df["dana"].sum())
col3.metric(label="Seafood 🦞", value=df["denizden"].sum())
col4.metric(label="Pork Recipes 🥓", value=df["pork"].sum())
col2.metric(label="Drinks 🍹", value=df["içecek"].sum())
col3.metric(label="Noodle Recipes 🍜", value=df["noodles"].sum())
col4.metric(label="Pasta Recipes 🍝", value=df["pasta"].sum())
col2.metric(label="Pie Recipes 🥧", value=df["pie"].sum())
col3.metric(label="Pizza 🍕", value=df["pizza"].sum())
col2.metric(label="Quick Recipes ⏳", value=df["quick"].sum())
col3.metric(label="Rice Recipes 🍚", value=df["rice"].sum())
col4.metric(label="Salad Recipes 🥗", value=df["salad"].sum())
col4.metric(label="Sandwich Recipes 🥪", value=df["sandwich"].sum())
col2.metric(label="Soup Recipes 🥣", value=df["soup"].sum())
col3.metric(label="Vegan Recipes 🥑", value=df["vegan"].sum())
col4.metric(label="Vegetarian Recipes 🥦", value=df["vegetarian"].sum())
col2.metric(label="Diet Recipes 🍏", value=df["diet"].sum())


# st.write(df)



# We can add multi-select box. It will make dropdown menu;
# st.multiselect('Where do you work', ('London','Istanbul','Berlin'))
# We can add sliders and some features,

# st.slider('Kaç dakikada yemek yapmak istiyorsun?', 200, step=5)
# We can write title and text;
# st.title('Web App')
# st.text('Hello Streamlit')

# We can write headers like that;
# st.header('This is a header')

# st.image(....)


# We can use markdown and its features on streamlit;
# st.markdown('This is a normal Markdown')
# st.markdown('# This is a bold Markdown')
# st.markdown('## This is a thin-bold Markdown')
# st.markdown('* This is a Markdown with point')
# st.markdown('** This is a small bold Markdown **')

# We can make colorful our text;
# st.success('Successful')
# st.markdown('`This is a markdown`')
# st.info("This is an information")
# st.warning('This is a warning')
# st.error('This is an error')


# st.select_slider('Pick a size', ['S', 'M', 'L'])
# st.text_input('First name')
# st.number_input('Pick a number', 0, 10)
# st.text_area('Text to translate')
# st.date_input('Your birthday')
# st.time_input('Meeting time')
# st.file_uploader('Upload a CSV')
# st.download_button('Download file', data)
# st.camera_input("Take a picture")
# st.color_picker('Pick a color')
# st.button('Click me')
# st.data_editor('Edit data', data)
# st.checkbox('I agree')
# st.toggle('Enable')
# st.slider('Pick a number', 0, 100)
