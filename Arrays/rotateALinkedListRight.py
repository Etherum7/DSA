# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        slow = head
        fast = head
        ln = 0
        p = head
        modk = k
        while p:
            ln += 1
            p = p.next
        if ln < k:
            modk = k % ln
            # print(modk)
        for i in range(modk):
            fast = fast.next
            # print(fast.val)
        if fast == None:
            fast = head
        # print(slow.val)
        while fast.next:
            slow = slow.next
            fast = fast.next
        fast.next = head
        head = slow.next
        slow.next = None
        return head
