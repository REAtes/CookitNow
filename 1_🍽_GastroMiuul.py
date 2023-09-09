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
    "Join Us in Preventing Food Waste Sustainably in the Kitchen")

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
# ---- Numbers ----
# df["tatli"] = df["search_terms"].apply(lambda search_terms: 1 if "cake" in search_terms.lower() or
#                                                                  "cookie" in search_terms.lower() or
#                                                                  "dessert" in search_terms.lower() or
#                                                                  "pudding" in search_terms.lower() else 0)
# df["tatli"].sum()
#
# df["tavuk"] = df["search_terms"].apply(lambda search_terms: 1 if "chicken" in search_terms.lower() else 0)
# df["tavuk"].sum()
#
# df["dana"] = df["search_terms"].apply(lambda search_terms: 1 if "beef" in search_terms.lower() else 0)
# df["dana"].sum()
#
# df["denizden"] = df["search_terms"].apply(lambda search_terms: 1 if "fish" in search_terms.lower() or
#                                                                     "seafood" in search_terms.lower() or
#                                                                     "shrimp" in search_terms.lower() else 0)
# df["denizden"].sum()
#
# df["kuzu"] = df["search_terms"].apply(lambda search_terms: 1 if "lamb" in search_terms.lower() else 0)
# df["kuzu"].sum()
#
# df["noodles"] = df["search_terms"].apply(lambda search_terms: 1 if "noodles" in search_terms.lower() else 0)
# df["noodles"].sum()
#
# df["pasta"] = df["search_terms"].apply(lambda search_terms: 1 if "pasta" in search_terms.lower() else 0)
# df["pasta"].sum()
#
# df["pie"] = df["search_terms"].apply(lambda search_terms: 1 if "pie" in search_terms.lower() else 0)
# df["pie"].sum()
#
# df["pizza"] = df["search_terms"].apply(lambda search_terms: 1 if "pizza" in search_terms.lower() else 0)
# df["pizza"].sum()
#
# df["pork"] = df["search_terms"].apply(lambda search_terms: 1 if "pork" in search_terms.lower() else 0)
# df["pork"].sum()
#
# df["rice"] = df["search_terms"].apply(lambda search_terms: 1 if "rice" in search_terms.lower() else 0)
# df["rice"].sum()
#
# df["salad"] = df["search_terms"].apply(lambda search_terms: 1 if "salad" in search_terms.lower() else 0)
# df["salad"].sum()
#
# df["sandwich"] = df["search_terms"].apply(lambda search_terms: 1 if "sandwich" in search_terms.lower() else 0)
# df["sandwich"].sum()
#
# df["soup"] = df["search_terms"].apply(lambda search_terms: 1 if "soup" in search_terms.lower() else 0)
# df["soup"].sum()
#
# df["vegan"] = df["search_terms"].apply(lambda search_terms: 1 if "vegan" in search_terms.lower() else 0)
# df["vegan"].sum()
#
# df["vegetarian"] = df["search_terms"].apply(lambda search_terms: 1 if "vegetarian" in search_terms.lower() else 0)
# df["vegetarian"].sum()
#
# df["diet"] = df["search_terms"].apply(lambda search_terms: 1 if "atkins" in search_terms.lower() or
#                                                                  "carb-free" in search_terms.lower() or
#                                                                  "dairy-free" in search_terms.lower() or
#                                                                  "diet" in search_terms.lower() or
#                                                                  "low-fat" in search_terms.lower() or
#                                                                  "low-sodium" in search_terms.lower() or
#                                                                  "low-sugar" in search_terms.lower() or
#                                                                  "noflour" in search_terms.lower() or
#                                                                  "salt-free" in search_terms.lower() or
#                                                                  "sodium-free" in search_terms.lower() or
#                                                                  "sugar-free" in search_terms.lower() or
#                                                                  "lowfat" in search_terms.lower() or
#                                                                  "low-carb" in search_terms.lower() or
#                                                                  "low-calorie" in search_terms.lower() or
#                                                                  "light" in search_terms.lower() or
#                                                                  "lactose-free" in search_terms.lower() or
#                                                                  "healthy" in search_terms.lower() or
#                                                                  "grain-free" in search_terms.lower() or
#                                                                  "gluten-free" in search_terms.lower() or
#                                                                  "flour-less" in search_terms.lower() or
#                                                                  "flourless" in search_terms.lower() or
#                                                                  "sugarless" in search_terms.lower() or
#                                                                  "diabetic" in search_terms.lower() else 0)
# df["diet"].sum()

st.write("---")


