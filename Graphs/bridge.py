def findBridges(v, adj, parent, tin, timer, low, vis ):
    vis[v]=True
    timer[0]+=1
    tin[v]=low[v]=timer[0]
    for neighbour in adj[v]:
        if neighbour[0]==parent:
            continue
        if not vis[neighbour[0]]:
            findBridges(neighbour[0],adj, v, tin, timer, low,vis )
            low[v]=min(low[v], low[neighbour[0]])
            # lowest insetion time among all adjacents 
            # if low of adjacent is greater than time of insertion of node
            if low[neighbour[0]]>tin[v]:
                print(v+'--'+neighbour[0])
        else:
            # before coming to twlve it was visited therefore doesnot matter if we remove
            low[v]=min(low[v], tin[neighbour[0]])

V=7
tin=[-1]*V 
# time of inserttion
low=[-1]*V
vis=[False]*V
timer=[0]
findBridges()
