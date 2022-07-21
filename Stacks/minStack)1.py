# O(2n)
# User function Template for python3

#User function Template for python3

class stack:
    def __init__(self):
        self.s=[]
        self.minEle=None

    def push(self,x):
        #CODE HERE
        if len(self.s)==0:
            self.s.append(x)
            self.minEle=x
        else:
            if x<self.minEle:
                self.s.append((2*x)-self.minEle)
                self.minEle=x
                # change minele
                # push modifies
            else:
                self.s.append(x)
            

    def pop(self):
        #CODE HERE
        if len(self.s):
            if self.s[-1]>self.minEle:
                return self.s.pop()
            else:
                newMini=(2*self.minEle)-self.s[-1]
                d=self.minEle
                self.minEle=newMini
                self.s.pop()
                return d
        return -1
        
class stack:
    def __init__(self):
        self.s = []
        self.minEle = None

    def push(self, x):
        # CODE HERE
        if len(self.s) == 0:
            self.s.append((x, x))
        else:
            if self.s[-1][1] >= x:
                self.s.append((x, x))
            else:
                self.s.append((x, self.s[-1][1]))

    def pop(self):
        # CODE HERE
        if len(self.s):
            return self.s.pop()[0]
        return -1

    def getMin(self):
        # CODE HERE
        if len(self.s):
            return self.s[-1][1]
        return -1


s = stack()

print(s)
s.push(3)
s.push(5)
print(s.getMin())
s.push(2)
s.push(1)
print(s.getMin())
print(s.pop())
s.getMin()
print(s.pop())
