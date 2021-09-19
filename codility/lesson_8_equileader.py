import collections
def solution(A):
    a_length = len(A)
    a_hash = collections.defaultdict(int)
    lead_num = 0

    for i, num in enumerate(A):
        a_hash[num] += 1 
        if a_hash[num] > a_length/2:
            lead_num = num 

    answer = 0
    count = 0
    for i, num in enumerate(A):
        if num == lead_num:
            count += 1
        if count > (i + 1) / 2 and a_hash[lead_num] - count > (a_length - i - 1) /2 :
            answer += 1

    return answer 