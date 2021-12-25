# from itertools import permutations
# from collections import deque
# from collections import defaultdict

# def solution(board, r, c):
    
#     num_card = defaultdict(list)
    
#     #for row in board:
#         #for num in row:
#             #if num!= 0: num_card[num].append([])
#     for row in range(4):
#         for col in range(4):
#             if board[row][col] != 0: num_card[board[row][col]].append([row, col])
    
#     answer = float("INF")
    
#     num_order = permutations(num_card.keys())
    
#     for order in num_order:
        
#         #현재 위치(r, c), 지워야 할 순서번호, 이동 수
#         queue = deque([[r, c, 0, 0]])
        
#         while queue:
#             del_now = queue.popleft()
            
#             if del_now[3] < len(order):
                
#                 next_1 = del_now[::]
#                 for i, num in enumerate(num_card[order[del_now[3]]]):
#                     if next_1[0] == num[0] and next_1[1] == num[1]:
#                         next_1[2] += 1
#                     elif next_1[0] == num[0] or next_1[1] == num[1]:
#                         next_1[2] += 2
#                     else:
#                         next_1[2] += 3
#                     next_1[0], next_1[1] = num[0], num[1]
#                 next_1[3] += 1
                
#                 queue.append(next_1)
                
#                 next_2 = del_now[::]
#                 for i, num in enumerate(num_card[order[del_now[3]]]):
#                     if next_2[0] == num[0] and next_2[1] == num[1]:
#                         next_2[2] += 1
#                     elif next_2[0] == num[0] or next_2[1] == num[1]:
#                         next_2[2] += 2
#                     else:
#                         next_2[2] += 3
#                     next_2[0], next_2[1] = num[0], num[1]
#                 next_2[3] += 1
                
#                 queue.append(next_2)
                
#             else: 
#                 answer = min(answer, del_now[2])
                
                
#     return answer

from itertools import permutations
from collections import deque 
from collections import defaultdict

def solution(board, r, c):
    
    card = defaultdict(list)
    
    for row in range(4):
        for col in range(4):
            if board[row][col] != 0:
                card[board[row][col]].append([row, col])
    
    key_order = permutations(card.keys())
    
    answer = float("INF")
    
    for order in key_order:
        queue = deque([])
        queue.append([r, c, 0, 0])
        
        while queue:
            now = queue.popleft()
            
            if now[3] < len(order):
                del_num = order[now[3]]
                first, second = now[::], now[::]
                
                # TODO : 가는 길에 다른 카드가 막고 있는 것 고려
                for i, num in enumerate(card[del_num]):
                    if num[0] == first[0] and num[1] == first[1]:
                        first[2] += 1
                    elif num[0] == first[0] or num[1] == first[1]:
                        first[2] += 2
                    else:
                        first[2] += 3
                    
                    first[0], first[1] = num[0], num[1]
                    
                    if i == 1:
                        first[3] += 1
                        queue.append(first)

                for i, num in enumerate(card[del_num][::-1]):
                    if num[0] == second[0] and num[1] == second[1]:
                        second[2] += 1
                    elif num[0] == second[0] or num[1] == second[1]:
                        second[2] += 2
                    else:
                        second[2] += 3
                    
                    second[0], second[1] = num[0], num[1]
                    
                    if i == 1:
                        second[3] += 1
                        queue.append(second)
            else:
                answer = min(answer, now[2])

    return answer




            
            
                