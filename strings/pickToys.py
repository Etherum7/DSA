def pickToys(s):
    i=j=0
    d={}
    cnt=0
    ans=0
    while j<len(s):
        if s[j] not in d:
            d[s[j]]=1
        else:
            d[s[j]]+=1
        if d[s[j]]==1:
            cnt+=1
        if cnt<=2:
            ans=max(ans, j-i+1)
            j+=1
        else:
            while cnt>2:
                d[s[i]]-=1
                if d[s[i]]==0:
                    cnt-=1
                i+=1
            j+=1
    return ans
print(pickToys('abaccab'))
print(pickToys('abc'))
print(pickToys('aaaa'))

