from heapq import heappush, heappop
class Solution:
    
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V, adj):
        #code here
        heap=[]
        keys=[float('inf')]*V
        parent=[-1]*V
        mst=[False]*V
        res=0
        keys[0]=0
        mst[0]=True
        heappush(heap, (0,0))
        
        while len(heap):
            top=heappop(heap)
            mst[top[1]]=True
            for neighbour in adj[top[1]]:
                if not mst[neighbour[0]] and keys[neighbour[0]]>neighbour[1]:
                    keys[neighbour[0]]=neighbour[1]
                    parent[neighbour[0]]=top[1]
                    heappush(heap, (keys[neighbour[0]],neighbour[0]))
        for i in range(1, V):
            # print(adj[parent[i]], i)
            for item in adj[parent[i]]:
                if item[0]==i:
                    res+=item[1]
            # res+=adj[parent[i]][i][1]
        return res
ob=Solution()
print(ob.spanningTree(3, [[[1,5],[2,1]],[[0,5],[2,3]],[[1,3],[0,1]]]))

class Solution2:
    def spanningTree(V, adj):
        mst=[False]*V
        parent=[-1]*V
        keys=[float('inf')]*V
        keys[0]=0
        heap=[]
        heappush(heap,(0,0 ))
        mst[0]=True
        # parent[0]=0
        while len(heap):
            node=heappop(heap)
            mst[node[1]]=True

            for nb in adj[node[1]]:
                if not mst[nb[0]] and nb[1]<keys[nb[0]]:
                    keys[nb[0]]=nb[1]
                    heappush((nb[1], nb[0]))
                    parent[nb[0]]=node[1]
        res=0
        for i in range(V):
            if parent[i]!=-1:
                for nb in adj[i]:
                    if(nb[0]==parent[i]):
                        res+=nb[1]
                        break
        return res





