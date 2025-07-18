Matriz = [
[1, 4, -2],
[5, 10, -3],
[12, 2, 8]
]

columnas = 3
elegido = int(input("Elija un numero para buscar en la matriz: "))

p = 0

for i in range(columnas):
    for j in range(columnas): 
        p = p + 1
        if Matriz[i][j] == elegido:
            posicion = (i, j)
            print("Tu numero esta en la posicion: ", posicion)

        elif p == 9:
            print("Tu numero no esta en la matriz ")

