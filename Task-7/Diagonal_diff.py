import math
import os
import random
import re
import sys

def diagonalDifference(arr,n):
    count=0
    sum1=0
    sum2=0
    m1=0
    m2=n-1
    while(count<n):
        sum1=sum1+arr[count][m1]
        sum2=sum2+arr[count][m2]
        count+=1
        m1+=1
        m2-=1
    return abs(sum1-sum2)
    
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr,n)

    fptr.write(str(result) + '\n')

    fptr.close()
