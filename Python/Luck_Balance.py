# you got the logic a bit wrong.Rethink

a = [[5, 1], [2, 1], [1, 1], [8, 1], [10, 0], [5, 0]]
k = 3
res = 0

res += sum([i[0] for i in a if i[1] == 0])
res += sum(sorted([i[0] for i in a if i[1] == 1])[:k])

print(res)
