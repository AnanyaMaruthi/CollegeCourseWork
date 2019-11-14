import sys

class Graph: 
    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.edges = edges
        self.matrix = [[sys.maxsize for column in range(vertices)] for row in range(vertices)]
        self.getMatrix()

    def getMatrix(self):
        print("Enter edges:")
        for x in range(self.edges):
            start, end, weight = list(map(int, input("Enter start and end vertex; and weights").split()))
            self.matrix[start][end] = weight
            self.matrix[end][start] = weight

    def getShortestPath(self, source):
        distances = [sys.maxsize for _ in range(self.vertices)]
        parents = [None for _ in range(self.vertices)]
        chosen = [False for _ in range(self.vertices)]

        for i in range(self.vertices):
            distances[i] = self.matrix[source][i]
            parents[i] = source

        distances[source] = 0
        chosen[source] = True
        vertexCount = 0

        while vertexCount != self.vertices:
            minDistance = sys.maxsize
            minVertex = source
            for vertex in range(self.vertices):
                if distances[vertex] < minDistance and chosen[vertex] == False:
                    minDistance = distances[vertex]
                    minVertex = vertex

            chosen[minVertex] = True
            vertexCount += 1
            for nextVertex in range(self.vertices):
                if (chosen[nextVertex] == False and minDistance + self.matrix[minVertex][nextVertex] < distances[nextVertex]):
                    distances[nextVertex] = minDistance + self.matrix[minVertex][nextVertex]
                    parents[nextVertex] = minVertex

        self.showMinPath(source, parents, distances)
        # print(distances)
        # print(parents)
        return parents, distances

    def showMinPath(self, source, parents, distances):
        for vertex in range(self.vertices):
            if vertex == source:
                continue
            print("Cost of vertex", vertex, "is", distances[vertex])
            path = []
            parent = parents[vertex]
            path.insert(0, vertex)
            path.insert(0, parent)
            while(parent != source):
                parent = parents[parent]
                path.insert(0, parent)
            print("The path is", path)

vertices, edges = map(int, input("Enter the vertices and edges").split())
graph = Graph(vertices, edges)
graph.getShortestPath(0)








