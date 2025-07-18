Matriz = [
[0, 4, -2],
[5, 0, -3],
[0, 2, 0]
]

columnas = 3
numeroMayor = -99999

for i in range(columnas):
    for j in range(columnas): 
        if Matriz[i][j] > numeroMayor:
            numeroMayor = Matriz[i][j]
            posicion = i,j

print(posicion)