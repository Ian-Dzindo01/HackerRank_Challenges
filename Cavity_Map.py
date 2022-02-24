s = ['1112', '1912', '1892', '1234']

arr = [[0 for x in range(len(s))] for x in range(len(s))]

for i in range(len(s)):
    for j in range(len(s)):
        arr[i][j] = int(s[i][j])

print(arr)

for i in range(1, len(s)-1):
    for j in range(1, len(i[j])-1):
        if

# 1112
# 1912
# 1892
# 1234
