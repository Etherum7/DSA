def unionCount0(A, B):
    return len(set(A+B))


def intersectionCount0(*args):
    hashMap = {}
    for arr in args:
        for i in arr:
            if not i in hashMap:
                hashMap[i] = 1
            else:
                hashMap[i] += 1
    total = 0
    for (k, v) in hashMap.items():
        if(v == len(args)):
            total += 1
    return total


def unionCount1(*args):
    hashMap = {}
    for arr in args:
        for i in arr:
            hashMap[i] = i

    return len(hashMap)


# print(unionCount1([1, 2], [1, 2, 3, 4, 5], [7, 8, 3]))
# print(intersectionCount0([1, 2, 3], [1, 2, 3, 4, 5]))


def unionSorted(A, B):
    C = []
    n = len(A)
    m = len(B)
    i = j = 0
    while(i < n and j < m):

        if(A[i] > B[j]):
            C.append(B[j])
            j += 1

        elif(A[i] < B[j]):
            C.append(A[i])
            i += 1

        else:
            C.append(B[j])
            # C[k] = B[j]

            while(j < m and C[-1] == B[j]):
                j += 1
            while(i < n and C[-1] == A[i]):
                i += 1

    while(i < n):
        C.append(A[i])
        while(i < n and C[-1] == A[i]):
            i += 1

    while(j < m):
        C.append(B[j])
        while(j < m and C[-1] == B[j]):
            j += 1

    return C


print(unionSorted([2, 3, 5, 8, 9], [4, 8, 9, 9, 15]))
# print(intersectionCount0([1, 2, 3], [1, 2, 3, 4, 5]))


def intersectionSorted(A, B):
    C = []
    n = len(A)
    m = len(B)
    i = j = 0
    while(i < n and j < m):

        if(A[i] == B[j]):
            C.append(B[j])
            # C[k] = B[j]

            while(j < m and C[-1] == B[j]):
                j += 1
            while(i < n and C[-1] == A[i]):
                i += 1
        elif(A[i] < B[j]):

            i += 1
        else:

            j += 1

    return C

print(intersectionSorted([2, 3, 5, 8, 9], [4, 8, 9, 9, 15]))