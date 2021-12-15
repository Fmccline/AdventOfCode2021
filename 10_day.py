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
        return self.get_auto_complete_score()

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

    def get_auto_complete_score(self):
        SCORES = {')': 1, ']': 2, '}': 3, '>': 4}
        OPEN_CHARS = set(['(', '[', '{', '<'])
        CLOSE_TO_OPEN = {')': '(', ']': '[', '}': '{', '>': '<'}
        OPEN_TO_CLOSE = {}
        for key, value in CLOSE_TO_OPEN.items():
            OPEN_TO_CLOSE[value] = key
        scores = []

        for line in self.lines:
            opens = []
            is_corrupt = False
            for c in line:
                if c in OPEN_CHARS:
                    opens.append(c)
                else:
                    inv_c = opens.pop()
                    if CLOSE_TO_OPEN[c] != inv_c:
                        is_corrupt = True
                        break
            if not is_corrupt:
                score = 0
                while opens:
                    c = opens.pop()
                    inv_c = OPEN_TO_CLOSE[c]
                    score = score*5 + SCORES[inv_c]
                scores.append(score)

        # return middle score
        return sorted(scores)[int(len(scores)/2)]
