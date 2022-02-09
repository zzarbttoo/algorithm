def find_max_sum(numbers):

    length = len(numbers)

    if length == 0: return 0
    if length == 1: return numbers[0]

    numbers.sort()

    return numbers[-1] + numbers[-2]
    
if __name__ == "__main__":
    print(find_max_sum([5, 9, 7, 11]))