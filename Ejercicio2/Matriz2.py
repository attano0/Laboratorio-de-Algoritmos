Matriz = [
[0, 4, -2],
[5, 0, -3],
[0, 2, 0]
]

columnas = 3
positivos = 0

for i in range(columnas):
    for j in range(columnas): 
        if Matriz[i][j] > 0:
            positivos = positivos +1

print("Tu matriz tiene ", positivos, " numeros positivos")
