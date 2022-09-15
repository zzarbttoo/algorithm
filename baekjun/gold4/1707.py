from collections import defaultdict
from collections import deque
from operator import ne

def test_case():

    con = defaultdict(list)   
    color = defaultdict(int) #0으로 초기화 
    oppo = {-1:1, 1:-1}

    V, E = map(int, input().split())
    for _ in range(E):
        N1, N2 = map(int, input().split())
        con[N1].append(N2)
        con[N2].append(N1)

    queue = deque([1]) 
    color[1] = 1 #1번 노드는 무조건 1번색

    while queue:
        now_node = queue.popleft()
        
        for next_node in con[now_node]:
            print(1, now_node, next_node, color[next_node], color[now_node])
            if next_node == 0:
                queue.append(next_node)
                color[next_node] = oppo[color[now_node]]
            elif color[next_node] != color[now_node]:
                return 'NO'
            print(2, now_node, next_node, color[next_node], color[now_node])

    return 'YES'

def solution():
    K = int(input())
    answer = []

    for _ in range(K):
        answer.append(test_case())

    for an in answer:
        print(an)

solution()       