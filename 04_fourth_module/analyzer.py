from transformers import pipeline

# BERT model pipeline (tek seferlik yüklenir)
sentiment_pipeline = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

def analyze_sentiment(text):
    """
    Returns BERT sentiment label (POSITIVE/NEGATIVE) and confidence score.
    """
    result = sentiment_pipeline(text)[0]
    return result["label"], result["score"]

def interpret_intention_label(label):
    """
    Interprets user's intention from sentiment label:
    POSITIVE → wants to CHANGE current feeling
    NEGATIVE → wants to STAY in current feeling
    """
    return "change" if label == "POSITIVE" else "stay"