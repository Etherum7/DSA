from queue import Queue


def util(s, m, n, d, visited, q):
    q.put(s)
    visited.add((s[0],s[1]))
    while not q.empty():
        state = q.get()
        if state[0] == 0 and state[1] == d or state[1] == 0 and state[0] == d:
            return state[2]
        if state[0] == 0:
            # fill 1
            if (m, state[1]) not in visited:
                t = state[2].copy()
                t.append((m, state[1]))
                q.put((m, state[1], t))
                visited.add((m, state[1]))
        if state[1] == 0:
            if (state[0], n) not in visited:
                t = state[2].copy()
                t.append((state[0], n))
                q.put((state[0], n, t))
                visited.add((state[0], n))

        # empty

        if (0, state[1]) not in visited:
            t = state[2].copy()
            t.append((0, state[1]))
            visited.add((0, state[1]))
            q.put((0, state[1], t))
        if (state[0], 0) not in visited:
            t = state[2].copy()
            t.append((state[0], 0))
            visited.add((state[0], 0))
            q.put((state[0], 0, t))

        # transfer

        # emptying one
        if state[0]+state[1] <= n:
            if (0, state[1]+state[0]) not in visited:
                t = state[2].copy()
                t.append((0, state[1]+state[0]))
                visited.add((0, state[1]+state[0]))
                q.put((0, state[1]+state[0], t))
        # emptying two
        if state[0]+state[1] <= m:
            if (state[1]+state[0], 0) not in visited:
                t = state[2].copy()
                t.append((state[1]+state[0], 0))
                visited.add((state[1]+state[0], 0))
                q.put((state[1]+state[0], 0, t))
        # filling two
        if state[0]+state[1] >= n:
            if (state[0]-(n-state[1]), n) not in visited:
                t = state[2].copy()
                t.append((state[0]-(n-state[1]), n))
                visited.add((state[0]-(n-state[1]), n))
                q.put((state[0]-(n-state[1]), n, t))
        # filling one
        if state[0]+state[1] >= m:
            if (m, state[1]-(m-state[0])) not in visited:
                t = state[2].copy()
                t.append((m, state[1]-(m-state[0])))
                visited.add((m, state[1]-(m-state[0])))
                q.put((m, state[1]-(m-state[0]), t))

    return -1


def waterJug(m, n, d):
    visited = set()
    q = Queue()
    ini = (0, 0, [0,0])
    
    print(util(ini, m, n, d, visited, q))
    
waterJug(4,3,2)