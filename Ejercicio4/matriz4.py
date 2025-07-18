Matriz = [
[0, 4, -2],
[5, 0, -3],
[0, 2, 0]
]

columnas = 3
numeroMayor = -99999

columna = int(input("Selecciona una columna de la matriz (del 0 al 2): "))

while columna > 2:
    print ("HACE CASO")
    columna = int(input("Selecciona una columna de la matriz (del 0 al 2): "))

while columna < 0:
    print ("HACE CASO")
    columna = int(input("Selecciona una columna de la matriz (del 0 al 2): "))

for i in range(columnas):
    for j in range(columnas): 
        if j == columna:
            if Matriz[i][j] > numeroMayor:
                numeroMayor = Matriz[i][j]

print(numeroMayor)
