# Iris Logistic Model

Bu proje, meşhur [Iris veri seti](https://archive.ics.uci.edu/ml/datasets/iris) üzerinde basit bir lojistik regresyon modeli oluşturmayı ve bu modeli kullanarak tahmin yapmayı göstermektedir. Eğitim, model kaydetme ve modelle tahmin adımları örnek dosyalarla birlikte paylaşılmıştır.

## 📂 Proje Dosyaları

- **iris_model.ipynb**  
  Modelin oluşturulma süreci, veri setinin yüklenmesi, görselleştirme, model eğitimi ve kaydedilmesi gibi tüm adımlar bu Jupyter defterinde yer alıyor.

- **iris_model.pkl**  
  Eğitilmiş lojistik regresyon modeli bu dosyada pickle formatında saklanıyor. Modeli yeniden eğitmeye gerek kalmadan doğrudan kullanılabilir.

- **test.py**  
  Kayıtlı modeli yükleyip, test verisi üzerinde tahmin yaparak sonucu ekrana yazdırır. Modelin doğru şekilde yüklendiğini ve çalıştığını kontrol etmek için kullanılabilir.

## ⚙️ Gereksinimler

Bu projeyi çalıştırmak için Python ve bazı popüler kütüphaneler gereklidir:

```bash
pip install scikit-learn pandas numpy

Eğer Jupyter defterini açmak isterseniz ayrıca:
pip install notebook

🚀 Nasıl Çalıştırılır?
Modeli eğitmek veya tekrar eğitmek için
iris_model.ipynb dosyasını Jupyter Notebook ile açın ve adım adım çalıştırın. Çalıştırmanın sonunda iris_model.pkl dosyası oluşturulacaktır.

Hazır modeli kullanarak tahmin yapmak için
test.py dosyasını şu komutu kullanarak çalıştırın:
python test.py

🧠 Kullanılan Yöntem
Lojistik regresyon modeli
scikit-learn kütüphanesi
Iris veri seti (3 farklı iris çiçeği türünü sınıflandırmak için)