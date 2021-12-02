DAY_1_FILE = 'day1_input.txt'
test_data = [199,200,208,210,200,207,240,269,260,263]

def read_input(filename):
    data = []
    with open(filename, "r") as file:
        for line in file:
            data.append(int(line))
    return data

def count_inc_depths(depths):
    if len(depths) < 2:
        return 0

    last = depths[0]
    num = 0

    for depth in depths[1:]:
        if depth > last:
            num += 1
        last = depth
    return num

if __name__ == '__main__':
    testing = False
    depths = test_data
    if not testing:
        depths = read_input(DAY_1_FILE)

    print(count_inc_depths(depths))