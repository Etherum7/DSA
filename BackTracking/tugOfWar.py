def util(arr, n, firstSet, secondSet, firstSum, secondSum, pos, total, res):
    # base case
    if pos >= n:
        return
    if total == n//2:
        if abs(secondSum-firstSum) < res[0]:
            res[0] = abs(secondSum-firstSum)
            res[1]=firstSet.copy()
            res[2]=secondSet.copy()
            return
    # 2 calls
    fS1=firstSet.copy()
    fS2=firstSet.copy()
    sS1=secondSet.copy()
    sS2=secondSet.copy()

    fS1[pos]=1
    sS1[pos]=0

    
    util(arr, n, fS1, sS1, firstSum +
         arr[pos], secondSum-arr[pos], pos+1, total+1, res)
    util(arr, n, fS2, sS2, firstSum, secondSum, pos+1, total, res)
    return


def tugOfWar(arr, n):
    res = [float('inf'),0,0]
    s = sum(arr)
    firstSet = [0]*n
    secondSet = [1]*n
    util(arr, n, firstSet, secondSet, 0, s, 0, 0, res)
    print(res[0])
    s=0


    for i in range(n):
        if res[1][i]==1:
            s+=arr[i]

            print(arr[i],' ',end=' ')
    print(s)
    s=0
    for i in range(n):
        if res[2][i]==1:
            s+=arr[i]
            print(arr[i],' ',end=' ')
    print(s)    


    return


arr = [23, 45, -34, 12, 0, 98,
       -99, 4, 189, -1, 4]
arr=[3, 4, 5, -3, 100, 1, 89, 54, 23, 20]
n = len(arr)
tugOfWar(arr, n)
