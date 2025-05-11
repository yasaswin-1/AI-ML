from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.visited = set()
        self.path = []

    def addedge(self, u, v):
        self.graph[u].append(v)

    def DLS(self, src, target, maxDepth):
        self.path.append(src)
        if src == target:
            return True
        if maxDepth <= 0:
            return False
        self.visited.add(src)
        for i in self.graph[src]:
            if i not in self.visited:
                if self.DLS(i, target, maxDepth - 1):
                    return True
                self.path.remove(i)
        return False

g = Graph()
for _ in range(int(input("Enter number of edges: "))):
    a, b = map(int, input("Enter edge (x y): ").split())
    g.addedge(a, b)

target = int(input("Enter target node: "))
maxDepth = int(input("Enter maximum depth: "))
src = int(input("Enter source node: "))

if g.DLS(src, target, maxDepth):
    print("Target is reachable from source within max depth")
    print("Path:", g.path)
else:
    print("Target is NOT reachable from source within max depth")
