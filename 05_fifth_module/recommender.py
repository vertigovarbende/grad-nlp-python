def recommend_songs(df, emotion_label, intention, k=5):
    pos = df[df["Valence"] > 0.6]
    neg = df[df["Valence"] < 0.4]

    if emotion_label == "NEGATIVE" and intention == "change":
        pool = pos
    elif emotion_label == "NEGATIVE" and intention == "stay":
        pool = neg
    elif emotion_label == "POSITIVE" and intention == "stay":
        pool = pos
    elif emotion_label == "POSITIVE" and intention == "change":
        pool = neg
    else:
        return {"error": "No rule matched."}

    if pool.empty:
        return {"error": "No songs found."}

    return pool.sample(min(k, len(pool)))[["Track", "Artist", "Album"]].to_dict("records")