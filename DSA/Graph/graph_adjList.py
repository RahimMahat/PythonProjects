from collections import deque

class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def addEdge(self,vertex, edge):
        self.gdict[vertex].append(edge)

    # in case of bfs we use queue data structure fro it's FIFO property
    def BFS(self, vertex):
        # add source vertex to the visited list
        visited = [vertex]
        queue = deque()
        # add source vertex in the queue
        queue.append(vertex)
        # running loop until there is queue 
        while queue:
            # dequeueing the vertex in FIFO manner
            deVertex = queue.popleft()
            # printing dequeued vertex
            print(deVertex, end=" ")
            # running loop to find adjacent vertices to the given vertex
            for adjacentVertex in self.gdict[deVertex]:
                # and iff adjacent vertices are not in visited list
                if adjacentVertex not in visited:
                    # add them to the visited list
                    visited.append(adjacentVertex)
                    # then add them to the queue
                    queue.append(adjacentVertex)

    # in case of dfs we use stack for it's LIFO property
    def DFS(self, vertex):
        '''
        In DFS we use same steps as BFS
        with one minor change and that is
        we use stack's LIFO property instead of
        queue's FIFO method
        '''
        visited = [vertex]
        stack = deque()
        stack.append(vertex)
        while stack:
            popVertex = stack.pop()
            print(popVertex, end=" ")
            for adjacentVertex in self.gdict[popVertex]:
                if adjacentVertex not in visited:
                    visited.append(adjacentVertex)
                    stack.append(adjacentVertex)





customDict = {
    "a": ["b","c"],
    "b": ["a", "d", "e"],
    "c": ["a", "e"],
    "d": ["b", "e", "f"],
    "e": ["d", "f"],
    "f": ["d", "e"]
}

graph = Graph(customDict)
graph.BFS("a")              #-> a b c d e f
graph.DFS("a")              #-> a c e f d b
