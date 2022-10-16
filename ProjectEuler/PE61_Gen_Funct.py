def polygonal(number, n):
    def p3(n):
        return (n*(n+1))/2
    def p4(n):
        return n**2
    def p5(n):
        return (n*((3*n)-1))/2
    def p6(n):
        return n*((2*n)-1)
    def p7(n):
        return (n*((5*n)-3))/2
    def p8(n):
        return (n*((3*n)-2))
    vec = [0,0,0,p3, p4, p5, p6, p7, p8,]
    return int(vec[number](n))

array = list(map(int,input().split()))

min = 19
max = 145

total = 0
marco = []

for j in range(len(array)):
    lista = []
    for i in range(15,200):
        res = polygonal(array[j],i)
        if res >= 1000 and res <= 9999:
            lista.append(str(res))
        elif res > 9999:
            break
    
    marco.append(lista)

for val in marco:
    print(val)