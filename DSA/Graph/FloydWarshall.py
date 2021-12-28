

INF = 9999

def printSolution(nV, distance):
    for i in range(nV):
        for j in range(nV):
            if distance[i][j] == INF:
                print("INF", end="  ")
            else:
                print(distance[i][j], end="   ")
        print(" ")

def floydWarshall(nV, G):
    # assigning distance var to Graph
    distance = G
    # running a loop through all the nodes in the graph
    for k in range(nV):
        # running a loop through the rows of the 2D array(graph)
        for i in range(nV):
            # running a loop through the columns of the 2D array(graph)
            for j in range(nV):
                distance[i][j] = min(distance[i][j], distance[i][k]+distance[k][j])

    printSolution(nV, distance)
    # TC: bigO(V^3), SC: bigO(V^2)

# graph in the form of adjacency matrix
G = [
    [0, 8, INF, 1],
    [INF, 0, 1, INF],
    [4, INF, 0, INF],
    [INF, 2, 9, 11],
    ]

floydWarshall(4, G)