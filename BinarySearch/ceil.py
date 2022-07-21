def findCeil(arr, N, x):
    start=0
    end=N-1
    res=0
    while start <= end:
        mid=(start+end)//2
        if arr[mid]==x:
            return arr[mid]
        elif arr[mid]>x:
            res=min(res, arr[mid])
            end=mid-1
        else:
            start=mid+1
    return res
        