
class Graph:
    def __init__(self, vertices):
        self.v = vertices
        self.graph = []
        self.nodes = []
    
    def addEdge(self, s, d, w):
        self.graph.append([s, d, w])
    
    def addNode(self, value):
        self.nodes.append(value)

    def printSolution(self, dist):
        print("Vertex distance from Source")
        for key, value in dist.items():
            print(f' {key} :  {value}')

    def bellmanFord(self, src):
        # set all the nodes value to infinity
        dist = {i: float('inf') for i in self.nodes}
        # set src node to 0 for further calculation simplicity
        dist[src] = 0

        # run the loop v-1 times
        for _ in range(self.v - 1):
            # iterate through graph
            for s, d, w in self.graph:
                # check if source is not infinity and
                # source distance + weight is less than destination distance
                if dist[s] != float('inf') and dist[s] + w < dist[d]:
                    # set destination distance to source distance + weight
                    dist[d] = dist[s] + w

        # run the loop again to find if it has negative cycle
        for s, d, w in self.graph:
            # if the values are still changing 
            if dist[s] != float('inf') and dist[s] + w < dist[d]:
                # then graph has negative cycle
                print("Graph contains negative cycle")
                return

        self.printSolution(dist)
        # TC: bigO(EV), SC: bigO(V)

g = Graph(5)
g.addNode("A")
g.addNode("B")
g.addNode("C")
g.addNode("D")
g.addNode("E")
g.addEdge("A", "C", 6)
g.addEdge("A", "D", 6)
g.addEdge("B", "A", 3)
g.addEdge("C", "D", 1)
g.addEdge("D", "C", 2)
g.addEdge("D", "B", 1)
g.addEdge("E", "B", 4)
g.addEdge("E", "D", 2)

g.bellmanFord("E")
