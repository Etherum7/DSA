from audioop import reverse


class Solution:
    def util(self, x, n):
        if n==0:
            return 1.0
        if n==1:
            return x
        res=self.util(x, n//2)
        if n%2!=0:
            return x*res*res
        return res*res
    def myPow(self, x: float, n: int) -> float:
        isNeg= n<0
        res=1.0
        ans = self.util(x, abs(n))
        if isNeg:
            return 1/ans
        else:
            return ans
# reverse no neg
def power(self,N,R):
        #Your code here
        ans=1
        while R:
            
            if R%2:
                ans=(ans*N)%(10**9+7)
                R-=1
            
            else:
                N=(N*N)%(10**9+7)
                R=R//2
        return ans