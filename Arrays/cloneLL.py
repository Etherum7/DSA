#User function Template for python3

'''
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
        self.arb=None
        
param: head:  head of linkedList to copy
return: the head of the copied linked list the #output will be 1 if successfully copied
'''
class Solution:
    #Function to clone a linked list with next and random pointer.
    def copyList(self, head):
        # code here
        d={}
        newHead=Node(head.data)
        d[head]=newHead
        temp=newHead
        p=head
        while p.next:
            
            temp.next=Node(p.next.data)
            d[p.next]=temp.next
            temp=temp.next
            p=p.next
        q=head
        # print(d)
        while q:
            if q.arb:
                d[q].arb=d[q.arb]
            q=q.next
        return newHead
        