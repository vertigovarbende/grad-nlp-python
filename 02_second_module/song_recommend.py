import random

pozitif_sarkilar = [
    "Happy - Pharrell Williams",
    "Good Life - OneRepublic",
    "Walking on Sunshine - Katrina & The Waves",
    "Can't Stop The Feeling - Justin Timberlake"
]

negatif_sarkilar = [
    "Someone Like You - Adele",
    "Fix You - Coldplay",
    "Hurt - Johnny Cash",
    "Creep - Radiohead"
]

def sarki_oner(duygu, tercih):
    """
    duygu: POSITIVE ya da NEGATIVE
    tercih: 'korumak' ya da 'değiştirmek'
    """
    if duygu == "NEGATIVE" and tercih == "değiştirmek":
        return random.choice(pozitif_sarkilar)
    elif duygu == "NEGATIVE" and tercih == "korumak":
        return random.choice(negatif_sarkilar)
    elif duygu == "POSITIVE" and tercih == "korumak":
        return random.choice(pozitif_sarkilar)
    elif duygu == "POSITIVE" and tercih == "değiştirmek":
        return random.choice(negatif_sarkilar)
    else:
        return "Bir hata oluştu, lütfen tekrar deneyin."