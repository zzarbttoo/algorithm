import sys 
input = sys.stdin.readline

def solution():
    N, M = map(int, input().split())
    num = []

    for _ in range(N):
        num.append(list(map(int,input().split())))
    
    di = [
        [[0, 0], [0, 1], [0, 2], [0, 3]],
        [[0, 0], [1, 0], [2, 0], [3, 0]],
        [[0, 0], [0, 1], [1, 0], [1, 1]],
        [[0, 0], [1, 0], [2, 0], [2, 1]],
        [[0, 1], [1, 1], [2, 0], [2, 1]],
        [[0, 0], [0, 1], [1, 0], [2, 0]],
        [[0, 0], [0, 1], [1, 1], [2, 1]],
        [[0, 0], [0, 1], [0, 2], [1, 0]],
        [[0, 0], [0, 1], [0, 2], [1, 2]],
        [[0, 0], [1, 0], [1, 1], [1, 2]],
        [[1, 0], [1, 1], [1, 2], [0, 2]],
        [[0, 0], [1, 0], [1, 1], [2, 1]],
        [[0, 1], [1, 1], [1, 0], [2, 0]],
        [[0, 0], [0, 1], [1, 1], [1, 2]],
        [[1, 0], [1, 1], [0, 1], [0, 2]],
        [[0, 0], [0, 1], [0, 2], [1, 1]],
        [[0, 1], [1, 0], [1, 1], [1, 2]],
        [[0, 0], [1, 0], [2, 0], [1, 1]],
        [[1, 0], [0, 1], [1, 1], [2, 1]]
    ]

    answer = 0

    for y in range(N):
        for x in range(M):
            #print("y ::: " + str(y))
            #print("x ::: " + str(x))
            for direction in di:
                sum = 0
                is_pos = True
                for d in direction:
                    ny, nx = y + d[0], x + d[1]
                    if 0 <= ny < N and 0 <= nx < M:
                        sum += num[ny][nx]
                    else:
                        is_pos = False
                        break
                if is_pos and answer < sum:
                    answer = sum
                #print("sum ::: " + str(sum))
    
    print(answer)


solution()