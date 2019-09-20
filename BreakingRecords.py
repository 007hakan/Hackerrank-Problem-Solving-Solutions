scores=[3, 4 ,21 ,36, 10 ,28 ,35, 5 ,24, 42]
yuksek=[]
dusuk=[]

for i in scores:
    if i > scores[0] and len(yuksek)<1:
        yuksek.append(i)

    elif i < scores[0] and len(dusuk)<1:
        dusuk.append(i)

for i in scores:
    for j in yuksek:
        if i>max(yuksek) and i not in yuksek:
            yuksek.insert(0, i)
            continue
    for j in dusuk:
        if i<min(dusuk) and i not in dusuk:
            dusuk.insert(0, i)
            continue
print(len(yuksek), len(dusuk))

print(yuksek)
print(dusuk)