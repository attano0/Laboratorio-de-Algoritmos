Matriz = [
[0, 4, -2],
[5, 0, -3],
[0, 2, 0]
]

columnas = 3
numeroMayor = -99999

Fila = int(input("Selecciona una fila de la matriz (del 0 al 2): "))

while Fila > 2:
    print ("HACE CASO")
    Fila = int(input("Selecciona una fila de la matriz (del 0 al 2): "))

while Fila < 0:
    print ("HACE CASO")
    Fila = int(input("Selecciona una fila de la matriz (del 0 al 2): "))

for i in range(columnas):
    for j in range(columnas): 
        if i == Fila:
            if Matriz[i][j] > numeroMayor:
                numeroMayor = Matriz[i][j]

print(numeroMayor)

