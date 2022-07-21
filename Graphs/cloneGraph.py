"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from queue import Queue


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node

        q = Queue()
        visited = {}
        q.put(node)
        visited[node.val] = Node(node.val)
        while not q.empty():
            t = q.get()
            cur_visited = visited[t.val]
            for nb in t.neighbors:
                if nb.val not in visited:
                    visited[nb.val] = Node(nb.val)
                    q.put(nb)
                cur_visited.neighbors.append(visited[nb.val])
        return visited[node.val]