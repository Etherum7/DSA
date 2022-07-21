'''
    lis[][0]:Petrol
    lis[][1]:Distance
'''

class Solution:
    
    #Function to find starting point where the truck can start to get through
    #the complete circle without exhausting its petrol in between.
    def tour(self,lis, n):
        #Code here
        temp=[lis[i][0]-lis[i][1] for i in range(n)]
        for i in range(n):
            if temp[i]>=0:
                p=0
                j=i
                while True:
                    p+=lis[j][0]
                    if p>=lis[j][1]:
                        p=p-lis[j][1]
                        j=(j+1)%n
                        if j==i:
                            return i
                    else:
                        break
        return -1
    def tour(self,lis, n):
        #Code here
        start=0
        s=d=0
        for i in range(n):
            s+=lis[i][0]-lis[i][1]
            if s<0:
                start=i+1
                d+=s
                s=0
        return start if s+d >=0 else -1