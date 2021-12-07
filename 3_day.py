from typing import List
from aoc_day import AoCDay


class AoCDay3(AoCDay):

    def __init__(self) -> None:
        super().__init__(3)
        self.bits_list = []

    def setup_data(self, data) -> List:
        self.bits_list = data
        return data

    def solve_part_one(self, data) -> None:
        return self.get_power_consumption_rate()

    def solve_part_two(self, data) -> None:
        return self.get_life_support_rating()

    def get_power_consumption_rate(self):
        bit_count = self.get_bit_count()
        gamma_rate = self.get_gamma_rate(bit_count)
        epsilon_rate = self.get_epsilon_rate(gamma_rate)
        consumption_rate = int(epsilon_rate, 2) * int(gamma_rate, 2)
        print(f'Epsilon * Gamma = {consumption_rate}')
        return consumption_rate

    def get_bit_count(self):
        bits_list = self.bits_list
        bit_count = [0 for _ in range(len(bits_list[0]))]
        for bits in bits_list:
            idx = 0
            for bit in bits:
                bit_count[idx] += 1 if bit == '1' else -1
                idx += 1
        return bit_count


    def get_gamma_rate(self, bit_count):
        bits = ''
        for count in bit_count:
            if count < 0:
                bits += '0'
            else:
                bits += '1'
        return bits


    def get_epsilon_rate(self, gamma_rate):
        eps_rate = ''
        for c in gamma_rate:
            eps_rate += '1' if c == '0' else '0'
        return eps_rate


    def get_gas_rating(self, is_oxygen):
        gas_rating = 0
        common_bits = self.bits_list
        for bit_idx in range(len(common_bits[0])):
            common_bits = self.get_common_bits(common_bits, bit_idx, is_oxygen)
            if len(common_bits) == 1:
                gas_rating = int(common_bits[0], 2)
                break
        return gas_rating


    def get_life_support_rating(self):
        oxy_rating = self.get_gas_rating(True)
        co2_rating = self.get_gas_rating(False)
        return oxy_rating*co2_rating


    def get_common_bits(self, bits_list, bit_idx, is_oxygen):
        common_bits = {'0': [], '1': []}
        for bits in bits_list:
            common_bits[bits[bit_idx]].append(bits)
        if is_oxygen:
            return common_bits['0'] if len(common_bits['1']) < len(common_bits['0']) else common_bits['1']
        else:
            return common_bits['1'] if len(common_bits['1']) < len(common_bits['0']) else common_bits['0']

