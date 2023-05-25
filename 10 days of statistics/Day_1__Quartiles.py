import statistics as st

inp = int(input())
arr = list(map(int, input().split(' ')[:inp]))
arr.sort()
firstHalf = []
lastHalf = []
q2 = round(st.median(arr))
if (inp % 2 == 0):
    for i in range(0, round(inp / 2)):
        firstHalf.append(arr[i])
    for i in range(round(inp / 2), inp):
        lastHalf.append(arr[i])
else:
    for i in range(0, round(inp / 2)):
        firstHalf.append(arr[i])
    for i in range(round(inp / 2)+1, inp):
        lastHalf.append(arr[i])
q1 = round(st.median(firstHalf))
q3 = round(st.median(lastHalf))

print(q1)
print(q2)
print(q3)