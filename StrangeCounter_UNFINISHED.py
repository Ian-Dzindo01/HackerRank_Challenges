# 1   3 -
# 2   2 -
# 3   1 -
# 4   6 -
# 5   5 -
# 6   4 -
# 7   3 -
# 8   2 -
# 9   1 -
# 10  12 -
# 11  11 -
# 12  10 -
# 13  9 -
# 14  8 -
# 15  7 -
# 16  6 -
# 17  5 -

# Do not make lists or dictionaries because you wont need to write out everything to retrieve just one element.
t = 13
t1 = 3
while(t1 < t):
    t -= t1
    t1 *= 2
    print(t)
    print(t1)

print(t1 - t + 1)
