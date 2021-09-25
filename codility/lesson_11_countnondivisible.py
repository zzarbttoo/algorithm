import collections
import math 

def solution(A):

    num_hash = collections.defaultdict(int)
    answer_hash = collections.defaultdict(lambda : -1)
    length = 0 

    for num in A:
        num_hash[num] += 1
        length += 1 

    answer = []

    for num in A:
        if answer_hash[num] != -1:
            answer.append(answer_hash[num])
            continue
        count = 0 
        for measure in range(1, math.floor(num ** (1/2)) + 1):
            if num % measure != 0:
                continue
            count += num_hash[measure]

            if measure * measure != num:
                count += num_hash[num // measure]
        
        answer_hash[num] = length - count 
        answer.append(length - count)
            
    return answer
