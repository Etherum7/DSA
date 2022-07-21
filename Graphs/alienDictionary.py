#User function Template for python3
from collections import defaultdict
class Solution:
    def util(self, wordA, wordB, adj):
        if not wordA or not wordB:
            return
        if wordA[0]!=wordB[0]:
            if not adj[ord(wordA[0])-ord('a')]:
                adj[ord(wordA[0])-ord('a')]=[]
            
            adj[ord(wordA[0])-ord('a')].append(ord(wordB[0])-ord('a'))
            
        else:
            self.util(wordA[1:], wordB[1:], adj)
        return
    def topoSort(self,v,  adj ,visited, st ):
        visited[v]=1
        for neighbour in adj[v]:
            if not visited[neighbour]:
                self.topoSort(neighbour, adj, visited, st)
        st.append(chr(v+ord('a')))
        
    def findOrder(self,d, N, K):
        adj=defaultdict(str)
        for i in range(N-1):
            self.util(d[i], d[i+1], adj)
        
        st=[]
        visited=[0]*K
        for i in range(K):
            if not visited[i]:
                self.topoSort(i, adj, visited, st)
        
        return list(reversed(st))