import sys

def howManyVertices(fileName):
    amountOfV = 0
    with open(fileName) as f:
        for line in f: 
            amountOfV += 1
    return amountOfV


def makeAdjacencyMatrix(fileName):
    

    #INF = float('inf')

    
    vertices = 0
    with open(fileName) as f:
        for line in f: 
            vertices += 1 #this tells you how many vertices you have

    rows, cols = (vertices, vertices)
    graph = [[INF for i in range(cols)] for j in range(rows)]
    #print(graph)

    #graph = [vertices][vertices] 
    with open(fileName) as f:
        ## Ignore header
        #f.readline()

        # Let's consider `line` equals to '2 : 1 2, 3 14, 4 5, 5 4'
        #split returns two items, a string and list, from_vertex would be the string and remaining_line is the list
        #go thru the file twice, first to find how many lines (rows - assume starts at 0) (how many vertices) make them inf/0 depending on code


        for line in f:
            # from_vertex: '2', remaining_line: '1 2, 3 14, 4 5, 5 4'
            # convert to int
            from_vertex, remaining_line = line.strip().split(" : ")

            # remaining_tokens: ['1 2', '3 14', '4 5', '5 4']
            remaining_tokens = remaining_line.split(", ")

            # remaning_values: [['1', '2'], ['3', '14'], ['4', '5'], ['5', '4']]
            remaining_values = [value.split(" ") for value in remaining_tokens]

            # to_vertex: '1', weight: '2'
            # to_vertex: '3', weight: '14'
            # to_vertex: '4', weight: '5'
            # to_vertex: '5', weight: '4'
            for to_vertex, weight in remaining_values:
                #print(from_vertex, to_vertex, weight)
                #Add to graph, replace INF (Convert to int() first)
                fromV, toV = int(from_vertex), int(to_vertex)
                if fromV >= vertices or toV >= vertices:
                    print("FromV or ToV is out of range", fromV, toV)
                    exit                    
                graph[int(from_vertex)][int(to_vertex)] = int(weight) #fixed this code so that weight is an int
    
    #print(graph)
    return graph




'''KRUSKALS ALGO SECTION'''

# Python implementation for Kruskal's
# algorithm
 
# Find set of vertex i
def find(i):
    while parent[i] != i:
        i = parent[i]
    return i
 
# Does union of i and j. It returns
# false if i and j are already in same
# set.
def union(i, j):
    a = find(i)
    b = find(j)
    parent[a] = b
 
# Find MST using Kruskal's algorithm
def kruskalMST(cost):
    mincost = 0 # Cost of min MST
 
    # Initialize sets of disjoint sets
    for i in range(V):
        parent[i] = i
 
    # Include minimum weight edges one by one
    edge_count = 0
    while edge_count < V - 1:
        min = INF
        a = -1
        b = -1
        for i in range(V):
            for j in range(V):
                if find(i) != find(j) and cost[i][j] < min:
                    min = cost[i][j]
                    a = i
                    b = j
        union(a, b)
        print('Edge {}:({}, {}) cost:{}'.format(edge_count, a, b, min))
        edge_count += 1
        mincost += min
 
    print("Minimum cost= {}".format(mincost))



# Prim's Algorithm
class Graph():
 
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                    for row in range(vertices)]
 
    # A utility function to print the constructed MST stored in parent[]
    def printMST(self, parent):
        print ("Edge \tWeight")
        for i in range(1, self.V):
            print (parent[i], "-", i, "\t", self.graph[i][ parent[i]])
 
    # A utility function to find the vertex with
    # minimum distance value, from the set of vertices
    # not yet included in shortest path tree
    def minKey(self, key, mstSet):
 
        # Initialize min value
        min = sys.maxsize
 
        for v in range(self.V):
            if key[v] < min and mstSet[v] == False:
                min = key[v]
                min_index = v
 
        return min_index
 
    # Function to construct and print MST for a graph
    # represented using adjacency matrix representation
    def primMST(self):
 
        # Key values used to pick minimum weight edge in cut
        key = [sys.maxsize] * self.V
        parent = [None] * self.V # Array to store constructed MST
        # Make key 0 so that this vertex is picked as first vertex
        key[0] = 0
        mstSet = [False] * self.V
 
        parent[0] = -1 # First node is always the root of
 
        for cout in range(self.V):
 
            # Pick the minimum distance vertex from
            # the set of vertices not yet processed.
            # u is always equal to src in first iteration
            u = self.minKey(key, mstSet)
 
            # Put the minimum distance vertex in
            # the shortest path tree
            mstSet[u] = True
 
            # Update dist value of the adjacent vertices
            # of the picked vertex only if the current
            # distance is greater than new distance and
            # the vertex in not in the shotest path tree
            for v in range(self.V):
 
                # graph[u][v] is non zero only for adjacent vertices of m
                # mstSet[v] is false for vertices not yet included in MST
                # Update the key only if graph[u][v] is smaller than key[v]
                if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]:
                        key[v] = self.graph[u][v]
                        parent[v] = u
 
        self.printMST(parent)


vertexCount = howManyVertices('real_input.txt')

'''DRIVER CODE FOR KRUSKALS'''
print("\nThis is Kruskal's Algorithm section\n")
V = vertexCount
parent = [i for i in range(V)]
INF = float('inf')
matrix = makeAdjacencyMatrix('real_input.txt')

# Print the solution
kruskalMST(matrix)


'''DRIVER CODE FOR PRIMS'''
'''Prim's Algo driver code section'''
print("\nThis is Prim's algorithm section\n")
matrixTwo = makeAdjacencyMatrix('real_input.txt')
#print(matrixTwo)
someGraph = Graph(vertexCount)
someGraph.graph = matrixTwo
someGraph.primMST()