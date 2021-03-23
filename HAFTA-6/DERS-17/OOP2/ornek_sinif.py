class Kalem():
    #renk ="Mavi"
    # sınıf degişkeni - özelliği
    sinif_adi = "Pencil"

    def __init__(self,renk):
        self.rengi = renk #nesne için değişken - property - tanımlanan
        print("Yapıcı constractor metod çalıştı.")


    # def'liye fonksiyon değil metod diyeceğiz artık
    def yazdir(self): #self- kendi demek

        print("Bu kalemin işi yazı yazmaktır.")