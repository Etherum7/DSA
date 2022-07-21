def reverseList(arr: list):
    # O(n/2)
    i = 0
    j = len(arr)-1
    mid = int(len(arr)/2)
    for i in range(0, mid):
        print(i)
        arr[i], arr[j] = arr[j], arr[i]
        j -= 1
    return arr

# in place recursive reverse


def recursiveReverse1(arr: list, start, end):
    if start <= end:
        arr[start], arr[end] = arr[end], arr[start]
        recursiveReverse1(arr, start+1, end-1)


def reverseList1(arr: list):
    return list(reversed(arr))
    # arr.reverse()
    # return arr[::-1]


def reverseList2(arr: list):
    arr1 = [0 for i in range(0, len(arr))]
    for i in range(0, len(arr)):
        arr1[len(arr)-1-i] = arr[i]
    return arr1


A = [4, 5, 1, 2, 3]
recursiveReverse1(A, 0, len(A)-1)
print(A)
