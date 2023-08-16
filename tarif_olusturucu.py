import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import seaborn as sns
from matplotlib import pyplot as plt
import missingno as msno
from datetime import date
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import LocalOutlierFactor
from sklearn.preprocessing import MinMaxScaler, LabelEncoder, StandardScaler, RobustScaler

pd.set_option('display.max_columns', 500)
pd.set_option("display.width", 3000)
tarifler = pd.read_csv("archive/Food_Ingredients.csv")

tarifler.head()
# eksik gozlem var mı yok mu sorgusu
tarifler.isnull().values.any()

# degiskenlerdeki eksik deger sayisi
tarifler.isnull().sum()

# degiskenlerdeki tam deger sayisi (dolu satırların toplamı)
tarifler.notnull().sum()

# veri setindeki toplam eksik deger sayisi
tarifler.isnull().sum().sum()

# en az bir tane eksik degere sahip olan gözlem birimleri (satır)
tarifler[tarifler.isnull().any(axis=1)]

# eksik değerleri hızlıca silmek
tarifler.dropna(inplace=True)


def check_df(dataframe):
    print("#################### Shape ####################")
    print(dataframe.shape)
    print("#################### Types ####################")
    print(dataframe.dtypes)
    print("#################### Num of Unique ####################")
    print(dataframe.nunique())  # "dataframe.nunique(dropna=False)" yazarsak null'larıda veriyor.
    print("#################### Head ####################")
    print(dataframe.head())
    print("#################### Tail ####################")
    print(dataframe.tail())
    print("#################### NA ####################")
    print(dataframe.isnull().sum())
    print("#################### Quantiles ####################")
    print(dataframe.describe().T)


check_df(tarifler)


######################
# Feature Engineering
######################

tarifler['tatli'] = tarifler['Title'].apply(lambda title: 1 if 'cake' in title.lower() or \
                                                                  'pudding' in title.lower() else 0)

tarifler["tatli"].sum()


#################################
# Çalışma Scriptinin Hazırlanması
##################################

def content_based_recommender(title, cosine_sim, dataframe):
    # index'leri olusturma
    indices = pd.Series(dataframe.index, index=dataframe['Title'])
    indices = indices[~indices.index.duplicated(keep='last')]
    # title'ın index'ini yakalama
    tarif_index = indices[title]
    # title'a gore benzerlik skorlarını hesapalama
    similarity_scores = pd.DataFrame(cosine_sim[tarif_index], columns=["score"])
    # kendisi haric ilk 10 yemek getirme
    tarif_indices = similarity_scores.sort_values("score", ascending=False)[1:11].index
    return dataframe['Title'].iloc[tarif_indices]


content_based_recommender("Broccoli and Cheddar Skillet Flan", cosine_sim, tarifler)


def calculate_cosine_sim(dataframe):
    tfidf = TfidfVectorizer(stop_words='english')
    dataframe['Ingredients'] = dataframe['Ingredients'].fillna('')
    tfidf_matrix = tfidf.fit_transform(dataframe['Ingredients'])
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
    return cosine_sim


cosine_sim = calculate_cosine_sim(tarifler)
content_based_recommender("Thanksgiving Mac and Cheese", cosine_sim, tarifler)

#########################################
# Item-Based Film Önerilerinin Yapılması
#########################################
