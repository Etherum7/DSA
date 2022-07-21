class Solution:
    def nullPoints(self, n, a, getAnswer):
        # Your code goes here
        for i in range(1, n):
            # points
            
            x = (a[i-1]+a[i])/2
            # print(x)
            right = left = 0.0

            for j in range(i):
                left = left+(1/(x-a[j]))
            for j in range(i, n):
                right = right+(1/(a[j]-x))
            force = right-left
            # print(x,force,right, left)
            p=a[i-1]
            next=a[i]

            while abs(force) >= 0.000001:
                print(force)
                if force > 0:
                    next=x
                    t=(x-p)/2
                    x = x-t
                    
                elif force < 0:
                    p=x
                    t=(next-x)/2
                    x = x+t
                
                right = left = 0.0
                for j in range(i):
                    left = left+(1/(x-a[j]))
                for j in range(i, n):
                    right = right+(1/(a[j]-x))
                
                force = right-left
                # print(force)
            getAnswer[i-1] = x
        return getAnswer
ob=Solution()
print(ob.nullPoints(4,[0,10,20,30],[0]*4))