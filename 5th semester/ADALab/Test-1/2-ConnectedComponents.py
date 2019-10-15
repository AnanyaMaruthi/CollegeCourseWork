# Using DFS/BFS, given an undirected graph, print all connected components line by line.
class Graph:
    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.edges = edges
        self.matrix = [[0 for _ in range(vertices)] for x in range(vertices)]
        self.getMatrix()

    def getMatrix(self):
        for i in range(self.edges):
            start, end = map(int, input("Enter start and end vertex: ").split())
            self.matrix[start][end] = 1
            self.matrix[end][start] = 1

    def getConnectedComponents(self):
        visited = [False for _ in range(self.vertices)]
        print(visited)
        print("The connected components are: ")
        for vertex in range(self.vertices):
            if visited[vertex] == False:
                print()
                self.dfs(vertex, visited)

    def dfs(self, vertex, visited):
        print(vertex, end=" ")
        visited[vertex] = True
        for i in range(self.vertices):
            if visited[i] == False:
                if self.matrix[vertex][i] == 1:
                    self.dfs(i, visited)

vertices, edges = map(int, input("Enter the number of vertices and edges: ").split())
# print(vertices)
# print(edges)
graph = Graph(vertices, edges)
graph.getConnectedComponents()
