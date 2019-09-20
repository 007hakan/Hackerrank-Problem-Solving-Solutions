st=[7 ,11]
ab=[5,15]

apples=[2, 3, -4]
oranges=[3,-2,-4]
def countApplesAndOranges(s, t, a, b, apples, oranges):
    ap=0
    op=0
    for i in range(s,t+1):
        for j in apples:
            if j<0:
                continue
            elif a+j==i:
                ap+=1
        for z in oranges:
            if z>0:
                continue
            if b+z==i:
                op += 1

    print(ap,op)

countApplesAndOranges(7,10,4,12,apples,oranges)