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
            
    def DFS(self):
        visited = [0 for _ in range(self.vertices)]
        for vertex in range(self.vertices):
            if(visited[vertex] == 0):
                print()
                self.dfs(vertex, visited)
                
    def dfs(self, vertex, visited):
        print(vertex, end=" ")
        visited[vertex] = 1
        for i in range(self.vertices):
            #Check if it is an adjacent vertex
            if(self.matrix[vertex][i] == 1):
                if(visited[i] == 0):
                    self.dfs(i, visited)
                    
                    
                    
vertices, edges = list(map(int, input("Enter the number of vertices and edges in the graph").split()))
graph = Graph(vertices, edges)
graph.DFS()

            
        
            
        
