from sys import stdin, setrecursionlimit
setrecursionlimit(10**7)


class Node():
    def __init__(self):
        self.links = [None]*26
        self.flag = False

    def containsKey(self, ch):
        return self.links[ord(ch)-ord('a')] != None

    def put(self, ch, node):
        self.links[ord(ch)-ord('a')] = node

    def get(self,ch):
        return self.links[ord(ch)-ord('a')]

    def setEnd(self):
        self.flag = True


class Trie:

    def __init__(self):
        self.root = Node()

        # constructor for the Trie
        pass
    # n

    def insert(self, string):
        node = self.root
        for ch in string:
            if not node.containsKey(ch):
                node.put(ch, Node())

            node = node.get(ch)
        node.setEnd()

    def search(self, word):
        node = self.root
        for ch in word:
            if node.containsKey(ch):
                node = node.get(ch)
            else:
                return False
        return node.flag

    def startWith(self, prefix):
        node = self.root
        for ch in prefix:
            if node.containsKey(ch):
                node = node.get(ch)
            else:
                return False
        return True


# main
t = int(input().strip())
root = Trie()
for i in range(t):

    q_str = stdin.readline().strip().split(" ")
    q = int(q_str[0].strip())
    str1 = q_str[1].strip()

    if(q == 1):
        root.insert(str1)

    elif (q == 2):
        if(root.search(str1)):
            print("true")

        else:
            print("false")

    else:
        if(root.startWith(str1)):
            print("true")

        else:
            print("false")
