def solution(N, task_array):
    task_list = sorted(task_array, key = lambda x: x[1])

    for hour in range(task_array[0][1] - task_array[0][0], -1, -1):
        count = hour
        for i, task in enumerate(task_list):
            if count + task[0] <= task[1]:
                count += task[0]
            else:
                break

        if i == N - 1 and count < 1000000:
            return hour
    return -1


N = int(input())
task_array = []

for _ in range(N):
    task_array.append(list(map(int, input().split())))


print(solution(N, task_array))

#N = 4
#task_array = [[3, 5], [8, 14], [5, 20], [1, 16]]
#task_array = [[3, 4], [1, 4], [5, 17], [2, 20]]
#print(solution(N, task_array))