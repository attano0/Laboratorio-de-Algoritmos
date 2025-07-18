Matriz = [
[0, 4, -2],
[5, 0, -3],
[0, 2, 0]
]

columnas = 3

col1 = int(input("Selecciona una columna de la matriz (del 0 al 2) para intercambiar: "))

while col1 > 2:
    print ("HACE CASO")
    col1 = int(input("Selecciona una columna de la matriz (del 0 al 2) para intercambiar: "))

while col1 < 0:
    print ("HACE CASO")
    col1 = int(input("Selecciona una columna de la matriz (del 0 al 2) para intercambiar: "))


col2 = int(input("Selecciona una columna de la matriz (del 0 al 2) para intercambiar: "))

while col2 > 2:
    print ("HACE CASO")
    col2 = int(input("Selecciona una columna de la matriz (del 0 al 2) para intercambiar: "))

while col2 < 0:
    print ("HACE CASO")
    col2 = int(input("Selecciona una columna de la matriz (del 0 al 2) para intercambiar: "))


q = 0
p = 0

for i in range(columnas):
    for j in range(columnas): 
        if j == col1:
            p = p +1
            if p == 1:
                numa1 = Matriz[i][j]
            if p == 2:
                numa2 = Matriz[i][j]
            if p == 3:
                numa3 = Matriz[i][j]
        
        if j == col2:
            q = q +1
            if q == 1:
                numb1 = Matriz[i][j]
            if q == 2:
                numb2 = Matriz[i][j]
            if q == 3:
                numb3 = Matriz[i][j]

Matriz[0][col2] = numa1
Matriz[1][col2] = numa2
Matriz[2][col2] = numa3

Matriz[0][col1] = numb1
Matriz[1][col1] = numb2
Matriz[2][col1] = numb3

print("Asi quedo la matriz: ", Matriz)