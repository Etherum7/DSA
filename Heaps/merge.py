def merge(arr1, arr2):
        n=len(arr1)
        m=len(arr2)
        arr3=[]
        i=0
        j=0
        while i< n and j< m:
            if arr1[i]<arr2[j]:
                arr3.append(arr1[i])
                i+=1
            elif arr1[i]>arr2[j]:
                arr3.append(arr2[j])
                j+=1
            else:
                arr3.append(arr1[i])
                i+=1
                j+=1
        while i< n:
            arr3.append(arr1[i])
            i+=1
        while j<m:
            arr3.append(arr2[j])
            j+=1
        return arr3
        
def mergeKArrays( arr, K):
    if K==1:
        return arr[0]
    elif K==2:
        print(arr)
        return merge(arr[0], arr[1])
    elif K>2:
        if K%2==0:
            split=K//2
            arr1=mergeKArrays(arr[:split],K-split)
            arr2=mergeKArrays(arr[split:], split)
        else:
            split=K//2
            arr1=mergeKArrays(arr[:split+1],K-split)
            arr2=mergeKArrays(arr[split+1:], split)
# bst to min heap

        
        
        return merge(arr1, arr2)

print(mergeKArrays([[2, 6, 12, 34],
                     [1, 9, 20, 1000],
                     [23, 34, 90, 2000],[3,6,7,9]],4))