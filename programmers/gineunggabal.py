import collections
import math
def solutions(progresses:list, speeds:list)->list:

    answer = []
    dates = []
    temp_max = 0
    done_date = collections.deque([math.ceil((100-progress)/speed) for progress, speed in zip(progresses, speeds)])

    print(done_date)

    while done_date:
        temp = done_date.popleft()
        temp_max = max(temp, temp_max)
        dates.append(temp_max)
    
    answer = list(collections.Counter(dates).values())

    return answer

print(solutions([93, 30, 55], [1, 30, 5]))
print(solutions([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))