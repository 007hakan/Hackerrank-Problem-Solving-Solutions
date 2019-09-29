def utopianTree(n):
    result=1
    if n%2==0:
        for i in range(n+1):
            if i==0:
                pass
            elif i%2==0:
                result+=1
            else:
                result*=2
    else:
        for i in range(n+1):
            if i==0:
                pass
            elif i%2==0:
                result+=1
            else:
                result*=2
    return result