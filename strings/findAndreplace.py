# User function Template for python3

class Solution:
    def findAndReplace(self, S, Q, index, sources, targets):
        # code here
        n = len(S)
        res = ''
        j = 0
        i = 0
        while i < n:
            if i in index:
                t = len(sources[j])
                if S[i:i+t] == sources[j]:
                    res += targets[j]
                    i = i+t
                else:
                    res += S[i]
                    i += 1
                j += 1
            else:
                res += S[i]
                i += 1

        return res


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        S = input()
        Q = int(input())
        index = list(map(int, input().split()))
        sources = list(map(str, input().split()))
        targets = list(map(str, input().split()))

        ob = Solution()
        print(ob.findAndReplace(S, Q, index, sources, targets))
# } Driver Code Ends
