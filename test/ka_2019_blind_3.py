from collections import defaultdict
from itertools import combinations

def solution(relation):

    answer = 0

    row_len = len(relation)
    col_len = len(relation[0])
    col_list = [str(i) for i in range(0, col_len)]
    vari_list = []
    visited = defaultdict(bool)

    def is_unique_and_not_visited(varification, sub_vari):

        nonlocal visited, relation
        count = defaultdict(int)

        for row in relation:
            temp = ""
            for vari in varification:
                temp+= str(row[int(vari)])
            count[temp] += 1
            if count[temp] >= 2: return False

        for sub in sub_vari:
            if visited[sub] == True:
                return False
        return True

    for i in range(1, col_len + 1):
        vari_list += list(combinations(col_list, i))

    for vari in vari_list:
        temp = []
        for j in range(1, len(vari) + 1):
            temp += list(combinations(vari, j))
        if is_unique_and_not_visited(vari, temp):
            visited[vari] = True
            answer += 1

    return answer

# # from collections import defaultdict

# # def solution(relation):
    
# #     answer = 0
# #     row_len = len(relation)
# #     col_len = len(relation[0])
    
# #     def is_unique(col_list):
# #         nonlocal relation
        
# #         uni = defaultdict(int)
        
# #         for row in relation:
# #             key_str = ""
# #             for col in col_list:
# #                 key_str += str(row[col])
# #             uni[key_str] += 1
# #             if uni[key_str] >= 2:
# #                 return False
# #         else:
# #             return True
    
# #     def dfs(before_list, now_idx):
        
# #         nonlocal relation, row_len, col_len, answer
        
# #         before_list.append(now_idx)
        
# #         #지금이 unique
# #         if is_unique(before_list):
# #             print(before_list)
# #             answer += 1
# #             return
        
# #         #아니면 다음
        
# #         for next_idx in range(now_idx + 1, col_len):
# #             next_list = before_list[::]
# #             dfs(next_list, next_idx)
    
    
# #     for i in range(0, col_len):
# #         dfs([], i)
        
# #     return answer


# from collections import defaultdict
# from itertools import combinations

# def solution(relation):
    
#     answer = 0
    
#     row_len = len(relation)
#     col_len = len(relation[0])
#     col_list = [str(i) for i in range(0, col_len)]
#     com_list = []
#     vari_list = []
#     visited = defaultdict(bool)
    
#     def is_unique_and_not_visited(varification):
        
#         nonlocal visited, relation
#         count = defaultdict(int)
        
#         for row in relation:
#             temp = ""
#             for vari in varification:
#                 if visited[vari] == True:
#                     return False
#                 temp+= str(row[int(vari)])
#             count[temp] += 1
#             if count[temp] >= 2: return False
#         return True
    
    
#     for i in range(1, col_len + 1):
#         vari_list += list(combinations(col_list, i))
    
#     for vari in vari_list:
#         if is_unique_and_not_visited(vari):
#             for col in vari:
#                 visited[col] = True
#             answer += 1
            
#     return answer

# print(solution([['a',1,'aaa','c','ng'],['b',1,'bbb','c','g'],['c',1,'aaa','d','ng'],['d',2,'bbb','d','ng']]))