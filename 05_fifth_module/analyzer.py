from transformers import pipeline

# 1) Duygu (positive / negative)
sentiment_clf = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

# 2) Niyet (stay / change) – zero-shot
intent_clf = pipeline(
    "zero-shot-classification",
    model="facebook/bart-large-mnli"
)

def analyze_sentiment(text: str):
    """Return ('POSITIVE' | 'NEGATIVE', confidence)"""
    res = sentiment_clf(text, truncation=True)[0]
    return res["label"], res["score"]

def analyze_intention(text: str):
    """
    Zero-shot classification:
    Labels = ['stay', 'change']
    Returns ('stay' | 'change', confidence)
    """
    candidate_labels = ["stay", "change"]
    res = intent_clf(text, candidate_labels, truncation=True)
    # highest scored label
    return res["labels"][0], res["scores"][0]