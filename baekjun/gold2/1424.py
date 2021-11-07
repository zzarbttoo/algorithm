def solution(N, L, C):

    max_music , last = divmod(C, L + 1)

    if last == L:
        max_music += 1
    if max_music % 13 == 0:
        max_music -= 1

    answer, last = divmod(N, max_music)

    if last > 0:
        if last % 13 == 0:
            if last + 1 <= max_music and answer != 0 and (max_music - 1) % 13 != 0:
                answer += 1
            else:
                answer += 2
        else:
            answer += 1
    return answer

N = int(input())
L = int(input())
C = int(input())

print(solution(N, L, C))
#N, L, C = 7, 2, 6
#N, L, C = 20, 1, 100
#N, L, C = 26, 1, 100
#N, L, C = 67, 271, 1000

#N, L, C = 100000, 1, 10000
#print(solution(N, L, C))