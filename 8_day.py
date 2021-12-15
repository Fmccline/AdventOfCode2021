from aoc_day import AoCDay
import util


class AoCDay8(AoCDay):

    # Num segments
    # 0: 6
    # 1: 2
    # 2: 5
    # 3: 5
    # 4: 4
    # 5: 5
    # 6: 6
    # 7: 3
    # 8: 7
    # 9: 6

    def __init__(self) -> None:
        super().__init__(8)
        self.digit_entries = []

    def setup_data(self, data):
        for line in data:
            line = line.split(' | ')
            _in = line[0].split(' ')
            _out = line[1].split(' ')
            self.digit_entries.append((_in,_out))

    def solve_part_one(self):
        uniques = 0
        is_unique = lambda l: True if len(l) in [2, 3, 4, 7] else False
        for _, output in self.digit_entries:
            for digit in output:
                if is_unique(digit):
                    uniques += 1
        return uniques

    def solve_part_two(self):
        return None