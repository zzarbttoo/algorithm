def find_max_sum(numbers):

    length = len(numbers)

    if length == 0: return 0
    if length == 1: return numbers[0]

    numbers.sort()

    return numbers[-1] + numbers[-2]

from sys import stdin

if __name__ == "__main__":

    input_nums = list(map(int, stdin.readline().split()))
    print(find_max_sum(input_nums))