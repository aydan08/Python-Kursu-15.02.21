class OrnekSinif():
    __sayac = 0
    def __init__(self, deger = 1):
        self.__ilk = deger
        self.ulasılan = "Gizli Değil"
        OrnekSinif.__sayac +=1

#__ gizli eleman, modülü kullanacak kişiden gizlenir.


ornek_nesne1 = OrnekSinif()
print(ornek_nesne1.ulasılan)

print(ornek_nesne1._OrnekSinif__sayac)
# nesneAdi._SınıfAdi__gizliOgeAdi 
#sınıfın gizli öğesine erişebilmee

print(hasattr(OrnekSinif, "__ozellik"))
print(hasattr(ornek_nesne1, "ulasılan"))
