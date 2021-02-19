import collections
def solution(bridge_length:int, weight:int, truck_weight:list) -> int:

    stay_queue = collections.deque(truck_weight)
    run_queue= collections.deque()
    sum_weight = 0

    while True:

        

        if sum_weight > weight:
            continue
        
        if not stay_queue and not run_queue:
            break 
        
        




    return 0

print(solution(2, 10, [7, 4, 5, 6]))
print(solution(100, 100, [10]))
print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10,10, 10, 10]))
