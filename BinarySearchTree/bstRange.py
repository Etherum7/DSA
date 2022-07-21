# Function to count number of nodes in BST that lie in the given range.
class Solution:
    def preorder(self, root, low, high, cnt):
        if root:
            if low <= root.data <= high:
                cnt[0] += 1
            if low <= root.data:
                self.preorder(root.left, low, high, cnt)
            if high >= root.data:
                self.preorder(root.right, low, high, cnt)

    def getCount(self, root, low, high):
        # Your code here
        cnt = [0]
        self.preorder(root, low, high, cnt)
        return cnt[0]
