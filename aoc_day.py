from typing import List
import util


class AoCDay:

    def __init__(self, day_num) -> None:
        self.day_num = day_num
        self.input_test_file = f'day{day_num}_test_input.txt'
        self.input_file = f'day{day_num}_input.txt'

    def get_solutions(self, is_test):
        input_file = self.input_test_file if is_test else self.input_file
        data = util.read_input(input_file)
        data = self.setup_data(data)
        part1 = self.solve_part_one(data)
        part2 = self.solve_part_two(data)
        return part1, part2

    def setup_data(self, data) -> List:
        return data

    def solve_part_one(self, data) -> None:
        return None

    def solve_part_two(self, data) -> None:
        return None