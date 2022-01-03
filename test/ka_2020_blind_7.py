
#dfs 최소 시간에 적합하지 않다
# from collections import defaultdict
# import sys
# sys.setrecursionlimit(10 ** 6)

# def solution(board):
#     visited = defaultdict(lambda : defaultdict(lambda : defaultdict(lambda : defaultdict(bool))))
#     count = defaultdict(lambda : defaultdict(lambda : defaultdict(lambda : defaultdict(int))))
#     N = len(board)
    
#     last_left, last_right = [N - 1, N - 2], [N - 1, N - 1]
    
#     def dfs(left, right, before_count):
        
#         nonlocal visited, last_left, last_right, count
        
#         #작은 쪽이 left, 큰 쪽이 right로 설정
#         if left[0] > right[0] or left[1] > right[1]:
#             left, right = right, left
            
        
#         #visited 여부 확인
#         if visited[left[0]][left[1]][right[0]][right[1]]:
#             if count[left[0]][left[1]][right[0]][right[1]] > before_count:
#                 count[left[0]][left[1]][right[0]][right[1]] = before_count
#             return  #visited 아니면 진행
#         else:
#             visited[left[0]][left[1]][right[0]][right[1]] = True
#             count[left[0]][left[1]][right[0]][right[1]] = before_count
            
        
#         next_count = before_count + 1
        
#         #가로로 있을 경우 
#         if left[0] == right[0]:
#             #상
#             if left[0] - 1 >= 0 and board[left[0] - 1][left[1]] == 0 and board[right[0] - 1][right[1]] == 0:
#                 next_left, next_right = [left[0] - 1, left[1]], [right[0] - 1, right[1]]
#                 dfs(next_left, next_right, next_count)
#             #하
#             if left[0] + 1 < N and board[left[0] + 1][left[1]] == 0 and board[right[0] + 1][right[1]] == 0:
#                 next_left, next_right = [left[0] + 1, left[1]], [right[0] + 1, right[1]]
#                 dfs(next_left, next_right, next_count)
#             #좌
#             if left[1] - 1 >= 0 and board[left[0]][left[1] - 1] == 0:
#                 next_left, next_right = [left[0], left[1] - 1], [right[0], right[1] - 1]
#                 dfs(next_left, next_right, next_count)
#             #우 
#             if right[1] + 1 < N and board[right[0]][right[1] + 1] == 0:
#                 next_left, next_right = [left[0], left[1] + 1], [right[0], right[1] + 1]
#                 dfs(next_left, next_right, next_count)
                
#             #우회전
#             if left[0] - 1 >= 0 and board[left[0] - 1][left[1]] == 0 and board[right[0] - 1][right[1]] == 0:
#                 next_left, next_right = [right[0] - 1, right[1]], [right[0], right[1]]
#                 dfs(next_left, next_right, next_count)
#             #좌회전
#             if left[0] - 1 >= 0 and board[left[0] - 1][left[1]] == 0 and board[right[0] - 1][right[1]] == 0:
#                 next_left, next_right = [left[0], left[1]], [left[0] - 1, left[1]]
#                 dfs(next_left, next_right, next_count)
#             #후진 우회전
#             if left[0] + 1 < N and board[left[0] + 1][left[1]] == 0 and board[right[0] + 1][right[1]] == 0:
#                 next_left, next_right = [left[0], left[1]], [left[0] + 1, left[1]]
#                 dfs(next_left, next_right, next_count)
#             #후진 좌회전
#             if left[0] + 1 < N and board[left[0] + 1][left[1]] == 0 and board[right[0] + 1][right[1]] == 0:
#                 next_left, next_right = [right[0] + 1, right[1]], [right[0], right[1]]
#                 dfs(next_left, next_right, next_count)
#         #세로로 있을 경우
#         elif left[1] == right[1]:
#             #상
#             if left[0] - 1 >= 0 and board[left[0] - 1][left[1]] == 0:
#                 next_left, next_right = [left[0] - 1, left[1]], [right[0] - 1, right[1]]
#                 dfs(next_left, next_right, next_count)
#             #하
#             if right[0] + 1 < N and board[right[0] + 1][right[1]] == 0: 
#                 next_left, next_right = [left[0] + 1, left[1]], [right[0] + 1, right[1]]
#                 dfs(next_left, next_right, next_count)
#             #좌
#             if left[1] - 1 >= 0 and board[left[0]][left[1] - 1] == 0 and board[right[0]][right[1] - 1] == 0:
#                 next_left, next_right = [left[0], left[1] - 1], [right[0], right[1] - 1]
#                 dfs(next_left, next_right, next_count)
#             #우 
#             if left[1] + 1 < N and board[left[0]][left[1] + 1] == 0 and board[right[0]][right[1] + 1] == 0:
#                 next_left, next_right = [left[0], left[1] + 1], [right[0], right[1] + 1]
#                 dfs(next_left, next_right, next_count)
                
