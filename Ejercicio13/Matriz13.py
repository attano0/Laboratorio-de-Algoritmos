Matriz = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]

columnas = 3

p = 0

for i in range(columnas):
    for j in range(columnas): 
            p = p +1
            if p == 1:
                num1 = Matriz[i][j]
            if p == 2:
                num2 = Matriz[i][j]
            if p == 3:
                num3 = Matriz[i][j]
            if p == 4:
                num4 = Matriz[i][j]
            if p == 5:
                num5 = Matriz[i][j]
            if p == 6:
                num6 = Matriz[i][j]
            if p == 7:
                num7 = Matriz[i][j]
            if p == 8:
                num8 = Matriz[i][j]
            if p == 9:
                num9 = Matriz[i][j]


Matriz[0][0] = num9
Matriz[0][1] = num1
Matriz[0][2] = num2

Matriz[1][0] = num3
Matriz[1][1] = num4
Matriz[1][2] = num5

Matriz[2][0] = num6
Matriz[2][1] = num7
Matriz[2][2] = num8

print(Matriz)