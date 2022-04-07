# two strings angrams if letters of one can be rearranged to form the other

s = 'mom'
n = len(s)

for i in range(1, n):
    for j in range(n-i+1):
        print(s[j:j+i])
