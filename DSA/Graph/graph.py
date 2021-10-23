from collections import deque

def addEdge(adj, u, v):
    # as it's an undirected graph it'll create the edge both ways
    adj[u].append(v)
    adj[v].append(u)

def printGraph(adj):
    for i in adj:
        print(i)


def BFS(adj, s, visited):
    # visited = [False] * len(adj)  -> if source is given
    q = deque()
    q.append(s)
    visited[s] = True
    while q:
        s = q.popleft()
        print(s, end=' ')
        for u in adj[s]:
            if visited[u] == False:
                q.append(u)
                visited[u] = True
        
# No source given and graph may be disconnected 
def BFSDis(adj):
    visited = [False] * len(adj)
    # if we also want to count the connected components in the graph <here we will use res variable to store the count>
    res = 0
    for u in range(len(adj)):
        if visited[u] == False:
            res += 1
            BFS(adj, u, visited)
        
    return res
    # TC: bigO(V+E)



def DFSRec(adj, s, visited):
    visited[s] = True
    print(s, end=' ')
    for u in adj[s]:
        if visited[u] == False:
            DFSRec(adj, u, visited)

def DFS(adj, s): # if you are traversing for the disconnected graph don't provide the source
    # for connected graph:
    visited = [False] * len(adj)
    DFSRec(adj, s, visited)

    # for disconnected graph:
    # visited = [False] * len(adj)
    ## for the connected component count
    # res = 0
    # for u in range(len(adj)):
    #     if visited[u] == False:
    #         res += 1
    #         DFSRec(adj, u, visited)
    # return res
    # TC: bigO(V+E)




v = 4
adj = [[] for i in range(v)]  # [[],[],[],[]]

addEdge(adj, 0, 1)      # [[1],[0],[],[]]
addEdge(adj, 0, 2)      # [[1,2],[0],[0],[]]
addEdge(adj, 1, 2)      # [[1,2],[0,2],[0,1],[]]
addEdge(adj, 1, 3)      # [[1,2],[0,2,3],[0,1],[1]]


# printGraph(adj)


# BFS(adj, 0)

# BFSDis(adj)


DFS(adj, 0) # connected

# DFS(adj) # disconnected