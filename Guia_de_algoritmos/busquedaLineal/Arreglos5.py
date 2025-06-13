N = 5

a = [26, 11, 2011, 23, 15, 9, 12, 18, 2018, 912, 91218, 9122018, 26062011, 6, 266, 2013]

facu = int(input("Ingresar número entero: "))

l = -1

for i in a:
    l = l + 1
    if i == facu:
        print(l)
        break
    elif l == 15:
        print("Número no encontrado")
