from collections import defaultdict
from collections import deque

def test_case():

    con = defaultdict(list)   
    color = defaultdict(int) #0으로 초기화 
    oppo = {-1:1, 1:-1}

    V, E = map(int, input().split())
    for _ in range(E):
        N1, N2 = map(int, input().split())
        con[N1].append(N2)
        con[N2].append(N1)

    queue = deque([]) 

    for node in range(1, V + 1):
        # print("node ::: " + str(node))
        if color[node] == 0:
            color[node] = 1
            queue.append(node)

            while queue:
                now_node = queue.popleft()

                for next_node in con[now_node]:
                    if color[next_node] == 0:
                        queue.append(next_node)
                        color[next_node] = oppo[color[now_node]]
                    elif color[next_node] == color[now_node]:
                        return 'NO'

    return 'YES'

def solution():
    K = int(input())
    answer = []

    for _ in range(K):
        answer.append(test_case())

    for an in answer:
        print(an)

solution()       