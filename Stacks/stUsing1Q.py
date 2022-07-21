from queue import Queue
from re import S
class st():
    def __init__(self):
        self.q=Queue()
        self.qsize=0
        
    def push(self, x):
        s=self.qsize
        self.q.put(x)
        for _ in range(0,s):
            a=self.q.get()
            # print(a)
            self.q.put(a)
        self.qsize+=1

    def pop(self):
        if not self.q.empty():
            self.qsize-=1
            return self.q.get()
        else:
            return -1
s=st()
s.push(40)
s.push(50)
s.push(70)
print(s.pop())
print(s.pop())
s.push(80)
s.push(90)
s.push(100)
print(s.pop())
print(s.pop())
        

