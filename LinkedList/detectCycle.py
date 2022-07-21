# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or head.next==None:
            return None
        slow=head
        fast=head
        entry=head
        while fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                while slow!=entry:
                    slow=slow.next
                    entry=entry.next
                return slow
        return None