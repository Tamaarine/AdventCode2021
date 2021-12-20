def day2p1(filename):
    file = open(filename, 'r')
    x = 0
    y = 0
    for line in file:
        line = line.strip('\n')
        splitted = line.split()
        if splitted[0] == 'forward':
            x += int(splitted[1])
        elif splitted[0] == 'down':
            y += int(splitted[1])
        else:
            y -= int(splitted[1])
        
    return x * y    
    
def day2p2(filename):
    file = open(filename, 'r')
    x = 0
    depth = 0
    aim = 0
    for line in file:
        line = line.strip('\n')
        splitted = line.split()
        arg = int(splitted[1])
        if splitted[0] == 'forward':
            x += arg
            depth += aim * arg
        elif splitted[0] == 'down':
            aim += arg
        else:
            aim -= arg
    
    return x * depth
if __name__ == "__main__":
    print(day2p1('input.txt'))    
    print(day2p2('input.txt'))    