#User function Template for python3
import sys
sys.setrecursionlimit(10**5)
class Solution:
    def isCycle(self, v, recStack, visited, adj):
        visited[v]=1
        recStack[v]=1
        for neighbour in adj[v]:
            if not visited[neighbour]:
                if self.isCycle(neighbour, recStack, visited, adj):
                    return True
            elif recStack[neighbour]==1:
                return True
        recStack[v]=False
        return False
    def isPossible(self,N,pre):
        #code here
        adj=[[] for i in range(N)]
        for p in pre:
            adj[p[0]].append(p[1])
        visited=[False]*N
        recStack=[0]*N
        for i in range(N):
            if not visited[i]:
                if self.isCycle(i,recStack, visited , adj):
                    return False
        return True
                
            
        
        
    

#{ 
#  Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        N=int(input())
        P=int(input())

        prerequisites=[]
        for _ in range(P):
            pair = [int(x) for x in input().split()]
            prerequisites.append(pair)
        ob=Solution()
        if(ob.isPossible(N,prerequisites)):
            print("Yes")
        else:
            print("No")
# } Driver Code Ends