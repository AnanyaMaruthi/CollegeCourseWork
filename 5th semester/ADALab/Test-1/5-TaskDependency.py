# Using Topological Sorting, find the ordering of tasks from given dependencies

class Graph:
    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.edges = edges
        self.matrix = [[0 for _ in range(vertices)] for x in range(vertices)]
        self.getMatrix()

    def getMatrix(self):
        for i in range(self.edges):
            start, end = map(int, input("Enter pair").split())
            self.matrix[end][start] = 1

    def getIndegree(self):
        indegree = [0 for _ in range(self.vertices)]
        for i in range(self.vertices):
            for j in range(self.vertices):
                indegree[j] += self.matrix[i][j]
        return indegree

    def getOrdering(self):
        indegree = self.getIndegree()
        order = []
        flag = False #Becomes true if we find indegree 0
        # To make sure all vertices are covered
        for i in range(self.vertices):
            flag = False
            # To find indegree 0
            for j in range(self.vertices):
                if indegree[j] == 0:
                    indegree[j] = -1
                    flag = True
                    order.append(j)
                    # Remove all edges from this vertex
                    for k in range(self.vertices):
                        if self.matrix[j][k] == 1:
                            indegree[k] -= 1
                    break
            if flag == False:
                print("No such order exists")
                return

        print("The order is: ")
        for x in order:
            print(x, end = " ")

vertices, edges = map(int, input("Enter number of tasks and dependency pairs: ").split())
graph = Graph(vertices, edges)
graph.getOrdering()