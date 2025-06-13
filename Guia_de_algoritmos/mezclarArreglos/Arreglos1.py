#Mezclar Arreglos
TAMANIO = 5

a = [ 5, 4, 3, 2, 78 ]

b = [ 1, 8, 6, 7, 106 ]

c = [ ]

i = 0

for i in range(TAMANIO):
    if i % 2 == 0:
        c.append(a[i])
    elif i % 2 == 1:
        c.append(b[i])

print(c)