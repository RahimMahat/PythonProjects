from collections import deque

class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def bfs(self, start, end):
        # start a queue with start vertex in it
        queue = deque()
        queue.append(start)
        # run a loop until queue is empty
        while queue:
            # dequeuing element out of queue
            path = queue.popleft()
            # get the last element
            node = path[-1]
            # check if last element is the end(destination) and return path
            if node == end:
                return path
            # else loop through it's adjacent vertices
            for adjacent in self.gdict.get(node, []):
                # assign a new path
                new_path = list(path)
                # append the adjacent vertices in new path
                new_path.append(adjacent)
                # append new path in the queue
                queue.append(new_path)
        # TC: bigO(E)


gdict = {
    "a": ["b", "c"],
    "b": ["d", "g"],
    "c": ["d", "e"],
    "d": ["f"],
    "e": ["f"],
    "g": ["f"]
}

graph = Graph(gdict)
print(graph.bfs("a", "f"))