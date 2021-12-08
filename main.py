import argparse
day1 = __import__('1_day')
day2 = __import__('2_day')
day3 = __import__('3_day')
day4 = __import__('4_day')
day5 = __import__('5_day')


TEST_CASES = {
    1: (day1.AoCDay1(), (7, 5), (1400, 1429)),
    2: (day2.AoCDay2(), (150, 900), (2117664, 2073416724)),
    3: (day3.AoCDay3(), (198, 230), (3959450, 7440311)),
    4: (day4.AoCDay4(), (4512, 1924), (44088, 23670)),
    5: (day5.AoCDay5(), (5, 12), (4421, -1))
}


parser = argparse.ArgumentParser(description='Advent of Code main. Runs and tests solututions to each day.')
parser.add_argument('-d', '--day', type=int, help='the day to be run')
parser.add_argument('-t', '--is_test', action='store_true', help='if test input should be used')

args = parser.parse_args()
day_num = args.day
is_test = args.is_test


days = [i for i in range(31)]
if day_num is not None:
    days = [day_num]

ASSERTION_IDX = 1 if is_test else 2
assertions = [0,0]
for day in days:
    if day in TEST_CASES.keys():
        aoc_day = TEST_CASES[day][0]
        part1, part2 = aoc_day.get_solutions(is_test)
        ans1, ans2 = TEST_CASES[day][ASSERTION_IDX]
        print(f'Day {day}')
        print(f'Part 1: [{part1 == ans1}] {part1} == {ans1} (Actual / Expected)')
        print(f'Part 2: [{part2 == ans2}] {part2} == {ans2} (Actual / Expected)')
        assertions[0] += 2
        if ans1 == part1:
            assertions[1] += 1
        if ans2 == part2:
            assertions[1] += 1

print('\nDone asserting.')
print(f'Correct: {assertions[1]}/{assertions[0]}')
print(f'Incorrect: {assertions[0] - assertions[1]}\n')

            
    