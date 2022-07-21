def inorder(a, n, index):
    global v
    if index >= n:
        return
    inorder(a, n, 2*index+1)
    v.append(a[index])
    inorder(a, n, 2*index+2)


def min_swaps():
    global v
    t = [[0, 0] for i in range(len(v))]
    for i in range(len(v)):
        t[i][0] = v[i]
        t[i][1] = i
    t = sorted(t)
    # print(t)
    i = 0
    ans = 0
    while i < len(t):
        if i == t[i][1]:
            i += 1
            continue
        else:
            m = t[i][1]
            # Swaping of elements
            t[i][0], t[m][0] = t[m][0], t[i][0]
            t[i][1], t[m][1] = t[m][1], t[i][1]
            # print(t)

        # Second is not equal to i
        if (i == t[i][1]):
            i -= 1

        i += 1

        ans += 1

    return ans
# Flatten to LL


class Solution:
    def join(self, root1, root2):
        if root1:
            while root1.right:
                root1 = root1.right
            root1.right = root2

    def swap(self, root):
        if root.left:
            root.right = root.left
            root.left = None

    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root:
            if root.right:
                self.join(root.left, root.right)
            self.swap(root)
            self.flatten(root.right)

# Binary Tree to dll format

# Function to convert a binary tree to doubly linked list.


class Solution:
    def __init__(self):
        self.pre = None

    def setLeft(self, root):
        if root:
            self.setLeft(root.left)
            root.left = self.pre
            self.pre = root
            self.setLeft(root.right)

    def setRight(self, root):
        while root and root.right:
            root = root.right
        while root and root.left:
            prev = root
            root = root.left
            root.right = prev
        return root

    def bToDLL(self, root):
        # do Code here
        # self.setLeft.pre=None
        self.setLeft(root)
        return self.setRight(root)


if __name__ == '__main__':
    v = []
    a = [5, 6, 7, 8, 9, 10, 11]
    # a=[1,2,3]
    n = len(a)
    index = 0
    inorder(a, n, index)
    # print(v)
    print(min_swaps())
