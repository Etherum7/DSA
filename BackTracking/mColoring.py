#User function Template for python3


#Function to determine if graph can be coloured with at most M colours such
#that no two adjacent vertices of graph are coloured with same colour.
def makeAdj(graph,V):
    adj=[[] for _ in range(V)]
    print(graph)
    # for u in range(0,len(graph), 2):
    #     adj[graph[u]].append(graph[u+1])
    #     adj[graph[u+1]].append(graph[u])
    return adj
# colors array store vertices color
def isSafe(vertex, adj, color, colorUsed, V):
    for i in range(V):
        if i!=vertex and adj[vertex][i]==1 and colorUsed[i]==color:
            return False
    return True
        
def util(vertex, adj, colorUsed,  V, k):
    if vertex==V:
        return True
    for color in range(1, k+1):
        if isSafe(vertex, adj,color , colorUsed, V):
            colorUsed[vertex]=color
            # print(vertex)
            if util(vertex+1, adj, colorUsed, V,k):
                return True
            colorUsed[vertex]=0
    return False
def graphColoring(graph, k, V):
    # print(graph)
    colorUsed=[0]*V
    
    return util(0, graph, colorUsed,  V, k)

