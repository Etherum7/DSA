from typing import *


class Node():
    def __init__(self):
        self.links = [None]*26
        self.flag = False

    def containsKey(self, ch):
        return self.links[ord(ch)-ord('a')] != None

    def put(self, ch, node):
        self.links[ord(ch)-ord('a')] = node

    def get(self, ch):
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

    def checkIfPrefixExists(self, word):
        node = self.root
        for ch in word:
            if node.containsKey(ch):
                node = node.get(ch)
                if node.flag == False:
                    return False
            else:
                return False
        return True


def completeString(n: int, a: List[str]) -> str:

    # Write your Code here
    ob = Trie()
    for s in a:
        ob.insert(s)
    res = ''
    for s in a:
        if ob.checkIfPrefixExists(s):
            if len(s) > len(res):
                res = s
            elif len(s) == len(res):
                if s < res:
                    res = s

    return res if res != ''else None
