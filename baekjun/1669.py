# def solution(monkey, dog):

#     min_count = 2 ** 31

#     def dfs(now_height, count, add_num):

#         nonlocal min_count

#         if now_height == dog:
#             min_count = min(min_count, count)
#             return
        
#         if count == 0:
#             dfs(now_height + 1, count + 1, 1)

#         if now_height > dog:
#             return 
#         if now_height < dog:
#                 next_count = count + 1
#                 if add_num + 1 >= 1:
#                     dfs(now_height + add_num + 1, next_count, add_num + 1)
#                 if add_num >= 1:
#                     dfs(now_height + add_num, next_count, add_num)
#                 if add_num -1>= 1:
#                     dfs(now_height + add_num -1 , next_count, add_num -1)

#     dfs(monkey, 0, 0)
#     print(min_count)




# monkey, dog = map(int, input().split())
# solution(monkey, dog)