#             #우회전
#             if left[1] + 1 < N and board[left[0]][left[1] + 1] == 0 and board[right[0]][right[1] + 1] == 0:
#                 next_left, next_right = [left[0], left[1]], [left[0], left[1] + 1]
#                 dfs(next_left, next_right, next_count)
#             #좌회전
#             if left[1] - 1 >= 0 and board[left[0]][left[1] - 1] == 0 and board[right[0]][right[1] - 1] == 0:
#                 next_left, next_right = [left[0], left[1] - 1], [left[0], left[1]]
#                 dfs(next_left, next_right, next_count)
#             #후진 우회전
#             if left[1] + 1 < N and board[left[0]][left[1] + 1] == 0 and board[right[0]][right[1] + 1] == 0:
#                 next_left, next_right = [right[0], right[1] + 1], [right[0], right[1]]
#                 dfs(next_left, next_right, next_count)
#             #후진 좌회전
#             if left[1] - 1 >= 0 and board[left[0]][left[1] - 1] == 0 and board[right[0]][right[1] - 1] == 0:
#                 next_left, next_right = [right[0], right[1] - 1], [right[0], right[1]]
#                 dfs(next_left, next_right, next_count)
            
#     dfs([0, 0], [1, 0], 0)
    
    
#     print(count[last_left[0]][last_left[1]][last_right[0]][last_right[1]])


# from queue import Queue 
# from collections import defaultdict


# def solution(board):
    
#     que = Queue()
#     visited = defaultdict(lambda : defaultdict(lambda : defaultdict(lambda : defaultdict(bool))))
#     N = len(board)
#     last_left, last_right = [N - 1, N - 2], [N - 1, N - 1]
#     direction_list = [[-1, 0], [1, 0], [0, -1], [0, 1]]  #상, 하, 좌, 우
    
#     que.put([[0, 0], [0, 1], 0]) #left, right, count
    
#     #bfs
#     while que.qsize():
#         left, right, before_count = que.get()
        
#         #if left[0] > right[0] or left[1] > right[1]:
#             #left , right = right, left
        
#         visited[left[0]][left[1]][right[0]][right[1]] = True
        
#         if left[0] == last_left[0] and left[1] == last_left[1] and right[0] == last_right[0] and right[1] == last_right[1]:
#             return before_count
        
#         #이동 
#         # 상, 하, 좌, 우
#         for direction in direction_list:
#             new_left = left[0] + direction[0],  left[1] + direction[1]
#             new_right = right[0] + direction[0], right[1] + direction[1]
            
#             #범위 안, 장애물 여부, 방문 여부
#             if (0 <= new_left[0] < N and 0 <= new_left[1] < N and
#                 0 <= new_right[0] < N and 0<= new_right[1] < N and 
#                	board[new_left[0]][new_left[1]] == 0 and 
#                 board[new_right[0]][new_right[1]] == 0 and
#                 visited[new_left[0]][new_left[1]][new_right[0]][new_right[1]] == False
#                ):
                
#                 que.put([new_left, new_right,before_count + 1])
                
