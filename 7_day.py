from aoc_day import AoCDay
import math

class AoCDay7(AoCDay):

    def __init__(self) -> None:
        super().__init__(7)
        self.positions = {}

    def setup_data(self, data):
        for str_num in data[0].split(','):
            num = int(str_num)
            if num not in self.positions.keys():
                self.positions[num] = 1
            else:
                self.positions[num] += 1

    def solve_part_one(self):
        return self.get_fuel(is_actual=False)

    def solve_part_two(self):
        return self.get_fuel(is_actual=True)

    def get_fuel(self, is_actual):
        if not is_actual:
            return self.get_fuel_expected_burn()
        else:
            return self.get_fuel_actual_burn()
            
    def get_fuel_expected_burn(self):
        min_fuel = None
        for start_pos in self.positions.keys():
            fuel = 0
            for pos, count in self.positions.items():
                if start_pos == pos:
                    continue
                fuel += abs(start_pos - pos)*count
            if min_fuel is None or min_fuel > fuel:
                min_fuel = fuel
        return min_fuel

    def get_fuel_actual_burn(self):
        sum_to_n = lambda n: (n+1)*n/2

        min_pos = min(self.positions.keys())
        max_pos = max(self.positions.keys())
        min_fuel = None
        min_fuel_pos = None
        for n in range(min_pos, max_pos):
            fuel = 0
            for pos, count in self.positions.items():
                fuel += sum_to_n(abs(pos - n))*count
            if min_fuel is None or min_fuel > fuel:
                min_fuel = fuel
                min_fuel_pos = n

        return min_fuel