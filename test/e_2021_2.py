# [프린터 번호, 프린터 도착 시간, 프린터 장수]가 담긴 리스트 전달 받음
# 빨리 프린트 되는 순서를 return 
# 프린터 장수가 클수록 뒤로 감 
# 프린트 끝나는 시간에 프린트가 도착한다면 그 때 새로운 프린트를 대기하도록 한다 

import heapq

def solution():
    pass

num = [[1, 0 ,5], [2, 2, 3], [3, 4, 4], [4, 5, 2], [5, 7, 1]]

answer = []

for number in num:
    heapq.heappush(answer, (number[1], [number[0], number[1], number[2]]))

print(answer)

while answer:
    print(heapq.heappop(answer))

