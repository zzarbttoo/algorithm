import collections

def solution(A):
    max_num = -1
    count_dict = collections.defaultdict(int)

    for i in A:
        max_num = max(i, max_num)
        count_dict[i] += 1
    
    for j in range(1, max_num + 1):
        if count_dict[j] == 0:
            return j

    if max_num <= 0:
        return 1
    else:
        return max_num + 1