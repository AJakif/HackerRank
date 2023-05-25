inp = int(input())
x = list(map(int, input().split(' ')[:inp]))
w = list(map(int, input().split(' ')[:inp]))
sumOfXiWi = 0
sumOfW = sum(w)

for i in range(0,inp):
    mult = (x[i] * w[i])
    sumOfXiWi += mult
print(round(sumOfXiWi/sumOfW,1))