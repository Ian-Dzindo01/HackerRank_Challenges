from collections import Counter

lst = []
arr = ['smp', 'mgm', 'hmh', 'rmtt', 'kmnk', 'bmvb', 'lmtc']

for i in range(len(arr)):
    for j in list(arr[i]):
        lst.append(j)

list_freq = Counter(lst)

cnt = 0

for i in list_freq.values():
    if i == len(arr)+1:
        cnt += 1

print(cnt)
