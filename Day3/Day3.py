def binary2dec(str):
    value = 1
    output = 0
    for letter in str[::-1]:
        if letter == '1':
            output += value
        value <<= 1
    return output

def day3p1(filename, col=12):
    file = open(filename, 'r')
    
    zero = [0 for _ in range(col)]
    ones = [0 for _ in range(col)]
    for line in file:
        for pair in enumerate(line.strip('\n')):
            if pair[1] == '0':
                zero[pair[0]] += 1
            else:
                ones[pair[0]] += 1
    
    gamma = "" # most common bit
    epsilon = "" # least common bit
    
    for i in range(len(zero)):
        if zero[i] > ones[i]:
            # zero is the most common bit
            gamma += "0"
            # one is the least common bit
            epsilon += "1"
        else:
            gamma += "1"
            epsilon += "0"
    return binary2dec(gamma) * binary2dec(epsilon)         
    
def day3p2(filename):
    file = open(filename, 'r').readlines()
    
    # Get oxygen generator rate
    # Most common bit
    oxygen_rate = find_most_least_common_bit(file)
    co2_rate = find_most_least_common_bit(file, most_common=False)
    return oxygen_rate * co2_rate    
        
def find_most_least_common_bit(file_lines, most_common=True):
    bool_array = [True for _ in range(len(file_lines))]
    counter = len(file_lines)
    
    bit = 0
    while counter > 1:
        zero = [i for i, line in enumerate(file_lines) if bool_array[i] and line[bit] == '0']
        one = [i for i, line in enumerate(file_lines) if bool_array[i] and line[bit] == '1']
        
        zero_more_common = False 
        
        if len(zero) > len(one):
            zero_more_common = True
        elif len(zero) == len(one):
            if most_common:
                zero_more_common = False
            else:
                zero_more_common = False
        
        # Delete the less common one
        if most_common:
            if zero_more_common:
                for index in one:
                    bool_array[index] = False
                counter -= len(one)
            else:
                for index in zero:
                    bool_array[index] = False
                counter -= len(zero)
        else:
            # Delete the more common more
            if zero_more_common:
                for index in zero:
                    bool_array[index] = False
                counter -= len(zero)
            else:
                for index in one:
                    bool_array[index] = False
                counter -= len(one)
        bit += 1
        
    for i, bool in enumerate(bool_array):
        if bool:
            rate = binary2dec(file_lines[i].strip("\n"))
            break
    return rate
    
if __name__ == "__main__":
    print(day3p1('input.txt'))
    print(day3p2('input.txt'))