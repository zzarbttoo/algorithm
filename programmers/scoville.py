import heapq

def solution(scoville:list, K:int)->int:

    count = 0
    heapq.heapify(scoville)

    while True:

        first = heapq.heappop(scoville)
        if first > K:
            break

        if len(scoville) == 0:
            return -1

        second = heapq.heappop(scoville)
        heapq.heappush(scoville, first + 2*second)
        count += 1
    
    return count


print(solution([1, 2, 3, 9, 10, 12], 7))