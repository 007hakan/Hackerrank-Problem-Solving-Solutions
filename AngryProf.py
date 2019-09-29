def angryProfessor(k, a):
    count=0
    for i in a:
        if i<=0:
            count+=1
        else:
            pass
    if count>=k:
        return "NO"
    else:
        return "YES"
