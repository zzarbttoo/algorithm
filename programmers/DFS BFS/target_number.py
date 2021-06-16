def solution(numbers, target):
    answer_list = [0]

    for j in numbers:
        temp_list = []
        for i in answer_list:
            temp_list.append(i - j)
            temp_list.append(i + j)
        answer_list = temp_list
    
    return answer_list.count(target)




numbers = [1, 1, 1, 1, 1]
target = 3
print(solution(numbers, target))