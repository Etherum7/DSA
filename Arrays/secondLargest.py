def secondLargest(A:list):
    if(len(A)<=1):
        return None
    if(A[0]>A[1]):
        max1=A[0]
        max2=A[1]
    elif(A[0]<=A[1]):
        max1=A[1]
        max2=A[0]
    for i in range(2, len(A)):
        if(A[i]>max2 and A[i]<max1):
            max2=A[i]
        elif (A[i]>max1 ):
            max2=max1
            max1=A[i]
    if(max1==max2):
        return None
    return max2
print(secondLargest([10,10,10]))
print(secondLargest([40,10, 90,30]))
print(secondLargest([20, 10, 20, 12]))
    


