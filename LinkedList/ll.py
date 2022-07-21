class Node():
    def __init__(self,data=0):
        self.data=data
        self.next=None
class LinkedList():
    def __init__(self):
        self.head=None
    def create(self,arr):
        self.head=Node(arr[0])
        last= self.head
        i=1
        while i< len(arr):
            last.next=Node(arr[i])
            last=last.next
            i+=1
    def insert(self, key):
        if not self.head:
            self.head=Node(key)
            return
        p=self.head
        while p.next:
            p=p.next
        p.next=Node(key)
    def print_ll(self):
        p=self.head
        while p:
            print(p.data)
            p=p.next
    def reverseIterative(self):
        if not self.head or not self.head.next:
            return 
        p=None
        q=self.head
        
        while q:
            r=q.next
            q.next=p
            p=q
            q=r
        self.head=p
    def reverseRecursive(self, curr, prev):
        if not curr.next:
            self.head=curr
            curr.next=prev
            return
        next= curr.next
        curr.next=prev
        self.reverseRecursive(next, curr)
        
        
    def reverse(self):
        if not self.head:
            return 
        self.reverseRecursive(self.head, None)
    def lastTofirst(self):
        q=None
        p=self.head
        while p.next:
            q=p
            p=p.next
        p.next=self.head
        q.next=None
        self.head=p
    def getMiddle(self):
        p=q=self.head
        while q and q.next:
            q=q.next
            if q.next:
                p=p.next
                q=q.next
        return p
class Solution:
    #Function to remove a loop in the linked list.
    def removeLoop(self, head):
        # code here
        # remove the loop without losing any nodes
        s=set()
        temp=head
        prev=None
        while temp:
            if temp in s:
                prev.next=None
                return True
            s.add(temp)
            prev=temp
            temp=temp.next
        return False
    def detectLoop(self, head):
        #code here
        p=q=head
        while p and  p.next and q and q.next:
            p=p.next 
            q=q.next.next
            if p==q:
                return True
        return False
def firstLoopNode(head):
    p=q=head
    while p and q and q.next:
        p=p.next
        q=q.next.next
        if p==q:
            p=head
            while p!=q:
                p=p.next
                q=q.next
            return p
    return None
def intersetPoint(head1,head2):
    #code here
    c1=c2=0
    p,q=head1,head2
    while p:
        c1+=1
        p=p.next
    while q:
        c2+=1
        q=q.next
    diff=abs(c1-c2)
    p,q=head1,head2
    if c1> c2:
        while diff:
            p=p.next
            diff-=1
    elif c1<c2:
        while diff:
            q=q.next
            diff-=1
    while p and q:
        if p!=q:
            p=p.next
            q=q.next
        else:
            return p.data
    return -1
def removeDuplicates(head):
    #code here
    p=head
    q=p.next
    while q:
        while p and q and p.data==q.data:
            q=q.next
        p.next=q
        p=q
        if q:
          q=q.next

ll=LinkedList()
ll.create([1,3,5,7,2])
# ll.reverse() 
ll.lastTofirst()
ll.print_ll()


        

        
