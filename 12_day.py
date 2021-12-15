from typing import Tuple
from aoc_day import AoCDay

class Cave:

    def __init__(self, label) -> None:
        self.label = label
        self.edges = []

    def add_edge(self, edge):
        self.edges.append(edge)

    def is_big(self):
        return str.isupper(self.label[0])

    def get_paths_to_end(self, curr_path, all_paths=set()):
        if self.label == 'end':
            curr_path = (*curr_path, 'end')
            all_paths.add(curr_path)
            return all_paths

        for edge in self.edges:
            if curr_path and edge.label == curr_path[-1]:
                continue
            if edge.label in curr_path and not edge.is_big():
                continue
            edge.get_paths_to_end((*curr_path, edge.label), all_paths)
        return all_paths


class AoCDay12(AoCDay):

    def __init__(self) -> None:
        super().__init__(12)
        self.caves = {}

    def setup_data(self, data):
        for line in data:
            caves = []
            labels = line.split('-')
            for label in labels:
                if label not in self.caves.keys():
                    self.caves[label] = Cave(label)
                cave = self.caves[label]
                caves.append(cave)
            caves[0].add_edge(caves[1])
            caves[1].add_edge(caves[0])

    def solve_part_one(self):
        all_paths = self.caves['start'].get_paths_to_end(('start',))
        return len(all_paths)

    def solve_part_two(self):
        return None
