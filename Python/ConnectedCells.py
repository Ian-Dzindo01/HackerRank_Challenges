# 1 1 0 0
# 0 1 1 0
# 0 0 1 0
# 1 0 0 0

# traverse the grid from top to bottom and start searching on any 1 that you find
# store the maximum value you found and if you find another one compare it and again store max
# implement a check function which will determine where to proceed after you found a path
# if the check function returns a coordinate, recall the check function with that new coordinate
# if it does not find a coordinate terminate and return the length of the region
# keep a counter to count each value traversed

 grid = [[1, 1, 1, 0], [0, 1, 1, 0], [0, 0, 1, 0], [1, 0, 0, 0]]

def check()
