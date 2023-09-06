import pandas as pd
import numpy as np
import streamlit as st
import requests
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
from streamlit_extras.metric_cards import style_metric_cards
import os
from PIL import Image
from streamlit_extras.stylable_container import stylable_container


st.set_page_config(page_title="Diğer Tarifler | GastroMiuul", page_icon="🦞")


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



# ---- New Features for filtering ---- #
    # ---- Recipe Type ---- #
df["tatli"] = df["search_terms"].apply(lambda search_terms: 1 if "cake" in search_terms.lower() or
                                                                 "cookie" in search_terms.lower() or
                                                                 "dessert" in search_terms.lower() or
                                                                 "pudding" in search_terms.lower() else 0)
df["tavuk"] = df["search_terms"].apply(lambda search_terms: 1 if "chicken" in search_terms.lower() else 0)
df["dana"] = df["search_terms"].apply(lambda search_terms: 1 if "beef" in search_terms.lower() else 0)
df["içecek"] = df["search_terms"].apply(lambda search_terms: 1 if "drink" in search_terms.lower() else 0)
df["denizden"] = df["search_terms"].apply(lambda search_terms: 1 if "fish" in search_terms.lower() or
                                                                    "seafood" in search_terms.lower() or
                                                                    "shrimp" in search_terms.lower() else 0)
df["kuzu"] = df["search_terms"].apply(lambda search_terms: 1 if "lamb" in search_terms.lower() else 0)
df["noodles"] = df["search_terms"].apply(lambda search_terms: 1 if "noodles" in search_terms.lower() else 0)
df["pasta"] = df["search_terms"].apply(lambda search_terms: 1 if "pasta" in search_terms.lower() else 0)
df["pie"] = df["search_terms"].apply(lambda search_terms: 1 if "pie" in search_terms.lower() else 0)
df["pizza"] = df["search_terms"].apply(lambda search_terms: 1 if "pizza" in search_terms.lower() else 0)
df["pork"] = df["search_terms"].apply(lambda search_terms: 1 if "pork" in search_terms.lower() else 0)
df["quick"] = df["search_terms"].apply(lambda search_terms: 1 if "quick" in search_terms.lower() else 0)
df["rice"] = df["search_terms"].apply(lambda search_terms: 1 if "rice" in search_terms.lower() else 0)
df["salad"] = df["search_terms"].apply(lambda search_terms: 1 if "salad" in search_terms.lower() else 0)
df["sandwich"] = df["search_terms"].apply(lambda search_terms: 1 if "sandwich" in search_terms.lower() else 0)
df["soup"] = df["search_terms"].apply(lambda search_terms: 1 if "soup" in search_terms.lower() else 0)
df["vegan"] = df["search_terms"].apply(lambda search_terms: 1 if "vegan" in search_terms.lower() else 0)
df["vegetarian"] = df["search_terms"].apply(lambda search_terms: 1 if "vegetarian" in search_terms.lower() or
                                                                      "nomeat" in search_terms.lower() else 0)

    # ---- Diet Type ---- #
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

    # ---- Cooking Style ---- #
df["baked"] = df["search_terms"].apply(lambda search_terms: 1 if "baked" in search_terms.lower() else 0)
df["barbecue"] = df["search_terms"].apply(lambda search_terms: 1 if "barbecue" in search_terms.lower() else 0)
df["braised"] = df["search_terms"].apply(lambda search_terms: 1 if "braised" in search_terms.lower() else 0)
df["casserole"] = df["search_terms"].apply(lambda search_terms: 1 if "casserole" in search_terms.lower() else 0)
df["roast"] = df["search_terms"].apply(lambda search_terms: 1 if "roast" in search_terms.lower() else 0)
df["stew"] = df["search_terms"].apply(lambda search_terms: 1 if "stew" in search_terms.lower() else 0)

    # ---- Cooking Time ---- #
df["breakfast"] = df["search_terms"].apply(lambda search_terms:
                                           1 if "breakfast" in search_terms.lower() else 0)  # 21219
df["dinner"] = df["search_terms"].apply(lambda search_terms:
                                        1 if "dinner" in search_terms.lower() else 0) # 118004
df["lunch"] = df["search_terms"].apply(lambda search_terms:
                                       1 if "lunch" in search_terms.lower() else 0)  # 28547
df["side"] = df["search_terms"].apply(lambda search_terms:
                                      1 if "side" in search_terms.lower() else 0)  # 29032
df["snack"] = df["search_terms"].apply(lambda search_terms:
                                       1 if "snack" in search_terms.lower() else 0)  # 12042
df["appetizer"] = df["search_terms"].apply(lambda search_terms:
                                           1 if "appetizer" in search_terms.lower() else 0)  # 26538



# ---- Streamlit sidebar filters ---- #

servings = st.sidebar.slider("Number of people to be served", 1, 8, 4)


def select_meal(df, meal, servings):
    if meal == "I don't mind" or meal == "Please choose":
        return df.loc[df["servings"] == servings]
    else:
        meal_df = df.loc[(df[meal.lower()] == 1) & (df["servings"] == servings)]
        return meal_df



