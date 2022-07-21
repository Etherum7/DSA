class Solution:

    def longestKSubstr(self, s, k):
        # code here
        d={}
        ans=-float('inf')
        i=j=0
        N=len(s)
        cnt=0
        
        while j< N:
            # print(d)
            if s[j] not in d:
                d[s[j]]=1 
            else:
               d[s[j]]+=1

            if d[s[j]]==1:
                cnt+=1

            if cnt<k:
                j+=1
            elif cnt==k:
                ans=max(ans, j-i+1)
                j+=1
            elif cnt>k:
                while cnt>k:
                    d[s[i]]-=1
                    if d[s[i]]==0:
                        cnt-=1
                    i+=1
                if cnt==k:
                    ans=max(ans, j-i+1)
                j+=1
        return -1 if ans ==-float('inf') else ans 
ob=Solution()
print(ob.longestKSubstr("aabacbebebe", 3))
print(ob.longestKSubstr("aaaa", 2))

