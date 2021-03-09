def giris_ekranı():
    print("Hangi işlemi yapmak istersiniz? ")
    print("""
    1- Toplama
    2- Çıkarma
    3- Çarpma
    4- Bölme 

    Çıkmak İçin Ç harfine basınız.

    Seçim için sıra numarasını yazınız:  
    """) 

def veri_girisi():

    sayilar = []
    while True:
        sayi = input("Sayıyı Girin (Çıkmak için Ç ye basın):")

        if sayi == "ç" or sayi == "Ç" :
            break
        
        sayi = int(sayi)

        sayilar.append(sayi)

    return sayilar

def toplama(a):
    toplam = 0

    for sayi in a:
        toplam = toplam + sayi
    print(f"Toplama Sonucu:  {toplam}")

def cikarma(b):
    fark = b[0]

    for index in range(1,len(b)):
        fark = fark - b[index]
    print(f"Çıkarma Sonucu:  {fark}")

def kullanici_secimi():
    k_secim = input()
    return k_secim
     

while True:

    giris_ekranı()
    
    secim = kullanici_secimi()

    if secim == "ç" or secim=="Ç" :
        break

    if  not (secim == "1" or secim == "2" or secim== "3" or secim == "4" ):
        print("Yanlış Giriş Yaptınız.")
        continue


    sayilar = veri_girisi()

    print(sayilar)

    if secim == "1":
        toplama(sayilar)

    elif secim == "2":
        cikarma(sayilar)

    elif secim == "3":
        carpma = 1
        for sayi in sayilar:
            carpma = carpma * sayi
        print(f"Çarpma Sonucu: {carpma}")  

    elif secim == "4":
        bolum = sayilar[0]
        # 1, 2, 3, 4 .....
        for index in range(1,len(sayilar)):
            bolum = bolum / sayilar[index]
        print(f"Bölmenin sonucu : {bolum}")

    else :
        print("Geçersiz Seçim Yaptınız!")
