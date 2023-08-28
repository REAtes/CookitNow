import pandas as pd
import numpy as np
import streamlit as st
from streamlit_option_menu import option_menu


with st.container():
    st.selectbox('# Yemek Türü Seç', ['Kuzu Etli Tarifler',
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