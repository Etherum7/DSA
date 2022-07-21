# #User function Template for python3
# class Solution:


#     def search(self,pat, txt):
#         # code here
#         cnt=0
#         i=j=0
#         K=len(pat)
#         N=len(txt)
#         cpat=[]
#         spat=''.join(sorted(list(pat)))


#         while j<N:
#             cpat.append(txt[j])
#             if j-i+1<K:
#                 j+=1
#             elif j-i+1==K:
#                 if ''.join(sorted(list(cpat)))==pat:
#                     cnt+=1
#                 cpat=cpat[1:]
#                 i+=1
#                 j+=1
#         return cnt


# #{
# #  Driver Code Starts
# #Initial Template for Python 3

# ob=Solution()
# ob.search()

# User function Template for python3
class Solution:

    def search(self, pat, txt):
        Map = {}
        for ch in pat:
            if ch not in Map:
                Map[ch] = 1
            else:
                Map[ch] += 1
        print(Map)
        cnt = len(Map)
        ans = 0
        i = 0
        j = 0
        k = len(pat)
        while j < len(txt):
            if txt[j] in Map:
                Map[txt[j]] -= 1
                if Map[txt[j]] == 0:
                    cnt -= 1
            if j-i+1 < k:
                j += 1
            elif j-i+1 == k:
                if cnt == 0:
                    ans += 1
                if txt[i] in Map:
                    Map[txt[i]] += 1
                    if Map[txt[i]] == 1:
                        cnt += 1
                i += 1
                j += 1
        return ans

    