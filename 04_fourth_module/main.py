from analyzer import analyze_sentiment, interpret_intention_label
from recommender import recommend_songs
from utils import load_dataset

# 1. Dataset yükle
df = load_dataset("Spotify_Youtube.csv")

# 2. Kullanıcının duygusal durumunu al
emotion_text = input("📝 Describe how you're feeling (in English):\n> ")
emotion_label, emotion_conf = analyze_sentiment(emotion_text)
print(f"\n📊 Emotion detected: {emotion_label} ({emotion_conf*100:.1f}% confidence)")

# 3. Kullanıcının bu duyguda kalmak mı yoksa çıkmak mı istediğini sor
intention_text = input("\n🔁 Do you want to stay in this emotional state or change it? (Describe in English):\n> ")
intention_label_raw, intention_conf = analyze_sentiment(intention_text)
intention = interpret_intention_label(intention_label_raw)
print(f"\n🧠 Intention detected: {intention.upper()} ({intention_conf*100:.1f}% confidence)")

# 4. Şarkı öner
songs = recommend_songs(df, emotion_label, intention)

# 5. Sonucu yazdır
if isinstance(songs, dict) and "error" in songs:
    print("⚠️", songs["error"])
else:
    print("\n🎧 Recommended songs for your situation:\n")
    for i, song in enumerate(songs, 1):
        print(f"{i}. 🎵 {song['Track']} - {song['Artist']} ({song['Album']})")