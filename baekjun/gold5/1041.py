def solution(N, dice):

    if N == 1: return sum(dice) - max(dice)

    group = [[dice[0], dice[5]], [dice[1], dice[4]], [dice[2], dice[3]]]
    min_group = [min(i) for i in group]
    min_group.sort()

    answer = 0   
    last_num = (N ** 2) * 5

    answer += 4 * sum(min_group)
    last_num -= 4 * 3

    answer += ((N - 2) + (N - 1)) * 4 * (min_group[0] + min_group[1])
    last_num -= ((N - 2) + (N - 1)) * 4 * 2

    answer += last_num * min_group[0]
    return answer


N = int(input())
dice = list(map(int, input().split()))

print(solution(N, dice))


N = 3
dice = [1, 2, 3, 4, 5, 6]

N = 1000000
dice = [50, 50, 50, 50, 50, 50]

N = 10
dice = [1, 1, 1, 1, 50, 1]




#print(1 * 8 + 2 * 8 + 3 * 4) #20
#print(4 * (1 + 2 + 3) + 12 * (1 + 2) + (45 - (3 * 4 + 12 * 2))) #45 





