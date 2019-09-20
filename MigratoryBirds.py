def migratoryBirds(*arr):
    dic={}
    for i in arr:
        x=arr.count(i)
        dic[i]=x
    bos = []
    for i,j in dic.items():
        if j==max(dic.values()):
            bos.append(i)
    return print(min(bos))

migratoryBirds(1,1,1,2,2,2,4,4,4,5)