class Node:
    def __init__(self, board, parent, g):
        self.board = board
        self.parent = parent
        self.g = g
        self.h = self.calculate_heuristic()
        self.f = self.g + self.h

    def __str__(self):
        return self.board

    def __eq__(self, value):
        if not isinstance(value, Node) or self.board != value.board:
            # don't attempt to compare against unrelated types
            return False
        return True
    
    def make_move(self, i1, i2):
        sequence_list = list(self.board)
        sequence_list[i1], sequence_list[i2] = sequence_list[i2], sequence_list[i1]
        return "".join(sequence_list)

    def get_possible_moves(self):
        possible_moves_list = {
            0: [1, 3],
            1: [0, 2, 4],
            2: [1, 5],
            3: [0, 4, 6],
            4: [1, 3, 5, 7],
            5: [2, 4, 8],
            6: [3, 7],
            7: [4, 6, 8],
            8: [5, 7],
        }

        zero_index = self.board.index("0")
        moves = possible_moves_list[zero_index]
        results = []

        for move in moves:
            results.append(self.make_move(zero_index, move))

        return results

    def calculate_heuristic(self):
        goal = "123456780"
        distance = 0
        for i in range(9):
            if self.board[i] != goal[i] and self.board[i] != 0:
                distance += 1
        return distance

def aStar(startSequence):
    openList = []
    closeList = []
    start = Node(startSequence, None, 0)

    openList.append(start)

    while True:
        openList.sort(key = lambda x:x.f)
        currentNode = openList.pop(0)
        print(currentNode)
        if currentNode.h == 0:
            print("Goal reached")
            return
        nextMoves = currentNode.get_possible_moves()
        for nextMove in nextMoves:
            if nextMove not in closeList:
                nextMoveNode = Node(nextMove, currentNode, currentNode.g + 1)
                if not findInOpenList(openList, nextMoveNode):
                    openList.append(nextMoveNode)
        closeList.append(currentNode)

    print("No solution")

def findInOpenList(openList, node):
    for index, value in enumerate(openList):
        if value.board == node.board:
            if value.f > node.f:
                del openList[index]
                openList.append(node)
                return True
    return False

aStar("123046758")

        

        
