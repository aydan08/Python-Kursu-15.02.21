a = 5
#b = 5/0

try:
    b = 5 / 0
except Exception as hata  : #oluşan hata mesajını alırızz
    print(hata)
    print("Hata Oluştu")

print("Hata oluştu ama program çökmedi.")