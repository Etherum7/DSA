class Solution:
    # def makeGraph(self, n,edges):
    #     adj=[]
    #     for i in range(n):
    #         adj.append([])
    #     for u,v, w in edges:
    #         adj[u].append([u,v,w])
    #     return adj

    def isNegativeWeightCycle(self, n, edges):
        # Code here
        dist1 = [float('inf')]*n

        dist1[0] = 0
        for i in range(n-1):
            for u, v, w in edges:
                if dist1[u]+w < dist1[v]:
                    dist1[v] = dist1[u]+w
        dist2 = dist1.copy()

        for u, v, w in edges:
            if dist2[u]+w < dist2[v]:
                return 1

        return 0
