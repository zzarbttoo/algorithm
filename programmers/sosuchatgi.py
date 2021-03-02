from itertools import permutations
def solution(numbers:list)-> int:
    answer:int = 0

    a = set()

    # list에 있는 수를 조합해서 만들 수 있는 모든 수 
    for i in range(len(numbers)):
        a|= set(map(int, map("".join, permutations(list(numbers), i+1))))

    # 소수에 0, 1은 포함되지 않는다
    a-= {0, 1}

    # 가능한 수 만들기 

    
    # 소수 제거 

    return 0

print(solution("17"))
print(solution("011"))
