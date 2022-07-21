# User function Template for python3

''' Node for linked list:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''


class Solution:
    def reverse(self, head):
        p = None
        q = None

        r = head

        while r:
            q = r
            r = r.next
            q.next = p
            p = q

        return q
    # Function to add two numbers represented by linked list.

    def addTwoLists(self, first, second):
        # code here
        # return head of sum list
        first = self.reverse(first)
        second = self.reverse(second)
        head = temp = Node(0)
        carry = 0
        while first or second or carry:
            temp.next = Node(0)
            temp = temp.next
            if first:
                temp.data += first.data
                first = first.next
            if second:
                temp.data += second.data
                second = second.next
            temp.data += carry
            if temp.data > 9:
                carry = 1
                temp.data = temp.data % 10
            else:
                carry = 0
        return self.reverse(head.next)
