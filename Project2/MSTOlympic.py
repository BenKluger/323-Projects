import sys # for INT_MAX
import pandas as pd
import numpy as np
print("hello minimum spanning tree")
# program for Prim's Minimum Spanning Tree (MST) algorithm
# program is for adjacency matrix representation of the graph
# geeksforgeeks.org/prims-minimum-spanning-tree-mst-greedy-algo-5/
class Graph():

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]

    def printMST(self, parent):
        print("Edge \t Weight")
        for i in range(1, self.V):
            print (parent[i], "-", i, "\t", self.graph[i][parent[i]])
    
    def minKey(self, key, mstSet):
        min = sys.maxint
        for v in range(self.V):
            if key[v] < min and mstSet[v] == False:
                min_index = v
        return min_index

    def primMST(self):
        key = [sys.maxint] * self.V
        parent = [None] * self.V
        key[0] = 0
        mstSet = [False] * self.V
        parent[0] = -1 

        for cout in range(self.V):
            u = self.minKey(key, mstSet)
            mstSet[u] = True
            for v in range(self.V):
                if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u


def insert(adj, u, v):
    adj[u].append(v)
    return

def printList(adj, V):
    for i in range(V):
        print(i, end = '')
        for j in adj[i]:
            print(' -->' + srt(j), end = '')
        
        print()
    print()

def convert(adj, V):
    matrix = [[0 for j in range(v)]
                 for i in range(V)]

    for i in range(V):
        for j in adj[i]:
            matrix[i][j] = 1
    
    return matrix

def printMatrix(adj, V):
    for i in range(V):
        for j in range(V):
            print(adj[i][j], end = ' ')

        print()
    
    print()
