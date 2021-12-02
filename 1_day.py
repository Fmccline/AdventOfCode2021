import util
DAY_1_FILE = 'day1_input.txt'
test_data = [199,200,208,210,200,207,240,269,260,263]

# Part 1
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


# Part 2
def sliding_window_depths(depths):
    if len(depths) < 2:
        return 0
    
    inc = 0
    for idx in range(0, len(depths) - 3):
        curr = depths[idx]
        next = depths[idx + 3]
        if curr < next:
            inc += 1
    return inc


if __name__ == '__main__':
    testing = False
    depths = test_data
    if not testing:
        depths = util.read_input(DAY_1_FILE)
        for idx in range(len(depths)):
            depths[idx] = int(depths[idx])

    print(sliding_window_depths(depths))