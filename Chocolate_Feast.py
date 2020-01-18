def chocolateFeast(n, c, m):
    wrappers = n/c
    num = wrappers
    while True:
        if wrappers/m == 1:
            return num

        leftoverwrappers = wrappers%m
        newchocs = int(wrappers/m)
        num += newchocs
        wrappers = newchocs + leftoverwrappers
        print(wrappers)

n = 15
c = 3
m = 2

result = chocolateFeast(n, c, m)
print(result)
