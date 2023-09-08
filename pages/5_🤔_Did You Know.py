import pandas as pd
import numpy as np
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
from streamlit_extras.metric_cards import style_metric_cards


st.set_page_config(page_title="Did You Know This | GastroMiuul", page_icon="🤔")

# --- Zübeyde ---
with st.container():  # with st.container() ile bir çerçeve çizip içinde çalışıyormuş gibi düşün. alt satıra inip boşluk bıraktıktan sonra çerçevenin içindesin. ama en solran yazmaya başladığın anda çerçeveden çıkarsın
    sol, sag = st.columns((1, 3))  #st.columns sayfaya kolon ekler. burada 2 eklenmiş. 4 eklemek istersen col1, col2, col3, col4 = st.columns dersin. parantez içinde yarattığın kolon sayısı kadar yani (4) girersen; tüm kolonların genişliğini eşit olarak 4e böler. ama kimisi geniş kimisi dar istersen şöyle yapailirsin ((1, 2, 2, 1))
    with sol: # with sol dedikten sonra sol ismini verdiğim kolonun içini dolduruyorum
        st.write("##") # tüm yazım işlemleri st.write ile. ("##") bu boşluk bırak demek
        st.write("##")
        st.image("Görseller_Streamlit/zubeyde_er.jpg")  # bu imajı getir demek
with sag: # burada sağ isimli kolonun içini dolduruyorum.
    st.subheader("Zübeyde Er")  # subheader başlık atarken kullanılıyor
    st.write(
        """
        Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of 
        typeand scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into 
        electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of 
        Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus 
        Page Maker including versions of Lorem Ipsum.
        """)
    st.write("---")  # bu da sayfaya çizgi eklemek için

