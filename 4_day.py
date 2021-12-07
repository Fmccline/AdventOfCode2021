from aoc_day import AoCDay

class Board:

    def __init__(self, matrix):
        self.baord = {}
        self.rows = [len(matrix) for _ in range(len(matrix))]
        self.cols = [len(matrix[0]) for _ in range(len(matrix[0]))]
        self.sum = 0
        self.is_winner = False
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                num = matrix[row][col]
                self.baord[num] = (row, col)
                self.sum += num

    def add_bingo_num(self, num):
        if num in self.baord.keys():
            self.sum -= num
            row, col = self.baord[num]
            self.rows[row] -= 1
            self.cols[col] -= 1
            self.is_winner = self.rows[row] == 0 or self.cols[col] == 0

    def get_sum(self):
        return self.sum

    def has_won(self):
        return self.is_winner
   


class AoCDay4(AoCDay):

    def __init__(self) -> None:
        super().__init__(4)
        self.numbers = []

    def solve_part_one(self, data):
        score = self.play_bingo(data, True)
        return score

    def solve_part_two(self, data):
        score = self.play_bingo(data, False)
        return score

    def setup_data(self, data):
        numbers = data[0].split(',')
        self.numbers = [int(number) for number in numbers]
        return data[2:]

    def play_bingo(self, data, is_trying):
        boards = self.make_boards(data)
        numbers = self.numbers
        winning_score = -1
        won_boards = set()
        for number in numbers:
            for board in boards:
                if board in won_boards:
                    continue

                board.add_bingo_num(number)
                if board.has_won():
                    board_score = board.get_sum()*number
                    if is_trying and board_score > winning_score:
                        winning_score = board_score
                    elif not is_trying:
                        winning_score = board_score
                    won_boards.add(board)
                    
            if is_trying and winning_score > 0:
                break

        return winning_score

    def make_matrix_boards(self, data):
        boards = []
        board = []
        for line in data:
            if len(line) <= 1:
                boards.append(board)
                board = []
                continue
            board.append([])
            row = line.strip().replace("  ", " ").split(' ')
            for col in row:
                board[-1].append(int(col))
        boards.append(board)
        return boards

    def make_boards(self, data):
        matrix_boards = self.make_matrix_boards(data)
        boards = []
        for matrix_board in matrix_boards:
            board = Board(matrix_board)
            boards.append(board)

        return boards

