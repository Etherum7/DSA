class Solution:
    def AlternatingaMaxLength(self, nums):
        # Code here
        n = len(nums)
        last = [[1 for i in range(n)] for j in range(2)]
        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    last[0][i] = max(last[0][i], last[1][j]+1)
                elif nums[j] > nums[i]:
                    last[1][i] = max(last[1][i], last[0][j]+1)
        return max(last[0][n-1], last[1][n-1])

# 2nd
# Python3 program for above approach


def LAS(arr, n):

    # "inc" and "dec" initialized as 1
    # as single element is still LAS
    inc = 1
    dec = 1

    # Iterate from second element
    for i in range(1, n):

        if (arr[i] > arr[i-1]):

            # "inc" changes iff "dec"
            # changes
            inc = dec + 1
        elif (arr[i] < arr[i-1]):

            # "dec" changes iff "inc"
            # changes
            dec = inc + 1

    # Return the maximum length
    return max(inc, dec)


# Driver Code
if __name__ == "__main__":
    arr = [10, 22, 9, 33, 49, 50, 31, 60]
    n = len(arr)

    # Function Call
    print(LAS(arr, n))
