import util
INPUT_FILE = 'day3_input.txt'
TEST_DATA = ['00100','11110','10110','10111','10101','01111','00111','11100','10000','11001','00010','01010']


def get_bit_count(bits_list):
    bit_count = [0 for _ in range(len(bits_list[0]))]
    for bits in bits_list:
        idx = 0
        for bit in bits:
            bit_count[idx] += 1 if bit == '1' else -1
            idx += 1
    return bit_count


def get_gamma_rate(bit_count):
    bits = ''
    for count in bit_count:
        if count < 0:
            bits += '0'
        else:
            bits += '1'
    return bits


def get_epsilon_rate(gamma_rate):
    eps_rate = ''
    for c in gamma_rate:
        eps_rate += '1' if c == '0' else '0'
    return eps_rate


def get_gas_rating(bits_list, is_oxygen):
    gas_rating = 0
    common_bits = bits_list
    for bit_idx in range(len(bits_list[0])):
        common_bits = get_common_bits(common_bits, bit_idx, is_oxygen)
        if len(common_bits) == 1:
            gas_rating = int(common_bits[0], 2)
            break
    return gas_rating


def get_life_support_rating(bits_list):
    oxy_rating = get_gas_rating(bits_list, True)
    co2_rating = get_gas_rating(bits_list, False)
    return oxy_rating, co2_rating, oxy_rating*co2_rating


def get_common_bits(bits_list, bit_idx, is_oxygen):
    common_bits = {'0': [], '1': []}
    for bits in bits_list:
        common_bits[bits[bit_idx]].append(bits)
    if is_oxygen:
        return common_bits['0'] if len(common_bits['1']) < len(common_bits['0']) else common_bits['1']
    else:
        return common_bits['1'] if len(common_bits['1']) < len(common_bits['0']) else common_bits['0']



if __name__ == '__main__':
    is_test = False
    data = TEST_DATA
    if not is_test:  
        data = util.read_input(INPUT_FILE)

    bit_count = get_bit_count(data)
    gamma_rate = get_gamma_rate(bit_count)
    epsilon_rate = get_epsilon_rate(gamma_rate)
    print('Epsilon * Gamma = ' + str(int(epsilon_rate, 2) * int(gamma_rate, 2)))
    print(f'(Oxygen rating, CO2 rating, Life support rating) : {get_life_support_rating(data)}')
    
    if is_test:
        print(bit_count)
        print("Gamma")
        print(gamma_rate)
        print(int(gamma_rate, 2))
        print("Epsilon")
        print(epsilon_rate)
        print(int(epsilon_rate, 2))