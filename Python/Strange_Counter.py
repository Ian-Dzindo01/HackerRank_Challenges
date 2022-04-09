# 1  3
# 2  2
# 3  1

# 4  6
# 5  5
# 6  4
# 7  3
# 8  2
# 9  1

# 10 12
# 11 11
# 12 10
# 13 9
# 14 8
# 15 7
# 16 6
# 17 5
# 18 4
# 19 3
# 20 2
# 21 1

# 22 24
# 23 23
# 24 22

# 46 48
# 47 47

# probably going to have a time limitation
# find and display the counter value at time t
# find a way to not have to generate the whole list each time
# maybe identify in which section the number is and work from there, generate only the starting number of each grid
# the formula is prev * 2 + 2
# I GET IT
# brilliant solution taken from the discussion page

t = 17
rem = 3
while t > rem:
    t -= rem
    # print(t)
    rem *= 2
    # print(rem)

print(rem-t+1)



