# Base image (resmi olarak PyTorch ve Transformers destekli Python)
FROM python:3.9-slim

# Gerekli sistem kütüphanelerini yükle
RUN apt-get update && apt-get install -y \
    git \
    && rm -rf /var/lib/apt/lists/*

# Çalışma dizini oluştur
WORKDIR /app

# Bağımlılıkları kopyala
COPY requirements.txt .

# Python kütüphanelerini yükle
RUN pip install --no-cache-dir -r requirements.txt

# Uygulama dosyalarını kopyala
COPY . .

# 5000 portunu dışa aç
EXPOSE 5000

# Uygulama başlatma komutu
CMD ["python", "app_api.py"]