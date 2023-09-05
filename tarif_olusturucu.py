import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
import missingno as msno
from datetime import date
from sklearn.metrics import accuracy_score, classification_report, roc_auc_score, mean_squared_error
from sklearn.metrics import confusion_matrix, RocCurveDisplay, mean_absolute_error
from sklearn.model_selection import train_test_split, GridSearchCV, cross_validate, RandomizedSearchCV
from sklearn.model_selection import validation_curve, cross_val_score
from sklearn.neighbors import LocalOutlierFactor, KNeighborsClassifier
from sklearn.preprocessing import MinMaxScaler, LabelEncoder, StandardScaler, RobustScaler
from statsmodels.stats.proportion import proportions_ztest
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, VotingClassifier
from sklearn.impute import KNNImputer
from xgboost import XGBClassifier
from lightgbm import LGBMClassifier
from catboost import CatBoostClassifier
from sklearn.tree import DecisionTreeClassifier, export_graphviz, export_text
from skompiler import skompile
import graphviz
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
import shap

df = pd.read_csv("C:/Users/remre/PycharmProjects/Tarif_Olusturucu/GastroMiuul/datasets/recipes_w_search_terms.csv")
lowercase = lambda x: str(x).lower()
df.rename(lowercase, axis='columns', inplace=True)
df.dropna(inplace=True)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 1500)
pd.set_option('display.float_format', lambda x: '%.3f' % x)
pd.set_option('display.width', 1500)


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
    print(dataframe.describe([0.01, 0.05, 0.75, 0.90, 0.95, 0.99]).T)


check_df(df)

df = df.reset_index()
df.drop(["index", "id"], axis=1, inplace=True)

search_terms = df["search_terms"]
search_terms.to_excel("search_terms.xlsx", index=False)




################################
# Değişken Tiplerin Yakalanması
################################

def grab_col_names(dataframe, cat_th=10, car_th=20):
    """

    Veri setindeki kategorik, numerik ve kategorik fakat kardinal değişkenlerin isimlerini verir.
    Not: Kategorik değişkenlerin içerisine numerik görünümlü kategorik değişkenler de dahildir.

    Parameters
    ------
        dataframe: dataframe
                Değişken isimleri alınmak istenilen dataframe
        cat_th: int, optional
                numerik fakat kategorik olan değişkenler için sınıf eşik değeri
        car_th: int, optinal
                kategorik fakat kardinal değişkenler için sınıf eşik değeri

    Returns
    ------
        cat_cols: list
                Kategorik değişken listesi
        num_cols: list
                Numerik değişken listesi
        cat_but_car: list
                Kategorik görünümlü kardinal değişken listesi

    Examples
    ------
        import seaborn as sns
        df = sns.load_dataset("iris")
        print(grab_col_names(df))


    Notes
    ------
        cat_cols + num_cols + cat_but_car = toplam değişken sayısı
        num_but_cat cat_cols'un içerisinde.
        Return olan 3 liste toplamı toplam değişken sayısına eşittir: cat_cols + num_cols + cat_but_car = değişken
        sayısı

    """

    # cat_cols, cat_but_car
    cat_cols = [col for col in dataframe.columns if dataframe[col].dtypes == "O"]
    num_but_cat = [col for col in dataframe.columns if dataframe[col].nunique() < cat_th and
                   dataframe[col].dtypes != "O"]
    cat_but_car = [col for col in dataframe.columns if dataframe[col].nunique() > car_th and
                   dataframe[col].dtypes == "O"]
    cat_cols = cat_cols + num_but_cat
    cat_cols = [col for col in cat_cols if col not in cat_but_car]

    # num_cols
    num_cols = [col for col in dataframe.columns if dataframe[col].dtypes != "O"]
    num_cols = [col for col in num_cols if col not in num_but_cat]

    print(f"Observations: {dataframe.shape[0]}")
    print(f"Variables: {dataframe.shape[1]}")
    print(f'cat_cols: {len(cat_cols)}')
    print(f'num_cols: {len(num_cols)}')
    print(f'cat_but_car: {len(cat_but_car)}')
    print(f'num_but_cat: {len(num_but_cat)}')
    return cat_cols, num_cols, cat_but_car


cat_cols, num_cols, cat_but_car = grab_col_names(tarifler)

######################
# Eksik Değer Var mı?
######################

# eksiklikleri değişken bazında %'lik olarak görmek için
(tarifler.isnull().sum() / tarifler.shape[0] * 100).sort_values(ascending=False)

# en az bir tane eksik degere sahip olan gözlem birimleri (satır)
eksik_satirlar = tarifler[tarifler.isnull().any(axis=1)]

# eksik değerleri hızlıca silmek
tarifler.dropna(inplace=True)

######################
# Feature Engineering
######################




#################################
# Cosine Similarity Matrisinin Oluşturulması
#################################

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

"""
--Veri tabanı seviyesinde nasıl gerçekleştiririz?
1) Kullanıcıların en fazla tarif alabileceği yemekleri belirlerin. IDlerini biliyoruz.
2) Burada gerçekleştirdiğimiz işleri, bu en fazla tarifi alınmasını düşündüğümüz yemekler için oluşturacağız ve bir 
tabloda tutuyor olacağız. (firmalar SQL formatında tutuyor olacak)
3) Bir kişi IDsini bildiğimiz (yukarıda çıkardığımız) yemeği hazırladığı zaman, direkt tablomuzdan yararlanarak 
önerilerde bulunacağız.
"""

#############################
# Eksik ürün arama
#############################

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def search_item(query):
    driver = webdriver.Chrome()
    # driver.get("https://www.a101kapida.com/")  # çalıştı = by="id", value="searchbar"
    driver.get("https://www.carrefoursa.com/")  # çalıştı = by="id", value="js-site-search-input"

    search_box = driver.find_element(by="id", value="js-site-search-input")
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)

    # Tarayıcıyı kapatmadan önce kullanıcının onayını bekliyoruz
    input(f"{query} aranıyor...")
    driver.quit()


search_item("badem")

# yukarıdaki ile deneme yapıldı