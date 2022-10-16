n = int(input())
coincidences = []
matrix = []

for i in range(n):
    code, coin = input().split()
    matrix.append(code)
    coincidences.append(int(coin))

