# model_egit.py
import nltk
import random
import re
import pickle
from nltk.corpus import movie_reviews, stopwords
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.preprocessing import LabelEncoder

nltk.download('movie_reviews')
nltk.download('stopwords')

# Veriyi hazırla
data = [(list(movie_reviews.words(fileid)), category)
        for category in movie_reviews.categories()
        for fileid in movie_reviews.fileids(category)]

random.shuffle(data)

texts = [" ".join(words) for words, label in data]
labels = [label for words, label in data]

# Temizleme fonksiyonu
stop_words = set(stopwords.words('english'))
stemmer = PorterStemmer()

def temizle_metin(metin):
    metin = re.sub(r'[^a-zA-Z\s]', '', metin.lower())
    kelimeler = metin.split()
    kelimeler = [stemmer.stem(k) for k in kelimeler if k not in stop_words]
    return " ".join(kelimeler)

temizlenmis_texts = [temizle_metin(t) for t in texts]

# Özellik çıkarımı (Bag of Words)
vectorizer = CountVectorizer(max_features=3000)
X = vectorizer.fit_transform(temizlenmis_texts)

# Etiket kodlaması
encoder = LabelEncoder()
y = encoder.fit_transform(labels)

# Modeli eğit
model = MultinomialNB()
model.fit(X, y)

# Model ve bileşenleri kaydet
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

with open("encoder.pkl", "wb") as f:
    pickle.dump(encoder, f)

print("Model başarıyla eğitildi ve kaydedildi.")