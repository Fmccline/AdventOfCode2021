from aoc_day import AoCDay



class LanternFish:

    def __init__(self, state) -> None:
        self.state = state
        self.children = []

    def add_days(self, days):
        for _ in range(days):
            self.add_day()

    def add_day(self):
        self.state -= 1
        for child in self.children:
            child.add_day()
        if self.state < 0:
            self.children.append(LanternFish(8))
            self.state = 6

    def get_total_fish(self):
        total = 1
        for child in self.children:
            total += child.get_total_fish()
        return total


class AoCDay6(AoCDay):

    DAYS = 80

    def __init__(self) -> None:
        super().__init__(6)
        self.starting_fish = []

    def setup_data(self, data):
        for num in data[0].split(','):
            state = int(num)
            self.starting_fish.append(LanternFish(state))

    def solve_part_one(self):
        total = 0
        for fish in self.starting_fish:
            fish.add_days(self.DAYS)
            total += fish.get_total_fish()
        return total

    def solve_part_two(self):
        return None

    

