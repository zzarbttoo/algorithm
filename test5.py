import collections

def solution(n:int)->int:

    count = 0
    #n을 이진수로 바꿨을 때 1의 갯수
    bin_n_count = collections.Counter(bin(n)[2:])['1']

    #n 이전의 값들과 비교
    for i in range(n):
        if collections.Counter(bin(i)[2:])['1'] == bin_n_count:
            count += 1

    return count
print(solution(9))