
class Solution:
    # Function to sort a linked list of 0s, 1s and 2s.
    def segregate(self, head):
        # code here
        z = o = t = 0
        p = head
        while p:
            if p.data == 0:
                z += 1
            elif p.data == 1:
                o += 1
            else:
                t += 1
            p = p.next

        p = head
        c = 0
        while p:
            if c < z:
                p.data = 0
            elif c >= z and c < o+z:
                p.data = 1
            elif c >= o+z and c < o+z+t:
                p.data = 2
            c += 1
            p = p.next
        return head
