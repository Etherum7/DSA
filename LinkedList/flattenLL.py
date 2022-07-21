# User function Template for python3


'''

class Node:
    def __init__(self, d):
        self.data=d
        self.next=None
        self.bottom=None
        
'''


def merge(head1, head2):
    head = Node(0)
    temp = head
    p = head1
    q = head2
    while p and q:
        if(p.data <= q.data):
            head.bottom = p
            head = head.bottom
            p = p.bottom
        else:
            head.bottom = q
            head = head.bottom
            q = q.bottom
    if p:
        head.bottom = p
    if q:
        head.bottom = q
    return temp.bottom


def flatten(root):
    # Your code here
    p = root.next
    while p:
        root = merge(root, p)
        p = p.next

    return root


# {
 # Driver Code Starts
# Initial Template for Python 3

class Node:
    def __init__(self, d):
        self.data = d
        self.next = None
        self.bottom = None


def printList(node):
    while(node is not None):
        print(node.data, end=" ")
        node = node.bottom

    print()


if __name__ == "__main__":
    t = int(input())
    while(t > 0):
        head = None
        N = int(input())
        arr = []

        arr = [int(x) for x in input().strip().split()]
        temp = None
        tempB = None
        pre = None
        preB = None

        flag = 1
        flag1 = 1
        listo = [int(x) for x in input().strip().split()]
        it = 0
        for i in range(N):
            m = arr[i]
            m -= 1
            a1 = listo[it]
            it += 1
            temp = Node(a1)
            if flag == 1:
                head = temp
                pre = temp
                flag = 0
                flag1 = 1
            else:
                pre.next = temp
                pre = temp
                flag1 = 1

            for j in range(m):
                a = listo[it]
                it += 1
                tempB = Node(a)
                if flag1 == 1:
                    temp.bottom = tempB
                    preB = tempB
                    flag1 = 0
                else:
                    preB.bottom = tempB
                    preB = tempB
        root = flatten(head)
        printList(root)

        t -= 1

# } Driver Code Ends
