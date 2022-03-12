s = 'RRGGBBXX'

def happyLadybugs(b):
    if len(b) == 1:
        return 'NO'

    if len(list(set(b))) == 1:
        return 'YES'



    if len(list(set(b))) > 1 and '_' not in list(b):
        return 'NO'

    for i in list(set(b)):
        if i == '_':
            continue

        if b.count(i) < 2:
            return 'NO'

    return 'YES'


print(happyLadybugs(s))
