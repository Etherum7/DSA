from collections import deque


def leftRotate0(A: list):
    A.append(A.pop(0))


def leftRotate1(A: list):
    return A[1:]+A[0:1]


def leftRotate2(A: list):
    x = A[0]
    for i in range(len(A)-1):
        A[i] = A[i+1]
    A[len(A)-1] = x


# A = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# leftRotate2(A)
# print(A)


def leftRotateD0(A: list, d: int):
    for j in range(d):
        x = A[0]
        for i in range(len(A)-1):
            A[i] = A[i+1]
        A[len(A)-1] = x


def leftRotateD1(A: list, d: int):
    return A[d:]+A[:d]


def leftRotateD2(A: list, d: int):
    dq = deque(A)
    dq.rotate(-d)
    l = list(dq)
    return l


def reverse(A: list, b, e):
    while(b < e):
        A[b], A[e] = A[e], A[b]
        b += 1
        e -= 1


def leftRotateD3(A: list, d: int):
    n = len(A)
    reverse(A, 0, d-1)
    reverse(A, d, n-1)
    reverse(A, 0, n-1)


def rightRotate(arr, n):

    X = arr[n-1]

    for i in range(n-2, -1, -1):
        arr[i+1] = arr[i]
    arr[0] = X


A = [1, 2, 3, 4, 5, 6, 7, 8, 9]
leftRotateD3(A, 4)
print(A)
