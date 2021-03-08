print("Hangi işlemi yapmak istersiniz? ")
print("""
1- Toplama
2- Çıkarma
3- Çarpma
4- Bölme
""")

secim = input("Seçim için sıra numarasını yazınız: ")

a= input("Birinci sayıyı girin= ")
a=int(a)
b=input("İkinci sayıyı girin= ")
b=int(b)

if secim == "1":
    c = a + b
    print("Toplama Sonucu= " , c )
elif secim == "2":
    c = a - b
    print("Çıkarma Sonucu= " , c)
elif secim == "3":
    c = a * b
    print("Çarpma Sonucu= " , c)    
elif secim == "4":
    c = a / b
    print("Bölme Sonucu= " , c)
else :
    print("Geçersiz Seçim Yaptınız!")
