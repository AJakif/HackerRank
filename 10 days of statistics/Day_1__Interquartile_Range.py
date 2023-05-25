import statistics as st

inp = int(input())
arr = list(map(int, input().split(' ')[:inp]))
freq = list(map(int, input().split(' ')[:inp]))
newArr = []
for i in range(0, inp):
    for j in range(0,freq[i]):
        newArr.append(arr[i])

newArr.sort()

firstHalf = []
lastHalf = []
# print(newArr)
# print(len(newArr))
if (len(newArr) % 2 == 0):
    for i in range(0, round(len(newArr) / 2)):
        firstHalf.append(newArr[i])
    for i in range(round(len(newArr) / 2), len(newArr)):
        lastHalf.append(newArr[i])
else:
    for i in range(0, round(len(newArr) / 2)):
        firstHalf.append(newArr[i])
    for i in range(round(len(newArr) / 2), len(newArr)):
        lastHalf.append(newArr[i])
q1 = st.median(firstHalf)
q2 = st.median(newArr)
q3 = st.median(lastHalf)
#
# print('First half ', firstHalf )
# print(len(firstHalf))
# print('last half ', lastHalf )
# print(len(lastHalf))
# print('q1 ', q1)
# print('q2 ', q2)
# print('q3 ', q3)
print(float(q3 - q1))