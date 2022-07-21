class Node:
    def __init__(self):
        self.links = [None]*26
        self.endWith = 0
        self.countPrefix = 0

    def containsKey(self, ch):
        return self.links[ord(ch)-ord('a')] != None

    def put(self, ch, node):
        self.links[ord(ch)-ord('a')] = node

    def get(self, ch):
        return self.links[ord(ch)-ord('a')]

    def increaseEnd(self):
        self.endWith += 1

    def increasePrefix(self):
        self.countPrefix += 1

    def deleteEnd(self):
        self.endWith -= 1

    def reducePrefix(self):
        self.countPrefix -= 1


class Trie:
    def __init__(self):
        # Write your code here.
        self.root = Node()

    def insert(self, word):
        # Write your code here.
        node = self.root
        for ch in word:
            if not node.containsKey(ch):
                node.put(ch, Node())
            node = node.get(ch)
            node.increasePrefix()
        node.increaseEnd()

    def countWordsEqualTo(self, word):
        node = self.root
        for ch in word:
            if not node.containsKey(ch):
                return 0
            node = node.get(ch)

        return node.endWith

    def countWordsStartingWith(self, word):
        node = self.root
        for ch in word:
            if not node.containsKey(ch):
                return 0
            node = node.get(ch)
        return node.countPrefix

    def erase(self, word):
        # Write your code here.
        node = self.root
        for ch in word:
            if not node.containsKey(ch):
                return
            node = node.get(ch)
            node.reducePrefix()
        node.deleteEnd()
ob=Trie()
ob.insert('samsung')
ob.insert('samsung')
ob.insert('vivo')
ob.erase('vivo')
print(ob.countWordsEqualTo('samsung'))
print(ob.countWordsStartingWith('wi'))