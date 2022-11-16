# l largo del pista circular
# lab starts the count from 0
# starting line or change of direction counts 1

t = int(input())

for i in range(t):
    l, n = map(int, input().split())
    pos = 0
    laps = 0
    actual = "C"
    
    for _ in range(n):
        d, c = input().split()
        d = int(d)
        
        if c == "C":
            pos += (d * 1)
        else:
            pos += (d * -1)
        
        if pos >= l:
            circles = pos // l
            laps += circles
            pos -= (l*circles)
        
        elif pos <= (-1*l):
            circles = ((pos*-1) // l)
            laps += circles
            pos += (l*circles)
    
    print("Case #{}: {}".format(i+1, laps))