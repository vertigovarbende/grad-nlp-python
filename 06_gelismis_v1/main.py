from analyzer import analyze_sentiment, analyze_intention
from recommender import recommend_songs
from utils import load_dataset

df = load_dataset("Spotify_Youtube.csv")

emo_text = input("# Describe your feelings (in English):\n> ")
emo_label, emo_conf = analyze_sentiment(emo_text)
print(f"# Emotion detected: {emo_label} ({emo_conf*100:.1f}%)")


intent_text = input("- Do you want to stay in this emotional state or change it?\n> ")
intent_label, intent_score = analyze_intention(intent_text)
print(f"- Intention: {intent_label.upper()} ({intent_score*100:.1f}%)")

songs = recommend_songs(df, emo_label, intent_label)

if isinstance(songs, dict) and "error" in songs:
    print("⚠️", songs["error"])
else:
    print("\n🎵 Recommended songs based on your emotion and intention:\n")
    for i, song in enumerate(songs, 1):
        print(f"{i}. {song['Track']} – {song['Artist']} ({song['Album']})")
