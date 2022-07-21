def add_vertex(v):
    global graph, vertices, vertices_no
    if v in vertices:
        print(f'vertex {v} already in graph')
        return
    vertices_no += 1
    vertices.append(v)
    graph.append([0]*vertices_no)

    pass


def add_edge(v1, v2, weight):
    if v1 not in vertices:
        print(f'vertex {v1} not exists')
    if v2 not in vertices:
        print(f'vertex {v2} not exists')
    index1 = vertices.index(v1)
    index2 = vertices.index(v2)
    graph[index1][index2] = weight


def print_graph():
    for i in range(vertices_no):
        for j in range(vertices_no):
            if graph[i][j] != 0:
                  print(vertices[i], " -> ", vertices[j]," edge weight: ", graph[i][j])
vertices = []
# stores the number of vertices in the graph
vertices_no = 0
graph = []
# Add vertices to the graph
add_vertex(1)
add_vertex(2)
add_vertex(3)
add_vertex(4)

add_edge(1, 2, 1)
add_edge(1, 3, 1)
add_edge(2, 3, 3)
add_edge(3, 4, 4)
add_edge(4, 1, 5)
print_graph()



