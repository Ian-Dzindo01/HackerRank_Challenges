distances = []
l = list(range(n))
for i in range(n):
    for a in range(i,n):
        if l[a] in c:
            distances.append(abs(l[a]-c[c.index(l[a])]))

    for b in reversed(list(range(i,n))):
        if l[b] in c:
            distances.append(abs(l[b]-c[c.index(l[b])]))

    return max(distances)
