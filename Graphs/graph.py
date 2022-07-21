import sys
from collections import defaultdict
from operator import ne
from queue import Queue


def bfsOfGraph(V, adj):
    # code here
    res = []
    q = Queue(V)
    visited = [0]*(V+1)
    q.put(1)
    res.append(1)
    visited[1]=1
    while not q.empty():
        t = q.get()
        
        for i in adj[t]:
            if visited[i] != 1:
                visited[i] = 1
                res.append(i)
                q.put(i)
    return res


def dfsOfGraph(V, adj):
    # code here
    res = []
    visited = [0]*(V+1)

    def util(i):
        res.append(i)
        visited[i] = 1
        for x in adj[i]:
            if visited[x] != 1:
                util(x)
        return res
    return util(1)


def dfsStack(V, adj):
    stack = []
    res = []
    visited = [0]*(V+1)
    stack.append(1)

    visited[1] = 1
    while len(stack) > 0:
        t = stack.pop()
        res.append(t)
        for neighbor in reversed(adj[t]):
            if visited[neighbor] != 1:

                visited[neighbor] = 1
                stack.append(neighbor)
    return res


def hasPathDFS(V, adj, source, destination):
    # code here
    # dfs
    visited = [0]*(V+1)
    visited[source] = 1

    def util(source, destination):
        if source == destination:
            return True
        for neighbor in adj[source]:
            if visited[neighbor] != 1:
                visited[neighbor] = 1
                if util(neighbor, destination) == True:
                    return True
        return False
    return util(source, destination)


def hasPathBFS(V, adj, source, destination):
    q = Queue()
    v = [0]*(V+1)
    if source == destination:
        return True
    v[source] = 1
    q.put(source)
    while not q.empty():
        t = q.get()
        for neighbor in adj[t]:
            if v[neighbor] != 1:
                if neighbor == destination:
                    return True
                v[neighbor] = 1
                q.put(neighbor)
    return False


def noOfConnectedComponents(V, adj):
    visited = [0]*(V+1)
    cnt = 0
    for v in range(1, V+1):
        if visited[v] != 1:
            DFSUtil(v, adj, visited)
            cnt += 1
    return cnt


def DFSUtil(v, adj, visited):
    visited[v] = 1
    for neighbour in adj[v]:
        if visited[neighbour] != 1:
            DFSUtil(neighbour, adj, visited)


def buildGraphFromEdgeList(edgeList):
    res = {}
    for edge in edgeList:
        [a, b] = edge
        if not a in res:
            res[a] = []
        if not b in res:
            res[b] = {}
        res[a].append(b)
        res[b].append(a)
    return res


def largest_component(graph):
    res = 0
    visited = set()

    for node in graph:
        c = exploreSize(node, graph, visited)
        if c >= res:
            res = c
    return res
def dfsU(v, temp, visited, graph):
    visited[v]=1
    temp[0]+=1
    for neighbor in graph[v]:
        if not visited[neighbor]:
            dfsU(neighbor, temp, visited, graph)

def largest_component2(graph):
    res=0
    
    N= len(graph)
    visited=[0]*(N)

    for i in range(N):
        temp=[0]
        if not visited[i]:
            dfsU(i, temp , visited, graph)
            res=max(res, temp[0])
    return res


def explore(node, graph, visited):
    q = Queue()
    q.put(node)
    visited.add(node)
    c = 1
    while not q.empty():
        t = q.get()
        for neighbour in graph[t]:
            if neighbour not in visited:
                visited.add(neighbour)
                q.put(neighbour)
                c += 1
    return c


def exploreSize(node, graph, visited):
    if node in visited:
        return 0
    visited.add(node)

    for neighbour in graph[node]:
        return 1 + exploreSize(neighbour, graph, visited)


def build_graph(edges):
    graph = defaultdict(list)
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])
    return graph


