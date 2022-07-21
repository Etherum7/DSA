def allSubset(ip):

    def util(inp:list, op):
        if len(inp) ==0:
            print(''.join(op))
            return
        op1=op.copy()
        op2=op.copy()
        op2.append(inp[0])
        # print(inp)
        tempip= inp.copy()
        tempip.pop(0)
        util(tempip, op1)
        util(tempip,op2)
    temp=list(ip)
    
    op=['']
    util(temp, op)
allSubset('ab')