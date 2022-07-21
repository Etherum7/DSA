class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class Stack():
    def __init__(self):
        self.top = None
        self.middle = None
        self.st = None
        self.len = 0

    def push(self, data):
        if not self.st:
            self.st = Node(data)
            self.top = self.st
            self.middle = self.top
            self.len += 1
        else:
            self.top.next = Node(data)
            self.top.next.prev = self.top
            self.top = self.top.next
            self.len += 1
            if self.len % 2 != 0:
                self.middle = self.middle.next


    def pop(self):
        if self.len:
            d=self.top.data
            p = self.top.prev
            p.next = None
            self.len -= 1
            self.top = p
            # print(self.top.data)
            if self.len % 2 == 0:
                self.middle = self.middle.prev
            return d

    def findMiddle(self):
        print(self.middle.data)
        return self.middle

    def delMiddle(self):
        d = self.middle.data
        if self.len == 1:
            self.top = None
            self.middle = None
            self.st = None
            self.len = 0
        if self.len:
            p = self.middle.prev
            p.next = self.middle.next
            self.len -= 1
            self.middle.next.prev = p
            if self.len % 2 == 0:
                self.middle = p
            else:
                self.middle = p.next
        return d


ms = Stack()
ms.push( 11)
ms.push( 22)
ms.push( 33)
ms.push( 44)
ms.push( 55)
ms.push( 66)
ms.push( 77)
ms.push( 88)
ms.push( 99)

print(ms.pop())
print(ms.pop())
ms.findMiddle()
print(ms.delMiddle())
ms.findMiddle()