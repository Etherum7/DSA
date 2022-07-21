def searchInNearlySorted(arr, k,n):
    start=0
    end=n-1
    while start<=end:
        mid=(start+end)//2
        if arr[mid]==k:
            return mid
        if mid-1>=start and arr[mid-1]==k:
            return mid-1
        if mid+1<=end and arr[mid+1]==k:
            return mid+1
        if arr[mid]<k:
            start=mid+2
        else:
            end=mid-2
    return -1
print(searchInNearlySorted([5,10,30,20,40],20,5))