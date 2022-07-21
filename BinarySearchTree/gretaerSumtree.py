
class Solution:
    def __init__(self):
        self.s = [0]

    def inorder(self, root):

        if not root:
            return 0
        self.inorder(root.right)
        temp = root.data
        root.data = self.s[0]
        self.s[0] += temp
        self.inorder(root.left)

    def transformTree(self, root):
        # code here
        self.inorder(root)

        return root
