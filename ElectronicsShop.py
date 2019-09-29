def getMoneySpent(keyboards, drives, b):
    keyboards.sort()
    drives.sort()
    result=[]
    for i in range(len(keyboards)):
        for j in range(len(drives)):
            if keyboards[i]+drives[j]<=b:
                result.append(keyboards[i]+drives[j])
            elif keyboards[i]+drives[j]>b:
                pass
    if len(result)>=1:
        print(max(result))
    else:
        print("-1")
getMoneySpent([4],[5],5)