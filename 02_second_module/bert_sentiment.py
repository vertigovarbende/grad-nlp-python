# bert_sentiment.py
from transformers import pipeline

# distilBERT modeli (küçük ve hızlı, İngilizce)
model_adi = "distilbert-base-uncased-finetuned-sst-2-english"

# NLP pipeline ile model yükleniyor
sentiment_pipeline = pipeline("sentiment-analysis", model=model_adi)

def analiz_et(metin):
    """
    Girdi: Metin (string)
    Çıktı: (etiket: POSITIVE/NEGATIVE, güven: 0.0-1.0)
    """
    sonuc = sentiment_pipeline(metin)[0]
    etiket = sonuc['label']         # POSITIVE ya da NEGATIVE
    skor = sonuc['score']           # Güven skoru
    return etiket, skor