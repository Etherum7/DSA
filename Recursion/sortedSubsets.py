class Solution:
    def subsets(self, A):
        #code here
        res=[]
        
        def util(ip, op):
            if len(ip)==0:
                res.append(op.copy())
                return
            op1=op.copy()
            op2=op.copy()
            op1.append(ip[0])
            tempip=ip.copy()
            tempip.pop(0)
            
            util(tempip, op2)
            util(tempip, op1)
            
        op=[]
        util(A,op)
        return sorted(res)