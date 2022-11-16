t = int(input())

for case in range(t):
    rs, rh = map(int, input().split())
    n = int(input())
    n_stones = [tuple(map(int, input().split())) for _ in range(n)]
    m = int(input())
    m_stones = [tuple(map(int, input().split())) for _ in range(m)]
    
    distance_n = [((x)**2 + (y)**2)**0.5 for x, y in n_stones]
    distance_m = [((x)**2 + (y)**2)**0.5 for x, y in m_stones]
    
    distance_n.sort()
    distance_m.sort()
    
    try:
        min_n = min(distance_n)
    except:
        min_n = 100**4
    
    try:
        min_m = min(distance_m)
    except:
        min_m = 100**4
    
    total_n = 0
    total_m = 0

    for dis in distance_n:
        if dis < min_m and dis <= rs+rh:
            total_n += 1
    
    for dis in distance_m:
        if dis < min_n and dis <= rs+rh:
            total_m += 1
    
    print("Case #{}: {} {}".format(case+1, total_n, total_m))