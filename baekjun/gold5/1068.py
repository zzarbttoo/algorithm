
# root가 0이 아닐 경우 고려 x
# def solution(num_hash, del_num, parent_list):

#     count = 0

#     def dfs(node):
#         nonlocal count
#         if node == del_num:
#             if len(num_hash[parent_list[node]]) == 1:
#                 count += 1
#             return
        
#         if num_hash[node]:
#             for num in num_hash[node]:
#                 dfs(num)
#         else:
#             count += 1


#     dfs(0)
#     print(count)

#solution(num_hash, del_num, parent_list)

from collections import defaultdict

def solution():

    N = int(input())
    parent_list = list(map(int, input().split()))
    num_hash = defaultdict(list)
    count_hash = defaultdict(int)
    count = 0

    for idx, num in enumerate(parent_list):
        if num == -1 : continue
        num_hash[num].append(idx)
        count_hash[num] += 1

    del_num = int(input())
    del_hash = defaultdict(int)

    #삭제할 노드에 대해서만 처리
    def dfs(node):
        del_hash[node] = -1

        for num in num_hash[node]:
            dfs(num)

    dfs(del_num)

    for i in range(N):
        if count_hash[i] == 0 and del_hash[i] == 0:
            count += 1
    
    if count_hash[parent_list[del_num]] == 1:
        count += 1
    
    return count

print(solution())