t = int(input())

for case in range(t):
    m, n, p = map(int, input().split())
    
    scoreboard = []
    for participant in range(m):
        if participant+1 != p:
            scoreboard.append(list(map(int, input().split())))
        else:
            jhon = list(map(int, input().split()))

    days = list(zip(*scoreboard))

    total = 0
    
    for i in range(n):
        extra = max(days[i]) - jhon[i]
        if extra > 0:
            total += extra
    
    print("Case #{}: {}".format(case+1, total))