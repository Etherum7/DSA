#User function Template for python3
class Node:
    def __init__(self):
        self.links = [None]*2

    def containsKey(self, bit):
        
        return self.links[bit] != None

    def put(self, bit, node):
        self.links[bit] = node

    def get(self, bit):
        return self.links[bit]
class Trie():
    def __init__(self):
        self.root=Node()
    def insert(self, num):
        node = self.root
        for i in range(31, -1, -1):
            bit = (num>>i)&1
            if not node.containsKey(bit):
                node.put(bit, Node())
            node=node.get(bit)
    def getMax(self, num):
        node=self.root
        maxNum=0
        for i in range(31, -1, -1):
            bit = (num>>i )& 1
            if node.containsKey(1-bit):
                maxNum= maxNum | 1<<i
                node=node.get(1-bit)
                
            else:
                node=node.get(bit)
        return maxNum
        
class Solution:
    def max_xor(self, arr, n):
        #code here
        trie=Trie()
        for num in arr:
            trie.insert(num)
        mx=-1
        for num in arr:
            mx=max(mx, trie.getMax(num))
        return mx

ob = Solution()
print(ob.max_xor([25, 10, 2, 8, 5, 3], 6))
