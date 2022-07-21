
class Solution:
    def util(self, ind, ip, n,res, op):
        if ind==n:
            res.append(op)
            return
        self.util(ind+1, ip, n,res, op+' '+ip[ind])
        self.util(ind+1, ip, n,res, op+ip[ind])
        
    def permutation (self, S):
        # code here
        ip=list(S)
        # ip.sort()
        # ip=''.join(ip)
        res=[]
        n=len(S)
        self.util(1, ip, n,res, ip[0])
        return res
class Solution:
    def permutation(self, S):
        # code here
        res = []

        def util(ip, op):
            if len(ip) == 0: 
                if op[-1] != ' ':
                    res.append(''.join(op))
                return
            op1 = op.copy()
            op2 = op.copy()
            op1.append(ip[0])
            op2.append(ip[0])
            op2.append(' ')
            tempip = ip.copy()
            tempip.pop(0)
            util(tempip, op1)
            util(tempip, op2)
        sip = list(S)
        
        op = ['']
        util(sip, op)
        return sorted(res)
ob=Solution()
print(ob.permutation('abc'))


