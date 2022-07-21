# User function Template for python3

class Solution:
    def swap(self, s, i, j):
        s[i], s[j] = s[j], s[i]
    # Function to find the largest number after k swaps.

    def util(self, s, k, res, pos):
        if k == 0:
            return
        if pos < len(s):
            m = max(s[pos:])
            if m != s[pos]:
                k -= 1
            for j in range(len(s)-1, -1, -1):
                if s[j] == m:
                    self.swap(s, j, pos)
                    res[0] = max(int(res[0]), int(''.join(s)))
                    self.util(s, k, res, pos+1)
                    self.swap(s, j, pos)

    def findMaximumNum(self, s, k):
        res = [s]
        self.util(list(s), k, res, 0)
        # code here
        return res[0]


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        k = int(input())
        s = input()
        ob = Solution()
        print(ob.findMaximumNum(s, k))

# } Driver Code Ends
