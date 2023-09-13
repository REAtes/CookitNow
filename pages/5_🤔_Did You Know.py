import pandas as pd
import numpy as np
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
from streamlit_extras.metric_cards import style_metric_cards


st.set_page_config(page_title="Did You Know This | GastroMiuul", page_icon="🤔")

col1, col2, col3= st.columns(3)
with col2:
    st.image("Görseller_Streamlit/diger/2.gif")

st.subheader(" :red[The Facts Of Food Waste]")
with st.expander("Read more"):
    st.write(
        """
    1. Roughly one-third of the food produced that is intended for human consumption every year- around 1.3 billion tons and valued at USD$1 trillion- is wasted or lost. This is enough to feed 3 billion people. 
    2. Food waste ends up wasting a quarter of our water supply in the form of uneaten food. That’s equated to USD$172billion in wasted water.
    3. Taking into account all the resources used to grow food, food waste uses up to 21% of freshwater, 19% of fertilisers, 18% of cropland, and 21% of landfill volume.
    4. The water used to produce the food wasted could be used by 9 billion people at around 200 litres per person per day. 
    5. The food currently wasted in Europe could feed 200 million people, in Latin America 300 million people, and in Africa 300 million people. 
    6. Annual per capita waste by consumers is between 95-115 kiograms a year for Europeans and North Americans, while in the south and southeastern Asia, it is 6-11kgs. 
    7. Food loss and waste account for about 4.4 gigatonnes of greenhouse gas emissions annually. 
    8. If food loss was a country, it would be the third-largest greenhouse gas emitter, behind China and the US.
    9. Breaking it down by food group, losses, and waste per year are roughly 30% for cereals, 40-50% for root crops and fruit and vegetables, 20% for oil seed and meat and dairy, and 35% for fish. 
    """)

st.write("##")

st.subheader(" :red[Fun Facts Of Vegetables]")
with st.expander("Read more"):
    st.write(
        """
    1. Roughly one-third of the food produced that is intended for human consumption every year- around 1.3 billion tons and valued at USD$1 trillion- is wasted or lost. This is enough to feed 3 billion people. 
    2. Food waste ends up wasting a quarter of our water supply in the form of uneaten food. That’s equated to USD$172billion in wasted water.
    3. Taking into account all the resources used to grow food, food waste uses up to 21% of freshwater, 19% of fertilisers, 18% of cropland, and 21% of landfill volume.
    4. The water used to produce the food wasted could be used by 9 billion people at around 200 litres per person per day. 
    5. The food currently wasted in Europe could feed 200 million people, in Latin America 300 million people, and in Africa 300 million people. 
    6. Annual per capita waste by consumers is between 95-115 kiograms a year for Europeans and North Americans, while in the south and southeastern Asia, it is 6-11kgs. 
    7. Food loss and waste account for about 4.4 gigatonnes of greenhouse gas emissions annually. 
    8. If food loss was a country, it would be the third-largest greenhouse gas emitter, behind China and the US.
    9. Breaking it down by food group, losses, and waste per year are roughly 30% for cereals, 40-50% for root crops and fruit and vegetables, 20% for oil seed and meat and dairy, and 35% for fish. 
    """)

st.write("##")

st.subheader(" :red[Fun Facts Of Fruits]")
with st.expander("Read more"):
    st.write(
            """
        1. Apples, peaches and raspberries are all members of the rose family.
        2. Pumpkins and avocados are fruits not a vegetable.
        3. Apples float in water because they are 25% air
        4. A half-cup of figs has as much calcium as a half-cup of milk.
        5. Green fruits help make your bones and teeth strong.
        6. Not all oranges are in fact orange
        7. Apples give you more energy than coffee
        8. Each pineapple plant only produces one pineapple per year
        9. Bananas have a natural antacid effect in the body, so if you suffer from heartburn, try eating a banana for soothing relief.
        10. A strawberry isn’t an actual berry, but a banana is!
            """)
st.write("##")

st.subheader(" :red[Fun Facts of Foods]")
with st.expander("Read more"):
    st.write(
        """
    1.	Pound cake got its name from the original recipe which called for a pound each of the ingredients needed--eggs, sugar, flour, and butter. 
    2.	The creation of the tea bag was an accident. A merchant sewed tiny bags to send out sample of his tea to customers and the trend caught on and was later commercialized. 
    3.	Peanuts aren't actually a nut. Instead, they are part of the legume family. 
    4.	When cranberries are ripe, they can bounce like rubber balls.
    5.	At one point in time, chocolate was used as a form of currency. 
    6.	The next time you decide to cook dinner using the sous vide method, add a ping pong ball or two as they can be used to prevent the water from evaporating. 
    7.	Cutting onions under cold running water or after briefly placing them in the freezer will keep your eyes from watering. 
    8.	Ice cubes can help keep garbage disposal blades sharp so throw a few down the drain while your disposal is running every once in a while. 
    9.	Despite frequently being used interchangeably, yams and sweet potatoes are not the same thing. Yams are less sweet than sweet potatoes and are cylindrical in shape with rough, brown, bark-like skin. They are also harder to find in the U.S.
    10.	In the 1800s, ketchup was considered a medicine and used to treat several maladies including diarrhea.
        """)

