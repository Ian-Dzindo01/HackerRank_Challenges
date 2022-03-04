# G - the grid to search
# P - the pattern to search for
# loop over each element and see if there is a match
# if yes continue len(P) times to iterate through the lower rows and see if there is a match with the same indices

G = ['7283455864', '6731158619', '8988242643', '3830589324', '2229505813', '5633845374', '6473530293', '7053106601', '0834282956', '4607924137']
P = ['9505', '3845', '3530']
n = len(P[0])

for i in range(len(G)):
    for j in range(i):
        if G[i][j:j+n] == P[0]:
            print('Yes')
            print(j, j+n)
            print(i)

        for a in len(P):
            if G[i+a][j:j+n] != P[a]:
                break


