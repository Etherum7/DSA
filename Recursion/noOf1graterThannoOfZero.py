def noOfOneGreaterThanNoOfZero(N):
    res=[]
    def util(N, no, nz, op):
        if N==0:
            res.append(''.join(op))
            return
        if nz+1<=no:
            op1=op.copy()
            op2=op.copy()
            op1.append('1')
            op2.append('0')
            util(N-1, no+1, nz, op1)
            util(N-1, no, nz+1, op2)
        else:
            op1=op.copy()
            op1.append('1')
            util(N-1, no+1, nz, op1)
    no=1
    nz=0
    op=['1']
    util(N-1, no, nz, op)
    return res
print(noOfOneGreaterThanNoOfZero(4))
