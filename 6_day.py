from aoc_day import AoCDay


class FishStates:

    def __init__(self, starting_fish):
        self.states = [0 for _ in range(9)]
        for fish_num in starting_fish:
            self.states[fish_num] += 1

    def add_days(self, days):
        for _ in range(days):
            self.add_day()

    def add_day(self):
        for idx in range(len(self.states) - 1):
            self.states[idx], self.states[idx+1] = self.states[idx+1], self.states[idx]
        self.states[6] += self.states[8]

    def get_total(self):
        total = 0
        for state in self.states:
            total += state
        return total


class AoCDay6(AoCDay):

    def __init__(self) -> None:
        super().__init__(6)
        self.starting_fish = []

    def setup_data(self, data):
        for num in data[0].split(','):
            state = int(num)
            self.starting_fish.append(state)

    def solve_part_one(self):
        DAYS = 80
        fish_states = FishStates(self.starting_fish)
        fish_states.add_days(DAYS)
        total = fish_states.get_total()
        return total

    def solve_part_two(self):
        DAYS = 256
        fish_states = FishStates(self.starting_fish)
        fish_states.add_days(DAYS)
        total = fish_states.get_total()
        return total
    

