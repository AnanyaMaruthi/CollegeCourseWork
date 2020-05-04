class Node:
    def __init__(self, parent, board, cost):
        super().__init__()
        self.board = board
        self.parent = parent
        self.g = cost
        self.h = 0
        self.f = self.h + self.g

    def __str__(self):
        return self.board

    def __eq__(self, value):
        if not isinstance(value, Node) or self.board != value.board:
            # don't attempt to compare against unrelated types
            return False
        return True

    def print_steps(self):
        node = self
        while node is not None:
            print(node.board)
            node = node.parent

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
        return self.calculate_manhattan_distance() + (
            2 * self.calculate_linear_conflict()
        )

    def calculate_manhattan_distance(self):
        distance = 0
        for index in range(9):
            value = self.board[index]
            if value == "0":
                continue

            row = index // 3
            column = index % 3

            goal_row, goal_column = self.get_goal_coordinate(value)

            distance += abs(row - goal_row) + abs(column - goal_column)

    def calculate_linear_conflict(self):
        conflicts = 0
        index = 0
        pairs = 0
        while pairs != 4:
            value = self.board[index]
            if value == "0":
                index += 1
                continue

            goal_index = self.get_goal_index(value)

            if goal_index != index:
                expected_value = self.board.index(goal_index)
                expected_value_goal_index = self.get_goal_index(expected_value)

                if expected_value_goal_index == index:
                    conflicts += 1

            index += 1
            pairs += 1

        return conflicts

    def get_goal_coordinate(self, value):
        goal_index = self.get_goal_index(value)
        goal_row = goal_index // 3
        goal_column = goal_index % 3

        return (goal_row, goal_column)

    def get_goal_index(self, value):
        return "123456780".index(value)


def AStar():
    start = Node(None, "123046758", 0)
    open_list = {0: [start]}
    closed_list = []

    while len(open_list) != 0:
        move = get_closest_node(open_list, closed_list)

        if move is None:
            print("No Solution")
        else:
            possible_moves = move.get_possible_moves()
            for possible_move in possible_moves:
                if possible_move == "123456780":
                    print(possible_move)
                    move.print_steps()
                    return

                if possible_move not in closed_list:
                    possible_move_node = Node(move, possible_move, move.g + 1)
                    f = possible_move_node.f

                    if f in open_list.keys():
                        found = False
                        for i in range(len(open_list[f])):
                            node = open_list[f][i]
                            if node.board == possible_move:
                                found = True
                                if node.f > possible_move_node.f:
                                    open_list[f].pop(i)
                                    open_list[f].append(possible_move_node)
                        if not found:
                            open_list[f].append(possible_move_node)
                    else:
                        open_list[f] = [possible_move_node]


def get_closest_node(open_list, closed_list):
    f = min(open_list.keys())

    possible_moves = open_list[f]
    possible_move = possible_moves.pop()
    closed_list.append(possible_move.board)

    if len(possible_moves) == 0:
        open_list.pop(f)

    return possible_move


if __name__ == "__main__":
    AStar()
