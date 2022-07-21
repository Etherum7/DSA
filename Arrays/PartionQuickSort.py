def partition(A: list, index: int):
    i = 0
    j = len(A)-1

    while(i < j):
        while(A[i] < A[index]):
            i += 1
        while(A[j] > A[index]):
            j -= 1
        if(i < j):
            A[i], A[j] = A[j], A[i]
    A[i], A[index] = A[index], A[i]
A=[7,6,3,2,4,1,0]
partition(A, 5)
print(A)