#         #회전
#         #가로방향
#         if left[0] == right[0]:
#             #상
#             if 0 <= left[0] - 1 < N and board[left[0] - 1][left[1]] == 0 and board[right[0] - 1][right[1]] == 0:
#                 #좌
#                 new_left, new_right = [left[0] - 1, left[1]], [left[0], left[1]]
#                 if visited[new_left[0]][new_left[1]][new_right[0]][new_right[1]] == False: que.put([new_left, new_right, before_count + 1])
#                 #우  
#                 new_left, new_right = [right[0] - 1, right[1]], [right[0], right[1]]
#                 if visited[new_left[0]][new_left[1]][new_right[0]][new_right[1]] == False: que.put([new_left, new_right, before_count + 1])
#             #하
#             if 0 <= left[0] + 1 < N and board[left[0] + 1][left[1]] == 0 and board[right[0] + 1][right[1]] == 0:
#                 #좌
#                 new_left, new_right = [left[0], left[1]], [left[0] + 1, left[1]]
#                 if visited[new_left[0]][new_left[1]][new_right[0]][new_right[1]] == False: que.put([new_left, new_right, before_count + 1])
#                 #우
#                 new_left, new_right = [right[0], right[1]], [right[0] + 1, right[1]]
#                 if visited[new_left[0]][new_left[1]][new_right[0]][new_right[1]] == False: que.put([new_left, new_right, before_count + 1])
#         #세로방향
#         if left[1] == right[1]:
#             #좌
#             if 0 <= left[1] -1 < N and board[left[0]][left[1] - 1] == 0 and board[right[0]][right[1] - 1] == 0:
#                 #상
#                 new_left, new_right = [left[0], left[1] - 1], [left[0], left[1]]
#                 if visited[new_left[0]][new_left[1]][new_right[0]][new_right[1]] == False: que.put([new_left, new_right, before_count + 1])
#                 #하
#                 new_left, new_right = [right[0], right[1] - 1], [right[0], right[1]]
#                 if visited[new_left[0]][new_left[1]][new_right[0]][new_right[1]] == False: que.put([new_left, new_right, before_count + 1])
#             #우
#             if 0 <= left[1] + 1 < N and board[left[0]][left[1] + 1] == 0 and board[right[0]][right[1] + 1] == 0:
#                 #상
#                 new_left, new_right = [left[0], left[1]], [left[0], left[1] + 1]
#                 if visited[new_left[0]][new_left[1]][new_right[0]][new_right[1]] == False: que.put([new_left, new_right, before_count + 1])
#                 #하
#                 new_left, new_right = [right[0], right[1]], [right[0], right[1] + 1]
#                 if visited[new_left[0]][new_left[1]][new_right[0]][new_right[1]] == False: que.put([new_left, new_right, before_count + 1])
        
 
# from queue import Queue 
# from collections import defaultdict


# def solution(board):
    
#     que = Queue()
#     visited = defaultdict(lambda : defaultdict(lambda : defaultdict(lambda : defaultdict(bool))))
#     N = len(board)
#     last_left, last_right = [N - 1, N - 2], [N - 1, N - 1]
#     direction_list = [[-1, 0], [1, 0], [0, -1], [0, 1]]  #상, 하, 좌, 우
    
#     que.put([[0, 0], [0, 1], 0]) #left, right, count
    
#     def is_valid(new_left, new_right):
#         nonlocal board, N, visited
        
#         if new_left[0] > new_right[0] or new_left[1] > new_right[1]:
#             new_left, new_right = new_right, new_left
        
#         if (0 <= new_left[0] < N and 0 <= new_left[1] < N and
#             0 <= new_right[0] < N and 0<= new_right[1] < N and 
#             board[new_left[0]][new_left[1]] == 0 and 
#             board[new_right[0]][new_right[1]] == 0 and
#             visited[new_left[0]][new_left[1]][new_right[0]][new_right[1]] == False
#            ):       
#             visited[new_left[0]][new_left[1]][new_right[0]][new_right[1]] = True 
#             return True
#         else:
#             return False

#     #bfs
#     while que.qsize():
        
