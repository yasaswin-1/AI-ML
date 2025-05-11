from queue import PriorityQueue

def a_star(s, t, g, h):
    pq, graph, parent = PriorityQueue(), {node: float('inf') for node in g}, {s: None}
    graph[s], pq.queue = 0, [(h[s], s, 0)]
    
    while not pq.empty():
        _, u, c = pq.get()
        if u == t:
            path = []
            while u is not None:
                path.append(u)
                u = parent[u]
            return graph[t], path[::-1]
        for v, cost in g[u]:
            tg = graph[u] + cost
            if tg < graph[v]:
                graph[v], parent[v] = tg, u
                pq.put((h[v] + tg, v, tg))
    return float('inf'), []

def main():
    vt = int(input("Enter number of vertices: "))
    g = {i: [] for i in range(vt)}
    for _ in range(int(input("Enter number of edges: "))):
        u, v, cost = map(int, input("Enter edge (u v cost): ").split())
        g[u].append((v, cost))
        g[v].append((u, cost))
    h = {i: int(input(f"Enter heuristic value for node {i}: ")) for i in range(vt)}
    s, t = int(input("Enter source vertex: ")), int(input("Enter target vertex: "))
    cost, path = a_star(s, t, g, h)
    if path:
        print(f"The shortest path from {s} to {t} has a cost of {cost}\nPath: {' -> '.join(map(str, path))}")
    else:
        print(f"No path found from {s} to {t}")

if __name__ == "__main__":
    main()
