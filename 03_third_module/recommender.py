import random

def recommend_songs(df, emotional_label, intention_label, count=5):
    """
    Recommend songs based on emotion + user's intention to stay/change.
    """

    positive = df[df["Valence"] > 0.6]
    negative = df[df["Valence"] < 0.4]

    # Decision matrix
    if emotional_label == "NEGATIVE" and intention_label == "POSITIVE":
        songs = positive
    elif emotional_label == "NEGATIVE" and intention_label == "NEGATIVE":
        songs = negative
    elif emotional_label == "POSITIVE" and intention_label == "POSITIVE":
        songs = positive
    elif emotional_label == "POSITIVE" and intention_label == "NEGATIVE":
        songs = negative
    else:
        return {"error": "Invalid sentiment combination."}

    if songs.empty:
        return {"error": "No suitable songs found."}

    return songs.sample(min(count, len(songs)))[["Track", "Artist", "Album"]].to_dict(orient="records")