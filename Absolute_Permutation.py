n = 2
k = 1

l = list(range(n+1))[1:]
print(l)
res = []
for i in l:
    for j in l:
        if abs(l[i-1]-j):
            res.append(j)
print(res)
