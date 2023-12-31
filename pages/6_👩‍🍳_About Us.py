import streamlit as st

st.set_page_config(page_title="About Us | CookitNow", page_icon="👩‍🍳")

st.title("Who Are The Culinary Chiefs Behind This Journey?")
st.write("##")

# --- Ayça ---
with st.container():
    sol, sag = st.columns((1, 3))
    with sol:
        st.write("##")
        st.write("##")
        st.image("Görseller_Streamlit/chiefs/ayca_maden.jpg")
    with sag:
        st.subheader("Ayça Maden")
        st.write(
            """
            Ayça Maden serves as an Assistant Professor at Beykent University. Since 2014, she has been involved in 
            administrative and academic work at various universities. Her main goal is to become a leading researcher 
            and an effective educator in her field. She completed her PhD in Industrial Engineering at Galatasaray 
            University, with a thesis titled "Evaluation of Blockchain Technology for Process Improvements in Supply 
            Chains Using Fuzzy QFD. 
            Some of Ayça Maden's publications include topics such as the evaluation of metaverse characteristics using
            scenario-based Fuzzy Cognitive Map, influential factor analysis for cloud computing technology service 
            providers, and she also has experience teaching various subjects.
            """)
        i1, l1, i2, l2, i3, l3 = st.columns((0.1, 0.2, 0.1, 0.2, 0.1, 0.2))
        with i1:
            st.image("Görseller_Streamlit/icons/linkedin.png")
        with l1:
            url = "https://www.linkedin.com/in/ay%C3%A7a-maden-ph-d-b1794843"
            st.write("[LinkedIn](%s)" % url)
        with i2:
            st.write(" ")
        with l2:
            st.write(" ")
        with i3:
            st.write(" ")
        with l3:
            st.write(" ")
        st.write("---")


# --- Zübeyde ---
with st.container():
    sol, sag = st.columns((1, 3))
    with sol:
        st.write("##")
        st.write("##")
        st.image("Görseller_Streamlit/chiefs/zubeyde_er.jpg")
with sag:
    st.subheader("Zübeyde Er")
    st.write(
        """
        I am a Warehouse Manager. I completed my bachelor and master studies in Physics at Namik Kemal University. 
        I have always been interested in data science and aimed to obtain accurate information by playing with data. 
        By expanding my curiosity with Machine Learning, I continue my journey in the field of Data Science, where I 
        get different excitement at every step.
        """)
    i1, l1, i2, l2, i3, l3, i4, l4= st.columns((0.1, 0.2, 0.1, 0.2, 0.1, 0.2, 0.1, 0.2))
    with i1:
        st.image("Görseller_Streamlit/icons/linkedin.png")
    with l1:
        url = "https://www.linkedin.com/in/z%C3%BCbeyde-er-b0285217b"
        st.write("[LinkedIn](%s)" % url)
    with i2:
        st.image("Görseller_Streamlit/icons/github-mark.png")
    with l2:
        url = "https://github.com/ZubeydEr"
        st.write("[GitHub](%s)" % url)
    with i3:
        st.image("Görseller_Streamlit/icons/medium.png")
    with l3:
        url = "https://medium.com/@zubeyde.physics"
        st.write("[Medium](%s)" % url)
    with i4:
        st.image("Görseller_Streamlit/icons/kaggle.png")
    with l4:
        url = "https://www.kaggle.com/zubeydeer"
        st.write("[Kaggle](%s)" % url)
    st.write("---")


