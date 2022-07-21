def largest(A):
    max = A[0]
    for i in A:
        if(i>max):
            max=i
    return max
print(largest([20, 30, 10, 40]))

