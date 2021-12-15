from aoc_day import AoCDay


class SegmentMapper:

    def __init__(self) -> None:
        self.num_mapping = {}
        for num in range(10):
            self.num_mapping[num] = None
        self.segments = {num: [] for num in range(2, 8)}
        self.seg_to_num = {}

    def map_segments(self, segments):
        mapped_segments = set()
        for segment in segments:
            segment = "".join(sorted(segment))
            if segment not in mapped_segments:
                self.segments[len(segment)].append(segment)
                mapped_segments.add(segment)
        self.num_mapping[1] = self.segments[2][0]
        self.num_mapping[7] = self.segments[3][0]
        self.num_mapping[4] = self.segments[4][0]
        self.num_mapping[8] = self.segments[7][0]
        self.map_3()
        self.map_9()
        self.map_2_and_5()
        self.map_0_and_6()

        for num, segment in self.num_mapping.items():
            self.seg_to_num[segment] = str(num)

    def map_3(self):
        segments = self.segments[5]
        for segment in segments:
            is_3 = True
            for c in self.num_mapping[7]:
                if c not in segment:
                    is_3 = False
                    break
            if is_3:
                self.num_mapping[3] = segment
                return
    
    def map_9(self):
        segments = self.segments[6]
        for segment in segments:
            diff_char = None
            for c in segment:
                if c not in self.num_mapping[3]:
                    if diff_char is None:
                        diff_char = c
                    else:
                        diff_char = None
                        break
            if diff_char is not None:
                self.num_mapping[9] = segment
                return

    def map_2_and_5(self):
        segments = self.segments[5]
        for segment in segments:
            # make sure not 3
            if segment == self.num_mapping[3]:
                continue
            # check for 5
            is_5 = True
            for c in segment:
                if c not in self.num_mapping[9]:
                    is_5 = False
                    break
            if is_5:
                self.num_mapping[5] = segment
            else:
                self.num_mapping[2] = segment

    def map_0_and_6(self):
        segments = self.segments[6]
        for segment in segments:
            # make sure not 9
            if segment == self.num_mapping[9]:
                continue
            # check for 6
            is_6 = True
            for c in self.num_mapping[5]:
                if c not in segment:
                    is_6 = False
            if is_6:
                self.num_mapping[6] = segment
            else:
                self.num_mapping[0] = segment

    def segement_to_number(self, output_segment):
        segment = ''.join(sorted(output_segment))
        return self.seg_to_num[segment]


class AoCDay8(AoCDay):

    def __init__(self) -> None:
        super().__init__(8)
        self.digit_entries = []

    def setup_data(self, data):
        for line in data:
            line = line.split(' | ')
            _in = line[0].split(' ')
            _out = line[1].split(' ')
            self.digit_entries.append((_in,_out))

    def solve_part_one(self):
        uniques = 0
        is_unique = lambda l: True if len(l) in [2, 3, 4, 7] else False
        for _, output in self.digit_entries:
            for digit in output:
                if is_unique(digit):
                    uniques += 1
        return uniques

    def solve_part_two(self):
        sum = 0
        for _input, _output in self.digit_entries:
            mapper = SegmentMapper()
            mapper.map_segments(_input + _output)
            curr_sum = ''
            for out_seg in _output:
                curr_sum += mapper.segement_to_number(out_seg)
            sum += int(curr_sum)
        return sum