import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    values = [calcula_hourglass(arr, linha_inicial, coluna_inicial) for linha_inicial in range(0,4) for coluna_inicial in range(0,4)]
    return max(values)

def calcula_hourglass(arr, linha_inicial, coluna_inicial):
    return arr[linha_inicial][coluna_inicial] + arr[linha_inicial][coluna_inicial + 1] + arr[linha_inicial][coluna_inicial + 2] + arr[linha_inicial + 1][coluna_inicial + 1] + arr[linha_inicial + 2][ coluna_inicial] + arr[linha_inicial + 2][coluna_inicial + 1] + arr[linha_inicial + 2][coluna_inicial + 2] 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

# Reference for the solution: https://www.youtube.com/watch?v=5EBCcP2JMoQ