which_meal = st.sidebar.selectbox(label="What meal would you like choose?",
                                  options=("Please choose", "I don't mind", 'Breakfast', 'Lunch',
                                           'Dinner', 'Appetizer', 'Snack', 'Side'))

def select_style(df, style, servings):
    if style == "I don't mind" or style == "Please choose":
        return df.loc[df["servings"] == servings]
    else:
        style_df = df.loc[(df[style.lower()] == 1) & (df["servings"] == servings)]
        return style_df


if which_meal == "I don't mind":
    df = select_meal(df, which_meal, servings)


    which_style = st.sidebar.selectbox("Which cooking style do you prefer:",
                                   ("Please choose", "I don't mind", 'Baked', 'Barbecue',
                                    'Braised', 'Casserole', 'Roast', 'Stew'),
                                   index=0)

    if which_style == "I don't mind":
        df = select_style(df, which_style, servings)

        secenek1 = ["Yes", "No"]
        diet_y_n = st.sidebar.radio("Do you follow any specific diet?", secenek1)

        if diet_y_n == "Yes":
            diet_turu = st.sidebar.selectbox(
                "Please select one of the diets",
                ('Atkins',
                 'Carb-Free',
                 'Dairy-Free',
                 'Diabetic',
                 'Gluten-Free',
                 'Grain-Free',
                 'Healthy',
                 'Lactose-Free',
                 'Low-Calorie',
                 'Low-Carb',
                 'Low-Fat',
                 'Low-Sodium',
                 'Low-Sugar',
                 'Salt-Free',
                 'Sodium-Free',
                 'Sugar-Free'))
            favori_diet_df = pd.DataFrame()
            if diet_turu == "Atkins":
                favori_diet_df = df.loc[(df["diet"] == 1) & (df["search_terms"].str.contains("atkins"))]
            if diet_turu == "Carb-Free":
                favori_diet_df = df.loc[(df["diet"] == 1) & (df["search_terms"].str.contains("carb-free"))]
            if diet_turu == "Dairy-Free":
                favori_diet_df = df.loc[(df["diet"] == 1) & (df["search_terms"].str.contains("dairy-free"))]
            if diet_turu == "Diabetic":
                favori_diet_df = df.loc[(df["diet"] == 1) & (df["search_terms"].str.contains("diabetic"))]
            if diet_turu == "Gluten-Free":
                favori_diet_df = df.loc[(df["diet"] == 1) & (df["search_terms"].str.contains("gluten-free"))]
            if diet_turu == "Healthy":
                favori_diet_df = df.loc[(df["diet"] == 1) & ((df["search_terms"].str.contains("diet"))
                                                             | (df["search_terms"].str.contains("diet"))
                                                             | (df["search_terms"].str.contains("light")))]
            if diet_turu == "Lactose-Free":
                favori_diet_df = df.loc[(df["diet"] == 1) & (df["search_terms"].str.contains("lactose-free"))]
            if diet_turu == "Low-Calorie":
                favori_diet_df = df.loc[(df["diet"] == 1) & (df["search_terms"].str.contains("low-calorie"))]
            if diet_turu == "Low-Carb":
                favori_diet_df = df.loc[(df["diet"] == 1) & (df["search_terms"].str.contains("low-carb"))]
            if diet_turu == "Low-Fat":
                favori_diet_df = df.loc[(df["diet"] == 1) & ((df["search_terms"].str.contains("low-fat"))
                                                             | (df["search_terms"].str.contains("lowfat")))]
            if diet_turu == "Low-Sodium":
                favori_diet_df = df.loc[(df["diet"] == 1) & (df["search_terms"].str.contains("low-sodium"))]
            if diet_turu == "Low-Sugar":
                favori_diet_df = df.loc[(df["diet"] == 1) & (df["search_terms"].str.contains("low-sugar"))]
            if diet_turu == "Salt-Free":
                favori_diet_df = df.loc[(df["diet"] == 1) & (df["search_terms"].str.contains("salt-free"))]
            if diet_turu == "Sodium-Free":
                favori_diet_df = df.loc[(df["diet"] == 1) & (df["search_terms"].str.contains("sodium-free"))]
            if diet_turu == "Sugar-Free":
                favori_diet_df = df.loc[(df["diet"] == 1) & ((df["search_terms"].str.contains("sugar-free"))
                                                             | (df["search_terms"].str.contains("sugarless")))]

        # ---- What is your Favorite? ---- #
        else:
            yemek_turu = st.sidebar.selectbox(
                "Please select one of them",
                ("Beef Recipes",
                 "Chicken Recipes",
                 "Diet Recipes",
                 "Dessert",
                 "Lamb Recipes",
                 "Noodle Recipes",
                 "Pasta Recipes",
                 "Pie Recipes",
                 "Pizza",
                 "Pork Recipes",
                 "Quick Recipes",
                 "Rice Recipes",
                 "Salad Recipes",
                 "Sandwich Recipes",
                 "Seafoods",
                 "Soup Recipes",
                 "Vegan Recipes",
                 "Vegetarian Recipes"
                 ))
            favori_yemek_df = pd.DataFrame()
            if yemek_turu == "Beef Recipes":
                favori_yemek_df = df.loc[df["dana"]== 1]
            if yemek_turu == "Chicken Recipes":
                favori_yemek_df = df.loc[df["tavuk"] == 1]
            if yemek_turu == "Diet Recipes":
                favori_yemek_df = df.loc[df["diet"] == 1]
            #if yemek_turu == "Drinks":
                #favori_yemek_df = df.loc[df["içecek"] == 1]
            if yemek_turu == "Dessert":
                favori_yemek_df = df.loc[df["tatli"] == 1]
            if yemek_turu == "Tatlılar":
                favori_yemek_df = df.loc[df["tatli"] == 1]
            if yemek_turu == "Lamb Recipes":
                favori_yemek_df = df.loc[df["kuzu"] == 1]
            if yemek_turu == "Noodle Recipes":
                favori_yemek_df = df.loc[df["noodles"] == 1]
            if yemek_turu == "Pasta Recipes":
                favori_yemek_df = df.loc[df["pasta"] == 1]
            if yemek_turu == "Pie Recipes":
                favori_yemek_df = df.loc[df["pie"] == 1]
            if yemek_turu == "Pizza":
                favori_yemek_df = df.loc[df["pizza"] == 1]
            if yemek_turu == "Pork Recipes":
                favori_yemek_df = df.loc[df["pork"] == 1]
            if yemek_turu == "Quick Recipes":
                favori_yemek_df = df.loc[df["quick"] == 1]
            if yemek_turu == "Rice Recipes":
                favori_yemek_df = df.loc[df["rice"] == 1]
            if yemek_turu == "Salad Recipes":
                favori_yemek_df = df.loc[df["salad"] == 1]
            if yemek_turu == "Sandwich Recipes":
                favori_yemek_df = df.loc[df["sandwich"] == 1]
            if yemek_turu == "Seafood Recipes":
                favori_yemek_df = df.loc[df["denizden"] == 1]
            if yemek_turu == "Soup Recipes":
                favori_yemek_df = df.loc[df["soup"] == 1]
            if yemek_turu == "Vegan Recipes":
                favori_yemek_df = df.loc[df["vegan"] == 1]
            if yemek_turu == "Vegetarian Recipes":
                favori_yemek_df = df.loc[df["vegetarian"] == 1]


            # ---- Would you like to choose a cuisine? ---- #

            secenek2 = ["No", "Yes"]
            cuisine_y_n = st.sidebar.radio("Would you like to choose a cuisine?", secenek2)

            if cuisine_y_n == "Yes":
                cuisine = st.sidebar.selectbox("*You can type*",
                                                 ['American', 'Crazilian', 'Caribbean', 'Chilean', 'Chinese', 'Creole', 'Cuban',
                                                  'Egyptian', 'English', 'Ethiopian', 'French', 'German', 'Greek', 'Indian',
                                                  'Indonesian', 'Irish', 'Italian', 'Jamaican', 'Japanese', 'Korean', 'Lebanese',
                                                  'Malaysian', 'Mexican', 'Moroccan', 'Nigerian', 'Persian', 'Peruvian', 'Polish',
                                                  'Russian', 'Scottish', 'Southern', 'Spanish', 'Thai', 'Turkish', 'Vietnamese'
                                                  ])
                favori_yemek_df = favori_yemek_df[favori_yemek_df["search_terms"].str.contains(cuisine.lower())]

            # ---- Or, would you like to choose a diet? ---- #

    else:
        df = select_style(df, which_style, servings)

        secenek1 = ["Yes", "No"]
        diet_y_n = st.sidebar.radio("Do you follow any specific diet?", secenek1)

        if diet_y_n == "Yes":
            diet_turu = st.sidebar.selectbox(
                "Please select one of the diets",
                ('Atkins',
                 'Carb-Free',
                 'Dairy-Free',
                 'Diabetic',
                 'Flour-Free',
                 'Gluten-Free',
                 'Grain-Free',
                 'Healthy',
                 'Lactose-Free',
                 'Low-Calorie',
                 'Low-Carb',
                 'Low-Fat',
                 'Low-Sodium',
                 'Low-Sugar',
                 'Salt-Free',
                 'Sodium-Free',
                 'Sugar-Free'
                 ))
            favori_diet_df = pd.DataFrame()
            if diet_turu == "Atkins":
                favori_diet_df = df.loc[(df["diet"] == 1) & (df["search_terms"].str.contains("atkins"))]
            if diet_turu == "Carb-Free":
                favori_diet_df = df.loc[(df["diet"] == 1) & (df["search_terms"].str.contains("carb-free"))]
            if diet_turu == "Dairy-Free":
                favori_diet_df = df.loc[(df["diet"] == 1) & (df["search_terms"].str.contains("dairy-free"))]
            if diet_turu == "Diabetic":
                favori_diet_df = df.loc[(df["diet"] == 1) & (df["search_terms"].str.contains("diabetic"))]
            if diet_turu == "Flour-Free":
                favori_diet_df = df.loc[(df["diet"] == 1) & (df["search_terms"].str.contains("flour-free"))]
            if diet_turu == "Gluten-Free":
                favori_diet_df = df.loc[(df["diet"] == 1) & (df["search_terms"].str.contains("gluten-free"))]
            if diet_turu == "Healthy":
                favori_diet_df = df.loc[(df["diet"] == 1) & ((df["search_terms"].str.contains("diet"))
                                                             | (df["search_terms"].str.contains("diet"))
                                                             | (df["search_terms"].str.contains("light")))]
            if diet_turu == "Lactose-Free":
                favori_diet_df = df.loc[(df["diet"] == 1) & (df["search_terms"].str.contains("lactose-free"))]
            if diet_turu == "Low-Calorie":
                favori_diet_df = df.loc[(df["diet"] == 1) & (df["search_terms"].str.contains("low-calorie"))]
            if diet_turu == "Low-Carb":
                favori_diet_df = df.loc[(df["diet"] == 1) & (df["search_terms"].str.contains("low-carb"))]
            if diet_turu == "Low-Fat":
                favori_diet_df = df.loc[(df["diet"] == 1) & ((df["search_terms"].str.contains("low-fat"))
                                                             | (df["search_terms"].str.contains("lowfat")))]
            if diet_turu == "Low-Sodium":
                favori_diet_df = df.loc[(df["diet"] == 1) & (df["search_terms"].str.contains("low-sodium"))]
            if diet_turu == "Low-Sugar":
                favori_diet_df = df.loc[(df["diet"] == 1) & (df["search_terms"].str.contains("low-sugar"))]
            if diet_turu == "Salt-Free":
                favori_diet_df = df.loc[(df["diet"] == 1) & (df["search_terms"].str.contains("salt-free"))]
            if diet_turu == "Sodium-Free":
                favori_diet_df = df.loc[(df["diet"] == 1) & (df["search_terms"].str.contains("sodium-free"))]
            if diet_turu == "Sugar-Free":
                favori_diet_df = df.loc[(df["diet"] == 1) & ((df["search_terms"].str.contains("sugar-free"))
                                                             | (df["search_terms"].str.contains("sugarless")))]
                # if diet_y_n != "I dont":
                #     change_diet_choice("I dont")


        # ---- What is your Favorite? ---- #
        else:
            yemek_turu = st.sidebar.selectbox(
                "Please select one of them",
                ("Beef Recipes",
                 "Chicken Recipes",
                 "Diet Recipes",
                 "Dessert",
                 "Lamb Recipes",
                 "Noodle Recipes",
                 "Pasta Recipes",
                 "Pie Recipes",
                 "Pizza",
                 "Pork Recipes",
                 "Quick Recipes",
                 "Rice Recipes",
                 "Salad Recipes",
                 "Sandwich Recipes",
                 "Seafoods",
                 "Soup Recipes",
                 "Vegan Recipes",
                 "Vegetarian Recipes"
                 ))
            favori_yemek_df = pd.DataFrame()
            if yemek_turu == "Beef Recipes":
                favori_yemek_df = df.loc[df["dana"] == 1]
            if yemek_turu == "Chicken Recipes":
                favori_yemek_df = df.loc[df["tavuk"] == 1]
            if yemek_turu == "Diet Recipes":
                favori_yemek_df = df.loc[df["diet"] == 1]
            # if yemek_turu == "Drinks":
            # favori_yemek_df = df.loc[df["içecek"] == 1]
            if yemek_turu == "Dessert":
                favori_yemek_df = df.loc[df["tatli"] == 1]
            if yemek_turu == "Tatlılar":
                favori_yemek_df = df.loc[df["tatli"] == 1]
            if yemek_turu == "Lamb Recipes":
                favori_yemek_df = df.loc[df["kuzu"] == 1]
            if yemek_turu == "Noodle Recipes":
                favori_yemek_df = df.loc[df["noodles"] == 1]
            if yemek_turu == "Pasta Recipes":
                favori_yemek_df = df.loc[df["pasta"] == 1]
            if yemek_turu == "Pie Recipes":
                favori_yemek_df = df.loc[df["pie"] == 1]
            if yemek_turu == "Pizza":
                favori_yemek_df = df.loc[df["pizza"] == 1]
            if yemek_turu == "Pork Recipes":
                favori_yemek_df = df.loc[df["pork"] == 1]
            if yemek_turu == "Quick Recipes":
                favori_yemek_df = df.loc[df["quick"] == 1]
            if yemek_turu == "Rice Recipes":
                favori_yemek_df = df.loc[df["rice"] == 1]
            if yemek_turu == "Salad Recipes":
                favori_yemek_df = df.loc[df["salad"] == 1]
            if yemek_turu == "Sandwich Recipes":
                favori_yemek_df = df.loc[df["sandwich"] == 1]
            if yemek_turu == "Seafood Recipes":
                favori_yemek_df = df.loc[df["denizden"] == 1]
            if yemek_turu == "Soup Recipes":
                favori_yemek_df = df.loc[df["soup"] == 1]
            if yemek_turu == "Vegan Recipes":
                favori_yemek_df = df.loc[df["vegan"] == 1]
            if yemek_turu == "Vegetarian Recipes":
                favori_yemek_df = df.loc[df["vegetarian"] == 1]


            # ---- Would you like to choose a cuisine? ---- #

            secenek2 = ["No", "Yes"]
            cuisine_y_n = st.sidebar.radio("Would you like to choose a cuisine?", secenek2)

            if cuisine_y_n == "Yes":
                cuisine = st.sidebar.selectbox("*You can type*",
                                               ['American', 'Crazilian', 'Caribbean', 'Chilean', 'Chinese', 'Creole',
                                                'Cuban',
                                                'Egyptian', 'English', 'Ethiopian', 'French', 'German', 'Greek', 'Indian',
                                                'Indonesian', 'Irish', 'Italian', 'Jamaican', 'Japanese', 'Korean',
                                                'Lebanese',
                                                'Malaysian', 'Mexican', 'Moroccan', 'Nigerian', 'Persian', 'Peruvian',
                                                'Polish',
                                                'Russian', 'Scottish', 'Southern', 'Spanish', 'Thai', 'Turkish',
                                                'Vietnamese'
                                                ])
                favori_yemek_df = favori_yemek_df[favori_yemek_df["search_terms"].str.contains(cuisine.lower())]

            # ---- Or, would you like to choose a diet? ---- #

