y=1880
x=y//100
if (x * 100) % 400 == 0 and (y % 4 == 0 and y % 100 == 0):
    print(True)
else:
    print((False))