def breakingRecords(scores):
    min_score = scores[0]
    max_score = scores[0]
    max_cnt = 0
    min_cnt = 0

    for x in range(len(scores)):
        if(scores[x] > max_score):
            max_score = scores[x]
            max_cnt += 1
        elif(scores[x] < min_score):
            min_score = scores[x]
            min_cnt += 1

    return max_cnt, min_cnt


scores = [10, 5, 20, 20, 4, 5, 2, 25, 1]

res1, res2 = breakingRecords(scores)

print(res1)
print(res2)
