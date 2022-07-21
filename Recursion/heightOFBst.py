class Node:
    def __init__(self, data):
        self.data=data
        self.left=None
        self.right=None
    
def height(root):
    if not root:
        return 0
    lh= height(root.left)
    rh= height(root.right)
    return 1+max(lh, rh)

root=Node(3)
root.left=Node(2)
root.left.left=Node(1)

root.right=Node(4)
# root.right.right=Node(5)
# root.right.right.right=Node(6)

print(height(root))



