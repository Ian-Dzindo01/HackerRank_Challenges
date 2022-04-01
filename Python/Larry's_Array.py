import numpy as np

# Rotations of triples by going backwards each iteration.
# this one is difficult
# Maybe traverse the array and see if triplets are descending, if not try to rearrange them using the provided procedure.
# Implement a special function for the procedure.

# A = [1, 6, 5, 2, 3, 4]

# for i in range(len(A)-2):
#     if sorted(A[i:i+3]) != A[i:i+3]:
#         temp = check(A[i:i+3])
#         if temp == 0:
#             return "NO"

# def check(l):
#     if np.roll(l, -1) == sorted(l):
#         return np.roll(l, -1)
#     elif np.roll(l, -2) == sorted(l):
#         return np.roll(l, -2)
#     elif np.roll(l, -3) == sorted(l):
#         return np.roll(l, -3)
#     else:
#         return 0







