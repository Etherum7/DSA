# User function Template for python3
'''
	Function to return the value at point of intersection
	in two linked list, connected in y shaped form.
	
	Function Arguments: head_a, head_b (heads of both the lists)
	
	Return Type: value in NODE present at the point of intersection
	             or -1 if no common point.

	Contributed By: Nagendra Jha

	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}
'''


def getDiff(head1, head2):
    len1 = len2 = 0
    while head1 or head2:
        if head1:
            len1 += 1
            head1 = head1.next
        if head2:
            len2 += 1
            head2 = head2.next
    return len1-len2

# Function to find intersection point in Y shaped Linked Lists.


def intersetPoint(head1, head2):
    # code here
    t1 = head1
    t2 = head2
    diff = getDiff(t1, t2)
    while diff > 0:
        head1 = head1.next
        diff -= 1
    while diff < 0:
        head2 = head2.next
        diff += 1
    while head1 and head1 != head2:
        head1 = head1.next
        head2 = head2.next
    return head1.data

# Hashing


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        d = {}
        while headA:
            d[headA] = 1
            headA = headA.next
        while headB:
            if headB in d:
                return headB
            headB = headB.next
        return None
