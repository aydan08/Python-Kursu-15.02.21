dosya = open("dosya.txt" , "a" , encoding='utf-8') #dosya.txt adında dosya oluşturdu
#"a"  olduğunda üstüne ekler, "w" old eskisini siler yenisini ekler
dosya.write("Birinci Satır\n")
dosya.write("İkinci Satır\n")

satirlar = ["Üçüncü Satır\n" , "Dördüncü Satır\n", "Beşinci Satır\n"]
dosya.writelines(satirlar)

dosya.close()