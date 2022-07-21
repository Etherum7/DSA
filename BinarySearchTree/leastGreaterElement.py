from typing import List


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(root, key):
    while root:
        t = root
        if root.data == key:
            return
        if key < root.data:
            root = root.left
        elif key > root.data:
            root = root.right
    node = Node(key)
    if key > t.data:
        t.right = node
    else:
        t.left = node


def search(root, key):
    res = None
    while root:
        if root.data > key:
            res = root
            root = root.left
        elif root.data <= key:
            root = root.right
    return res


class Solution:
    def findLeastGreater(self, n: int, arr: List[int]) -> List[int]:
        # code here
        root = Node(arr[n-1])
        res = [-1]*n

        for i in range(n-2, -1, -1):
            pos = search(root, arr[i])
            if pos:
                res[i] = pos.data
            insert(root, arr[i])
        return res


# {
#  Driver Code Starts
class IntArray:
    def __init__(self) -> None:
        pass

    def Input(self, n):
        arr = [int(i) for i in input().strip().split()]  # array input
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        n = int(input())

        arr = IntArray().Input(n)

        obj = Solution()
        res = obj.findLeastGreater(n, arr)

        IntArray().Print(res)


# } Driver Code Ends
