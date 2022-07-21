from collections import defaultdict


class Solution:
    def checkMirrorTree(self, n, e, A, B):
        # code here
        d = defaultdict(list)

        for i in range(0, e*2, 2):
            d[A[i]].append(A[i+1])

        for i in range(0, e*2, 2):
            if d[B[i]].pop() != B[i+1]:
                return 0
        return 1


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, e = map(int, input().split())

        A = list(map(int, input().split()))
        B = list(map(int, input().split()))

        ob = Solution()
        print(ob.checkMirrorTree(n, e, A, B))
# } Driver Code Ends
