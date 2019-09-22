#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    k=0
    result=[]
    while k<len(grades):
        for i in grades:
            if i < 38:
                # return i
                result.append(i)
                k+=1
                continue
            else:
                for a in list(filter(lambda x:x%5==0,list(x for x in range(38,101)))):
                    if i==a:
                        result.append(i)
                        k += 1
                        break
                    elif i>=38 and ((i+2)==a or i+1==a):
                        result.append(a)
                        k+=1
                        break#return a
                    elif i-2==a or i-1==a:
                        result.append(i)
                        k+=1
                        break
                    else:
                        continue
                else:
                    result.append(i)#return i
                    k+=1
                    break
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()