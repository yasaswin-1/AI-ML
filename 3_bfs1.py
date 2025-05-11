from queue import PriorityQueue
v=14
graph=[[] for i in range(v)]
def addedge(x,y,cost):
    graph[x].append((y,cost))
    graph[y].append((x,cost))
def bestFirstSearch(source,target,n):
    visted=[False]*n
    pq=PriorityQueue()
    pq.put((0,source))
    visted[source]=True
    while pq.empty()==False:
        u=pq.get()[1]
        print(u,end=" ")
        if(u==target):
            break
        for v,c in graph[u]:
            if(visted[v]==False):
                visted[v]=True
                pq.put((c,v))
    print()
addedge(0,1,2)
addedge(0,2,6)
addedge(0,3,5)
addedge(1,4,1)
addedge(1,5,8)
addedge(2,6,12)
addedge(2,7,14)
addedge(3,8,2)
addedge(8,9,9)
addedge(8,10,6)
addedge(9,11,1)
addedge(9,12,10)
addedge(9,13,2)
source=0
target=9
bestFirstSearch(source,target,v)