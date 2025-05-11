from collections import defaultdict

# Initialize the graph and visited set
graph = defaultdict(list)
visited = set()

def addedge(x, y):
    graph[x].append(y)
    graph[y].append(x)

def dfs(visited, graph, start):
    if start not in visited:
        print(start, end=" ")
        visited.add(start)
        for neighbor in graph[start]:
            dfs(visited, graph, neighbor)

# Taking user input for the graph edges
num_edges = int(input("Enter the number of edges: "))
print("Enter the edges (e.g., '0 1' for an edge between 0 and 1):")
for _ in range(num_edges):
    x, y = map(int, input().split())
    addedge(x, y)

# Taking user input for the starting node
start_node = int(input("Enter the starting node for DFS: "))

# Perform DFS traversal
dfs(visited, graph, start_node)
