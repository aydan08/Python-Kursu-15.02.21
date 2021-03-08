#1 den 100 e kadar olan tek sayıların toplamı
toplam = 0
for tek_sayi in range(1,100,2): #(1 DAHİLDİR,100 DAHİL DEĞİLDİR,+2 ARTIŞ MİKTARIDIR)
    toplam = toplam + tek_sayi
else:
    print("...Döngü Bitti...")    

print("Tek Sayıların Toplamı: ", toplam) #yerine alttaki de kullanılıyorr
print(f"Tek Sayıların Toplamı: {toplam}")