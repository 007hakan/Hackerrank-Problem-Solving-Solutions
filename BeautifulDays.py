def beautifulDays(i, j, k):
    sayac=0
    for j in range(i,j+1):
        reverse=str(j)
        z=int(reverse[::-1])
        if abs(j-z)%k==0:
            sayac+=1
    print(sayac)
beautifulDays(13,45,3)