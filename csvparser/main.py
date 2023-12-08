import csv

# İlk CSV dosyasındaki verileri bir listeye aktar
ilk_dosya_path = '/Users/mobil/Desktop/ilk_dosya.csv'
ikinci_dosya_path = '/Users/mobil/Desktop/ikinci_dosya.csv'
hedef_dosya_path = '/Users/mobil/Desktop/sonuc_dosyasi.csv'

ilk_liste = []

with open(ilk_dosya_path, 'r', newline='') as dosya:
    okuyucu = csv.reader(dosya)
    for satir in okuyucu:
        ilk_liste.append(satir[0])


# İkinci CSV dosyasındaki verileri bir listeye aktar
ikinci_liste = []

with open(ikinci_dosya_path, 'r', newline='') as dosya:
    okuyucu = csv.reader(dosya)
    for satir in okuyucu:
        ikinci_liste.append(satir[0])

# İki listeyi birbirinden çıkar
sonuc_liste = list(set(ilk_liste) - set(ikinci_liste))

# Sonucu yeni bir CSV dosyasına yaz
with open(hedef_dosya_path, 'w', newline='') as dosya:
    yazici = csv.writer(dosya)
    for eleman in sonuc_liste:
        yazici.writerow([eleman])

print("İşlem tamamlandı. Sonuç dosyası:", hedef_dosya_path)
print(len(ilk_liste))
print(len(ikinci_liste))
print(len(sonuc_liste))