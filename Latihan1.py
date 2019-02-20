print("Bilangan acak yang lebih kecil dari 0.5\n")

import random

n = int(input("Masukkan nilai N: "))
a = 0
for i in range(n):
    a +=1
    b = random.uniform(0.0,0.5)
    print('Data ke: ',a, '==>',b)
print("Selesai")