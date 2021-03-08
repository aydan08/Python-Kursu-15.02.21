sayilar = []

while True:
    sayi = input("Sayıyı Girin (Çıkmak için Ç ye basın):")

    if sayi == "ç" or sayi == "Ç" :
        break
    
    sayi = int(sayi)

    sayilar.append(sayi)

print(sayilar)