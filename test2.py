
import collections
def solution(numbers:list)->int:

    count_num=collections.Counter(numbers)
    print(count_num)
    if count_num.most_common()[0][1] > len(numbers) // 2:
        return count_num.most_common()[0][0]

    



    return -1

print(solution([6, 1, 6, 6, 7, 6, 6, 7]))
print(solution([6, 1, 6, 6, 7, 5, 6, 7]))