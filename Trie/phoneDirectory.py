ser function Template for python3


class Node():
    def __init__(self):
        self.links = [None]*26
        self.words = []

    def containsKey(self, ch):
        return self.links[ord(ch)-ord('a')] != None

    def put(self, ch, node):
        self.links[ord(ch)-ord('a')] = node

    def get(self, ch):
        return self.links[ord(ch)-ord('a')]


class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, string, ind):
        node = self.root

        for ch in string:
            if not node.containsKey(ch):

                node.put(ch, Node())

            node = node.get(ch)
            node.words.append(ind)

    def search(self, word, ind, res, contacts):
        node = self.root
        for ch in word:
            if node.containsKey(ch):
                node = node.get(ch)
            else:
                res[ind].append(0)
                return
        for i in node.words:
            res[ind].append(contacts[i])


class Solution:
    def displayContacts(self, n, contacts, s):
        # code here
        trie = Trie()
        contacts.sort()

        i = 0
        while i < n:
            while(i < n-1 and contacts[i+1] == contacts[i]):
                i += 1
            trie.insert(contacts[i], i)
            i += 1
        m = len(s)
        res = [[] for _ in range(m)]
        for i in range(m):
            trie.search(s[:i+1], i, res, contacts)
        # print(res)
        return res
