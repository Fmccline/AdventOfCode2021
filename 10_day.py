from aoc_day import AoCDay


class AoCDay10(AoCDay):

    def __init__(self) -> None:
        super().__init__(10)
        self.lines = []

    def setup_data(self, data):
        self.lines = data

    def solve_part_one(self):
        return self.get_corrupted_score()

    def solve_part_two(self):
        return None

    def get_corrupted_score(self):
        SCORES = {')': 3, ']': 57, '}': 1197, '>': 25137}
        NESTS = {')': '(', ']': '[', '}': '{', '>': '<'}
        OPEN_CHARS = set(['(', '[', '{', '<'])
        opens = []
        score = 0
        for line in self.lines:
            for c in line:
                if c in OPEN_CHARS:
                    opens.append(c)
                else:
                    inv_c = opens.pop()
                    if NESTS[c] != inv_c:
                        score += SCORES[c]
                        break
        return score
                    