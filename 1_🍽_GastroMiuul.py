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




st.set_page_config(page_title="GastroMiuul - Daha Sürdürülebilir Dünya İçin", page_icon="🍽", layout="wide")

# ---- Load Data ----



@st.cache_data  # 👈 Add the caching decorator
def load_data(url, page):
    df = pd.read_excel(url, sheet_name=page)
    return df


df = pd.read_csv("C:/Users/remre/PycharmProjects/Tarif_Olusturucu/GastroMiuul/datasets/dataframe_060923csv1.csv")
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
    col1, col2, col3 = st.columns((1, 4, 1))
    with col2:
        with st.container():
            sol_col, sag_col = st.columns(2)
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
                    malzemeye_gore = st.button("**Elimdeki Malzemeye Göre**")
                    if malzemeye_gore:
                        switch_page("Malzemeye Göre Tarifler")
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

                        diger = st.button("**Diğer Tariflere Göz At**")
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
st.container
st.set_page_config( layout="wide")

st.write("---")

with st.container():
    c1, c2, c3, c4, c5, c6 = st.columns(6)
    with c1:
        card(title="1",
             text="1",
             image="https://images.unsplash.com/photo-1506224477000-07aa8a76be20?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1170&q=80")
        card(title="2",
             text="Beef Recipes",
             image="https://images.unsplash.com/photo-1476718406336-bb5a9690ee2a?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=987&q=80")
        card(title="3",
             text="Beef Recipes",
             image="https://images.unsplash.com/photo-1546069901-ba9599a7e63c?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1160&q=80")
    with c2:
        card(title="4",
             text="Beef Recipes",
             image="https://images.unsplash.com/photo-1607455849478-86754d8816f0?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1114&q=80")
        card(title="5",
             text="Beef Recipes",
             image="https://images.unsplash.com/photo-1490645935967-10de6ba17061?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1153&q=80")
        card(title="6",
             text="Beef Recipes",
             image="https://images.unsplash.com/photo-1481070414801-51fd732d7184?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1024&q=80")
    with c3:
        card(title="7",
             text="Beef Recipes",
             image="https://images.unsplash.com/photo-1602534923950-d2c7e6be0ca0?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1112&q=80")
        card(title="8",
             text="Beef Recipes",
             image="https://images.unsplash.com/photo-1602534923950-d2c7e6be0ca0?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1112&q=80")
    with c4:
        card(title="9",
             text="Beef Recipes",
             image="https://images.unsplash.com/photo-1578596371629-0fe8c3c12f80?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1170&q=80")
        card(title="10",
             text="Beef Recipes",
             image="https://images.unsplash.com/photo-1625944228741-cf30983ecb91?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1162&q=80")
    with c5:
        card(title="11",
             text="Beef Recipes",
             image="https://images.unsplash.com/photo-1506224477000-07aa8a76be20?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1170&q=80")
        card(title="12",
             text="Beef Recipes",
             image="https://images.unsplash.com/photo-1523986490752-c28064f26be3?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1169&q=80")
    with c6:
        card(title="13",
             text="Beef Recipes",
             image="https://images.unsplash.com/photo-1506224477000-07aa8a76be20?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1170&q=80")
        card(title="14",
             text="Beef Recipes",
             image="https://images.unsplash.com/photo-1506224477000-07aa8a76be20?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1170&q=80")





