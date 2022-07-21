class Solution:
    def getNextFib(self,res):
        res.append(res[-1]+res[-2])
    def solve(self, N, A):
        res=[1,1]
        i=j=0
        cnt=0
       
        while i< N and j<N:
            if A[i]==res[j]:
                self.getNextFib(res)
                i+=1
                j+=1
                cnt+=1
            else:
                i+=1
        return cnt