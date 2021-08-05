import collections
def solution(A):

    count_num = collections.defaultdict(int)

    for i in A:
        count_num[i] += 1

    return len(count_num.keys())
    
# test code 
solution([])
