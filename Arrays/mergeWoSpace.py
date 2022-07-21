# def sort(A, i):
#     while A[i]>A[i+1]:
#        A[i], A[i+1]=A[i+1],A[i]
#        i+=1

# def merge(arr1,arr2, n,m):
#     i=0
#     j=0
#     while i<n and j<m:
#         if(arr1[i]>arr2[j]):
#             arr1[i],arr2[j] = arr2[j],arr1[i]
#             i+=1
#             sort(arr2, j)
#         elif(arr1[i]<=arr2[j]):
#             i+=1
#     return arr1+arr2

# print(merge([1, 3, 5, 7],[0, 2, 6, 8, 9],4,5))

def merge(arr1,arr2, n,m):
    for i in range(m-1,-1,-1):
        # find correct position 
        last =arr1[n-1]
        j=n-2
        while j>= 0 and arr1[j]>arr2[i]:
            arr1[j+1]=arr1[j]
            j-=1
        # if greater found
        if  j!=n-2 or last> arr2[i]:
            arr1[j+1]=arr2[i]
            arr2[i]=last
    return arr1+arr2

print(merge([1, 3, 5, 7],[0, 2, 6, 8, 9],4,5))