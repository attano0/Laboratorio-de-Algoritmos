Matriz = [
[1.1, 2.1 ],
[3.4, 4.0 ]
]

columnas = 2

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
         

Matriz[0][0] = num1
Matriz[0][1] = num3
Matriz[1][0] = num2
Matriz[1][1] = num4

print(Matriz)