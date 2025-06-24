# main.py
from song_logic import yorumla

print("🎵 Şarkı Duygu Analizi Sistemine Hoş Geldiniz 🎵")
while True:
    giris = input("\nBir metin girin (çıkmak için 'q'): ")

    if giris.lower() == 'q':
        print("Çıkılıyor...")
        break

    duygu = yorumla(giris)

    if duygu == "pos":
        print("➡️ Pozitif bir duygu algılandı. Neşeli bir şarkı önerilecek!")
    else:
        print("➡️ Negatif bir duygu algılandı. Daha sakin bir şarkı önerilecek.")