print("Menentukan Bilangan Terbesar\n")

max = 0
while True:
    a = int(input("Masukkan Bilangan : "))
    if max < a:
        max = a
    if a == 0:
        break
print("Bilangan terbesar adalah : ",max)