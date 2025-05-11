def create_graph():
    n = int(input("Enter number of vertices: "))
    print("Enter adjacency matrix:")
    return [list(map(int, input().split())) for _ in range(n)]

def color_graph(G):
    n = len(G)
    colors = ["Blue", "Red", "Yellow", "Green"]
    result = [-1] * n
    result[0] = 0

    for u in range(1, n):
        available = [False] * len(colors)
        for i in range(n):
            if G[u][i] == 1 and result[i] != -1:
                available[result[i]] = True
        result[u] = next(c for c, available in enumerate(available) if not available)

    return {chr(97 + i): colors[result[i]] for i in range(n)}

G = create_graph()
solution = color_graph(G)
print(solution)
for node, color in sorted(solution.items()):
    print(f"Node {node} = {color}")
