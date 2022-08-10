from collections import defaultdict
import sys 

sys.setrecursionlimit(10 ** 6)

def solution():
    N = int(input())
    con = defaultdict(list)
    vi = defaultdict(bool)
    memo = defaultdict(lambda : defaultdict(int))

    for _ in range(N - 1):
        n1, n2 = map(int, input().split())
        con[n1].append(n2)
        con[n2].append(n1)

    def dfs(node):
        nonlocal con, vi, memo 
        memo[node][True] = 1
        memo[node][False] = 0

        print(node)

        for link in con[node]:
            link_true, link_false = dfs(link)
            print(link, link_true, link_false)
            memo[node][False] += link_true
            memo[node][True] += min(link_true, link_false)

        print(node ,memo[node][True], memo[node][False])
        return memo[node][True], memo[node][False]
    
    #memo[1][True] = 1 #현재 노드가 influ, influ 갯수
    #memo[1][False] = 0 
    print(min(dfs(1))) #1번 노드부터 시작 
                                                    

solution()

# def solution():

#     N = int(input())
#     con = defaultdict(list)

#     for _ in range(N - 1):
#         n1, n2 = map(int, input().split())
#         con[n1].append(n2)
#         con[n2].append(n1)

#     vis = defaultdict(bool)
#     queue = deque([])
#     influ = set()

#     #root 
#     queue.append(1)

#     while queue:
#         now = queue.popleft()
#         cnt = 0

#         if not vis[now]:
#             vis[now] = True
#             influ.add(now)

#         for next in con[now]:

#             #자식 중 자식이 있음 
#             if not vis[next] and len(con[next]) - 1 > 0:
#                 queue.append(next)
#                 influ.add(next)
            
#             if next in influ:
#                 cnt += 1

#         print("now ::: " + str(now))
#         print("length ::: " + str(len(con[now])))
#         print("cnt ::: " + str(cnt))

#         print("influ :::" + str(influ))

#         if cnt == len(con[now]):
#             influ.remove(now)


#     print(influ)
#     print(len(influ))

# solution()

# from collections import defaultdict
# from collections import deque

# def solution():

#     N = int(input())
#     con = defaultdict(list)

#     for _ in range(N - 1):
#         n1, n2 = map(int, input().split())
#         con[n1].append(n2)
#         con[n2].append(n1)

#     vis = defaultdict(bool)
#     queue = deque([])
#     influ = set()

#     #root 
#     queue.append(1)

#     while queue:
#         now = queue.popleft()
#         cnt = 0

#         if not vis[now]:
#             vis[now] = True

#         for next in con[now]:

#             #자식 중 자식이 있음 
#             if not vis[next] and len(con[next]) - 1 > 0:
#                 queue.append(next)
#                 cnt += 1

#         if len(con[now]) > cnt:
#             influ.add(now)


#     print(influ)
#     print(len(influ))

# solution()