#         left, right, before_count = que.get()
        
#         if left[0] > right[0] or left[1] > right[1]:
#             left, right = right, left
        
#         if left[0] == last_left[0] and left[1] == last_left[1] and right[0] == last_right[0] and right[1] == last_right[1]:
#             return before_count
        
#         #이동 
#         # 상, 하, 좌, 우
#         for idx, direction in enumerate(direction_list):
#             new_left = left[0] + direction[0],  left[1] + direction[1]
#             new_right = right[0] + direction[0], right[1] + direction[1]
            
#             #범위 안, 장애물 여부, 방문 여부
#             if is_valid(new_left, new_right):
#                 que.put([new_left, new_right,before_count + 1])
#                 rotate_left, rotate_right = left, [left[0] + direction[0], left[1] + direction[1]]
#                 if is_valid(rotate_left, rotate_right) : que.put([rotate_left, rotate_right, before_count + 1])
#                 rotate_left, rotate_right = right, [right[0] + direction[0], right[1] + direction[1]]
#                 if is_valid(rotate_left, rotate_right) : que.put([rotate_left, rotate_right, before_count + 1])
                    
                     
from queue import Queue 
from collections import defaultdict


def solution(board):
    
    que = Queue()
    visited = defaultdict(lambda : defaultdict(lambda : defaultdict(lambda : defaultdict(bool))))
    N = len(board)
    last_left, last_right = [N - 1, N - 2], [N - 1, N - 1]
    direction_list = [[-1, 0], [1, 0], [0, -1], [0, 1]]  #상, 하, 좌, 우
    
    que.put([[0, 0], [0, 1], 0]) #left, right, count
    
    def is_valid(new_left, new_right):
        nonlocal board, N, visited
        
        if new_left[0] > new_right[0] or new_left[1] > new_right[1]:
            new_left, new_right = new_right, new_left
        
        if (0 <= new_left[0] < N and 0 <= new_left[1] < N and
            0 <= new_right[0] < N and 0<= new_right[1] < N and 
            board[new_left[0]][new_left[1]] == 0 and 
            board[new_right[0]][new_right[1]] == 0 and
            visited[new_left[0]][new_left[1]][new_right[0]][new_right[1]] == False
           ):       
            visited[new_left[0]][new_left[1]][new_right[0]][new_right[1]] = True 
            return True
        else:
            return False

    #bfs
    while que.qsize():
        
        left, right, before_count = que.get()
        
        if left[0] > right[0] or left[1] > right[1]:
            left, right = right, left
        
        if left[0] == last_left[0] and left[1] == last_left[1] and right[0] == last_right[0] and right[1] == last_right[1]:
            return before_count
        
        #이동 
        # 상, 하, 좌, 우
        for idx, direction in enumerate(direction_list):
            new_left = left[0] + direction[0],  left[1] + direction[1]
            new_right = right[0] + direction[0], right[1] + direction[1]
            
            #범위 안, 장애물 여부, 방문 여부
            if is_valid(new_left, new_right):
                que.put([new_left, new_right,before_count + 1])
                if idx == 0 or idx == 2:
                    rotate_left, rotate_right = [left[0] + direction[0], left[1] + direction[1]] , left
                    if is_valid(rotate_left, rotate_right) : que.put([rotate_left, rotate_right, before_count + 1])
                    rotate_left, rotate_right = [right[0] + direction[0], right[1] + direction[1]], right
                    if is_valid(rotate_left, rotate_right) : que.put([rotate_left, rotate_right, before_count + 1])
                if idx == 1 or idx == 3:
                    rotate_left, rotate_right = left, [left[0] + direction[0], left[1] + direction[1]]
                    if is_valid(rotate_left, rotate_right) : que.put([rotate_left, rotate_right, before_count + 1])
                    rotate_left, rotate_right = right, [right[0] + direction[0], right[1] + direction[1]]
                    if is_valid(rotate_left, rotate_right) : que.put([rotate_left, rotate_right, before_count + 1])


        

        
          
        
        
