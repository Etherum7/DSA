def orderAgnosticBS(arr, k, n):

    if n == 1:
        return 0 if arr[0] == k else -1

    if arr[0] <= arr[-1]:
        start = 0
        end = n = 1
        while start <= end:
            mid = (start+end)//2
            if arr[mid] == k:
                return mid
            elif arr[mid] > k:
                end = mid-1
            else:
                start = mid+1
        return -1
    else:
        start = 0
        end = n-1
        while start <= end:
            mid = (start+end)//2
            if arr[mid] == k:
                return mid
            elif arr[mid] > k:
                start = mid+1
            else:
                end = mid-1
        return -1


print(orderAgnosticBS([20, 10, 5, 3], 5, 4))
print(orderAgnosticBS([1,1,1,1,1], 1, 5))
