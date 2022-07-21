

class Solution:

    # Function to find the minimum number of swaps required to sort the array.
    def minSwaps(self, nums):
        # Code here
        arrpos = [*enumerate(nums)]
        arrpos.sort(key=lambda x: x[1])
        res = 0
        visited = {v: False for v in range(n)}
        for i in range(len(nums)):
            if visited[i] or i == arrpos[i][0]:
                continue
            c_size = 0
            j = i
            while not visited[j]:
                visited[j] = True
                j = arrpos[j][0]
                c_size += 1

            if c_size > 0:
                res += (c_size-1)
        return res

# {
#  Driver Code Starts


if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n = int(input())
        nums = list(map(int, input().split()))
        obj = Solution()
        ans = obj.minSwaps(nums)
        print(ans)

# } Driver Code Ends
