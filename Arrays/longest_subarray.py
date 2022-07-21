def longest_subarray(A:list[int])->int:
    if(not A):return 0
    max_so_far=0
    max_ending_here=0
    prev=A[0]
    for i in range(len(A)):
        if(prev==A[i]):
            max_ending_here+=1
        else:
            max_ending_here=1
        max_so_far= max(max_ending_here, max_so_far)


        prev=A[i]
    return max_so_far
print(longest_subarray([0,1,0,1,2]))



