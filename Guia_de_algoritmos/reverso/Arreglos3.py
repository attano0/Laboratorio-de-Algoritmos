N = 5

a = [5, 0, 7, 8, 9]

b = [ ]

i = 0

for i in range(N):
    b.append(a[N - (i + 1)])

print(b)