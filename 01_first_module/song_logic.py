# song_logic.py
import re
import pickle
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
nltk.download('stopwords')

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

with open("vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

with open("encoder.pkl", "rb") as f:
    encoder = pickle.load(f)

stop_words = set(stopwords.words('english'))
stemmer = PorterStemmer()

def temizle_metin(metin):
    metin = re.sub(r'[^a-zA-Z\s]', '', metin.lower())
    kelimeler = metin.split()
    kelimeler = [stemmer.stem(k) for k in kelimeler if k not in stop_words]
    return " ".join(kelimeler)

def yorumla(metin):
    temiz = temizle_metin(metin)
    vektor = vectorizer.transform([temiz])
    tahmin = model.predict(vektor)
    etiket = encoder.inverse_transform(tahmin)[0]
    return etiket