# --- Burak ---
with st.container():
    sol, sag = st.columns((1, 3))
    with sol:
        st.write("##")
        st.write("##")
        st.image("Görseller_Streamlit/chiefs/burak_sevim.jpg")
    with sag:
        st.subheader("Burak Sevim")
        st.write(
            """
            I'm an industrial engineer with 15 years' experience, focusing on public transportation planning, operations
            management, and optimization. After 13 years in various roles in Istanbul, a complex city for public 
            transportation, I've spent the past year in senior management overseeing public transportation in Mecca, 
            Saudi Arabia. Currently, I'm dedicated to data science, analyzing our vast operational data to predict 
            trends and develop algorithms for more efficient public transportation. I'm also working on my doctoral 
            research, which includes creating such an algorithm.
            """)
        i1, l1, i2, l2, i3, l3 = st.columns((0.1, 0.2, 0.1, 0.2, 0.1, 0.2))
        with i1:
            st.image("Görseller_Streamlit/icons/linkedin.png")
        with l1:
            url = "https://www.linkedin.com/in/buraksevim/"
            st.write("[LinkedIn](%s)" % url)
        with i2:
            st.image("Görseller_Streamlit/icons/github-mark.png")
        with l2:
            url = "https://github.com/brksvm"
            st.write("[GitHub](%s)" % url)
        with i3:
            st.image("Görseller_Streamlit/icons/kaggle.png")
        with l3:
            url = "https://www.kaggle.com/buraksevim"
            st.write("[Kaggle](%s)" % url)
        st.write("---")


# --- Emre ---
with st.container():
    sol, sag = st.columns((1, 3))
    with sol:
        st.write("##")
        st.write("##")
        st.image("Görseller_Streamlit/chiefs/emre_ates.jpg")
    with sag:
        st.subheader("Emre Ateş")
        st.write(
            """
            As a seasoned marketing professional, I bring a wealth of expertise in digital marketing, a proficiency with
            Google Tools, and a strong background in optimizing UX/UI and website strategy. My career journey has 
            spanned diverse industries, ranging from paper and packaging to video gaming and fintech. My recent 
            commitment to Data Scientist training is a testament to my profound passion for this field, as I aspire to 
            further advance my skills in data analysis and machine learning, pushing the boundaries of what's possible.
            """)
        i1, l1, i2, l2, i3, l3 = st.columns((0.1, 0.2, 0.1, 0.2, 0.1, 0.2))
        with i1:
            st.image("Görseller_Streamlit/icons/linkedin.png")
        with l1:
            url = "https://www.linkedin.com/in/emreates/"
            st.write("[LinkedIn](%s)" % url)
        with i2:
            st.image("Görseller_Streamlit/icons/github-mark.png")
        with l2:
            url = "https://github.com/REAtes"
            st.write("[GitHub](%s)" % url)
        with i3:
            st.image("Görseller_Streamlit/icons/medium.png")
        with l3:
            url = "https://medium.com/@emre_ates"
            st.write("[Medium](%s)" % url)
        st.write("---")


# --- Mehmet ---
with st.container():
    sol, sag = st.columns((1, 3))
    with sol:
        st.write("##")
        st.write("##")
        st.image("Görseller_Streamlit/chiefs/mehmet_helva.jpg")
    with sag:
        st.subheader("Mehmet Helva")
        st.write(
            """I am a research assistant at Mimar Sinan Fine Arts University, 
            conducting studies in theoretical physics and on a continuous journey of 
            personal and professional growth. I have a keen interest
             in data science and am eager to further develop my expertise in 
             this field. My curiosity extends to machine learning, LLM's, deep learning 
             and I have a particular fondness for the Python programming language.""")
        i1, l1, i2, l2, i3, l3 = st.columns((0.1, 0.2, 0.1, 0.2, 0.1, 0.2))
        with i1:
            st.image("Görseller_Streamlit/icons/linkedin.png")
        with l1:
            url = "https://www.linkedin.com/in/mehmet-helva-b2993a273/"
            st.write("[LinkedIn](%s)" % url)
        with i2:
            st.image("Görseller_Streamlit/icons/github-mark.png")
        with l2:
            url = "https://github.com/mhelva"
            st.write("[GitHub](%s)" % url)
        with i3:
            st.image("Görseller_Streamlit/icons/medium.png")
        with l3:
            url = "https://medium.com/@m.helva34"
            st.write("[Medium](%s)" % url)


