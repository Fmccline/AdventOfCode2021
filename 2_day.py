import util 

INPUT_FILE = 'day2_input.txt'
HORIZONTAL = 0
DEPTH = 1
AIM = 2
COMMANDS = {'forward': (HORIZONTAL, 1), 'down': (DEPTH, 1), 'up': (DEPTH, -1)}
TEST = ['forward 5','down 5','forward 8','up 3','down 8','forward 2']


def normalize_commands(str_commands):
    normalized = []
    for str_command in str_commands:
        commands = str_command.split(' ')
        command = commands[0]
        value = int(commands[1])
        normalized.append((command, value))
    return normalized


# Part 1
def get_position(commands):
    pos = [0, 0] # [h_pos, d_pos] where h is horizontal and d is depth
    for command, value in commands:
        pos_idx = COMMANDS[command][0]
        pos_change = value*COMMANDS[command][1]
        pos[pos_idx] += pos_change
    return pos[0]*pos[1]


# Part 2
def get_position_with_aim(commands):
    pos = [0, 0, 0] # [h_pos, d_pos, aim] where h is horizontal, d is depth, and aim is aim
    for command, value in commands:
        pos_idx = COMMANDS[command][0]
        if pos_idx == HORIZONTAL:
            pos[HORIZONTAL] += value
            pos[DEPTH] += value*pos[AIM]
        else:
            pos_change = value*COMMANDS[command][1]
            pos[AIM] += pos_change
    return pos[0]*pos[1]


if __name__ == '__main__':
    is_part_1 = False
    is_test = False
    str_commands = TEST
    if not is_test:
        str_commands = util.read_input(INPUT_FILE)
    
    commands = normalize_commands(str_commands)
    if is_part_1:
        print(get_position(commands))
    else:
        print(get_position_with_aim(commands))