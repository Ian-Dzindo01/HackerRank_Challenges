# split the string into two and of equal length and subtract the number of shared letters from the length of one of the separated strings
# return -1 if there is nothing that can be done

s = 'abccde'
s1 = s[:len(s)//2]
s2 = s[len(s)//2:]

