import pandas as pd
import numpy as np
import streamlit as st
import requests
import streamlit_lottie
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.metric_cards import style_metric_cards
from streamlit_card import card
from streamlit_extras.stylable_container import stylable_container



st.set_page_config(page_title="CookitNow - In Pursuit of a More Sustainable World", page_icon="🍽")

# ---- Load Data ----

@st.cache_data  # 👈 Add the caching decorator


# ---- Main Page Gif ----
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()



# ---- Gif ---- #
lottie_coding = load_lottieurl("https://lottie.host/e0d42b11-4946-49b5-9a81-81668287d921/HRxgsl3GLT.json")

with st.container():
    col1, col2, col3 = st.columns((1, 4, 1))
    with col2:
        st.write('# CookitN🍽w')
        st_lottie(lottie_coding)


# ---- Texts ---- #
st.write('# The Culinary Journey Begins')

st.write(
    """
    CookitNow is here to add purpose to your culinary journey! We're redefining your cooking experience with 
    three distinct services:
    """)
st.write("##")
st.write(" ## Sustainability Journey 🌿")
st.write(
    """
    It's time to reduce food waste and embrace sustainable kitchen habits worldwide. No more tossing 
    ingredients with approaching expiration dates or those on the verge of spoilage. Just wonder, "What can I make with 
    what I have?" and let us provide you with the best recipes!
    """)
st.write(
    "Join us in preventing food waste **`sustainably`** in the kitchen.")
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
    malzemeye_gore = st.button("**Tell Me What Do You Have**")
    if malzemeye_gore:
        switch_page("Ingredient-Based")
st.write("##")
st.write(" ## Creative Recipes 🍽️")
st.write(
    """
    For those who love to cook or want to explore new recipes, we offer 16 different diet options, 18 different 
    cuisine types, and flavors from 32 different countries. Plus, we provide various filters to help you decide what to 
    cook, what ingredients to use, and even how to prepare your meal.
    """)
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
    diger = st.button("**All Recipes**")
    if diger:
        switch_page("All Recipes")
st.write("##")
st.write(" ## Surprise Me 🎁️")
st.write(
    """
    For those who say, "Let it be a surprise!" We've got you covered! This feature offers you a surprise recipe based 
    on the ingredients you love to experiment with. Try it out to discover a new flavor every day.
    """)
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
st.write(
    """
    With CookitNow, infuse meaning into your kitchen, make a difference in sustainability, and embark on a flavorful 
    culinary adventure. Take the first step towards your cooking purpose today!
    """)