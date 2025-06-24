from analyzer import analyze_sentiment, analyze_intention
from recommender import recommend_songs
from utils import load_dataset

df = load_dataset("Spotify_Youtube.csv")

# 1) Emotion
emo_text = input("📝 Describe your feelings (English):\n> ")
emo_label, emo_conf = analyze_sentiment(emo_text)
print(f"\n📊 Emotion: {emo_label} ({emo_conf*100:.1f}%)")

# 2) Intention
int_text = input("\n🔁 Tell if you want to stay in this state or change it:\n> ")
intent, intent_conf = analyze_intention(int_text)
print(f"🧠 Intention detected: {intent.upper()} ({intent_conf*100:.1f}%)")

# 3) Recommend
songs = recommend_songs(df, emo_label, intent)

if isinstance(songs, dict):
    print("⚠️", songs["error"])
else:
    print("\n🎧 5 song suggestions:\n")
    for i, s in enumerate(songs, 1):
        print(f"{i}. {s['Track']} – {s['Artist']} ({s['Album']})")