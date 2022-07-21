import math


def binarySearch(A: list, key: int, low: int, high: int):
    mid = math.floor((low+high)/2)
    if(low <= high):
        if(A[mid] == key):
            return mid
        elif(A[mid] < key):
            low = mid+1
        else:
            high = mid-1
        return binarySearch(A, key, low, high)
    return -1


print(binarySearch([3, 6, 8, 10, 12, 15, 17, 19], 3, 0, 7))
