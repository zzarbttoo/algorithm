def solution(n, param_array):

    count_array = [1 for _ in range(n)]

    for current_index, current_num in enumerate(param_array):
        compare_count_array = []
        for before_index in range(current_index):
            if param_array[before_index] > current_num:
                compare_count_array.append(count_array[before_index])
        if compare_count_array:
            count_array[current_index] += max(compare_count_array)

    return max(count_array)
            


# n = 6
# param_array = [10, 30, 10, 20, 20, 10]


n = int(input())
param_array = list(map(int, input().split()))

print(solution(n, param_array))
