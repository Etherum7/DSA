def moveAllNegative(A: list):
    low = -1
    high = len(A)
    mid = 0
    while(mid < high):
        if(A[mid] < 0):
            low += 1
            mid += 1
        else:
            A[mid], A[high-1] = A[high-1], A[mid]
            high -= 1

# def moveAllNegativeOrder(A):
#     last_negative_index=-1
#     for i in range(0, len(A)):
#         if(A[i]<0):
#             last_negative_index +=1
#             A[i],A[last_negative_index] = A[last_negative_index], A[i]
#             if(i-last_negative_index>=2):
#                 temp=A[i]
#                 j=last_negative_index+1
#                 k=i-1
#                 while(k>=j):
#                     A[k+1]=A[k]
#                     k-=1
#                 A[j]=temp

#     return
# A=[-2,0,-3,9,-1,-7, 98,  8,-5]
# moveAllNegativeOrder(A)
# print(A)



def sort012(A,n):
        # code here
        zero=-1
        one=0
        two=n-1
        while one<=two:
            if A[one]==0:

                zero+=1
                A[zero],A[one]=A[one],A[zero]
                one+=1
            elif A[one]==1:
                one+=1
            else:
                A[one],A[two]=A[two],A[one]
                two-=1
A=[2,0,1,2,1,0,0,0,1,2,2]
sort012(A,len(A))
print(A)
# A = [-12, 11, -13, -5, 6, -7, 5, -3, -6]
# moveAllNegative(A)
# print(A)

