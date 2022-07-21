# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, cur):
        prev = None
        nex = None
        while cur:
            nex = cur.next
            cur.next = prev
            prev = cur
            cur = nex
        return prev

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        slow.next = self.reverse(slow.next)
        slow = slow.next
        dummy = head
        while slow:
            if dummy.val != slow.val:
                return False
            dummy = dummy.next
            slow = slow.next
        return True


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        res1 = 0
        res2 = 0
        temp = 1
        p = head
        while p:
            res1 = (res1*10)+p.val
            res2 = res2+(p.val*temp)
            temp = temp*10
            p = p.next
        return res2 == res1
