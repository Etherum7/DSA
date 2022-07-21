class Solution:
    def minChar(self, str):
        # Write your code here

        n = len(str)
        i = n-1
        lp = 0
        while i > -1:
            if str[i] != str[0]:
                i -= 1
            else:
                l = 0
                r = i
                while r > l+1 and str[l] == str[r]:
                    l += 1
                    r -= 1
                if l == r or (r == l+1 and str[l] == str[r]):
                    return n-i-1
                else:
                    # already checked above
                    i = r
