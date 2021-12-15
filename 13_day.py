from aoc_day import AoCDay


class AoCDay13(AoCDay):

    def __init__(self) -> None:
        super().__init__(13)
        self.points = []
        self.folds = []

    def setup_data(self, data):
        for line in data:
            if ',' in line:
                line = line.split(',')
                x = int(line[0])
                y = int(line[1])
                self.points.append((x, y))
            elif line == '':
                continue
            else:
                line = line.split(' ')[2].split('=')
                axis = line[0]
                num = line[1]
                self.folds.append((axis, int(num)))
        self.points = sorted(self.points)

    def solve_part_one(self):
        points = self.get_points_after_folds(self.folds[:1])
        return len(points)

    def solve_part_two(self):
        points = self.get_points_after_folds(self.folds)
        MAX_X = max(points, key=lambda p: p[0])[0]
        MAX_Y = max(points, key=lambda p: p[1])[1]
        grid = []
        for _ in range(0, MAX_Y + 1):
            row = []
            for _ in range(0, MAX_X + 1):
                row.append(' ')
            grid.append(row)
        for x, y in points:
            grid[y][x] = '*'
        as_str = ''
        for row in reversed(grid):
            row_str = ''.join(reversed(row))
            as_str += row_str + '\n'
        return as_str
        
    def get_points_after_folds(self, folds):
        for fold_axis, origin in folds:
            for point_idx in range(len(self.points)):
                x, y = self.points[point_idx]
                if fold_axis == 'x':
                    if x < origin:
                        x += 2*(origin - x) - origin - 1
                    else:
                        x -= origin + 1
                else:
                    if y < origin:
                        y += 2*(origin - y) - origin - 1
                    else:
                        y -= origin + 1
                self.points[point_idx] = (x, y)

        unique_points = set()
        for point in self.points:
            unique_points.add(point)
        return unique_points
