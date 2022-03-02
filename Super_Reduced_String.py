# maybe iterate through the array and delete every occurence of adjacent letters
# end when string is empty or the program does not find any matches
# you will probably have to use a while loop

s = 'aaabccddd'
s = list(s)

while(True):
    found = False
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            s.pop(i+1)
            s.pop(i)
            print(s)
            found = True
            break

    if s == '' or found == False:
        break

print(s)
