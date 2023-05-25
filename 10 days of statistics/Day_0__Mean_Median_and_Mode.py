import statistics as st
inp = int(input())
arr = list(map(int, input().split(' ')[:inp]))
print(round(st.mean(arr), 1))
print(round(st.median(arr),1))
if (len(st.multimode(arr)) > 1):
    var = st.multimode(arr)
    var.sort()
    print(var[0])
else:
    print(st.mode(arr))