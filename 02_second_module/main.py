# main.py
from bert_sentiment import analiz_et
from song_recommend import sarki_oner

print("🎵 Müzik ve Duygu Analizi Sistemine Hoş Geldiniz 🎵")

while True:
    metin = input("\n📝 Duygunuzu anlatan bir cümle girin (çıkmak için 'q'): ")

    if metin.lower() == 'q':
        print("Program sonlandırıldı. Görüşmek üzere 🎧")
        break

    # 1. BERT ile duygu analizi yap
    duygu, skor = analiz_et(metin)
    print(f"\n📊 Analiz sonucu: {duygu} (%{skor*100:.1f} güven)")

    # 2. Kullanıcının bu ruh halini sürdürmek mi yoksa değiştirmek mi istediğini sor
    tercih = input("🧠 Bu ruh halini 'korumak' mı yoksa 'değiştirmek' mi istersiniz?: ").strip().lower()

    if tercih not in ['korumak', 'değiştirmek']:
        print("❌ Geçersiz giriş. Lütfen sadece 'korumak' veya 'değiştirmek' yazın.")
        continue

    # 3. Şarkı öner
    sarki = sarki_oner(duygu, tercih)
    print(f"\n🎧 Önerilen şarkı: {sarki}")