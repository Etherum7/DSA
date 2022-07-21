class Solution:
    
    def josephus(self,n,k):
        #Your code here
        res=[i for i in range(1, n+1)]
        def util(i, k):
            if len(res)==1:
                return res[0]
            res.pop(i)
            index=(i+k)%len(res)
            return util(index, k)
        
        return util((k-1)%n, k-1)