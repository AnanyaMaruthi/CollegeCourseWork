class Graph:
    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.edges = edges
        self.matrix = [[0 for _ in range(vertices)] for x in range(vertices)]
        self.getMatrix()
    
    def getMatrix(self):
        print("Enter edges:")
        for x in range(edges):
            start, end = list(map(int, input("Enter start and end vertex").split()))
            self.matrix[start][end] = 1
            #self.matrix[end][start] = 1
            
    def topologicalSort(self):
        indegree = [0 for _ in range(self.vertices)]
        for i in range(self.vertices):
            for j in range(self.vertices):
                indegree[i] += self.matrix[j][i]
                
        for i in range(self.vertices):
            for j in range(self.vertices):
                if indegree[j] == 0:
                    print(j, end = " ")
                    indegree[j] = -1
                    for k in range(self.vertices):
                        if self.matrix[j][k] == 1:
                            indegree[k] -= 1
                              
vertices, edges = list(map(int, input("Enter the number of vertices and edges").split()))
graph = Graph(vertices, edges)
graph.topologicalSort()
