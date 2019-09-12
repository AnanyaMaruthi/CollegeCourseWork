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
            self.matrix[end][start] = 1
            
    def bfs(self):
        visited = [0 for _ in range(self.vertices)]
        source = int(input("Enter source vertex"))
        vertexQueue = []
        vertexQueue.append(source)
        visited[source] = 1
        while (vertexQueue != []):
            currentVertex = vertexQueue.pop(0)
            print(currentVertex, end=" ")
            for i in range(self.vertices):
                    vertexQueue.append(i)
                    visited[i] = 1
        print()
        
vertices, edges = list(map(int, input("Enter the number of vertices and edges in the graph").split()))
graph = Graph(vertices, edges)
graph.bfs()
            
