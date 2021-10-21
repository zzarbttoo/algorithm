def solution(N, M, before, after):

    count = 0
    for i in range(N):
        for j in range(M):
            if i + 3 <= N and j + 3 <= M:
                if before[i][j] != after[i][j]:
                    count += 1
                    for y in range(3):
                        for x in range(3):
                            if before[i + y][j + x] == 0:
                                before[i + y][j + x] = 1
                            else:
                                before[i + y][j + x] = 0
            
    for i in range(N):
        for j in range(M):
            if before[i][j] != after[i][j]:
                return -1 

    return count
N, M = map(int, input().split())

before = []
after = []

for _ in range(N):
    before.append([int(a) for a in str(input())])
for _ in range(N):
    after.append([int(a) for a in str(input())])


print(solution(N, M, before, after))