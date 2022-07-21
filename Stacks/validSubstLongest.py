
class Solution:
    def findMaxLen(ob, s):
        # code here
        N = len(s)
        longest = [0]*N
        curMax = 0
        for i in range(1, len(s)):
            if ((s[i] == ')' and i - longest[i - 1] - 1 >= 0 and s[i - longest[i - 1] - 1] == '(')):

                longest[i] = longest[i - 1] + 2
                if (i - longest[i - 1] - 2 >= 0):
                    longest[i] += (longest[i - longest[i - 1] - 2])
                else:
                    longest[i] += 0
            curMax = max(longest[i], curMax)
        return curMax
# User function Template for Python3


class Solution:
    def maxLength(self, S):
        # code here
        st = []
        st.append(-1)
        res = 0
        for i in range(len(S)):

            if S[i] == '(':
                st.append(i)
            else:
                if len(st):
                    st.pop()
                if len(st):
                    res = max(res, i-st[-1])
                else:
                    st.append(i)
        return res


# {
#  Driver Code Starts
# Initial Template for Python3
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        S = input()

        ob = Solution()
        print(ob.maxLength(S))
# } Driver Code Ends
