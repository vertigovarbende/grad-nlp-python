def recommend_songs(df, emotion_label, intention, count=5):
    """
    Recommends songs based on emotional state and user's intention.
    """
    positive = df[df["Valence"] > 0.6]
    negative = df[df["Valence"] < 0.4]

    # Decision logic
    if emotion_label == "NEGATIVE" and intention == "change":
        pool = positive
    elif emotion_label == "NEGATIVE" and intention == "stay":
        pool = negative
    elif emotion_label == "POSITIVE" and intention == "stay":
        pool = positive
    elif emotion_label == "POSITIVE" and intention == "change":
        pool = negative
    else:
        return {"error": "Invalid decision combination."}

    if pool.empty:
        return {"error": "No songs found."}

    return pool.sample(min(count, len(pool)))[["Track", "Artist", "Album"]].to_dict(orient="records")