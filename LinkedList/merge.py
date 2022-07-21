# User function Template for python3
'''
	Function to merge two sorted lists in one
	using constant space.
	
	Function Arguments: head_a and head_b (head reference of both the sorted lists)
	Return Type: head of the obtained list after merger.

	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}

'''
# Function to merge two sorted linked list.


def sortedMerge(head1, head2):
    # code here

    t1 = head1
    t2 = head2
    head3 = t3 = Node(0)
    while t1 and t2:
        if t1.data <= t2.data:
            t3.next = t1
            t1 = t1.next
            t3 = t3.next
        elif t1.data > t2.data:
            t3.next = t2
            t2 = t2.next
            t3 = t3.next
    while t1:
        t3.next = t1
        t1 = t1.next
        t3 = t3.next
    while t2:
        t3.next = t2
        t2 = t2.next
        t3 = t3.next

    return head3.next
