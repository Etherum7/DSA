# python program to count Minimum number
# of jumps to reach end

# Returns minimum number of jumps to reach arr[n-1] from arr[0]
def minJumps(arr, n):

    if(n == 1):
        if(arr[0] == 0):
            return -1
        else:
            return 0
    jump = 1
    step = arr[0]
    maxReach = arr[0]
    for i in range(1, n):
        if(i == n-1):
            return jump
        maxReach = max(maxReach, i+arr[i])
        step -= 1
        if(step == 0):
            jump += 1
            if(i >= maxReach):
                # handling zero case
                return -1
            step = maxReach-i
    return -1


# Driver program to test above function
arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
# arr1 = [1, 4, 3, 2, 6, 7]

arr2 = [2, 3, 1, 1, 2, 4, 2, 0, 1, 1]
# # arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
# arr3 = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
# arr4 = [10, 8, 12, 17, 1, 21, 5, 17, 20, 11, 5, 27, 23, 8,
#         12, 18, 16, 12, 9, 8, 17, 12, 23, 26, 0, 5, 9, 24, 10]


size = len(arr2)

# Calling the minJumps function
print("Minimum number of jumps to reach end is % d " % minJumps(arr2, size))

# This code is contributed by Aditi Sharma
