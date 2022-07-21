# Following is the Binary Tree node structure:
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def getTreeTraversal(root):
    # Write your code here.
    res = [[] for _ in range(3)]
    st = []
    if not root:
        return res
    st.append((root, 1))
    while len(st):
        t = st.pop()
        if t[1] == 1:
            res[1].append(t[0].data)
            st.append((t[0], 2))
            if t[0].left:
                st.append((t[0].left, 1))
        elif t[1] == 2:
            res[0].append(t[0].data)
            st.append((t[0], 3))
            if t[0].right:
                st.append((t[0].right, 1))
        else:
            res[2].append(t[0].data)

    return res
