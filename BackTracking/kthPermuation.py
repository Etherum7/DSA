def kthPermutaion(N, K):
    num= [i for i in range(1, N+1)]
    
    def util(op, remaining, c):
        
        if len(op)==N :
            c[0]+=1
            if c[0]==K:
                s = [str(i) for i in op]
                return int(''.join(s))
        for i in remaining:
            op1=op.copy()
            t= remaining.copy()
            t.remove(i)
            op1.append(i)
            ans=util(op1,t, c)
            if ans:
                return ans
    return util([], num, [0])
print(kthPermutaion(3,4))
print(kthPermutaion(2,1))
