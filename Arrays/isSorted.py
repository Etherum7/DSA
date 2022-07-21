def isSorted0(A: list):
    i = 1
    while(i < len(A)):
        if(A[i] < A[i-1]):
            return False
        i+=1
    return True


def isSorted1(A: list):
    return sorted(A) == A

print(isSorted0([1,2,3,4,5]))