else:
    df = select_meal(df, which_meal, servings)

    which_style = st.sidebar.selectbox("Which cooking style do you prefer:",
                                       ("Please choose", "I don't mind", 'Baked', 'Barbecue',
                                        'Braised', 'Casserole', 'Roast', 'Stew'),
                                       index=0)

    if which_style == "I don't mind":
        df = select_style(df, which_style, servings)

        secenek1 = ["Yes", "No"]
        diet_y_n = st.sidebar.radio("Do you follow any specific diet?", secenek1)

        if diet_y_n == "Yes":
            diet_turu = st.sidebar.selectbox(
                "Please select one of the diets",
                ('Atkins',
                 'Carb-Free',
                 'Dairy-Free',
                 'Diabetic',
                 'Flour-Free',
                 'Gluten-Free',
                 'Grain-Free',
                 'Healthy',
                 'Lactose-Free',
                 'Low-Calorie',
                 'Low-Carb',
                 'Low-Fat',
                 'Low-Sodium',
                 'Low-Sugar',
                 'Salt-Free',
                 'Sodium-Free',
                 'Sugar-Free'))
            favori_diet_df = pd.DataFrame()
            if diet_turu == "Atkins":
                favori_diet_df = df.loc[(df["diet"] == 1) & (df["search_terms"].str.contains("atkins"))]
            if diet_turu == "Carb-Free":
                favori_diet_df = df.loc[(df["diet"] == 1) & (df["search_terms"].str.contains("carb-free"))]
            if diet_turu == "Dairy-Free":
                favori_diet_df = df.loc[(df["diet"] == 1) & (df["search_terms"].str.contains("dairy-free"))]
            if diet_turu == "Diabetic":
                favori_diet_df = df.loc[(df["diet"] == 1) & (df["search_terms"].str.contains("diabetic"))]
            if diet_turu == "Flour-Free":
                favori_diet_df = df.loc[(df["diet"] == 1) & (df["search_terms"].str.contains("flour-free"))]
            if diet_turu == "Gluten-Free":
                favori_diet_df = df.loc[(df["diet"] == 1) & (df["search_terms"].str.contains("gluten-free"))]
            if diet_turu == "Healthy":
                favori_diet_df = df.loc[(df["diet"] == 1) & ((df["search_terms"].str.contains("diet"))
                                                             | (df["search_terms"].str.contains("diet"))
                                                             | (df["search_terms"].str.contains("light")))]
            if diet_turu == "Lactose-Free":
                favori_diet_df = df.loc[(df["diet"] == 1) & (df["search_terms"].str.contains("lactose-free"))]
            if diet_turu == "Low-Calorie":
                favori_diet_df = df.loc[(df["diet"] == 1) & (df["search_terms"].str.contains("low-calorie"))]
            if diet_turu == "Low-Carb":
                favori_diet_df = df.loc[(df["diet"] == 1) & (df["search_terms"].str.contains("low-carb"))]
            if diet_turu == "Low-Fat":
                favori_diet_df = df.loc[(df["diet"] == 1) & ((df["search_terms"].str.contains("low-fat"))
                                                             | (df["search_terms"].str.contains("lowfat")))]
            if diet_turu == "Low-Sodium":
                favori_diet_df = df.loc[(df["diet"] == 1) & (df["search_terms"].str.contains("low-sodium"))]
            if diet_turu == "Low-Sugar":
                favori_diet_df = df.loc[(df["diet"] == 1) & (df["search_terms"].str.contains("low-sugar"))]
            if diet_turu == "Salt-Free":
                favori_diet_df = df.loc[(df["diet"] == 1) & (df["search_terms"].str.contains("salt-free"))]
            if diet_turu == "Sodium-Free":
                favori_diet_df = df.loc[(df["diet"] == 1) & (df["search_terms"].str.contains("sodium-free"))]
            if diet_turu == "Sugar-Free":
                favori_diet_df = df.loc[(df["diet"] == 1) & ((df["search_terms"].str.contains("sugar-free"))
                                                             | (df["search_terms"].str.contains("sugarless")))]
                # if diet_y_n != "I dont":
                #     change_diet_choice("I dont")


        # ---- What is your Favorite? ---- #
        else:
            yemek_turu = st.sidebar.selectbox(
                "Please select one of them",
                ("Beef Recipes",
                 "Chicken Recipes",
                 "Diet Recipes",
                 "Dessert",
                 "Lamb Recipes",
                 "Noodle Recipes",
                 "Pasta Recipes",
                 "Pie Recipes",
                 "Pizza",
                 "Pork Recipes",
                 "Quick Recipes",
                 "Rice Recipes",
                 "Salad Recipes",
                 "Sandwich Recipes",
                 "Seafoods",
                 "Soup Recipes",
                 "Vegan Recipes",
                 "Vegetarian Recipes"
                 ))
            favori_yemek_df = pd.DataFrame()
            if yemek_turu == "Beef Recipes":
                favori_yemek_df = df.loc[df["dana"]== 1]
            if yemek_turu == "Chicken Recipes":
                favori_yemek_df = df.loc[df["tavuk"] == 1]
            if yemek_turu == "Diet Recipes":
                favori_yemek_df = df.loc[df["diet"] == 1]
            #if yemek_turu == "Drinks":
                #favori_yemek_df = df.loc[df["içecek"] == 1]
            if yemek_turu == "Dessert":
                favori_yemek_df = df.loc[df["tatli"] == 1]
            if yemek_turu == "Tatlılar":
                favori_yemek_df = df.loc[df["tatli"] == 1]
            if yemek_turu == "Lamb Recipes":
                favori_yemek_df = df.loc[df["kuzu"] == 1]
            if yemek_turu == "Noodle Recipes":
                favori_yemek_df = df.loc[df["noodles"] == 1]
            if yemek_turu == "Pasta Recipes":
                favori_yemek_df = df.loc[df["pasta"] == 1]
            if yemek_turu == "Pie Recipes":
                favori_yemek_df = df.loc[df["pie"] == 1]
            if yemek_turu == "Pizza":
                favori_yemek_df = df.loc[df["pizza"] == 1]
            if yemek_turu == "Pork Recipes":
                favori_yemek_df = df.loc[df["pork"] == 1]
            if yemek_turu == "Quick Recipes":
                favori_yemek_df = df.loc[df["quick"] == 1]
            if yemek_turu == "Rice Recipes":
                favori_yemek_df = df.loc[df["rice"] == 1]
            if yemek_turu == "Salad Recipes":
                favori_yemek_df = df.loc[df["salad"] == 1]
            if yemek_turu == "Sandwich Recipes":
                favori_yemek_df = df.loc[df["sandwich"] == 1]
            if yemek_turu == "Seafood Recipes":
                favori_yemek_df = df.loc[df["denizden"] == 1]
            if yemek_turu == "Soup Recipes":
                favori_yemek_df = df.loc[df["soup"] == 1]
            if yemek_turu == "Vegan Recipes":
                favori_yemek_df = df.loc[df["vegan"] == 1]
            if yemek_turu == "Vegetarian Recipes":
                favori_yemek_df = df.loc[df["vegetarian"] == 1]


            # ---- Would you like to choose a cuisine? ---- #

            secenek2 = ["No", "Yes"]
            cuisine_y_n = st.sidebar.radio("Would you like to choose a cuisine?", secenek2)

            if cuisine_y_n == "Yes":
                cuisine = st.sidebar.selectbox("*You can type*",
                                                 ['American', 'Crazilian', 'Caribbean', 'Chilean', 'Chinese', 'Creole', 'Cuban',
                                                  'Egyptian', 'English', 'Ethiopian', 'French', 'German', 'Greek', 'Indian',
                                                  'Indonesian', 'Irish', 'Italian', 'Jamaican', 'Japanese', 'Korean', 'Lebanese',
                                                  'Malaysian', 'Mexican', 'Moroccan', 'Nigerian', 'Persian', 'Peruvian', 'Polish',
                                                  'Russian', 'Scottish', 'Southern', 'Spanish', 'Thai', 'Turkish', 'Vietnamese'
                                                  ])
                favori_yemek_df = favori_yemek_df[favori_yemek_df["search_terms"].str.contains(cuisine.lower())]

            # ---- Or, would you like to choose a diet? ---- #

    else:
        df = select_style(df, which_style, servings)

        secenek1 = ["Yes", "No"]
        diet_y_n = st.sidebar.radio("Do you follow any specific diet?", secenek1)

        if diet_y_n == "Yes":
            diet_turu = st.sidebar.selectbox(
                "Please select one of the diets",
                ('Atkins',
                 'Carb-Free',
                 'Dairy-Free',
                 'Diabetic',
                 'Flour-Free',
                 'Gluten-Free',
                 'Grain-Free',
                 'Healthy',
                 'Lactose-Free',
                 'Low-Calorie',
                 'Low-Carb',
                 'Low-Fat',
                 'Low-Sodium',
                 'Low-Sugar',
                 'Salt-Free',
                 'Sodium-Free',
                 'Sugar-Free'
                 ))
            favori_diet_df = pd.DataFrame()
            if diet_turu == "Atkins":
                favori_diet_df = df.loc[(df["diet"] == 1) & (df["search_terms"].str.contains("atkins"))]
            if diet_turu == "Carb-Free":
                favori_diet_df = df.loc[(df["diet"] == 1) & (df["search_terms"].str.contains("carb-free"))]
            if diet_turu == "Dairy-Free":
                favori_diet_df = df.loc[(df["diet"] == 1) & (df["search_terms"].str.contains("dairy-free"))]
            if diet_turu == "Diabetic":
                favori_diet_df = df.loc[(df["diet"] == 1) & (df["search_terms"].str.contains("diabetic"))]
            if diet_turu == "Flour-Free":
                favori_diet_df = df.loc[(df["diet"] == 1) & (df["search_terms"].str.contains("flour-free"))]
            if diet_turu == "Gluten-Free":
                favori_diet_df = df.loc[(df["diet"] == 1) & (df["search_terms"].str.contains("gluten-free"))]
            if diet_turu == "Healthy":
                favori_diet_df = df.loc[(df["diet"] == 1) & ((df["search_terms"].str.contains("diet"))
                                                             | (df["search_terms"].str.contains("diet"))
                                                             | (df["search_terms"].str.contains("light")))]
            if diet_turu == "Lactose-Free":
                favori_diet_df = df.loc[(df["diet"] == 1) & (df["search_terms"].str.contains("lactose-free"))]
            if diet_turu == "Low-Calorie":
                favori_diet_df = df.loc[(df["diet"] == 1) & (df["search_terms"].str.contains("low-calorie"))]
            if diet_turu == "Low-Carb":
                favori_diet_df = df.loc[(df["diet"] == 1) & (df["search_terms"].str.contains("low-carb"))]
            if diet_turu == "Low-Fat":
                favori_diet_df = df.loc[(df["diet"] == 1) & ((df["search_terms"].str.contains("low-fat"))
                                                             | (df["search_terms"].str.contains("lowfat")))]
            if diet_turu == "Low-Sodium":
                favori_diet_df = df.loc[(df["diet"] == 1) & (df["search_terms"].str.contains("low-sodium"))]
            if diet_turu == "Low-Sugar":
                favori_diet_df = df.loc[(df["diet"] == 1) & (df["search_terms"].str.contains("low-sugar"))]
            if diet_turu == "Salt-Free":
                favori_diet_df = df.loc[(df["diet"] == 1) & (df["search_terms"].str.contains("salt-free"))]
            if diet_turu == "Sodium-Free":
                favori_diet_df = df.loc[(df["diet"] == 1) & (df["search_terms"].str.contains("sodium-free"))]
            if diet_turu == "Sugar-Free":
                favori_diet_df = df.loc[(df["diet"] == 1) & ((df["search_terms"].str.contains("sugar-free"))
                                                             | (df["search_terms"].str.contains("sugarless")))]
                # if diet_y_n != "I dont":
                #     change_diet_choice("I dont")


        # ---- What is your Favorite? ---- #
        else:
            yemek_turu = st.sidebar.selectbox(
                "Please select one of them",
                ("Beef Recipes",
                 "Chicken Recipes",
                 "Diet Recipes",
                 "Dessert",
                 "Lamb Recipes",
                 "Noodle Recipes",
                 "Pasta Recipes",
                 "Pie Recipes",
                 "Pizza",
                 "Pork Recipes",
                 "Quick Recipes",
                 "Rice Recipes",
                 "Salad Recipes",
                 "Sandwich Recipes",
                 "Seafoods",
                 "Soup Recipes",
                 "Vegan Recipes",
                 "Vegetarian Recipes"
                 ))
            favori_yemek_df = pd.DataFrame()
            if yemek_turu == "Beef Recipes":
                favori_yemek_df = df.loc[df["dana"] == 1]
            if yemek_turu == "Chicken Recipes":
                favori_yemek_df = df.loc[df["tavuk"] == 1]
            if yemek_turu == "Diet Recipes":
                favori_yemek_df = df.loc[df["diet"] == 1]
            # if yemek_turu == "Drinks":
            # favori_yemek_df = df.loc[df["içecek"] == 1]
            if yemek_turu == "Dessert":
                favori_yemek_df = df.loc[df["tatli"] == 1]
            if yemek_turu == "Tatlılar":
                favori_yemek_df = df.loc[df["tatli"] == 1]
            if yemek_turu == "Lamb Recipes":
                favori_yemek_df = df.loc[df["kuzu"] == 1]
            if yemek_turu == "Noodle Recipes":
                favori_yemek_df = df.loc[df["noodles"] == 1]
            if yemek_turu == "Pasta Recipes":
                favori_yemek_df = df.loc[df["pasta"] == 1]
            if yemek_turu == "Pie Recipes":
                favori_yemek_df = df.loc[df["pie"] == 1]
            if yemek_turu == "Pizza":
                favori_yemek_df = df.loc[df["pizza"] == 1]
            if yemek_turu == "Pork Recipes":
                favori_yemek_df = df.loc[df["pork"] == 1]
            if yemek_turu == "Quick Recipes":
                favori_yemek_df = df.loc[df["quick"] == 1]
            if yemek_turu == "Rice Recipes":
                favori_yemek_df = df.loc[df["rice"] == 1]
            if yemek_turu == "Salad Recipes":
                favori_yemek_df = df.loc[df["salad"] == 1]
            if yemek_turu == "Sandwich Recipes":
                favori_yemek_df = df.loc[df["sandwich"] == 1]
            if yemek_turu == "Seafood Recipes":
                favori_yemek_df = df.loc[df["denizden"] == 1]
            if yemek_turu == "Soup Recipes":
                favori_yemek_df = df.loc[df["soup"] == 1]
            if yemek_turu == "Vegan Recipes":
                favori_yemek_df = df.loc[df["vegan"] == 1]
            if yemek_turu == "Vegetarian Recipes":
                favori_yemek_df = df.loc[df["vegetarian"] == 1]


            # ---- Would you like to choose a cuisine? ---- #

            secenek2 = ["No", "Yes"]
            cuisine_y_n = st.sidebar.radio("Would you like to choose a cuisine?", secenek2)

            if cuisine_y_n == "Yes":
                cuisine = st.sidebar.selectbox("*You can type*",
                                               ['American', 'Crazilian', 'Caribbean', 'Chilean', 'Chinese', 'Creole',
                                                'Cuban',
                                                'Egyptian', 'English', 'Ethiopian', 'French', 'German', 'Greek', 'Indian',
                                                'Indonesian', 'Irish', 'Italian', 'Jamaican', 'Japanese', 'Korean',
                                                'Lebanese',
                                                'Malaysian', 'Mexican', 'Moroccan', 'Nigerian', 'Persian', 'Peruvian',
                                                'Polish',
                                                'Russian', 'Scottish', 'Southern', 'Spanish', 'Thai', 'Turkish',
                                                'Vietnamese'
                                                ])
                favori_yemek_df = favori_yemek_df[favori_yemek_df["search_terms"].str.contains(cuisine.lower())]

            # ---- Or, would you like to choose a diet? ---- #




