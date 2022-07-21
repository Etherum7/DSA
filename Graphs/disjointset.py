parent=[i for i in range(100)]
rank=[0]*101
def findPar(u):
    if u==parent(u):
        return u
    parent[u]=findPar(parent[u])
    return parent[u]

def union(u,v):
    u=findPar(u)
    v=findPar(v)
    if u==v:
        return
    if rank(u)>rank(v):
        parent[v]=u
    elif rank[u]<rank[v]:
        parent[u]=v
    else:
        parent[v]=u
        rank[u]+=1

class Solution:
    
    #Function to merge two nodes a and b.
    def union_(self,a,b,parent,rank):
        # code here
        u=parent[a]
        v=parent[b]
        if u==v:
            return
        if rank[u]>rank[v]:
            parent[v]=u
        elif rank[v]>rank[u]:
            parent[u]=v
        else:
            parent[v]=u
            rank[u]+=1
            
        
    #Function to check whether 2 nodes are connected or not.
    
    def findPar(self, x, par):
        if par[x]==-1:
            return x
        return self.findPar(par[x], par)
        
    def isConnected(self,x,y,par,rank1):
        # code here
        return self.findPar(x, par)==self.findPar(y, par)