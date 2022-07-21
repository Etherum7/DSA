from itertools import permutations


def tspSimp(graph, src, N):
    vertex = []
    for i in range(N):
        if i != src:
            vertex.append(i)
    res = float('inf')
    next_permutation = permutations(vertex)
    # print(list(next_permutation))
    for path in next_permutation:
        t = 0
        k = s
        for i in path:
            t += graph[k][i]
            k = i

        t += graph[k][src]
        print(t)
        res = min(res, t)
    return res


graph = [[0, 10, 15, 20], [10, 0, 35, 25],
         [15, 35, 0, 30], [20, 25, 30, 0]]
s = 0
# print(tspSimp(graph, s, 4))


def dfs(pos, graph, visited, d, res, N):

    if not False in visited:
        res[0] = min(res[0], d+graph[pos][0])
        return
    for i in range(N):
        if not visited[i] and graph[pos][i]:
            visited[i] = True
            dfs(i, graph, visited, d+graph[pos][i], res,  N)
            visited[i] = False


def tspDfs(graph, N):
    visited = [False]*N
    # visited[0] = True
    res = [float('inf')]

    dfs(0, graph,  visited, 0, res, N)
    return res[0]


N = 4
graph = [[0, 10, 15, 20],
         [10, 0, 35, 25],
         [15, 35, 0, 30],
         [20, 25, 30, 0]]
print(tspDfs(graph, N))
