# Start with the first number and generate a list of the next n numbers and see if it matches the given list
# Because the only numbers that will give 1 as a difference are the ones that are 1 bigger than your number
# Start with the first number, than the first 2, than the first 3 and keep on going like that.

s = '1234'
n = len(s)

t = list(range(int(s[0]), int(s[0]) + n))
t = ''.join(str(e) for e in t)

for i in range(1, n):
    temp = int(s[:i])
    t = list(range(temp, temp + n))
    t = ''.join(str(e) for e in t)







