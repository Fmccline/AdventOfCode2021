from aoc_day import AoCDay


class AoCDay14(AoCDay):

    def __init__(self) -> None:
        super().__init__(14)
        self.rules = {}
        self.polymer = ''

    def setup_data(self, data):
        self.polymer = data[0]
        for line in data[2:]:
            line = line.split(' -> ')
            start = line[0]
            end = line[1]
            self.rules[start] = end

    def solve_part_one(self):
        steps = 10
        poly = self.polymer
        for _ in range(steps):
            curr_poly = poly[0]
            for poly_idx in range(len(poly) - 1):
                a = poly[poly_idx]
                b = poly[poly_idx + 1]
                p = self.rules[a + b]
                curr_poly += p + b
            poly = curr_poly

        min_occur = None
        max_occur = None
        occurences = {}
        for c in poly:
            if c not in occurences.keys():
                occurences[c] = 1
            else:
                occurences[c] += 1
        min_occur = sorted(occurences.values())[0]
        max_occur = sorted(occurences.values())[-1]
       
        return max_occur - min_occur


    def solve_part_two(self):
        return None