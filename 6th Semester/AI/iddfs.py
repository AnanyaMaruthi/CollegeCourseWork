class Node:
    def __init__(self, current, previous=[]):
        self.current = current
        self.previous = previous


possibleMoves = {
    0: [1, 3],
    1: [0, 2, 4],
    2: [1, 5],
    3: [0, 4, 6],
    4: [1, 5, 7, 3],
    5: [2, 4, 8],
    6: [3, 7],
    7: [4, 6, 8],
    8: [5, 7]
}

def makeMove(sequence, i1, i2):
    sequence = list(sequence)
    sequence[i1], sequence[i2] = sequence[i2], sequence[i1]
    return "".join(sequence)

def getNextMoves(sequence):
    zeroIndex = sequence.index("0")
    moves = possibleMoves[zeroIndex]
    nextMoves = []
    for move in moves:
        nextMoves.append(makeMove(sequence, zeroIndex, move))
    return nextMoves

def checkGoal(sequence):
    if sequence == "123456780":
        return True
    return False

def dfs(node, depth):
    global nodeTraversed
    if depth <= 0:
        return False
    nodeTraversed += 1
    if checkGoal(node.current):
        print("Goal reached")
        print("Number of moves needed: ", len(node.previous))
        return True
    nextMoves = getNextMoves(node.current)
    for move in nextMoves:
        if move not in node.previous:
            nextNode = Node(move, node.previous + [node.current])
            if dfs(nextNode, depth - 1):
                return True
    return False

nodeTraversed = 0

def iddfs(sequence):
    global nodeTraversed
    depth = 1
    node = Node(sequence)
    while True:
        nodeTraversed = 0
        print("Depth: ", depth)
        if dfs(node, depth):
            print("Number of nodes traversed ", nodeTraversed)
            break
        else:
            depth += 1
    
def main():
    sequence = "314826057"
    iddfs(sequence)

main()