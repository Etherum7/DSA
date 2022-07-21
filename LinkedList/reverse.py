class Solution:
    # Function to reverse a linked list.
    def reverseList(self, head):
        # Code here
        p = q = None
        r = head
        while r:
            q = r
            r = r.next
            q.next = p
            p = q
        head = q
        return head
