from flask import Flask, request, jsonify
from analyzer import analyze_sentiment, analyze_intention
from recommender import recommend_songs
from utils import load_dataset

app = Flask(__name__)

# CSV dosyasını baştan yüklüyoruz
df = load_dataset("Spotify_Youtube.csv")

@app.route("/")
def index():
    return jsonify({"message": "Welcome to the Emotion-Based Song Recommender API!"})

@app.route("/analyze", methods=["POST"])
def analyze_and_recommend():
    data = request.get_json()

    if not data or "text" not in data:
        return jsonify({"error": "Please provide 'text' in the JSON body."}), 400

    text = data["text"]

    # Duygu analizi
    emotion_label, emotion_score = analyze_sentiment(text)

    # Niyet analizi (kullanıcı niyeti de metin içinde)
    intent_label, intent_score = analyze_intention(text)

    # Şarkı önerisi
    songs = recommend_songs(df, emotion_label, intent_label)

    if isinstance(songs, dict) and "error" in songs:
        return jsonify({
            "emotion": {"label": emotion_label, "confidence": round(emotion_score, 3)},
            "intention": {"label": intent_label, "confidence": round(intent_score, 3)},
            "error": songs["error"]
        }), 404

    return jsonify({
        "emotion": {"label": emotion_label, "confidence": round(emotion_score, 3)},
        "intention": {"label": intent_label, "confidence": round(intent_score, 3)},
        "recommendations": songs
    })

if __name__ == "__main__":
    app.run(debug=True)
