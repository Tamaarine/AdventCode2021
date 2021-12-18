def day1p1(filename):
    file = open(filename, 'r')
    lines = file.readlines()
    
    count = 0
    for i in range(1, len(lines)):
        if int(lines[i]) > int(lines[i - 1]):
            count += 1
    return count

def day1p2(filename):
    file = open(filename, 'r')
    lines = file.readlines()
    
    dp = [0 for i in range(len(lines) - 2)]
    dp[0] = sum([int(line) for line in lines[:3]])
    count = 0
    for i in range(1, len(lines) - 2):
        dp[i] = int(lines[i]) + int(lines[i + 1]) + int(lines[i + 2])
        if dp[i] > dp[i - 1]:
            count += 1
    return count
        
if __name__ == "__main__":
    print(day1p1('input.txt'))
    print(day1p2('input.txt'))