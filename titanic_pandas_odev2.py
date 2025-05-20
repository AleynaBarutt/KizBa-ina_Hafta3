import pandas as pd

# Kullanıcıdan veri seti dosya yolunu al
file_path = input("Lütfen Titanic veri seti (train.csv) dosya yolunu giriniz: ")
df_titanic = pd.read_csv(file_path)

# 1. Kazada ölenlerin yaş ortalamasını bulunuz
## Kazada ölenler Survived == 0 olanlardır. Yaş ortalamasını hesaplıyoruz.
olenlerin_yas_ortalamasi = df_titanic[df_titanic['Survived'] == 0]['Age'].mean()
print(f"Kazada ölenlerin yaş ortalaması: {olenlerin_yas_ortalamasi:.2f}")

# 2. Kazada ölenlerin bilet fiyatlarının ortalamasını ve medyanını bulunuz
## Ölenlerin bilet fiyatları (Fare) için ortalama ve medyan hesaplıyoruz.
olenlerin_bilet_ortalamasi = df_titanic[df_titanic['Survived'] == 0]['Fare'].mean()
olenlerin_bilet_medyani = df_titanic[df_titanic['Survived'] == 0]['Fare'].median()
print(f"Kazada ölenlerin bilet fiyatı ortalaması: {olenlerin_bilet_ortalamasi:.2f}")
print(f"Kazada ölenlerin bilet fiyatı medyanı: {olenlerin_bilet_medyani:.2f}")

# 3. Kazada ölen erkeklerin yaş ortalamasını bulunuz
## Ölen erkekler: Survived == 0 ve Sex == 'male'
olen_erkeklerin_yas_ortalamasi = df_titanic[(df_titanic['Survived'] == 0) & (df_titanic['Sex'] == 'male')]['Age'].mean()
print(f"Kazada ölen erkeklerin yaş ortalaması: {olen_erkeklerin_yas_ortalamasi:.2f}")

# 4. Kazada ölen kadınların yaş ortalamasını bulunuz
## Ölen kadınlar: Survived == 0 ve Sex == 'female'
olen_kadinlarin_yas_ortalamasi = df_titanic[(df_titanic['Survived'] == 0) & (df_titanic['Sex'] == 'female')]['Age'].mean()
print(f"Kazada ölen kadınların yaş ortalaması: {olen_kadinlarin_yas_ortalamasi:.2f}")

# 5. Kazadan kurtulanların yaş ortalamasını bulunuz
## Kurtulanlar: Survived == 1
kurtulanlarin_yas_ortalamasi = df_titanic[df_titanic['Survived'] == 1]['Age'].mean()
print(f"Kazadan kurtulanların yaş ortalaması: {kurtulanlarin_yas_ortalamasi:.2f}")

# 6. Kazadan kurtulanların bilet fiyatlarının ortalamasını bulunuz
## Kurtulanların bilet fiyatları (Fare) için ortalama hesaplıyoruz.
kurtulanlarin_bilet_ortalamasi = df_titanic[df_titanic['Survived'] == 1]['Fare'].mean()
print(f"Kazadan kurtulanların bilet fiyatı ortalaması: {kurtulanlarin_bilet_ortalamasi:.2f}")

# 7. Kazadan kurtulan toplam kişi sayısını bulunuz
## Kurtulanlar: Survived == 1
kurtulan_sayisi = len(df_titanic[df_titanic['Survived'] == 1])
print(f"Kazadan kurtulan toplam kişi sayısı: {kurtulan_sayisi}")

# 8. 10 yaşından küçüklerin bilet fiyatlarının medyan değerini bulunuz
## 10 yaşından küçükler: Age < 10
on_yas_altı_bilet_medyani = df_titanic[df_titanic['Age'] < 10]['Fare'].median()
print(f"10 yaşından küçüklerin bilet fiyatı medyanı: {on_yas_altı_bilet_medyani:.2f}")

# 9. 1. sınıf, 2. sınıf ve 3. sınıf bilet fiyatlarının ortalama ve medyanlarını karşılaştırınız
## Pclass değişkenine göre gruplama yaparak ortalama ve medyan hesaplıyoruz.
sinif_ortalamalari = df_titanic.groupby('Pclass')['Fare'].mean()
sinif_medyani = df_titanic.groupby('Pclass')['Fare'].median()
print("\nBilet sınıflarına göre ortalama fiyatlar:")
for sinif, ortalama in sinif_ortalamalari.items():
    print(f"{sinif}. sınıf ortalama bilet fiyatı: {ortalama:.2f}")
print("\nBilet sınıflarına göre medyan fiyatlar:")
for sinif, medyan in sinif_medyani.items():
    print(f"{sinif}. sınıf medyan bilet fiyatı: {medyan:.2f}")

# 10. Kazada ölen kadınların oranı ile erkeklerin oranını karşılaştırınız
## Ölen erkeklerin oranı: Ölen erkekler / Toplam erkekler
## Ölen kadınların oranı: Ölen kadınlar / Toplam kadınlar
toplam_erkekler = len(df_titanic[df_titanic['Sex'] == 'male'])
olen_erkekler = len(df_titanic[(df_titanic['Sex'] == 'male') & (df_titanic['Survived'] == 0)])
erkek_olen_orani = olen_erkekler / toplam_erkekler

toplam_kadinlar = len(df_titanic[df_titanic['Sex'] == 'female'])
olen_kadinlar = len(df_titanic[(df_titanic['Sex'] == 'female') & (df_titanic['Survived'] == 0)])
kadin_olen_orani = olen_kadinlar / toplam_kadinlar

print(f"Kazada ölen erkeklerin oranı: {erkek_olen_orani:.2%}")
print(f"Kazada ölen kadınların oranı: {kadin_olen_orani:.2%}")
