import collections

def solution():

    M, N, K = map(int, input().split())
    field = collections.defaultdict(lambda: collections.defaultdict(lambda :-1))
    direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    K_list = []
    count = 0

    for _ in range(K):
        X, Y = map(int, input().split())
        field[X][Y] = 1
        K_list.append([X, Y])

    def search(now_x, now_y):

        field[now_x][now_y] = -1

        for direct in direction:
            next_x, next_y = now_x + direct[0], now_y + direct[1]
            if next_x >= 0 and next_x < M and next_y >= 0 and next_y < N:
                if field[next_x][next_y] == 1:
                    search(next_x, next_y)

    count = 0

    for k in K_list:
        if field[k[0]][k[1]] == 1:
            count += 1
            search(k[0], k[1])

    return count

test_case = int(input())

for _ in range(test_case):
    print(solution())






