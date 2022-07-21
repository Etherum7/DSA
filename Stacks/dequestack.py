from collections import deque
class stack:
    def __init__(self):
        self.st=deque()
        self.top=None
    def isEmpty(self):
        if len(self.st)==0:
            return True
        return False

    def push(self, x):
        self.st.append(x)
        
    def pop(self):
        if not self.isEmpty():
            d=self.st.pop()
            
            return d
s=stack()
s.push(1)
s.push(2)
s.push(3)

print(s.pop())
print(s.pop())
print(s.pop())
    

