# def add_vertex(vertex_no):
#     global graph
#     global vertices_no
#     if vertex_no in graph:
#         print(f'Vertex {vertex_no} already exists in graph')
#         return
#     vertices_no += 1
#     graph[vertex_no] = []


# def add_edge(v1, v2, weight):
#     global graph
#     if v1 not in graph:
#         print(f'Vertex {v1} does not exist in graph')
#         return
#     if v2 not in graph:
#         print(f'Vertex {v2} does not exist in graph')
#         return
#     temp = [v2, weight]
#     graph[v1].append(temp)


# def print_graph():
#     global graph
#     for key, val in graph.items():
#         for edges in val:
#             print(key, " -> ", edges[0], " edge weight: ", edges[1])


# graph = {}
# vertices_no = 0

# add_vertex(1)
# add_vertex(2)
# add_vertex(3)
# add_vertex(4)
# # Add the edges between the vertices by specifying
# # the from and to vertex along with the edge weights.
# add_edge(1, 2, 1)
# add_edge(1, 3, 1)
# add_edge(2, 3, 3)
# add_edge(3, 4, 4)
# add_edge(4, 1, 5)
# print_graph()


