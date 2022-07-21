class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        M=len(needle)
        N=len(haystack)
        if M>N:
            return -1
        p=0
        t=0
        d=256
        h=d**(M-1)
        q=101
        for i in range(M):
            p=(d*p+ord(needle[i]))%q
            t=(d*t+ord(haystack[i]))%q
        for i in range(N-M+1):
            if p==t:
                for j in range(M):
                    if haystack[i+j]!=needle[j]:
                        break
                if j==M-1 and haystack[i+j]==needle[j]:
                    return i
            if i<N-M:
                t=(d*(t-ord(haystack[i])*h)+ord(haystack[i+M]))%q
        return -1
# bad
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i = 0
        j = 0
        k = len(needle)
        while j < len(haystack):
            if j-i+1 < k:
                j += 1
            elif j-i+1 == k:
                if haystack[i:j+1] == needle:
                    return i
                i += 1
                j += 1
        return -1
