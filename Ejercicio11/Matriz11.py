Matriz = [
[0, 4, -2],
[5, 0, -3],
[0, 2, 0]
]

columnas = 3

Fila1 = int(input("Selecciona una fila de la matriz (del 0 al 2) para intercambiar: "))

while Fila1 > 2:
    print ("HACE CASO")
    Fila1 = int(input("Selecciona una fila de la matriz (del 0 al 2) para intercambiar: "))

while Fila1 < 0:
    print ("HACE CASO")
    Fila1 = int(input("Selecciona una fila de la matriz (del 0 al 2) para intercambiar: "))


Fila2 = int(input("Selecciona una fila de la matriz (del 0 al 2) para intercambiar: "))

while Fila2 > 2:
    print ("HACE CASO")
    Fila2 = int(input("Selecciona una fila de la matriz (del 0 al 2) para intercambiar: "))

while Fila2 < 0:
    print ("HACE CASO")
    Fila2 = int(input("Selecciona una fila de la matriz (del 0 al 2) para intercambiar: "))


q = 0
p = 0

for i in range(columnas):
    for j in range(columnas): 
        if i == Fila1:
            p = p +1
            if p == 1:
                numa1 = Matriz[i][j]
            if p == 2:
                numa2 = Matriz[i][j]
            if p == 3:
                numa3 = Matriz[i][j]
        
        if i == Fila2:
            q = q +1
            if q == 1:
                numb1 = Matriz[i][j]
            if q == 2:
                numb2 = Matriz[i][j]
            if q == 3:
                numb3 = Matriz[i][j]

Matriz[Fila2] = [numa1, numa2, numa3]

Matriz[Fila1] = [numb1, numb2, numb3]

print("Asi quedo la matriz: ", Matriz)