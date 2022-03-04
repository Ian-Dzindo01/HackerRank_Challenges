# G - the grid to search
# P - the pattern to search for
# loop over each element and see if there is a match
# if yes continue len(P) times to iterate through the lower rows and see if there is a match with the same indices

G = ['34889246430321978567', '58957542800420926643', '35502505614464308821', '14858224623252492823', '72509980920257761017', '22842014894387119401', '01112950562348692493', '16417403478999610594', '79426411112116726706', '65175742483779283052', '89078730337964397201', '13765228547239925167', '26113704444636815161', '25993216162800952044', '88796416233981756034', '14416627212117283516', '15248825304941012863', '88460496662793369385', '59727291023618867708', '19755940017808628326']

P = ['1641', '7942', '6517', '8907', '1376', '2691', '2599']

n = len(P[0])

def gridSearch(G, P):
    for i in range(len(G)):
        for j in range(i):
            cond = True
            if G[i][j:j+n] == P[0]:
                # print('Yes')
                # print(j, j+n)
                # print(i)

                for a in range(len(P)):
                    if G[i+a][j:j+n] != P[a]:
                        cond = False
                        break

                if cond == True:
                    return 'YES'

    return 'NO'

res = gridSearch(G, P)
print(res)
