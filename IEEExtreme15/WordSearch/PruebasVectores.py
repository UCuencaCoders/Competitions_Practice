B = [[1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15],
    [16,17,18,19,20]]

A = [[6,7],
    [11,12]]

def compara():
    for fila in A:
        print(fila)

    print()

    C = []
    for fila in B[1:3]:
        C.append(fila[0:2])

    print(A == C)

res = list(zip(*B))

for fila in B:
    print(fila)

print()

for fila in res:
    print(fila)

print()

for fila in res[::-1]:
    print(fila)

print()

for fila in reversed(res):
    print(fila)





