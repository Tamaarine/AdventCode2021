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
    
    zero = [0 for _ in range(12)]
    ones = [0 for _ in range(12)]
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
if __name__ == "__main__":
    print(day3p1('input.txt'))