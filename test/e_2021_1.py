#n이 주어질 때 n까지 몫과 나머지가 같은 수의 합을 구하는 것
def solution(n):

    answer = 0
    #n까지 
    for i in range(1, n):
        div, mod = divmod(n, i)
        if div == mod:
            answer += i

    return answer


# 0 ~ 1000000 까지 
# 몫인 n이 주어짐
n = 3
print(solution(n))

n = 5
print(solution(n))
