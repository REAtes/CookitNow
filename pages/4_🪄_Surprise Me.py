import pandas as pd
import numpy as np
import streamlit as st
import requests
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
from streamlit_extras.metric_cards import style_metric_cards

st.set_page_config(page_title="Surprise Me | GastroMiuul", page_icon="🪄")


# ---- Main Screen  ---- #
import streamlit as st

on = st.toggle('Activate feature')

if on:
    st.write('Feature activated!')

"""overwrite deneme"""