topic = ['10101', '11001', '10111', '10000', '01110']

def acmTeam(topic):
    d = dict.fromkeys(range(1, len(topic)+2), 0)

    for i in range(len(topic)):
        for j in range(i, len(topic)):
            temp = 0
            for a in range(len(topic[i])):
                if topic[i][a] == '1' or topic[j][a] == '1':
                    temp += 1

            d[int(temp)] += 1

    return d

res = acmTeam(topic)
print(res)

key = max(res.keys())
# print(key)
# print(res[key])

