from typing import List
import util


class AoCDay:

    def __init__(self, day_num) -> None:
        self.day_num = day_num
        path = './input_files/'
        self.input_test_file = f'{path}day{day_num}_test_input.txt'
        self.input_file = f'{path}day{day_num}_input.txt'

    def get_solutions(self, is_test):
        input_file = self.input_test_file if is_test else self.input_file
        data = util.read_input(input_file)
        self.setup_data(data)
        part1 = self.solve_part_one()
        part2 = self.solve_part_two()
        return part1, part2

    def setup_data(self, data):
        pass

    def solve_part_one(self):
        return None

    def solve_part_two(self):
        return None