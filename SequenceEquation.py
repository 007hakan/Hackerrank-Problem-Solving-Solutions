# def permutationEquation(p):
#     result=[]
#     for i in range(1,len(p)+1):
#         for j in p:
#             if j==p[(p[i])]:
#                 result.append(p[i])
#     print(result)
# permutationEquation([2 ,3 ,1])

def wrap(string, max_width):
    for i in range(len(string)):
        print()
        if i%max_width==0:
            print(string[i],end="")
        continue


wrap("ABCDEFGHIJKLIMNOQRSTUVWXYZ",4)