import collections

def solution(bridge_length, weight, truck_weights):

    #bridge length 를 0으로 채움(그럼 len=0 예외처리가 쉬워짐)
    
    q = collections.deque([0]*bridge_length)
    t = collections.deque(truck_weights)

    second = 0
    sum = 0

    while q:
        second += 1
        sum -= q.popleft()
        if t:
            if sum + t[0] <= weight:
                tvalue = t.popleft()
                sum += tvalue
                q.append(tvalue)

            else:
                q.append(0)

    return second
        

print(solution(2, 10, [7, 4, 5, 6]))
print(solution(100, 100, [10]))
print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10,10, 10, 10]))
