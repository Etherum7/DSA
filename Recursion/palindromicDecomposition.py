from typing import List
class Solution:
    def util(self, pos, S,s, res, op):
        if len(op)>0 and op[-1]!=op[-1][::-1]:
            return
        if ''.join(op)==S:
            res.append(op)
            return
        if pos<len(s):
            
            op1=op.copy()
            op1.append(s[:pos+1])
            op2=op.copy()
            s1=s[pos+1:]
            self.util(0, S,s1, res, op1)
            self.util(pos+1, S,s, res, op2)
        
            
    def partition(self, s: str) -> List[List[str]]:
        res=[]
        op=[]
        self.util(0, s,s, res, op)
        return res


from itertools import groupby
class Solution:
    def allPalindromicPerms(self, S):
        # code here
        res=[]
        n=len(S)

        def util(ip, op, pos):
            # if len(op)>0 and op[-1]!=op[-1][::-1]:
            #     return
            if ''.join(op)==S :
                res.append(op.copy())
                return
            if pos<=len(ip):

                op1=op.copy()
                op2=op.copy()
                tempip1=ip.copy()
                tempip2=ip.copy()
                
                op1.append(''.join(ip[:pos+1]))
                tempip1=tempip1[pos+1:]
                if len(op1)>0 and op1[-1]==op1[-1][::-1]:
                    util(tempip1, op1, 0 )

                util(tempip2, op2, pos+1)
                

        ip=list(S)
        util(ip, [], 0)
        res.sort()

        return list(k for k,_ in groupby(res) )
ob=Solution()
# print(ob.allPalindromicPerms('aaa'))

# def palindromicDecomposition(text):
#     res=[]
#     def util(offset, partial):
#         if offset==len(text):
#             res.append(partial.copy())
#             return
#         for i in range(offset+1, len(text)+1):
#             prefix=text[offset: i]
#             if prefix==prefix[::-1]:
#                 util(i, partial+[prefix])
#     util(0, [])
#     return res
# print(palindromicDecomposition('aab'))
def isPalindrome(s, start, end):
    while start<end:
        if(s[start]!=s[end]):
            return False
        start+=1
        end-=1
    return True

def partition(ind, s, n, res, op):
    if(ind==n):
        res.append(op.copy())
        return
    for i in range(ind, n):
        if(isPalindrome(s, ind, i)):
            op.append(s[ind:i+1])
            partition(i+1, s, n, res, op)
            op.pop()
def allPalindromicPerms(s, n):
    res=[]
    op=[]
    partition(0, s, n, res, op)
    return res

print(allPalindromicPerms('aaab', 4))