def shortest_path(edges, node_A, node_B):
    graph = build_graph(edges)
    print(graph)
    q = Queue()
    visited = set()
    q.put((node_A, 0))
    visited.add(node_A)
    while not q.empty():
        t = q.get()
        if t[0] == node_B:
            return t[1]
        for neighbour in graph[t[0]]:
            if not neighbour in visited:
                visited.add(neighbour)
                q.put((neighbour, t[1]+1))
    return -1


def island_count(grid):
    visited = set()
    cnt = 0
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            # if grid[row][col] != 'W' and (row, col) not in visited:
            if(dfs_island((row, col), grid, visited)):
                cnt += 1
    return cnt


def dfs_island(s, grid, visited: set):
    rowInBounds = 0 <= s[0] < len(grid)
    colInBounds = 0 <= s[1] < len(grid[0])
    if not rowInBounds or not colInBounds:
        return False
    if grid[s[0]][s[1]] == 'W':
        return False
    if s in visited:
        return False
    visited.add(s)
    dfs_island((s[0]+1, s[1]), grid, visited)
    dfs_island((s[0], s[1]+1), grid, visited)
    dfs_island((s[0]-1, s[1]), grid, visited)
    dfs_island((s[0], s[1]-1), grid, visited)
    return False


def minimum_island(grid):
    visited = set()
    res = float('inf')

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            c = exploreIsland((row, col), grid, visited)
            if c > 0 and c < res:
                res = c
    return res


def exploreIsland(pos, grid, visited):
    rowInBounds = 0 <= pos[0] < len(grid)
    colInBounds = 0 <= pos[1] < len(grid[0])
    if not rowInBounds or not colInBounds:
        return 0
    if grid[pos[0]][pos[1]] == 'W':
        return 0
    if pos in visited:
        return 0
    visited.add(pos)
    return 1+explore((pos[0]+1, pos[1]), grid, visited)+explore((pos[0]-1, pos[1]), grid, visited)+explore((pos[0], pos[1]+1), grid, visited)+explore((pos[0], pos[1]-1), grid, visited)


class Solution1:

    # Function to detect cycle in an undirected graph.
    def util(self, v,  adj, visited, parent):
        visited[v] = 1
        for neighbour in adj[v]:
            if not visited[neighbour]:
                if self.util(neighbour, adj, visited, v):
                    return 1
            elif neighbour != parent:
                return 1
        return 0

    def isCycle(self, V, adj):
        # Code here
        visited = [False]*(V+1)

        for v in range(V):
            if not visited[v]:
                if self.util(v, adj, visited, -1):
                    return 1
        return 0
# User function Template for python3


class Solution2:

    # Function to detect cycle in a directed graph.

    def isCyclic(self, V, adj):
        # code here
        visited = [False]*(V)
        recStack = [False]*(V)

        for vertex in range(V):
            if not visited[vertex]:
                if self.isCyclicUtil(vertex, adj, visited, recStack):
                    return True
        return False

    def isCyclicUtil(self, v, adj, visited, recStack):
        visited[v] = True
        recStack[v] = True
        for neighbour in adj[v]:
            if not visited[neighbour]:
                if self.isCyclicUtil(neighbour, adj, visited, recStack):
                    return True
            elif recStack[neighbour]:
                return True
        recStack[v] = False
        return False
# bfs cycle detection






adj = [[], [2, 3, 4], [1, 3, 4], [1, 2, 4], [1, 3, 5], [3, 4, 6, 7], [5], [5]]
adj2 = [[], [2, 4], [3], [], [2, 6], [4], []]
adj3 = [[], [2], [1], [], [5, 6, 8, 7], [4, 6, 7, 8],
        [4, 5, 7, 8], [4, 5, 6, 8], [4, 5, 6, 7]]
# print(bfsOfGraph(7, adj))
print(largest_component2(adj2))
# print(dfsOfGraph(6, adj2))
# print(dfsStack(6, adj2))

# print(hasPathDFS(6, adj2, 1,5))
# print(hasPathBFS(6, adj2, 5,6))

# print(noOfConnectedComponents(8, adj3))
