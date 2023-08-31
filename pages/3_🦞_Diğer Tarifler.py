import pandas as pd
import numpy as np
import streamlit as st
import requests
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
from streamlit_extras.metric_cards import style_metric_cards
import os
from PIL import Image


st.set_page_config(page_title="Diğer Tarifler | GastroMiuul", page_icon="🦞")

df = pd.read_csv("C:/Users/remre/PycharmProjects/Tarif_Olusturucu/GastroMiuul/archive/Food_Ingredients.csv")
lowercase = lambda x: str(x).lower()
df.rename(lowercase, axis='columns', inplace=True)
df.drop("unnamed: 0", axis=1, inplace=True)
df.dropna(inplace=True)


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


with st.sidebar.header("🦞 Diğer Tarifler"):
    yemek_turu = st.radio(
        "Favorin Hangisi?",
        ["Dana Etli Yemekler",
         "Deniz Mahsüllü Yemekler",
         "Domuz Etli Yemekler",
         "Hindi Yemekleri",
         "Kuzu Etli Yemekler",
         "Tatlılar",
         "Tavuk Yemekleri",
         "Vejeteryan"
         #"Dana Etli Yemekler 🥩",
         #"Deniz Mahsüllü Yemekler 🦞",
         #"Domuz Etli Yemekler 🥓",
         #"Hindi Yemekleri 🍗",
         #"Kuzu Etli Yemekler 🍖",
         #"Tatlılar 🍰",
         #"Tavuk Yemekleri 🍗",
         #"Vejeteryan 🥦"
         ])


###
# Streamlit kenar çubuğundaki seçenekleri oluşturun
st.sidebar.write("---")
secenek = ["Yok", "Var"]
istemedigin_urun_var_mi = st.sidebar.radio("Tarifte olmasını ***istemediğin*** ürün var mı?", secenek)

if istemedigin_urun_var_mi == "Var":
    st.sidebar.write("Hangi ürün ya da ürünleri istemiyorsun?")
    istenmeyen_urun = st.sidebar.multiselect("*Yazmaya başladığında ürünler otomatik şekilde listelenecek. Birden fazla ürün seçebilirsin.*",
                                             ["lamb", "chicken", "milk", "1 cup evaporated milk", "Domates", "Soğan", "Sarımsak", "Biber", "Tavuk", "Kırmızı Et", "Pirinç",
                                              "Makarna", "Patates", "Havuç", "Ispanak", "Brokoli", "Bezelye", "Mantar",
                                              "Kabak", "Kırmızı Mercimek", "Nohut", "Yoğurt", "Peynir", "Zeytin",
                                              "Zeytinyağı", "Tereyağı", "Süt", "Un", "Yumurta", "Maydanoz", "Dereotu",
                                              "Nane", "Kekik", "Tarçın", "Zencefil", "Kırmızı Pul Biber", "Kekik",
                                              "Krema", "Limon", "Limon Suyu", "Elma", "Armut", "Çilek", "Üzüm",
                                              "Portakal", "Muz", "Ananas", "Avokado", "Karpuz", "Kavun", "Badem",
                                              "Ceviz", "Fındık", "Susam", "Ayçiçek Yağı", "Bal", "Tahin", "Hardal",
                                              "Mayonez", "Ketçap", "Salça", "Balık", "Karides", "Midye", "Kalamar",
                                              "Tavuk Göğsü", "Pastirma", "Salam", "Sucuk", "Sosis", "Zeytin Ezmesi",
                                              "Süzme Yoğurt", "Kıvırcık", "Roka",
                                              "Lahana", "Karnabahar", "Turşu", "Salatalık", "Kırmızı Lahana",
                                              "Beyaz Lahana", "Brokoli", "Kabak", "Brüksel Lahanası", "Patlıcan",
                                              "Enginar",
                                              "Bamya", "Kırmızı Biber", "Acı Biber", "Enginar", "Mısır", "Bezelye",
                                              "Yeşil Fasulye", "Kuşkonmaz", "Sarımsak", "Kereviz", "Havuç", "Patates",
                                              "Taze Soğan", "Roka", "Marul", "Semizotu", "Dereotu", "Taze Nane",
                                              "Kıvırcık Maydanoz", "Ruşeym", "Quinoa", "Kinoa", "Bulgur", "Couscous"
                                             ])

# ---- Kullanıcıya Özel DF ----
with st.container():
    if istemedigin_urun_var_mi == "Var":
        st.write(f"**İçinde kesinlikle `{', '.join(istenmeyen_urun)}` olmasın!**")
        oneri_tarifler = df[df["cleaned_ingredients"].str.contains("|".join(istenmeyen_urun))]
        oneri_tarifler_indexes = oneri_tarifler.index.tolist()
        images_paths = []
        for index in oneri_tarifler_indexes:
            a = oneri_tarifler.loc[index, "image_name"]
            image_path = f"C:/Users/remre/PycharmProjects/Tarif_Olusturucu/GastroMiuul/archive/Food_Images/{a}.jpg"
            images_paths.append(image_path)

        displayed_images_indexes = oneri_tarifler_indexes[10:]
        show_more_button = st.button("Gelsin Tarifler")

        if show_more_button:
            st.write(" # İşte Tarifler")
            images_to_display = displayed_images_indexes[:10]
            images_paths = []
            for index in images_to_display:
                a = oneri_tarifler.loc[index, "image_name"]
                image_path = f"C:/Users/remre/PycharmProjects/Tarif_Olusturucu/GastroMiuul/archive/Food_Images/{a}.jpg"
                images_paths.append(image_path)
            # Görselleri iki sütun halinde gösterme
            col1, col2 = st.columns(2)
            for i, image in enumerate(images_paths):
                if i % 2 == 0:
                    column = col1
                else:
                    column = col2

                column.image(Image.open(image),
                             caption=oneri_tarifler.loc[images_to_display[i], "title"],
                             use_column_width=True)




    if istemedigin_urun_var_mi == "Yok":
        st.write(f"**Bana her şey uyar! 👌**")




# ---- Görseller ----
#oneri_tarifler = df[~df["cleaned_ingredients"].str.contains("|".join(istenmeyen_urun))]




