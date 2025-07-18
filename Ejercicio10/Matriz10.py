Matriz = [
[0, 4, -2],
[5, 0, -3],
[0, 2, 0]
]

columnas = 3

col = int(input("Selecciona una columna de la matriz (del 0 al 2) para sumarla: "))

while col > 2:
    print ("HACE CASO")
    col = int(input("Selecciona una columna de la matriz (del 0 al 2): "))

while col < 0:
    print ("HACE CASO")
    col = int(input("Selecciona una columna de la matriz (del 0 al 2): "))

p = 0

for i in range(columnas):
    for j in range(columnas): 
        if j == col:
            p = p +1
            if p == 1:
                num1 = Matriz[i][j]
            if p == 2:
                num2 = Matriz[i][j]
            if p == 3:
                num3 = Matriz[i][j]

suma = num1 + num2 + num3

print("La suma de la columna es: ", suma)