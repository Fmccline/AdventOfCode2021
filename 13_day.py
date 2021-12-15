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
        fold_axis, origin = self.folds[0]

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
        return len(unique_points)

    def solve_part_two(self):
        return None