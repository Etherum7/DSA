# User function Template for python3

'''
    :param head: head of unsorted linked list 
    :return: head of sorted linkd list
    
    # Node Class
    class Node:
        def __init__(self, data):  # data -> value stored in node
            self.data = data
            self.next = None
'''
import sys
import io
import atexit


class Solution:
    # Function to sort the given linked list using Merge Sort.
    def findMid(self, head):
        slow = head
        fast = head.next
        while fast and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        return slow

    def merge(self, head1, head2):
        p = head1
        q = head2
        merged = Node(0)
        temp = merged

        while (p and q):
            if(p.data > q.data):
                temp.next = q
                temp = temp.next
                q = q.next
            else:
                temp.next = p
                temp = temp.next
                p = p.next
        while p:
            temp.next = p
            temp = temp.next
            p = p.next
        while q:
            temp.next = q
            temp = temp.next
            q = q.next
        return merged.next

    def mergeSort(self, head):
        if(head.next == None):
            return head
        mid = self.findMid(head)
        head2 = mid.next
        mid.next = None
        finalHead1 = self.mergeSort(head)
        finalHead2 = self.mergeSort(head2)
        return self.merge(finalHead1, finalHead2)


# {
#  Driver Code Starts
# Initial Template for Python 3

# Contributed by : Nagendra Jha

# Node Class

class Node:
    def __init__(self, data):  # data -> value stored in node
        self.data = data
        self.next = None


# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node

# prints the elements of linked list starting with head


def printList(head):
    if head is None:
        print(' ')
        return
    curr_node = head
    while curr_node:
        print(curr_node.data, end=" ")
        curr_node = curr_node.next
    print(' ')


if __name__ == '__main__':
    t = int(input())
    for cases in range(t):
        n = int(input())
        p = LinkedList()  # create a new linked list 'a'.
        nodes_p = list(map(int, input().strip().split()))
        for x in nodes_p:
            p.append(x)  # add to the end of the list

        printList(Solution().mergeSort(p.head))

# } Driver Code Ends
