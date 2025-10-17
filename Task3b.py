def aStarAlgo(start_node, stop_node):
    open_set = set([start_node])
    closed_set = set()
    g = {}
    parents = {}
    g[start_node] = 0
    parents[start_node] = start_node

    while len(open_set) > 0:
        n = None
        for v in open_set:
            if n is None or g[v] + heuristic(v) < g[n] + heuristic(n):
                n = v

        if n == stop_node or n is None or n not in Graph_nodes:
            break
        else:
            for m, weight in get_neighbors(n):
                if m not in open_set and m not in closed_set:
                    open_set.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight
                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n
                        if m in closed_set:
                            closed_set.remove(m)
                            open_set.add(m)

        open_set.remove(n)
        closed_set.add(n)

    if n is None:
        print('Path does not exist!')
        return None

    if n == stop_node:
        path = []
        while parents[n] != n:
            path.append(n)
            n = parents[n]
        path.append(start_node)
        path.reverse()
        print('Path found:', path)
        return path

    print('Path does not exist!')
    return None

def get_neighbors(v):
    if v in Graph_nodes:
        return Graph_nodes[v]
    else:
        return None

def heuristic(n):
    return h_dist[n]

h_dist = {
    'S': 10, 'T': 8, 'U': 5, 'V': 7,
    'W': 3, 'X': 6, 'Y': 4, 'Z': 0
}

Graph_nodes = {
    'S': [('T', 2), ('U', 4)],
    'T': [('S', 2), ('V', 3)],
    'U': [('S', 4), ('W', 2)],
    'V': [('T', 3), ('X', 5)],
    'W': [('U', 2), ('Y', 3)],
    'X': [('V', 5), ('Z', 4)],
    'Y': [('W', 3), ('Z', 2)],
    'Z': [('X', 4), ('Y', 2)]
}

print("Following is the A* Algorithm:")
aStarAlgo('S', 'Z')
