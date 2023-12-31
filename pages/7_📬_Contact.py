import pandas as pd
import numpy as np
import streamlit as st
import requests
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(page_title="Contact | CookitNow", page_icon="📬")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


lottie_coding3 = load_lottieurl("https://lottie.host/8b6bc538-6f20-43f4-b425-b102abf6cdce/yADpOUyIij.json")


# ---- Use Local CSS ---


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")



with st.container():
    st.header("Get in Touch!")
    st.write("""We’re here to help! If you have any issues.""")

    contact_form = """
    <form action="https://formsubmit.io/send/r.emreates@gmail.com" method="POST">
        <input type="text" name="name" placeholder="Name and surname" required>
        <input type="email" name="email" placeholder="E-mail address" required>  
        <textarea name="message" placeholder="Your message..." required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_col, righy_col = st.columns(2)
    with left_col:
        st.markdown(contact_form, unsafe_allow_html=True)
    with righy_col:
        st_lottie(lottie_coding3)