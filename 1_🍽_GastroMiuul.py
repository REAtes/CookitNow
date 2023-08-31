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

df = pd.read_csv("C:/Users/remre/PycharmProjects/Tarif_Olusturucu/GastroMiuul/archive/Food_Ingredients.csv")
lowercase = lambda x: str(x).lower()
df.rename(lowercase, axis='columns', inplace=True)
df.drop("unnamed: 0", axis=1, inplace=True)
df.dropna(inplace=True)


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

df['tatli'] = df['title'].apply(lambda title: 1 if 'cake' in title.lower() or
                                                   'pudding' in title.lower() else 0)
df["sekerli"] = df['cleaned_ingredients'].apply(lambda cleaned_ingredients:
                                                1 if 'cup sugar' in cleaned_ingredients.lower() else 0)
df.loc[(df['sekerli'] == 1) & (df['tatli'] == 0), 'tatli'] = 1

df["tatli"].sum()

df['tavuk'] = df['cleaned_ingredients'].apply(lambda cleaned_ingredients:
                                              1 if 'chicken' in cleaned_ingredients.lower() else 0)
df["tavuk"].sum()

df['hindi'] = df['cleaned_ingredients'].apply(lambda cleaned_ingredients:
                                              1 if 'turkey' in cleaned_ingredients.lower() else 0)
df["hindi"].sum()

df["sekerli"] = df['cleaned_ingredients'].apply(lambda cleaned_ingredients:
                                                1 if 'cup sugar' in cleaned_ingredients.lower() else 0)
df.loc[(df['sekerli'] == 1) & (df['tatli'] == 0), 'tatli'] = 1
df["sekerli"].sum()


df["kuzu"] = df['cleaned_ingredients'].apply(lambda cleaned_ingredients:
                                             1 if 'lamb' in cleaned_ingredients.lower() else 0)
df["kuzu"].sum()

df["deniz_mahsulu"] = df['cleaned_ingredients'].apply(lambda cleaned_ingredients:
                                                      1 if 'shrimp' in cleaned_ingredients.lower() or
                                                           'lobster' in cleaned_ingredients.lower() or
                                                           'crab' in cleaned_ingredients.lower() or
                                                           'clam' in cleaned_ingredients.lower() or
                                                           'oyster' in cleaned_ingredients.lower() or
                                                           'scallop' in cleaned_ingredients.lower() or
                                                           'squid' in cleaned_ingredients.lower() or
                                                           'octopus' in cleaned_ingredients.lower() or
                                                           'tuna' in cleaned_ingredients.lower() or
                                                           'salmon' in cleaned_ingredients.lower() or
                                                           'cod' in cleaned_ingredients.lower() or
                                                           'haddock' in cleaned_ingredients.lower() or
                                                           'trout' in cleaned_ingredients.lower() or
                                                           'sardine' in cleaned_ingredients.lower() or
                                                           'anchovy' in cleaned_ingredients.lower() or
                                                           'mackerel' in cleaned_ingredients.lower() else 0)
df["deniz_mahsulu"].sum()

df["dana"] = df['cleaned_ingredients'].apply(lambda cleaned_ingredients:
                                             1 if 'beef' in cleaned_ingredients.lower() or
                                                  'steam' in cleaned_ingredients.lower() or
                                                  'roast beef' in cleaned_ingredients.lower() or
                                                  'ground beef' in cleaned_ingredients.lower() or
                                                  'beef tenderloin' in cleaned_ingredients.lower() or
                                                  'ribeye' in cleaned_ingredients.lower() or
                                                  'sirloin' in cleaned_ingredients.lower() or
                                                  'brisket' in cleaned_ingredients.lower() or
                                                  'chuck' in cleaned_ingredients.lower() or
                                                  'flank steak' in cleaned_ingredients.lower() or
                                                  'short ribs' in cleaned_ingredients.lower() or
                                                  'rump steak' in cleaned_ingredients.lower() or
                                                  'filet mignon' in cleaned_ingredients.lower() or
                                                  'prime rib' in cleaned_ingredients.lower() or
                                                  't-bone' in cleaned_ingredients.lower() or
                                                  'ground chuck' in cleaned_ingredients.lower() or
                                                  'ground round' in cleaned_ingredients.lower() or
                                                  'stew meat' in cleaned_ingredients.lower() or
                                                  'skirt steak' in cleaned_ingredients.lower() or
                                                  'eye of round' in cleaned_ingredients.lower() or
                                                  'top round' in cleaned_ingredients.lower() or
                                                  'bottom round' in cleaned_ingredients.lower() or
                                                  'london broil' in cleaned_ingredients.lower() or
                                                  'strip steak' in cleaned_ingredients.lower() or
                                                  'cube steak' in cleaned_ingredients.lower() or
                                                  'ground beef patties' in cleaned_ingredients.lower() or
                                                  'ground beef patties' in cleaned_ingredients.lower() or
                                                  'ground beef chunks' in cleaned_ingredients.lower() or
                                                  'bratwurst' in cleaned_ingredients.lower() or
                                                  'corned beef' in cleaned_ingredients.lower() or
                                                  'corned beef' in cleaned_ingredients.lower() or
                                                  'pastrami' in cleaned_ingredients.lower() or
                                                  'beef ribs' in cleaned_ingredients.lower() or
                                                  'beef sausage' in cleaned_ingredients.lower() or
                                                  'beef liver' in cleaned_ingredients.lower() or
                                                  'ground sirloin' in cleaned_ingredients.lower() else 0)
df["dana"].sum()

df["domuz"] = df['cleaned_ingredients'].apply(lambda cleaned_ingredients:
                                              1 if 'pork' in cleaned_ingredients.lower() else 0)
df["domuz"].sum()

st.write("---")
st.write("## Menümüzde Neler Var?")
col1, col2, col3, col4 = st.columns(4)
col1.metric(label="Tarifler 🧄", value=df.shape[0])
col2.metric(label="Tatlı Tarifleri 🍰", value=df["tatli"].sum())
col3.metric(label="Tavuk Tarifleri 🍗", value=df["tavuk"].sum())
col4.metric(label="Hindi Tarifleri 🍗", value=df["hindi"].sum())
col2.metric(label="Kuzu Eti Tarifleri 🍖", value=df["kuzu"].sum())
col3.metric(label="Dana Eti Tarifleri 🥩", value=df["dana"].sum())
col4.metric(label="Deniz Mahsülü 🦞", value=df["deniz_mahsulu"].sum())
col2.metric(label="Domuz Eti Tarifleri 🥓", value=df["domuz"].sum())


style_metric_cards()

st.write(df)



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
