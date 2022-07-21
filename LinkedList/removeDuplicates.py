class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

def removeDuplicates( head):
    # code here
    # return head after editing list
    curr = head
    t = set()
    prevNode = None
    newHead = None

    while curr:
        # print(curr.data)
        if curr.data not in t:
            # print(curr.data)
            t.add(curr.data)
            if  prevNode:
                prevNode.next = Node(curr.data)
                prevNode=prevNode.next
                
            else:
                prevNode = Node(curr.data)
                newHead = prevNode
        curr = curr.next
    print(t)
    return newHead

def printLL(node):
    while node:
        print(node.data)
        node=node.next
root=Node(5)
root.next = Node(2)
root.next.next = Node(2)
root.next.next.next = Node(4)

nr=removeDuplicates(root)
printLL(nr)
