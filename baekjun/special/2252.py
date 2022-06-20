from collections import deque 
from collections import defaultdict


def solution():
    N, M = map(int, input().split())

    queue = deque([])
    cnt = defaultdict(int)
    connect = defaultdict(list)

    for _ in range(M):
        A, B = map(int, input().split())
        cnt[B] += 1
        connect[A].append(B)

    for i in range(1, N + 1):
        if cnt[i] == 0:
            queue.append(i)
    
    answer = []

    while queue:
        node = queue.popleft()
        answer.append(node)

        for next in connect[node]:
            cnt[next] -= 1
            if cnt[next] == 0:
                queue.append(next)

    print(' '.join(map(str, answer)))






        
solution()

