def recommend_songs(df, emotion_label, intention, k=5):
    df = df.copy()
    val_mean = df["Valence"].mean()
    like_mean = df["Likes"].mean()
    view_mean = df["Views"].mean()

    if emotion_label == "NEGATIVE" and intention == "change":
        pool = df[
            (df["Valence"] > 0.6) &
            (df["Energy"] > 0.5) &
            (df["Danceability"] > 0.5) &
            (df["Tempo"] > 80) &
            (df["Speechiness"] < 0.5) &
         #  (df["Views"] > view_mean) &
         #  (df["Likes"] > like_mean) &
            (df["Liveness"] > 0.1) & (df["Liveness"] < 0.8)
        ]

    elif emotion_label == "NEGATIVE" and intention == "stay":
        pool = df[
            (df["Valence"] < 0.4) &
            (df["Acousticness"] > 0.6) &
            (df["Energy"] < 0.4) &
            (df["Instrumentalness"] > 0.5) &
            (df["Speechiness"] < 0.5) &
            (df["Loudness"] < -10)
        ]

    elif emotion_label == "POSITIVE" and intention == "stay":
        pool = df[
            (df["Valence"] > 0.6) &
            (df["Danceability"] > 0.5) &
            (df["Energy"] > 0.5) & (df["Energy"] < 0.8) &
            (df["Tempo"] > 80) & (df["Tempo"] < 130) &
            (df["Views"] > view_mean) &
            (df["Likes"] > like_mean) &
            (df["Speechiness"] < 0.5)
        ]

    elif emotion_label == "POSITIVE" and intention == "change":
        pool = df[
            (df["Valence"] < 0.4) &
            (df["Energy"] < 0.5) &
            (df["Tempo"] < 90) &
            (df["Acousticness"] > 0.5) &
            (df["Instrumentalness"] > 0.3) &
            (df["Speechiness"] < 0.5)
        ]

    else:
        return {"error": "No rule matched your case."}

    if pool.empty:
        return {"error": "No matching songs found."}

    return pool.sample(min(k, len(pool)))[["Track", "Artist", "Album"]].to_dict("records")