# ---- Main Screen ---- #


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


diger = load_lottieurl("https://lottie.host/7b794219-f74e-42dd-a8ad-26b78ec7d7a4/yyVc2FxcgP.json")

st.write('# What would you like to cook today?')
col1, col2, col3 = st.columns((1,3,1))
with col2:
    st_lottie(diger)
st.subheader("Are you ready to cook a new recipe?")

with stylable_container(
        key="yellow_button",
        css_styles="""
        button {
            background-color: #FFBC42;
            color: white;
            border-radius: 5px;
        }
        """,
):
    tarifler_gelsin = st.button("**Here are our superstar recipes**")


def urun_getir(df, adet=20):
    name = df["name"].tolist()
    ingredients = df["ingredients_raw_str"].tolist()
    steps = df["steps"].tolist()

    if adet > len(name):
        adet = len(name)
    if len(name) == 0:
        st.write("We will start to add at least one recipe for this filtering 👩‍🍳")

    for a in range(adet):
        st.subheader(f':red[{name[a]}]')
        tab1, tab2, tab3 = st.tabs(["Calori & Carbon Footprint", "Ingredients", "Cooking Steps"])
        with tab1:
            st.write("Calori & Carbon Footprint")
        with tab2:
            st.write(ingredients[a])
        with tab3:
            st.write(steps[a])


if tarifler_gelsin:
    if which_meal == "Please choose":
        st.write("Please choose a meal on the sidebar 👈")
    elif which_style == "Please choose":
        st.write("Please choose a style on the sidebar 👈")
    elif diet_y_n == "Yes":
        with st.container():
            urun_getir(favori_diet_df, adet=20)
    else:
        with st.container():
            urun_getir(favori_yemek_df, adet=20)





#------Görsel ekleme------#
#from googleapiclient.discovery import build
#def google_image_search(query, api_key, cse_id, num=1):
#    service = build("customsearch", "v1", developerKey=api_key)
#    res = service.cse().list(q=query, cx=cse_id, searchType='image', num=num).execute()
#    return res['items'][0]['link']

# Google search için api ve cse id'lerim.
#api_key = "AIzaSyDld5RyAGvlO3KNzHLP3R2CCZV_Uz8cYbg"
#cse_id = "c42eb241a8bb244c0"
#buraya seçilen yemeğin ismi gelecek
#query = "kuru fasülye"
#Fonksiyon görselin url'sini çekiyor..
#image_url1 = google_image_search(query1, api_key, cse_id)
#print(image_url1)

# st.image(image_url1, caption=query1)















