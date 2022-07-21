from math import floor

def merge(A: list, low: int, mid: int, high: int):
    
    i = low
    k = low
    j = mid+1
    A3 = [0 for i in range(low+high+1)]

    while(i <= mid and j <= high):
        if(A[i] < A[j]):
            A3[k] = A[i]
            i += 1
            k += 1
        elif(A[i] > A[j]):
            A3[k] = A[j]
            j += 1
            k += 1
        else:
            A3[k] = A[i]
            k += 1
            i += 1
            j += 1
    while(i <= mid):
        A3[k] = A[i]
        i += 1
        k += 1
    while(j <= high):
        A3[k] = A[j]
        j += 1
        k += 1
    for i in range(low, high+1):
        # print(i)
        A[i] = A3[i]


def mergeSort(A: list, low: int, high: int):
    if(low < high):
        mid = floor((low+high)/2)
        mergeSort(A, low, mid)
        mergeSort(A, mid+1, high)
        merge(A, low, mid, high)
        # print(A)


def kthSmallest(arr, k, low, high):
    mergeSort(arr, low, high)
    return arr[k-1]


if __name__ == '__main__':
    arr = [12, 3, 5, 7, 19]
    # A = [2, 1, 43, 89, 3, 7, 5, 34, 19]
    # arr2 = [2, 4, 6, 7, 8, 20]
    # n = len(arr)

    # print(A)
    k = 2
    print("K'th smallest element is",
          kthSmallest(arr, k, 0, len(arr)-1))
