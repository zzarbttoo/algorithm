from collections import defaultdict
from queue import Queue

#방향의 차이도 고려해야함
def solution(board):

    #상, 하, 좌, 우
    di = [[-1, 0], [1, 0], [0, -1], [0, 1]] # 0, 1, 2, 3 #-1은 아무곳이나
    now = [0, 0, -1 , 0] #count
    l = len(board)
    end = [l - 1, l - 1]
    visited = defaultdict(lambda : defaultdict(lambda : defaultdict(lambda : float('INF')))) #최댓값 가격 세팅

    q = Queue()
    q.put(now)
    visited[now[0]][now[1]][-1] = 0
    visited[now[0]][now[1]][0] = 0
    visited[now[0]][now[1]][1] = 0
    visited[now[0]][now[1]][2] = 0
    visited[now[0]][now[1]][3] = 0

    while q.qsize():

        before = q.get()
        count = before[3]

        if visited[before[0]][before[1]][before[2]] < count:
            count = visited[before[0]][before[1]][before[2]]

        for i_d, d in enumerate(di): #다음 행선지
            if (before[2] == 0 and i_d == 1) or (before[2] == 1 and i_d == 0) or (before[2] == 2 and i_d == 3) or (before[2] == 3 and i_d == 2):
                continue
            #꺾기 가능 여부
            if 0 <= before[0] + d[0]<= l-1 and 0<= before[1] + d[1] <= l - 1 and board[before[0] + d[0]][before[1] + d[1]] != 1:
                new_count = count
                if i_d == 0 or i_d == 1: #다음 상/하
                    if before[2] == 2 or before[2] == 3: 
                        new_count += 500
                else: #다음 좌/우
                    if before[2] == 0 or before[2] == 1:
                        new_count += 500
                new_count += 100

                if visited[before[0] + d[0]][before[1] + d[1]][i_d] > new_count:
                    visited[before[0] + d[0]][before[1] + d[1]][i_d] = new_count
                    q.put([before[0] + d[0], before[1] + d[1], i_d, new_count])

    return min(visited[end[0]][end[1]].values())


#11 번 runtime error
# from collections import defaultdict
# from queue import Queue

# #방향의 차이도 고려해야함
# def solution(board):
    
#     #상, 하, 좌, 우
#     di = [[-1, 0], [1, 0], [0, -1], [0, 1]] # 0, 1, 2, 3 #-1은 아무곳이나
#     now = [0, 0, -1 , 0] #count
#     l = len(board)
#     end = [l - 1, l - 1]
#     visited = defaultdict(lambda : defaultdict(lambda : defaultdict(lambda : float('INF')))) #최댓값 가격 세팅
    
#     q = Queue()
#     q.put(now)
#     visited[now[0]][now[1]][-1] = 0
#     visited[now[0]][now[1]][0] = 0
#     visited[now[0]][now[1]][1] = 0
#     visited[now[0]][now[1]][2] = 0
#     visited[now[0]][now[1]][3] = 0
    
#     while q.qsize():
        
#         before = q.get()
#         count = before[3]
        
#         if visited[before[0]][before[1]][before[2]] < count:
#             count = visited[before[0]][before[1]][before[2]]
            
#         for i_d, d in enumerate(di): #다음 행선지
#             #꺾기 가능 여부
#             if 0 <= before[0] + d[0]<= l-1 and 0<= before[1] + d[1] <= l - 1 and board[before[0] + d[0]][before[1] + d[1]] != 1:
#                 new_count = count
#                 if i_d == 0 or i_d == 1: #다음 상/하
#                     if before[2] == 2 or before[2] == 3: 
#                         new_count += 500
#                 else: #다음 좌/우
#                     if before[2] == 0 or before[2] == 1:
#                         new_count += 500
#                 new_count += 100
                   
#                 if visited[before[0] + d[0]][before[1] + d[1]][i_d] >= new_count:
#                     visited[before[0] + d[0]][before[1] + d[1]][i_d] = new_count
#                     q.put([before[0] + d[0], before[1] + d[1], i_d, new_count])
                    
                    
#     return visited[end[0]][end[1]].values()



# from collections import defaultdict
# from queue import Queue

# #방향의 차이도 고려해야함
# def solution(board):
    
#     #상, 하, 좌, 우
#     di = [[-1, 0], [1, 0], [0, -1], [0, 1]] # 0, 1, 2, 3 #-1은 아무곳이나
#     now = [0, 0, -1 , 0] #count
#     l = len(board)
#     end = [l - 1, l - 1]
#     visited = defaultdict(lambda : defaultdict(lambda : float('INF'))) #최댓값 가격 세팅
#     vis = defaultdict(lambda : defaultdict(lambda: defaultdict(bool)))
    
#     q = Queue()
#     q.put(now)
#     visited[now[0]][now[1]] = 0
    
#     while q.qsize():
        
#         before = q.get()
#         count = before[3]
        
#         if visited[before[0]][before[1]] < count:
#             count = visited[before[0]][before[1]]
            
#         for i_d, d in enumerate(di): #다음 행선지
#             #꺾기 가능 여부
#             if 0 <= before[0] + d[0]<= l-1 and 0<= before[1] + d[1] <= l - 1 and board[before[0] + d[0]][before[1] + d[1]] != 1:
#                 new_count = count
#                 if i_d == 0 or i_d == 1: #다음 상/하
#                     if before[2] == 2 or before[2] == 3: 
#                         new_count += 500
#                 else: #다음 좌/우
#                     if before[2] == 0 or before[2] == 1:
#                         new_count += 500
#                 new_count += 100
                   
#                 if visited[before[0] + d[0]][before[1] + d[1]] >= new_count:
#                     visited[before[0] + d[0]][before[1] + d[1]] = new_count
#                     q.put([before[0] + d[0], before[1] + d[1], i_d, new_count])
                    
#                 if not vis[before[0] + d[0]][before[1] + d[1]][i_d]:
#                     vis[before[0] + d[0]][before[1] + d[1]][i_d] = True
                    
#     return visited[end[0]][end[1]]