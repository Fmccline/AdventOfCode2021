import argparse
day4 = __import__('4_day')


TEST_CASES = {
    4: (day4.AoCDay4(), (4512, 1924), (44088, 23670))
}


parser = argparse.ArgumentParser(description='Advent of Code main. Runs and tests solututions to each day.')
parser.add_argument('-d', '--day', type=int, help='the day to be run')
parser.add_argument('-t', '--is_test', action='store_true', help='if test input should be used')
parser.add_argument('-a', '--should_assert', action='store_true', help='if the solutions should be tested for correct output')

args = parser.parse_args()


day_num = args.day
is_test = args.is_test
should_assert = args.should_assert

days = [i for i in range(31)]
if day_num is not None:
    days = [day_num]

ASSERTION_IDX = 1 if is_test else 2
for day in days:
    if day in TEST_CASES.keys():
        aoc_day = TEST_CASES[day][0]
        part1, part2 = aoc_day.get_solutions(is_test)
        if should_assert:
            ans1, ans2 = TEST_CASES[day][ASSERTION_IDX]
            print(f'Day {day}')
            print(f'{part1 == ans1}: {part1} == {ans1} (Actual / Expected)')
    