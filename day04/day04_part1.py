class Bingo:
    def __init__(self) -> None:
        self.boards = self.construct_boards()
        self.input = self.get_puzzle_input()

    def get_puzzle_input(self) -> list[str]:
        with open("day04/input.txt", "r") as infile:
            lines = []
            for line in infile.readlines():
                new_line = line.rstrip("\n")
                lines += [int(line) for line in new_line.split(",")]
        return lines

    def construct_boards(self) -> dict[int, list[list[str]]]:
        with open("day04/boards.txt", "r") as infile:
            board_data = [line.rstrip("\n") for line in infile.readlines()]

        boards = {}

        blank_line_counter = 1
        for line in board_data:
            if line:
                line = line.rstrip()
                if not boards.get(blank_line_counter):
                    boards[blank_line_counter] = []
                tiles = line.split(",")
                if len(tiles) != 5:
                    print(f"Board {blank_line_counter} is malformed.")
                boards[blank_line_counter].append([int(tile) for tile in tiles])
            else:
                blank_line_counter += 1
        return boards

    def find_number_on_board(self, number: int) -> dict[int, list[int]]:
        boards_found = {}
        for board_number, board in self.boards.items():
            for i in range(5):
                for j in range(5):
                    if board[i][j] == number:
                        if not boards_found.get(board_number):
                            boards_found[board_number] = []
                        boards_found[board_number].append({"row": i, "column": j})

        return boards_found

    def scan_column(self, board: list[list[int]], board_number):
        column = []
        for i in range(5):
            for j in range(5):
                if board[j][i] == -1:
                    column.append(-1)
                    if len(column) == 5:
                        print(f"Board {board_number} has 5 in a column!")
                        return board
                else:
                    column = []

    def play(self):
        for bingo_number in self.input:
            results = self.find_number_on_board(bingo_number)
            for board_number, row_locations in results.items():
                for location in row_locations:
                    row_number = location["row"]
                    column_number = location["column"]
                    self.boards[board_number][row_number][column_number] = -1

                    if self.scan_column(self.boards[board_number], board_number):
                        print(f"Winning number: {bingo_number}")
                        print(f"Board {board_number} won!")
                        return {
                            "winning_number": bingo_number,
                            "board": self.boards[board_number],
                        }

                    if (
                        len(
                            [
                                tile
                                for tile in self.boards[board_number][row_number]
                                if tile == -1
                            ]
                        )
                        == 5
                    ):
                        print(f"Winning number: {bingo_number}")
                        print(
                            f"Board {board_number}, row {location['row'] + 1} got the bingo!"
                        )
                        return {
                            "winning_number": bingo_number,
                            "board": self.boards[board_number],
                        }


if __name__ == "__main__":
    b = Bingo()
    winning_board = b.play()
    print(winning_board)
    sum_of_tiles = 0
    for row in winning_board["board"]:
        for tile in row:
            if tile != -1:
                sum_of_tiles += int(tile)
    print(f"Answer: {sum_of_tiles * int(winning_board['winning_number'])}")
