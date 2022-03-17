l1 = 'cde'
l2 = 'abc'


print(abs(len(list(set(l1).intersection(l2))) - (len(l1)+len(l2))) - 1)
