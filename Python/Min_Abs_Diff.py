arr = [[8, 1], [4, 2], [5, 6], [3, 1], [4, 3]]

def jimOrders(orders):
    d = {}
    for i in range(len(orders)):
        d[i+1] = orders[i][0] + orders[i][1]

    d = dict(sorted(d.items(), key=lambda item: item[1]))

    print(list(d.keys()))
