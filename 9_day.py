from aoc_day import AoCDay 


class AoCDay9(AoCDay):

    def __init__(self) -> None:
        super().__init__(9)
        self.height_map = []
        self.basins = []
        self.MAX_ROW = 0
        self.MAX_COL = 0

    def setup_data(self, data):
        for line in data:
            row = [int(c) for c in line]
            basin_row = [False for _ in range(len(line))]
            self.height_map.append(row)
            self.basins.append(basin_row)
        self.MAX_ROW = len(self.height_map)
        self.MAX_COL = len(self.height_map[0])

    def solve_part_one(self):
        return self.get_total_risk_rating()

    def solve_part_two(self):
        return self.get_largest_basins()
    
    def get_total_risk_rating(self):
        risk = 0
        for row in range(self.MAX_ROW):
            for col in range(self.MAX_COL):
                if self.is_low_point(row, col):
                    risk += self.height_map[row][col] + 1
        return risk

    def is_low_point(self, row, col):
        height = self.height_map[row][col]
        higher = lambda row, col: self.is_higher_point(row, col, height)
        return higher(row, col + 1) and higher(row, col - 1) and higher(row + 1, col) and higher(row - 1, col)
        
    def is_higher_point(self, row, col, height):
        if self.in_bounds(row, col):
            return self.height_map[row][col] > height
        else:
            return True

    def in_bounds(self, row, col):
        return row >= 0 and row < self.MAX_ROW and col >= 0 and col < self.MAX_COL

    def get_largest_basins(self):
        b1 = 0
        b2 = 0
        b3 = 0
        for row in range(self.MAX_ROW):
            for col in range(self.MAX_COL):
                if self.is_low_point(row, col):
                    basin = self.get_basin_size(row, col, -1)
                    if basin > b1:
                        b1, b2, b3 = basin, b1, b2
                    elif basin > b2:
                        b2, b3 = basin, b2
                    elif basin > b3:
                        b3 = basin
        return b1*b2*b3

    def get_basin_size(self, row, col, prev_height):
        if not self.in_bounds(row, col) or self.basins[row][col] is True or self.height_map[row][col] == 9:
            return 0

        basin_size = 0
        height = self.height_map[row][col]
        if height > prev_height:
            self.basins[row][col] = True
            basin_size += 1
            basin_size += self.get_basin_size(row + 1, col, height)
            basin_size += self.get_basin_size(row - 1, col, height)
            basin_size += self.get_basin_size(row, col + 1, height)
            basin_size += self.get_basin_size(row, col - 1, height)
        
        return basin_size
