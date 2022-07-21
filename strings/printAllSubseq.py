def util(ind, s, n,res, op):
    if(ind==n):
        res.append(op)
        return
    if(ind!=0):
        while(ind<n-1 and s[ind]==s[ind+1]):
            ind+=1
    util(ind+1, s, n,res, op+s[ind])
    util(ind+1, s,n, res, op)
    return

def printAll(s):
    res=[]
    op=''
    n=len(s)
    util(0, s,n,res, op)
    # res=set(res)
    return res
# print(printAll('abc'))

print(printAll('aaa'))
