class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i=j=0
        d={}
        N=len(s)
        mx=0
        while j<N:
            if s[j] not in d:
                d[s[j]]=1
                mx=max(mx, j-i+1)
            else:
                while d[s[j]]!=0:
                    d[s[i]]-=1
                    i+=1
                d[s[j]]=1
                mx=max(mx,j-i+1)
                pass
            j+=1
        return mx
ob=Solution()
print(ob.lengthOfLongestSubstring('abcabcbb'))

from collections import defaultdict
class Solution:

    def longestSubstrDistinctChars(self, S):
        # code here
        i=j=0
        n=len(S)
        res=0
        cmap=defaultdict(int)
        while j< n:
            cmap[S[j]]+=1
            if cmap[S[j]]>1:
                while cmap[S[j]]>1:
                    # if S[i] in cmap and cmap[S[i]]>0:
                        cmap[S[i]]-=1
                        i+=1
            
            res=max(res,j-i+1)
            j+=1
        return res

