class Solution:
    def isValid(self, A,N,M, mid):
        noOfStudent=1
        s=0
        for i in range(N):
            s=s+A[i]
            if s>mid:
                noOfStudent+=1
                s=A[i]
        if noOfStudent>M:
            return False
        return True
    #Function to find minimum number of pages.
    def findPages(self,A, N, M):
        #code here
        start=max(A)
        end=sum(A)
        res=-1
        if M>N:
            return -1
        while start<=end:
            mid=(start+end)//2
            if self.isValid(A, N, M, mid):
                res=mid
                end=mid-1
            else:
                start=mid+1
        return res