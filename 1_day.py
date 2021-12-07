from aoc_day import AoCDay 
DAY_1_FILE = 'day1_input.txt'
test_data = [199,200,208,210,200,207,240,269,260,263]


class AoCDay1(AoCDay):

    def __init__(self) -> None:
        super().__init__(1)
        self.depths = []

    def setup_data(self, data):
        for str_num in data:
            self.depths.append(int(str_num))

    def solve_part_one(self):
        return self.count_inc_depths()

    def solve_part_two(self):
        return self.sliding_window_depths()

    # Part 1
    def count_inc_depths(self):
        depths = self.depths
        if len(depths) < 2:
            return 0

        last = depths[0]
        num = 0

        for depth in depths[1:]:
            if depth > last:
                num += 1
            last = depth
        return num

    # Part 2
    def sliding_window_depths(self):
        depths = self.depths
        if len(depths) < 2:
            return 0
        
        inc = 0
        for idx in range(0, len(depths) - 3):
            curr = depths[idx]
            next = depths[idx + 3]
            if curr < next:
                inc += 1
        return inc
