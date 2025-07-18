Matriz = [
[0, 4, 2],
[5, 0, 3],
[0, 2, 0]
]

columnas = 3
suma = 0

for i in range(columnas):
    for j in range(columnas): 
        suma += Matriz[i][j] 

print("La suma de la matriz es: ", suma)
