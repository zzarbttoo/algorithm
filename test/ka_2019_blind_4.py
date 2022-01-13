from collections import defaultdict

def solution(food_times, k):
    
    idx_hash = defaultdict(list)
    time_hash = defaultdict(int)
    length = len(food_times)
    
    for idx, food in enumerate(food_times):
        time_hash[food] += 1
        idx_hash[food].append(idx + 1)
    
    
    clock = 0
    
    for key in sorted(time_hash.keys()):
        
        next_clock = clock + time_hash[key] * length
        
        if next_clock > k:
            break
            
        length -= time_hash[key]
        clock = next_clock
    temp = []
    
    for last_key in time_hash.keys():
        if last_key >= key:
            temp += idx_hash[last_key]
    
    if temp:
        temp.sort()
        return temp[(k - clock) % len(temp)]
        
    return -1 
        