
def solution(N):
    binary_num = format(N, 'b')

    strings = str(binary_num).split('1')

    binary_gap = 0
    for i, number in enumerate(strings):
        if i-1 >= 0 and i + 1 < len(strings):
          binary_gap = max(binary_gap, len(number))
    
    return binary_gap