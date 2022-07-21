def inversionCount(arr,n):
    res=0
    for i in range(n):
        for j in range(i,n):
            if(arr[i]>arr[j]):
                res+=1
    return res
# n2
print(inversionCount([2,4,1,3,5],5))
print(inversionCount([5,4,3,2,1],5))