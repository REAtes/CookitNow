import pandas as pd
import numpy as np
import streamlit as st
import requests
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(page_title="GastroMiuul - Daha Sürdürülebilir Dünya İçin", page_icon="🍽")

# ---- Load Data ----

df = pd.read_csv("C:/Users/remre/PycharmProjects/Tarif_Olusturucu/GastroMiuul/archive/Food_Ingredients.csv")
lowercase = lambda x: str(x).lower()
df.rename(lowercase, axis='columns', inplace=True)


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
    st.write('## Mutfak Maceranız Başlıyor!')


st.write(
    """
    Mutfakta **sürdürülebilir** bir yaklaşımla hem doğayı korumaya hem de yiyecek israfını önlemeye hazır mısınız? 
    """)
st.write(
    """
    İster elinizdeki malzemeye göre ister diğer tariflere göz atın ve mutfak maceranızı başlatın!
    """)

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
