
class DistjointSet:
    def __init__(self, vertices):
        self.vertices = vertices
        self.parent = {}
        for v in vertices:
            self.parent[v] = v

        self.rank = dict.fromkeys(vertices, 0)
        # TC: bigO(n), SC: bigO(n)

    def find(self, item):
        if self.parent[item] == item:
            return item

        return self.find(self.parent[item])
        #TC: bigO(1)

    def union(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)
        
        if self.rank[xroot] < self.rank[yroot]:
            self.parent[xroot] = yroot
        elif self.rank[xroot] > self.rank[yroot]:
            self.parent[yroot] = xroot
        else:
            self.parent[yroot] = xroot
            self.rank[xroot] += 1
        # TC: bigO(1)

if __name__ == '__main__':
    vertices = ["A", "B", "C", "D", "E"]

    ds = DistjointSet(vertices)
    ds.union("A", "E")
    print(ds.find("E"))
            