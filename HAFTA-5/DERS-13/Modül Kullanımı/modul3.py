from math import sin , pi

print("Modulden " , sin(pi / 2 )) #modülden gelen

pi = 3.14 #özel

def sin(x):
    if 2 * x == pi :
        return 0.99999999
    else:
        return None

print ("Özelden " , sin(pi / 2)) #özel tanımlanan