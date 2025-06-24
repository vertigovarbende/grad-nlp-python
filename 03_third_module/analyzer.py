from transformers import pipeline

# Load BERT model once
sentiment_pipeline = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

def analyze_sentiment(text: str):
    """
    Analyze sentiment using BERT.
    Returns label: POSITIVE or NEGATIVE and score.
    """
    result = sentiment_pipeline(text)[0]
    return result["label"], result["score"]