import sys

class Graph: 
    def __init__(self, vertices):
        self.vertices = vertices
        # self.edges = edges
        self.matrix = [[0 for column in range(vertices)] for row in range(vertices)]
        # self.getMatrix()

    # def getMatrix(self):
    #     print("Enter edges:")
    #     for x in range(self.edges):
    #         start, end = list(map(int, input("Enter start and end vertex").split()))
    #         self.matrix[start][end] = 1
    #         self.matrix[end][start] = 1

    def getMSTCost(self, parent): 
        cost = 0
        # print("Edge \t Weight")
        for i in range(1, self.vertices): 
            # print (parent[i], "-", i, "\t", self.matrix[i][ parent[i] ] )
            cost += self.matrix[i][parent[i]]
        print("The cost is", cost)

    def minKey(self, key, mstSet):  
        min = 9999 
        for vertex in range(self.vertices):
            if key[vertex] < min and mstSet[vertex] == False:
                min = key[vertex] 
                min_index = vertex 
        return min_index 

    def primMST(self): 

        key = [9999] * self.vertices 
        parent = [None] * self.vertices
        key[0] = 0
        mstSet = [False] * self.vertices 
        cost = 0

        parent[0] = -1 

        for _ in range(self.vertices): 

            minVertex = self.minKey(key, mstSet) 
            mstSet[minVertex] = True
            for vertex in range(self.vertices):
                if self.matrix[minVertex][vertex] > 0 and mstSet[vertex] == False and key[vertex] > self.matrix[minVertex][vertex]: 
                        key[vertex] = self.matrix[minVertex][vertex] 
                        parent[vertex] = minVertex 

        self.getMSTCost(parent) 

g = Graph(6) 
g.matrix = [[0, 1, 2, 0, 0, 0],
            [1, 0, 0, 0, 0, 3],
            [2, 0, 0, 5, 8, 6],
            [0, 0, 5, 0, 6, 0],
            [0, 0, 8, 6, 0, 4],
            [0, 3, 0, 0, 4, 0]
]

g.primMST()

