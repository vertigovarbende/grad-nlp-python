from analyzer import analyze_sentiment
from recommender import recommend_songs
from utils import load_dataset

# Yeni yorumlayıcı fonksiyon
def interpret_intention_label(label):
    return "change" if label == "POSITIVE" else "stay"

# Load dataset
df = load_dataset("Spotify_Youtube.csv")

# Step 1: User emotional input
emotion_text = input("📝 Please describe how you are feeling right now (in English):\n> ")
emotion_label, emotion_score = analyze_sentiment(emotion_text)

print(f"\n📊 Your emotional state is: {emotion_label} ({emotion_score*100:.1f}% confidence)")

# Step 2: Ask user's intention about this feeling
intention_text = input("\n🔁 Do you want to stay in this emotional state or change it? Write a sentence:\n> ")
intent_label_raw, intent_score = analyze_sentiment(intention_text)
intent_logical = interpret_intention_label(intent_label_raw)

print(f"\n🧠 Your intention is interpreted as: {intent_logical.upper()} ({intent_score*100:.1f}% confidence)")

# Step 3: Recommend songs
songs = recommend_songs(df, emotion_label, intent_label_raw)

# Step 4: Output result
if isinstance(songs, dict) and "error" in songs:
    print("⚠️", songs["error"])
else:
    print("\n🎧 Recommended songs based on your emotional situation:\n")
    for idx, song in enumerate(songs, 1):
        print(f"{idx}. 🎵 {song['Track']} - {song['Artist']} ({song['Album']})")