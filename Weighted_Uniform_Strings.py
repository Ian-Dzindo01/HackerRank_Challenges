def weightedUniformStrings(s):
    res = []
    for i in range(len(s)):
        temp = 0
        for j in range(i, len(s)):
            if s[i] != s[j]:
                res.append(temp)
                break

            temp +=  ord(s[i])-96


    return res


s = 'aaabbbbcccddd'
r = weightedUniformStrings(s)
print(r)

# brute forcing like this will not work, has to be in n time.
