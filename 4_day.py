import util
INPUT_FILE = 'day4_input.txt'
TEST_INPUT_FILE = 'day4_test_input.txt'


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


def play_bingo(numbers, boards, is_trying):
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
    

def make_matrix_boards(data):
    data = data[2:]
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


def print_boards(boards):
    for board_idx in range(len(boards)):
        board = boards[board_idx]
        print(f'Board {board_idx}')
        for row in board:
            print(row)
        print()


def make_boards(data):
    matrix_boards = make_matrix_boards(data)
    boards = []
    for matrix_board in matrix_boards:
        board = Board(matrix_board)
        boards.append(board)

    return boards
    

if __name__ == '__main__':
    is_test = False
    input_file = TEST_INPUT_FILE if is_test else INPUT_FILE
    data = util.read_input(input_file)
    
    numbers = data[0].split(',')
    numbers = [int(number) for number in numbers]

    print(play_bingo(numbers, make_boards(data), True))
    print(play_bingo(numbers, make_boards(data), False))


