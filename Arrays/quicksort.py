def partition(A, low, high):
    pivot=A[low]
    i=low+1
    j=high
    while True:
        # print(i,j)

        while i<=j and A[i]<=pivot:
            i+=1
        while i<=j and A[j]>=pivot:
            j-=1
        if(j<i):
            break
        else:
            A[i],A[j]=A[j],A[i]
    A[low],A[j]=A[j],A[low]
    return j
    
def quickSort(A,l,h,k):
    if(l<h):
        j= partition(A,l,h)
        print(j)
        if j-1==k-1:
          return A[j]
        if j-1< k-1:
           quickSort(A,l,j-1,k)
        else:
            quickSort(A,j+1,h,k)
A=[7, 10, 4, 3, 20, 15]
print(quickSort(A, 0, 5,2))
print(A)



