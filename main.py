import argparse
day3 = __import__('3_day')
day4 = __import__('4_day')



TEST_CASES = {
    3: (day3.AoCDay3(), (198, 230), (3959450, 7440311)),
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
assertions = [0,0]
for day in days:
    if day in TEST_CASES.keys():
        aoc_day = TEST_CASES[day][0]
        part1, part2 = aoc_day.get_solutions(is_test)
        if should_assert:
            ans1, ans2 = TEST_CASES[day][ASSERTION_IDX]
            print(f'Day {day}')
            print(f'Part 1: [{part1 == ans1}] {part1} == {ans1} (Actual / Expected)')
            print(f'Part 2: [{part2 == ans2}] {part2} == {ans2} (Actual / Expected)')
            assertions[0] += 2
            if ans1 == part1:
                assertions[1] += 1
            if ans2 == part2:
                assertions[1] += 1

if should_assert:
    print('\nDone asserting.')
    print(f'Correct: {assertions[1]}/{assertions[0]}')
    print(f'Incorrect: {assertions[0] - assertions[1]}\n')

            
    