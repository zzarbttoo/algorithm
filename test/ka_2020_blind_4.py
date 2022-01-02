# from collections import defaultdict

# def solution(n, build_frame):
    
#     #[start(0)/end(1), 기둥(0)/보(1), [연결 좌표]]
#     build = defaultdict(lambda : defaultdict(list))
    
#     #TODO : n 범위 내에 들어가나 확인
#     for frame in build_frame:
#         #추가 작업
#         if frame[3] == 1:
#             if frame[2] == 0: #기둥
#                 #땅에 붙어있거나
#                 if frame[1] == 0:
#                     print(frame)
#                     build[frame[0]][frame[1]].append([0, 0, frame[0], frame[1] + 1])
#                     build[frame[0]][frame[1] + 1].append([1, 0, frame[0], frame[1]])
#                     continue
#                 #기둥 위에 있거나 
#                 #보 한쪽에 있거나
#                 bridge_count = 0
#                 is_pillar = False
#                 for before in build[frame[0]][frame[1] + 1]:
#                     if before[0] == 1 and before[1] == 0:
#                         is_pillar = True
#                         break
#                     if before[1] == 1 and before[1] == 1:
#                         bridge_count += 1
#                 if is_pillar or bridge_count == 1:
#                     build[frame[0]][frame[1]].append([0, 0, frame[0], frame[1] + 1])
#                     build[frame[0]][frame[1] + 1].append([1, 0, frame[0], frame[1]])
#                     continue
#             else: #보 
#                 is_pillar = False
#                 left_bridge = False
#                 right_bridge = False
                
#                 #한쪽이 기둥 위에 있거나 
#                 for before in build[frame[0]][frame[1]]:
#                     if before[0] == 1 and before[1] == 0:
#                         is_pillar = True
#                         build[frame[0]][frame[1]].append([0, 1, frame[0], frame[1]])
#                         build[frame[0]][frame[1]].append([1, 1, frame[0] + 1, frame[1]])
#                         break
#                     if before[0] == 1 and before[1] == 1:
#                         left_bridge = True
                
#                 #양쪽이 보와 연결 되어있거나
#                 for before in build[frame[0] + 1][frame[1]]:
#                     if before[0] == 0 and before[1] == 1:
#                         right_bridge = True
#                 if left_bridge and right_bridge:
#                     build[frame[0]][frame[1]].append([0, 1, frame[0], frame[1]])
#                     build[frame[0]][frame[1]].append([1, 1, frame[0] + 1, frame[1]])
#         #삭제 작업
#         if frame[3] == 0:
#             if frame[2] == 0: #기둥
#                 pass
#             else: # 보
#                 pass
        
#         for i in range(n + 1):
#             for j in range(n + 1):
#                 for before in build[i][j]:
#                     if before and before[0] == 0:
#                         print(before)
        
                    
from collections import defaultdict 

def solution(n, build_frame):
    #x, y, 기둥(0)/보(1), start(0)/end(1) -> True, False
    build = defaultdict(lambda : defaultdict(lambda : defaultdict(lambda : defaultdict(bool))))
    
    #frame = x, y, 기둥/보(0/1), 삭제/설치(0/1)
    for frame in build_frame: # 0 기둥, 1 보
        if frame[3] == 1: #설치
            if frame[2] == 0: #기둥
                #땅에 붙어있거나
                if frame[1] == 0:
                    build[frame[0]][frame[1]][0][0] = True
                    build[frame[0]][frame[1] + 1][0][1] = True
                    continue
                #기둥 위거나 
                if build[frame[0]][frame[1]][0][1]:
                    build[frame[0]][frame[1]][0][0] = True
                    build[frame[0]][frame[1] + 1][0][1] = True
                    continue
                #보의 끝에 있거나
                if (build[frame[0]][frame[1]][1][0] == False and build[frame[0]][frame[1]][1][1]):
                    build[frame[0]][frame[1]][0][0] = True
                    build[frame[0]][frame[1] + 1][0][1] = True
                    continue
                if (build[frame[0]][frame[1]][1][0] and build[frame[0]][frame[1]][1][1] == True):
                    build[frame[0]][frame[1]][0][0] = True
                    build[frame[0]][frame[1] + 1][0][1] = True
                    continue
            else: #보
                #한쪽이 기둥 위에 있거나
                if build[frame[0]][frame[1]][0][1] or build[frame[0] + 1][frame[1]][0][1]:
                    build[frame[0]][frame[1]][1][0] = True
                    build[frame[0] + 1][frame[1]][1][1] = True
                    continue
                #양쪽이 보와 연결 돼있거나
                if build[frame[0]][frame[1]][1][1] and build[frame[0] + 1][frame[1]][1][0]:
                    build[frame[0]][frame[1]][1][0] = True
                    build[frame[0] + 1][frame[1]][1][1] = True
                    continue
        else: #삭제
            if frame[2] == 0: #기둥
                #위에 보, 기둥 있는 경우 고려
                #기둥 있는데 보의 끝 지점이 아닐 경우(중간)
                if build[frame[0]][frame[1] + 1][0][0]:
                    if build[frame[0]][frame[1] + 1][1][1] == False:
                        continue
                    if build[frame[0]][frame[1] + 1][1][1] and build[frame[0]][frame[1] + 1][1][0]:
                        continue
                #보가 하나만 연결 돼있을 때
                if build[frame[0]][frame[1] + 1][1][1] and build[frame[0]][frame[1] + 1][1][0] == False:
                    continue
                if build[frame[0]][frame[1] + 1][1][1] == False and build[frame[0]][frame[1] + 1][1][0]:
                    continue
                build[frame[0]][frame[1]][0][0] = False
                build[frame[0]][frame[1] + 1][0][1] = False
            else: #보
                #위에 기둥
                if build[frame[0]][frame[1]][0][0] and build[frame[0]][frame[1]][0][1] == False:
                    continue
                #위에 보 
                if build[frame[0]][frame[1]][1][1] and build[frame[0] - 1][frame[1]][1][1] == False:
                    continue
                if build[frame[0] + 1][frame[1]][1][0] and build[frame[0] + 1][frame[1]][0][1] == False:
                    continue
                    
                build[frame[0]][frame[1]][1][0] = False
                build[frame[0] + 1][frame[1]][1][1] = False
            
        
    answer = []
    
    for i in range(n + 1):
        for j in range(n + 1):
            for kind in [0, 1]:
                if build[i][j][kind][0]:
                    #print((i, j, kind))
                    answer.append([i, j, kind])
    return answer