'''
import collections

def solution(priorities:list, location:list)->int:
    
    stay:list = [[index, priority] for index, priority in enumerate(priorities)]

    stay = sorted(stay, key=lambda x: (-x[1], x[0]))

    sum = 0

    for paper in stay:
        print(paper)
        if paper[0] is location:
            break
        sum +=1

    return sum


'''


import collections
def solution(priorities:list, location:list)->int:

    stay = collections.deque([[index, priority] for index, priority in enumerate(priorities)])
    sum = 0

    while stay:
        temp = stay.popleft()

        if [x for x in stay if temp[1] < x[1]]:
            stay.append(temp)
        else:
            sum += 1
            if temp[0] == location:
                return sum
            

    return sum

print(solution([2,1,3,2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))