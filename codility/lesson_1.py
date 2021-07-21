def solution(N):
    # write your code in Python 3.6

    binary_num = format(N, 'b')
    #print(binary_num)
    
    strings = str(binary_num).split('1')
    #print(strings)

    binary_gap = 0
    for number in strings:
        binary_gap = max(binary_gap, len(number))
    
    #print(binary_gap)
    return binary_gap

print(solution(32))