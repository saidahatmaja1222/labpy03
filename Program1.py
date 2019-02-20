x = 100000000
jum = 0
y = 0
lb = [int(0), int(0),int(x)*1,int(x)*1,int(x)*5,int(x)*5,int(x)*5,int(x)*2]
print("Modal awal pengusaha : ", x)
for i in lb:
    jum = jum + i
    y +=1
    print('Laba bulan ke - ',y, 'sebesar : ',i)
print("Total laba yang di dapat adalah : ", jum)
