def sub(arr):
    for i in range(len(arr)):
        if i == 0: 
            past = arr[i]
        else:
            past += arr[i]
        
        if past < 0:
            return 0
    return past

t = int(input())

for case in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    total = 0
    for i in range(n):
        for j in range(i+1,n+1):
            total += sub(a[i:j])
    
    print("Case #{}: {}".format(case+1, total))