tek_sayilar = 0
çift_sayilar = 0

sayi = input("Bir Sayı Girin: ")
sayi = int(sayi)

while sayi != 0:
    
    if sayi % 2 == 1:  
       tek_sayilar += 1
    else:
       çift_sayilar += 1
    
    sayi = int(input("Yeni sayı girin ya da çıkmak için 0 girin: "))

print("Tek Sayıların Sayısı: " , tek_sayilar)
print("Çift Sayıların Sayısı: " , çift_sayilar)