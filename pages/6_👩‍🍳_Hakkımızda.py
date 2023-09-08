import streamlit as st

st.set_page_config(page_title="Hakkımızda | GastroMiuul", page_icon="👩‍🍳")

st.title("Bu işin mutfağında kim var?")
st.write("##")

# --- Ayça ---
with st.container():
    sol, sag = st.columns((1, 3))
    with sol:
        st.write("##")
        st.write("##")
        st.image("Görseller_Streamlit/ayca_maden.jpg")
    with sag:
        st.subheader("Ayça Madenci")
        st.write(
            """
            Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of 
            typeand scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into 
            electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of 
            Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus 
            Page Maker including versions of Lorem Ipsum.
            """)
        st.write("---")


# --- Zübeyde ---
with st.container():
    sol, sag = st.columns((1, 3))
    with sol:
        st.write("##")
        st.write("##")
        st.image("Görseller_Streamlit/zubeyde_er.jpg")
with sag:
    st.subheader("Zübeyde Er")
    st.write(
        """
        Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of 
        typeand scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into 
        electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of 
        Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus 
        Page Maker including versions of Lorem Ipsum.
        """)
    st.write("---")


# --- Burak ---
with st.container():
    sol, sag = st.columns((1, 3))
    with sol:
        st.write("##")
        st.write("##")
        st.image("Görseller_Streamlit/burak_sevim.jpg")
    with sag:
        st.subheader("Burak Sevim")
        st.write(
            """
            Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of 
            typeand scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into 
            electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of 
            Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus 
            Page Maker including versions of Lorem Ipsum.
            """)
        st.write("---")

# --- Emre ---
with st.container():
    sol, sag = st.columns((1, 3))
    with sol:
        st.write("##")
        st.write("##")
        st.image("Görseller_Streamlit/emre_ates.jpg")
    with sag:
        st.subheader("Emre Ateş")
        st.write(
            """
            Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of 
            typeand scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into 
            electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of 
            Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus 
            Page Maker including versions of Lorem Ipsum.
            """)
        st.write("---")


# --- Mehmet ---
with st.container():
    sol, sag = st.columns((1, 3))
    with sol:
        st.write("##")
        st.write("##")
        st.image("Görseller_Streamlit/mehmet_helva.jpg")
    with sag:
        st.subheader("Mehmet Helva")
        st.write(
            """
            Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of 
            typeand scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into 
            electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of 
            Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus 
            Page Maker including versions of Lorem Ipsum.
            """)
        st.write("---")


