import statistics as st
import math

inp = int(input())
arr = list(map(int, input().split(' ')[:inp]))
arr.sort()
meanVal = st.mean(arr)
arrSqrSum = 0
for i in range(0,inp):
    arrSqrSum = arrSqrSum + (arr[i] - meanVal)**2

print(round(math.sqrt(arrSqrSum/inp),1))