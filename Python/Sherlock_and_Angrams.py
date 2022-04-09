# two strings angrams if letters of one can be rearranged to form the other
# the idea is to traverse the values of this dictionary divide each of the counts by 2 and add that to the tally
s = 'mom'

def sherlockAndAnagrams(s):
    subs = []
    r = 0
    for i in range(1, len(s)):
        d = {}                              #temporarily store the count of the substrings in the dictionary
        for j in range(len(s)-i+1):            # loop used to extract all of the substrings of the string
            subs = ''.join(sorted(s[j:j+i]))
            if subs not in d:                   # sorts them in the dictionary
                d[subs] = 1
            else:
                d[subs] += 1

            r += d[subs] - 1

    return r


res = sherlockAndAnagrams(s)
print(res)
