s = 'www.abc.xy'
k = 87
res = ''

ran = list(range(65,91)) + list(range(97,123))

for i in s:
    if ord(i) not in ran:
        res += i
        continue

    if ord(i) in list(range(91-k, 91)):
        res += chr(65 + k-1-(90-ord(i)))
        continue


    if ord(i) in list(range(123-k, 123)):
        res += chr(97 + k-1-(122-ord(i)))
        continue

    res += chr(ord(i)+k)


print(res)
