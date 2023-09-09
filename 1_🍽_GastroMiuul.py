import pandas as pd
import numpy as np
import streamlit as st
import requests
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.metric_cards import style_metric_cards
from streamlit_card import card
from streamlit_extras.stylable_container import stylable_container



st.set_page_config(page_title="GastroMiuul - In Pursuit of a More Sustainable World", page_icon="🍽")

# ---- Load Data ----

@st.cache_data  # 👈 Add the caching decorator
#def load_data(url):
#   df = pd.read_excel(url)
#   return df


# df = load_data("C:/Users/remre/PycharmProjects/Tarif_Olusturucu/GastroMiuul/datasets/dataframe_060923.xlsx")
# lowercase = lambda x: str(x).lower()
# df.rename(lowercase, axis='columns', inplace=True)
# pd.set_option('display.max_columns', None)
# pd.set_option('display.max_rows', 500)
# pd.set_option('display.width', 1500)



# ---- Main Page Gif ----
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()



# ---- Gif ---- #
lottie_coding = load_lottieurl("https://lottie.host/53a4d2ce-e9fd-48e7-bd10-688f975eb3c5/imx9F1N56R.json")

with st.container():
    col1, col2, col3 = st.columns((1, 4, 1))
    with col2:
        st.write('# Gastr🍽Miuul')
        st_lottie(lottie_coding)


# ---- Texts ---- #
st.write('## The Culinary Journey Begins')

st.write(
    "Join Us in Preventing Food Waste **`Sustainably`** in the Kitchen")

st.write("""
Whether you're cooking with what you have or exploring our chef's creations, embark on your culinary 
journey with purpose!
""")

# ---- Buttons ---- #
with st.container():
    col1, col2, col3 = st.columns((1, 4, 1))
    with col2:
        with st.container():
            sol_col, orta, sag_col = st.columns(3)
            with sol_col:
                with stylable_container(
                        key="red_button",
                        css_styles="""
                        button {
                            background-color: #FFBC42;
                            color: green;
                            border-radius: 5px;
                        }
                        """,
                ):
                    malzemeye_gore = st.button("**By Ingredient**")
                    if malzemeye_gore:
                        switch_page("Ingredient-Based")
            with orta:
                with stylable_container(
                        key="yellow_button",
                        css_styles="""
                                button {
                                    background-color: #FFBC42;
                                    color: #FFFFFF;
                                    border-radius: 5px;
                                }
                                """,
                ):
                    diger = st.button("**Other Recipes**")
                    if diger:
                        switch_page("Other Recipes")
            with sag_col:
                with stylable_container(
                        key="yellow_button",
                        css_styles="""
                                button {
                                    background-color: #FFBC42;
                                    color: #FFFFFF;
                                    border-radius: 5px;
                                }
                                """,
                ):
                    diger = st.button("**Surprise Me!**")
                    if diger:
                        switch_page("Surprise Me")