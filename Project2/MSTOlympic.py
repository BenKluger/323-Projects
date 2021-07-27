import sys # for INT_MAX
print("hello minimum spanning tree")

class Graph():

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertice)]

    def printMST(self, parent):
        print("Edge \t Weight")
        for i in range(1, self.V):
            print parent[i], "-", i, "\t", self.graph[i][parent[i]]

