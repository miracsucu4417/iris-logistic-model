import joblib

# Modeli yükle
model = joblib.load("iris_model.pkl")

# Yeni bir çiçek örneği verelim (4 özellik)
yeni_veri = [[150, 3.0, 10, 1.9]]

# Tahmin al
tahmin = model.predict(yeni_veri)

print("Tahmin edilen çiçek türü kodu:", tahmin[0])
