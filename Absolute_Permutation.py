n = 10
k = 3

l = list(range(n+1))[1:]

def absolutePermutation(n,k):
    l = list(range(n+1))[1:]
    res = []
    for i in l:
        for j in l:
            print(l[i-1],j)
            if abs(j-l[i-1]) == k:
                res.append(j)

    print(l)
    print(res)
    # if len(res) != len(l):
    #     return [-1]

    return res


r = absolutePermutation(n,k)
# print(l)
# print(r)
