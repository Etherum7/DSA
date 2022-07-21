from collections import defaultdict


def topo(v, adj, visited, st):
    visited[v] = True
    for neighbor in adj[v]:
        if not visited[neighbor]:
            topo(neighbor, adj, visited, st)
    st.append(v)


def minTimeReqd(V, adj):
    st = []
    visited = [False]*V
    for i in range(V):
        if not visited[i]:
            topo(i, adj, visited, st)
    st = st[::-1]
    time = [0]*V
    adj1 = [[] for i in range(V)]
    for i, item in enumerate(adj):
        for j in item:
            adj1[j].append(i)
    for job in st:
        res = 0

        for dep in adj1[job]:
            res = max(res, time[dep])
        time[job] = res+1
    return time


# Class to represent a graph


class Graph:

    def __init__(self, vertices, edges):

        # Dictionary containing adjacency List
        self.graph = [[] for _ in range(vertices)]

        # No. of vertices
        self.n = vertices

        # No. of edges
        self.m = edges

    # Function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)


n = 11
m = 13

g = Graph(n, m)

# Given Directed Edges of graph
g.addEdge(1, 3)
g.addEdge(1, 4)
g.addEdge(1, 5)
g.addEdge(2, 3)
g.addEdge(2, 8)
g.addEdge(2, 9)
g.addEdge(3, 6)
g.addEdge(4, 6)
g.addEdge(4, 8)
g.addEdge(5, 8)
g.addEdge(6, 7)
g.addEdge(7, 8)
g.addEdge(8, 10)
print(minTimeReqd(11, g.graph))


# Python3 program for the above approach
from collections import defaultdict

# Class to represent a graph
class Graph:
	
	def __init__(self, vertices, edges):
		
		# Dictionary containing adjacency List
		self.graph = defaultdict(list)
		
		# No. of vertices
		self.n = vertices
		
		# No. of edges
		self.m = edges
		
	# Function to add an edge to graph
	def addEdge(self, u, v):
		self.graph[u].append(v)
	
	# Function to find the minimum time
	# needed by each node to get the task
	def printOrder(self, n, m):
	
		# Create a vector to store indegrees of all
		# vertices. Initialize all indegrees as 0.
		indegree = [0] * (self.n + 1)
		
		# Traverse adjacency lists to fill indegrees
		# of vertices. This step takes O(V + E) time
		for i in self.graph:
			for j in self.graph[i]:
				indegree[j] += 1
				
		# Array to store the time in which
		# the job i can be done
		job = [0] * (self.n + 1)
		
		# Create an queue and enqueue all
		# vertices with indegree 0
		q = []
		
		# Update the time of the jobs
		# who don't require any job to
		# be completed before this job
		for i in range(1, self.n + 1):
			if indegree[i] == 0:
				q.append(i)
				job[i] = 1
				
		# Iterate until queue is empty
		while q:
			
			# Get front element of queue
			cur = q.pop(0)
			
			for adj in self.graph[cur]:
				
				# Decrease in-degree of
				# the current node
				indegree[adj] -= 1
			
				# Push its adjacent elements
				if (indegree[adj] == 0):
					job[adj] = 1 + job[cur]
					q.append(adj)
					
		# Print the time to complete
		# the job
		for i in range(1, n + 1):
			print(job[i], end = " ")
			
		print()

# Driver Code

# Given Nodes N and edges M
n = 10
m = 13

g = Graph(n, m)

# Given Directed Edges of graph
g.addEdge(1, 3)
g.addEdge(1, 4)
g.addEdge(1, 5)
g.addEdge(2, 3)
g.addEdge(2, 8)
g.addEdge(2, 9)
g.addEdge(3, 6)
g.addEdge(4, 6)
g.addEdge(4, 8)
g.addEdge(5, 8)
g.addEdge(6, 7)
g.addEdge(7, 8)
g.addEdge(8, 10)

# Function Call
g.printOrder(n, m)

# This code is contributed by Aanchal Tiwari
