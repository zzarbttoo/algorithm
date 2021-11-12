# def solution(N, K, game):

#     start_limit = N - K
#     sort_game = sorted(game)
#     #print("sort game ::: " + str(sort_game))
#     if sort_game == game: return 0
#     min_num = float("INF")

#     def dfs(rev_idx, last_k , rev_list, count):
#         nonlocal min_num
#         temp_rev = rev_list[:]

#         temp_rev[rev_idx], temp_rev[N -rev_idx - 1] = temp_rev[N-rev_idx - 1], temp_rev[rev_idx]
#         count += 1
#         last_k -= 1

#         if temp_rev == sort_game:
#             min_num = min(min_num, count)
#             return
#         if last_k == 0 or rev_idx + 1 == N:
#             return
#         else:
#             for idx in range(rev_idx + 1, N - last_k + 1):
#                 dfs(idx, last_k, temp_rev, count)

#     for rev_idx in range(start_limit + 1):
#         dfs(rev_idx , K ,game, 0)
    
#     print("min ::: " + str(min_num))

# from collections import defaultdict

# def solution(N, K, game):

#     sorted_game = sorted(game)
#     print("sorted ::: " + str(sorted_game))
#     answer = float("INF")
#     visited = defaultdict(int)


#     def dfs(before_count, before_game):

#         nonlocal answer 
#         nonlocal visited 

#         if sorted_game == before_game:
#             print("sorted :: " + str(sorted_game))
#             answer = min(answer, before_count)
#             return 

#         before_str = " ".join(before_game)
#         visited[before_str] = -1

#         for idx in range(N - K + 1):

#             next_game = before_game[:]
#             next_game[idx:idx + K] = before_game[idx:idx + K][::-1]
#             #print(before_game[idx:idx + K])
#             next_count = before_count + 1

#             next_str = " ".join(next_game)

#             if visited[next_str] == 0: 
#                 visited[next_str] = -1
#                 dfs(next_count, next_game)

                    
#     dfs(0, game)
#     if answer == float("INF"): print(-1)
#     else: print(answer)
    
    

# DFS 가 아니라 BFS 이용

from collections import deque 
from collections import defaultdict

def solution(N, K, game):

    queue = deque([])
    visited = defaultdict(int)
    visited_count = defaultdict(int)
    answer_word = sorted(game)
    answer = float("INF")

    queue.append(game)
    visited[" ".join(game)] = -1

    while queue:
        now_word = queue.popleft()
        now_str = "".join(now_word)

        if now_word == answer_word:
            answer = min(answer, visited_count[now_str])

        for idx in range(N - K + 1):
            next_word = now_word[:]
            next_word[idx:idx + K] = now_word[idx:idx + K][::-1]
            next_str = "".join(next_word)

            if visited[next_str] == 0:
                visited_count[next_str] = visited_count[now_str] + 1
                visited[next_str] = -1
                queue.append(next_word)

    
    if answer == float("INF"): return -1
    return answer
            

N, K = map(int, input().split())
game = list(input().split())

print(solution(N, K, game))