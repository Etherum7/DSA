# Recursive
class Solution:
    def reverse(self,head, k):
        # Code here
        if not head:
            return None
        p=None
        q=head
        r=None
        i=0
        while q and i<k:
                r=q.next
                q.next=p
                p=q
                q=r
                i+=1
        if r:
            head.next=self.reverse(r,k)
        return p