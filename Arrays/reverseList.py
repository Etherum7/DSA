def reverse0(A:list):
    return list(reversed(A))
    # return A[::-1]
def reverse1(A:list):
    i=0 
    j=len(A)-1

    while(i<j):
        A[i], A[j] = A[j], A[i]
        i+=1
        j-=1
A=[1,2,3,4,5]

reverse1(A)
print(A)