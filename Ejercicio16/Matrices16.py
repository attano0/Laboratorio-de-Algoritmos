Matriz1 = [
[1.1, 2.1 ],
[3.4, 4.0 ]
]

Matriz2 = [
[9.1, 2.1 ],
[1.4, 3.0 ]
]

columnas = 2

p = 0
q = 0

for i in range(columnas):
    for j in range(columnas): 
        p = p +1
        if p == 1:
           numa1 = Matriz1[i][j]
        if p == 2:
           numa2 = Matriz1[i][j]
        if p == 3:
           numa3 = Matriz1[i][j]
        if p == 4:
           numa4 = Matriz1[i][j]

        q = q+1
        if q == 1:
            numb1 = Matriz2[i][j]
        if q == 2:
            numb2 = Matriz2[i][j]
        if q == 3:
            numb3 = Matriz2[i][j]
        if q == 4:
            numb4 = Matriz2[i][j]
         
MatrizFinal = [
    [0, 0],
    [0, 0]
]

resta1 = numa1 - numb1
resta2 = numa2 - numb2
resta3 = numa3 - numb3
resta4 = numa4 - numb4

MatrizFinal[0][0] = resta1
MatrizFinal[0][1] = resta2
MatrizFinal[1][0] = resta3
MatrizFinal[1][1] = resta4

print(MatrizFinal)