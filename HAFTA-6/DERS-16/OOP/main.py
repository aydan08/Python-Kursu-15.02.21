from ornek_sinif import Kalem

kalem1 = Kalem("Mavi")
print(kalem1.rengi)
print(kalem1.sinif_adi)

kalem2 = Kalem("Kırmızı")
print(kalem2.rengi)
print(kalem2.sinif_adi)

kalem3 = Kalem("Sarı")
print(kalem3.rengi)
print(kalem3.sinif_adi)

kalem1.yazdir()


#üsttekinin önceden kullandığımız hali
#liste = [1,2,3,4]
#print(liste.count(3)) #count(3) 3 ten kaç tane olduğunu verir

#---Sınıf değişkeni o sınıfta üretilen
#tüm nesneler için aynıyken
#nesne degişkeni siniftan oluşturulan
#her nesne için farklıdır.---
