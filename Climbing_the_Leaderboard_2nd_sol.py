from bisect import bisect_right, bisect_left

n = int(input())
scores = sorted(set(map(int,input().split())))

m = int(input())
players = map(int,input().split())

for i in players:
    print(len(scores)-bisect_right(scores,i)+1)
