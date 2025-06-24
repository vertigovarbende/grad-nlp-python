from transformers import pipeline

sentiment_clf = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

intent_clf = pipeline(
    "zero-shot-classification",
   model="facebook/bart-large-mnli"
  #  model="distilbert-base-uncased-finetuned-sst-2-english"
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