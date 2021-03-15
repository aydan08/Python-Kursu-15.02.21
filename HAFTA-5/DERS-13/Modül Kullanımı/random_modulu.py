import random 

#random.seed(45)

rastgele_sayi = random.random()
print(rastgele_sayi)


r_s_2 = random.randrange(100)
print(r_s_2)

r_s_3 = random.randrange(100, 1000, 40)
print(r_s_3)

liste = [1,2,3,4,5,6,7,8,9,10]
print(random.choice(liste))

print(random.sample(liste,3))