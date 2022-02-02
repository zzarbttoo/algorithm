import math 

def solution(progresses, speeds):
    
    done = [math.ceil((100 - pro) / sp) for pro, sp in zip(progresses, speeds)]
    
    answer = []
    count = 0
    std = done[0]
    
    for work in done:
        if work > std:
            answer.append(count)
            count, std = 1, work
        else:
            count += 1
    answer.append(count)
    
    return answer