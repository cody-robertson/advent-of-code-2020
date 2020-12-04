class TobogganTrajectory:
    def __init__(self, board: list[list[chr]]):
        self.board = board

    def trees_at_slope(self, x_right, y_down) -> int:
        return self.trees_at_slope_recurse(0, 0, x_right, y_down)

    def trees_at_slope_recurse(self, current_x, current_y, x_right, y_down) -> int:
        if current_y >= len(self.board):
            return 0
        else:
            tree: int = 1 if self.board[current_y][current_x % len(self.board[current_y])] == '#' else 0
            return tree + self.trees_at_slope_recurse(current_x + x_right, current_y + y_down, x_right, y_down)


if __name__ == "__main__":
    board_input: list[list[chr]] = []
    with open('input.txt') as input_file:
        for line in input_file:
            board_input.append(list(line.strip()))
    program = TobogganTrajectory(board_input)
    trees_found = 1
    for pair in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
        current_trees = program.trees_at_slope(pair[0], pair[1])
        trees_found *= current_trees
        print("Trees found at {} right and {} down: {}".format(pair[0], pair[1], current_trees))
    print("Result:", trees_found)
