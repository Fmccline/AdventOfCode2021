from aoc_day import AoCDay


class AoCDay2(AoCDay):

    HORIZONTAL = 0
    DEPTH = 1
    AIM = 2
    COMMANDS = {'forward': (HORIZONTAL, 1), 'down': (DEPTH, 1), 'up': (DEPTH, -1)}

    def __init__(self) -> None:
        super().__init__(2)
        self.commands = []
    
    def setup_data(self, data):
        normalized = []
        for str_command in data:
            commands = str_command.split(' ')
            command = commands[0]
            value = int(commands[1])
            normalized.append((command, value))
        self.commands = normalized
        return normalized

    def solve_part_one(self, data):
        return self.get_position()

    def solve_part_two(self, data):
        return self.get_position_with_aim()

    def get_position(self):
        pos = [0, 0] # [h_pos, d_pos] where h is horizontal and d is depth
        for command, value in self.commands:
            pos_idx = self.COMMANDS[command][0]
            pos_change = value*self.COMMANDS[command][1]
            pos[pos_idx] += pos_change
        return pos[0]*pos[1]

    def get_position_with_aim(self):
        pos = [0, 0, 0] # [h_pos, d_pos, aim] where h is horizontal, d is depth, and aim is aim
        for command, value in self.commands:
            pos_idx = self.COMMANDS[command][0]
            if pos_idx == self.HORIZONTAL:
                pos[self.HORIZONTAL] += value
                pos[self.DEPTH] += value*pos[self.AIM]
            else:
                pos_change = value*self.COMMANDS[command][1]
                pos[self.AIM] += pos_change
        return pos[0]*pos[1]
