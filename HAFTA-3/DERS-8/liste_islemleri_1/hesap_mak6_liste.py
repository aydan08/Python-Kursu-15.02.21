while True:
    print("Hangi işlemi yapmak istersiniz? ")
    print("""
    1- Toplama
    2- Çıkarma
    3- Çarpma
    4- Bölme 

    Çıkmak İçin Ç harfine basınız.

    Seçim için sıra numarasını yazınız:  
    """) 

    secim = input()

    if secim == "ç" or secim=="Ç" :
        break

    if  not (secim == "1" or secim == "2" or secim== "3" or secim == "4" ):
        print("Yanlış Giriş Yaptınız.")
        continue


    sayilar = []
    while True:
        sayi = input("Sayıyı Girin (Çıkmak için Ç ye basın):")

        if sayi == "ç" or sayi == "Ç" :
            break
        
        sayi = int(sayi)

        sayilar.append(sayi)

    print(sayilar)

    if secim == "1":
        toplam = 0

        for sayi in sayilar:
            toplam = toplam + sayi
        print(f"Toplama Sonucu:  {toplam}")

    elif secim == "2":
        fark = sayilar[0]
        for index in range(1,len(sayilar)):
            fark = fark - sayilar[index]
        print(f"Çıkarma Sonucu:  {fark}") 

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
