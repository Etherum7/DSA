# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = temp = ListNode(0)
        carry = 0
        while (l1 or l2) or carry:
            # print(carry)
            temp.next = ListNode(0)
            temp = temp.next
            if l1:
                temp.val += l1.val
                l1 = l1.next
            if l2:
                temp.val += l2.val
                l2 = l2.next
            temp.val += carry
            if temp.val > 9:
                carry = 1
                temp.val = temp.val % 10
            else:
                carry = 0
        return head.next
