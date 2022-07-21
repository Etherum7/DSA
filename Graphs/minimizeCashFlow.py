def util(netAmount):

    mD=netAmount.index(min(netAmount))
    mC=netAmount.index(max(netAmount))
    if netAmount[mD]==0 and netAmount[mC]==0:
        return

    x=min(abs(netAmount[mD]),netAmount[mC])
    print(f'{mD+1} pay to {mC+1} {x} rupees')
    netAmount[mD]+=x
    netAmount[mC]-=x
    util(netAmount)

def minCashFlow(graph):
    n=len(graph)
    netAmount=[0]*n
    for i in range(n):
        for j in range(n):
            if graph[i][j]!=0:
                netAmount[i]-=graph[i][j]
                netAmount[j]+=graph[i][j]
    # print(netAmount)
    util(netAmount)

    



graph = [ [0, 1000, 2000],
          [0, 0, 5000],
          [0, 0, 0] ]
 
minCashFlow(graph)