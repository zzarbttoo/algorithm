import collections

def solution(A):

    count = collections.defaultdict(int)

    for i in A:
        count[i] += 1

    for key, value in count.items():
        if value % 2 != 0:
            return key

    
    









A = [9, 3, 9, 3, 9, 7, 9]
A = []
print(solution(A))