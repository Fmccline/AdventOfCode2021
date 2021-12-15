from aoc_day import AoCDay


class Octopus:

    def __init__(self, row, col, state):
        self.state = state
        self.row = row
        self.col = col
        self.children = []
        self.has_flashed = False
    
    def add_children(self, matrix):
        row, col, = self.row, self.col
        if self.in_bounds(row + 1, col, matrix):
            self.children.append(matrix[row + 1][col])
        if self.in_bounds(row - 1, col, matrix):
            self.children.append(matrix[row - 1][col])
        if self.in_bounds(row, col + 1, matrix):
            self.children.append(matrix[row][col + 1])
        if self.in_bounds(row, col - 1, matrix):
            self.children.append(matrix[row][col - 1])
        if self.in_bounds(row + 1, col + 1, matrix):
            self.children.append(matrix[row + 1][col + 1])
        if self.in_bounds(row + 1, col - 1, matrix):
            self.children.append(matrix[row + 1][col - 1])
        if self.in_bounds(row - 1, col + 1, matrix):
            self.children.append(matrix[row - 1][col + 1])
        if self.in_bounds(row - 1, col - 1, matrix):
            self.children.append(matrix[row - 1][col - 1])

    def in_bounds(self, row, col, matrix):
        ROWS = len(matrix)
        COLS = len(matrix[0])
        return row >= 0 and row < ROWS and col >= 0 and col < COLS

    def add_one(self):
        self.has_flashed = False
        self.state += 1

    def get_flashes(self):
        flashes = 0
        state = self.state
        if state > 9:
            self.has_flashed = True
            flashes += 1
            for child in self.children:
                if not child.has_flashed:
                    child.add_one()
                    child_flashes = child.get_flashes()
                    flashes += child_flashes
            state = 0
        self.state = state
        return flashes



class AoCDay11(AoCDay):

    def __init__(self):
        super().__init__(11)
        self.octopi = []
        self.data = []

    def setup_data(self, data):
        self.data = data
        
    def setup_octopi(self):
        self.octopi = []
        matrix = []
        octo_matrix = []
        for line in self.data:
            row = [int(c) for c in line]
            matrix.append(row)
        for row in range(len(matrix)):
            octo_matrix.append([])
            for col in range(len(matrix[0])):
                octo = Octopus(row, col, matrix[row][col])
                octo_matrix[-1].append(octo)
                self.octopi.append(octo)

        for octo in self.octopi:
            octo.add_children(octo_matrix)

    def solve_part_one(self):
        self.setup_octopi()
        return self.get_flashes_after_100_steps()

    def solve_part_two(self):
        self.setup_octopi()
        return self.get_steps_to_all_flashing()

    def get_flashes_after_100_steps(self):
        flashes = 0
        for _ in range(100):
            flashers = []
            for octo in self.octopi:
                octo.add_one()
                if octo.state > 9:
                    flashers.append(octo)
            for octo in flashers:
                flashes += octo.get_flashes()
        return flashes

    def print(self):
        matrix = [[0 for _ in range(10)] for _ in range(10)]
        for octo in self.octopi:
            matrix[octo.row][octo.col] = octo.state
        for row in matrix:
            print(row)

    def get_steps_to_all_flashing(self):
        steps = 0
        while steps < 1000: # Arbitrary, could be while True
            flashes = 0
            flashers = []
            steps += 1
            for octo in self.octopi:
                octo.add_one()
                if octo.state > 9:
                    flashers.append(octo)
            for octo in flashers:
                flashes += octo.get_flashes()
            if flashes == 100:
                break
        return steps