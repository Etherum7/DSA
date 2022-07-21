class Solution:

    # Function to rotate a linked list.
    def rotate(self, head, k):
        # code here
        last = Node(0)
        cur = Node(0)
        last.next = head
        cur.next = head
        i = 0
        while last.next:
            if i < k:
                cur = cur.next
                i += 1
            last = last.next
        last.next = head
        head = cur.next
        cur.next = None
        return head
