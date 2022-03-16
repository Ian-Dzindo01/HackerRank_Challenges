# Start with the first number and generate a list of the next n numbers and see if it matches the given list
# Because the only numbers that will give 1 as a difference are the ones that are 1 bigger than your number
# Start with the first number, than the first 2, than the first 3 and keep on going like that.

s = '99100'
n = len(s)

# adjust it to form the same number of integers as the length in the string, not more than that
# keep on adding numbers until the lengths are the same, dont use the length of the s string because that is wrong

# adjust the return statement as well
def separateNumbers(s):
    for i in range(1, n):
        temp = int(s[:i])

        t = list(range(temp, temp + n))
        t = ''.join(str(e) for e in t)
        print(t)
        print('YES' + ' ' + t[0] if t[:len(s)] == s else 'NO')
        return 0

separateNumbers(s)