# st.container()
# col1, col2, col3, col4 = st.columns(4)
# with col1:
#     st.subheader("The Facts Of Food Waste")
#     st.write(
#         """
#     1. Roughly one-third of the food produced that is intended for human consumption every year- around 1.3 billion tons and valued at USD$1 trillion- is wasted or lost. This is enough to feed 3 billion people.
#     2. Food waste ends up wasting a quarter of our water supply in the form of uneaten food. That’s equated to USD$172billion in wasted water.
#     3. Taking into account all the resources used to grow food, food waste uses up to 21% of freshwater, 19% of fertilisers, 18% of cropland, and 21% of landfill volume.
#     4. The water used to produce the food wasted could be used by 9 billion people at around 200 litres per person per day.
#     5. The food currently wasted in Europe could feed 200 million people, in Latin America 300 million people, and in Africa 300 million people.
#     6. Annual per capita waste by consumers is between 95-115 kiograms a year for Europeans and North Americans, while in the south and southeastern Asia, it is 6-11kgs.
#     7. Food loss and waste account for about 4.4 gigatonnes of greenhouse gas emissions annually.
#     8. If food loss was a country, it would be the third-largest greenhouse gas emitter, behind China and the US.
#     9. Breaking it down by food group, losses, and waste per year are roughly 30% for cereals, 40-50% for root crops and fruit and vegetables, 20% for oil seed and meat and dairy, and 35% for fish.
#     """)
# with col2:
#     st.subheader("Fun Facts Of Vegetables")
#     st.write(
#         """
#     1.	Bell peppers are usually sold green, but they can also be red, purple or yellow.
#     2.	Tomatoes are very high in the carotenoid Lycopene; eating foods with carotenoids can lower your risk of cancer.
#     3.	Other vegetables high in carotenoids are carrots, spinach, sweet potatoes, and collard greens.
#     4.	Most of the nutrients in a potato reside just below the skin layer.
#     5.	A horn worm can eat an entire tomato plant by itself in one day!
#     6.	In the United States, more tomatoes are consumed than any other single fruit or vegetable!
#     7.	California produces almost all of the broccoli sold in the United States.
#     8.	White potatoes were first cultivated by local Indians in the Andes Mountains of South America.
#     9.	Yams and sweet potatoes are not the same thing!
#     10.	A baked potato (with skin) is a good source of dietary fiber (4 grams).
#     """)
#
# with col3:
#     st.subheader("Fun Facts Of Fruits")  # subheader başlık atarken kullanılıyor
#     st.write(
#         """
#     1. Apples, peaches and raspberries are all members of the rose family.
#     2. Pumpkins and avocados are fruits not a vegetable.
#     3. Apples float in water because they are 25% air
#     4. A half-cup of figs has as much calcium as a half-cup of milk.
#     5. Green fruits help make your bones and teeth strong.
#     6. Not all oranges are in fact orange
#     7. Apples give you more energy than coffee
#     8. Each pineapple plant only produces one pineapple per year
#     9. Bananas have a natural antacid effect in the body, so if you suffer from heartburn, try eating a banana for soothing relief.
#     10. A strawberry isn’t an actual berry, but a banana is!
#         """)
# with col4:
#     st.subheader("Fun Facts of Foods")  # subheader başlık atarken kullanılıyor
#     st.write(
#     """
# 1.	Pound cake got its name from the original recipe which called for a pound each of the ingredients needed--eggs, sugar, flour, and butter.
# 2.	The creation of the tea bag was an accident. A merchant sewed tiny bags to send out sample of his tea to customers and the trend caught on and was later commercialized.
# 3.	Peanuts aren't actually a nut. Instead, they are part of the legume family.
# 4.	When cranberries are ripe, they can bounce like rubber balls.
# 5.	At one point in time, chocolate was used as a form of currency.
# 6.	The next time you decide to cook dinner using the sous vide method, add a ping pong ball or two as they can be used to prevent the water from evaporating.
# 7.	Cutting onions under cold running water or after briefly placing them in the freezer will keep your eyes from watering.
# 8.	Ice cubes can help keep garbage disposal blades sharp so throw a few down the drain while your disposal is running every once in a while.
# 9.	Despite frequently being used interchangeably, yams and sweet potatoes are not the same thing. Yams are less sweet than sweet potatoes and are cylindrical in shape with rough, brown, bark-like skin. They are also harder to find in the U.S.
# 10.	In the 1800s, ketchup was considered a medicine and used to treat several maladies including diarrhea.
#     """)
#
