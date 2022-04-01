import numpy as np

# Rotations of triples by going backwards each iteration.
# this one is difficult
# Maybe traverse the array and see if triplets are descending, if not try to rearrange them using the provided procedure.
# Implement a special function for the procedure.


# Cannot use numpy in the submissions on HackerRank, will upload this to GitHub, but also search for another solution.
# This will also need improvement. Does not work properly.

A = [1, 6, 5, 2, 3, 4]

def larrysArray(A):
    while(True):
        for i in range(1, len(A)-2):
            if sorted(A[i:i+3]) != A[i:i+3]:
                temp = check(A[i:i+3])
                if temp == 0:
                    return "NO"
                else:
                    A[i:i+3] = temp

                print(A)

            if A == sorted(A):
                return "YES"

def check(l):
    print(l)
    if list(np.roll(l, -1)) == sorted(l):
        return list(np.roll(l, -1))
    elif list(np.roll(l, -2)) == sorted(l):
        return list(np.roll(l, -2))
    elif list(np.roll(l, -3)) == sorted(l):
        return list(np.roll(l, -3))
    else:
        return 0

r = larrysArray(A)
print(r)
