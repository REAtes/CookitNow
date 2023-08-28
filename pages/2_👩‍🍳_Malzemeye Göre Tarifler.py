import pandas as pd
import numpy as np
import streamlit as st
import requests
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu

# ---- Header Section ----


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


lottie_coding2 = load_lottieurl("https://lottie.host/cc7f103d-8c61-410d-b2c3-dd12baca3c5e/NSfWO4QLy3.json")
st.title('Elimdeki Malzemeye Göre Tarifler')
with st.container():
    col1, col2, col3 = st.columns((1, 4, 1))
    with col2:
        st_lottie(lottie_coding2)
    st.subheader('Elindeki Malzemeyi Söyle, Sana Ne Yapacağını Söyleyeyim!')



with st.container():
    st.multiselect('Elindeki Malzemeleri seç "Enter"a bas', ["Domates", "Soğan", "Sarımsak", "Biber", "Tavuk",
                                                                 "Kırmızı Et","Pirinç", "Makarna", "Patates", "Havuç",
                                                                 "Ispanak", "Brokoli","Bezelye", "Mantar", "Kabak",
                                                                 "Kırmızı Mercimek", "Nohut", "Yoğurt", "Peynir",
                                                                 "Zeytin", "Zeytinyağı", "Tereyağı", "Süt", "Un",
                                                                 "Yumurta","Maydanoz", "Dereotu", "Nane", "Kekik",
                                                                 "Tarçın", "Zencefil","Kırmızı Pul Biber", "Kekik",
                                                                 "Krema", "Limon", "Limon Suyu", "Elma","Armut",
                                                                 "Çilek", "Üzüm", "Portakal", "Muz", "Ananas",
                                                                 "Avokado","Karpuz", "Kavun", "Badem", "Ceviz",
                                                                 "Fındık", "Susam", "Ayçiçek Yağı", "Bal", "Tahin",
                                                                 "Hardal", "Mayonez", "Ketçap", "Salça", "Balık",
                                                                 "Karides", "Midye", "Kalamar", "Tavuk Göğsü",
                                                                 "Pastirma", "Salam", "Sucuk", "Sosis", "Zeytin Ezmesi",
                                                                 "Süzme Yoğurt", "Kıvırcık", "Roka", "Lahana",
                                                                 "Karnabahar", "Turşu", "Salatalık", "Kırmızı Lahana",
                                                                 "Beyaz Lahana", "Brokoli", "Kabak","Brüksel Lahanası",
                                                                 "Patlıcan", "Enginar", "Bamya", "Kırmızı Biber",
                                                                 "Acı Biber", "Enginar", "Mısır", "Bezelye",
                                                                 "Yeşil Fasulye","Kuşkonmaz", "Sarımsak", "Kereviz",
                                                                 "Havuç", "Patates", "Taze Soğan","Roka", "Marul",
                                                                 "Semizotu", "Dereotu", "Taze Nane",
                                                                 "Kıvırcık Maydanoz", "Ruşeym", "Quinoa", "Kinoa",
                                                                 "Bulgur", "Couscous"
                                                                 ])
    with st.container():
            st.button('Gelsin Tarifler')
            #st.subheader('Mehmet Şef Hazır! İşte sana önerdiğimiz tarifler')
            #st.image("Görseller_Streamlit/mehmet.gif")

    with st.container():
            tab1, tab2 = st.tabs(["Gereken Malzemeler", "Tarif"])
            tab1.write("""What is Lorem Ipsum? Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem 
            Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type 
            and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into 
            electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset 
            sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker 
            including versions of Lorem Ipsum.""")
            tab2.write("""Why do we use it? It is a long established fact that a reader will be distracted by the readable content 
            of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution 
            of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop 
            publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem 
            ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by 
            accident, sometimes on purpose (injected humour and the like).""")

            with tab2:
                st.radio('Select one:', ["a", "b2"])

from streamlit_extras.metric_cards import style_metric_cards

# c()functionstreamlit_extras.metric_cards.style_metric_cards(background_color: str = '#FFF', border_size_px: int = 1,
# border_color: str = '#CCC', border_radius_px: int = 5, border_left_color: str = '#9AD8E1', box_shadow: bool = True)


def style_metric_cards(
    background_color: str = "#FFF",
    border_size_px: int = 1,
    border_color: str = "#CCC",
    border_radius_px: int = 5,
    border_left_color: str = "#9AD8E1",
    box_shadow: bool = True,
):

    box_shadow_str = (
        "box-shadow: 0 0.15rem 1.75rem 0 rgba(58, 59, 69, 0.15) !important;"
        if box_shadow
        else "box-shadow: none !important;"
    )
    st.markdown(
        f"""
        <style>
            div[data-testid="metric-container"] {{
                background-color: {background_color};
                border: {border_size_px}px solid {border_color};
                padding: 5% 5% 5% 10%;
                border-radius: {border_radius_px}px;
                border-left: 0.5rem solid {border_left_color} !important;
                {box_shadow_str}
            }}
        </style>
        """,
        unsafe_allow_html=True,
    )


col1, col2, = st.columns(2)
col1.metric(label="Karbon Ayakizi", value=5000)
col2.metric(label="Kalori", value=500)
style_metric_cards()