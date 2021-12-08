from aoc_day import AoCDay


class AoCDay5(AoCDay):

    def __init__(self) -> None:
        super().__init__(5)
        self.points = []
    
    def setup_data(self, data):
        for line in data:
            points = line.split(' -> ')
            if len(points) != 2:
                raise Exception("Error splitting line along ' -> '")
            x1, y1 = self.get_coords(points[0])
            x2, y2 = self.get_coords(points[1])
            if x1 == x2 or y1 == y2:
                self.points.append((x1,y1,x2,y2))
    
    def get_coords(self, point):
        coord = point.split(',')
        if len(coord) != 2:
            raise Exception(f"Error splitting coord along ',' got {len(coord)} wanted 2: {coord}")
        x = int(coord[0])
        y = int(coord[1])
        return x, y

    def solve_part_one(self):
        intercepts = 0
        grid = {}
        for x1, y1, x2, y2 in self.points:
            if y1 == y2:
                y = y1
                for x in range(min(x1, x2), max(x1, x2) + 1):
                    intercepts += self.get_intercepts(x, y, grid)
            else:
                x = x1
                for y in range(min(y1, y2), max(y1, y2) + 1):
                    intercepts += self.get_intercepts(x, y, grid)
        return intercepts

    def solve_part_two(self):
        return None

    def get_intercepts(self, x, y, grid):
        intercepts = 0
        if (x, y) in grid.keys():
            if grid[(x, y)] == 1:
                grid[(x, y)] = 2
                intercepts += 1
        else:
            grid[(x, y)] = 1
        return intercepts


