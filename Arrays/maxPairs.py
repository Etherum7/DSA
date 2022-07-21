import math
class Solution:
    def countKdivPairs(self, arr, n, k):
        #code here
        d={}
        m=max(arr)
        mul=[k*i for i in range(1,(math.ceil(m/k)*2)+1)]
        res=set()
        print(mul)
        for i in arr:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        print(d)
        for key, cnt in d.items():
            # print(key,cnt)
            c=cnt-1
            for j in mul:
                if j-key >m:
                    break
                # print(j-key)
            
                if (j-key) in d:
                    # print('U')
                    if j-key != key :
                        if not (key, j-key) in res and not (j-key, key)  in res:
                            res.add((key, j-key))
                    elif j-key==key and c>=1:
                        if not (key, j-key) in res and not (j-key, key)  in res:
                            res.add((key, j-key))
       
        return len(res)
ob=Solution()
print(ob.countKdivPairs([2,2,1,7,5,3],6,4))