def pickingNumbers(a):
    result = []
    for i in range(len(a)):
        fox = []
        for j in a:
            if a[i] - j == 1 or a[i] - j == 0:
                fox.append(j)
            result.append(len(fox))
    print(max(result))
pickingNumbers([1, 2, 2, 3, 1, 2])