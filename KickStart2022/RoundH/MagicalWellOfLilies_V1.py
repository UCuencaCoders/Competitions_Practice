#Coins > Lilies
#Basket is empty
#1 Coin = 1 Lily
#4 Coins: The well counts de lilies and take a note
#2 Coins: The well will toss out as many lilies as it had last note

t = int(input())

for i in range(t):
    l = int(input())
    res = l
    
    while(True):
        if l < 4:
            break
        else:
            res += (l//4)
            l = (l//4) + (l%4)    
    
    print("Case #{}: {}".format(i+1, l))