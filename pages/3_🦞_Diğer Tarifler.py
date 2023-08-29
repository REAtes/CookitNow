import pandas as pd
import numpy as np
import streamlit as st
import requests
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
from streamlit_extras.metric_cards import style_metric_cards

st.set_page_config(page_title="Diğer Tarifler | GastroMiuul", page_icon="🦞")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


diger = load_lottieurl("https://lottie.host/7b794219-f74e-42dd-a8ad-26b78ec7d7a4/yyVc2FxcgP.json")

st.write('# Canın Ne Çekti?')
col1, col2, col3 = st.columns((1,3,1))
with col2:
    st_lottie(diger)
with st.container():
    st.subheader("İstediğin yemek türünü seç")
    st.selectbox('',
                 ['Kuzu Etli Tarifler',
                  'Dana Etli Tarifler',
                  "Tavuk Etli Tarifler",
                  "Hindi Etli Tarifler",
                  "Av Hayvanları Tarifleri",
                  "Vejeteryan Tarifler",
                  "Etli Sebze Yemekleri",
                  "Etsiz Sebze Yemekleri",
                  "Tatlılar",
                  "Tuzlular",
                  "Mezeler"
                  ])




