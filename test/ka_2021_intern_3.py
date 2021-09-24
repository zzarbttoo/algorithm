# import heapq

# def solution(n, k, cmd):
    
#     left_heap = []
#     right_heap = []
#     stack = []
#     temp_list= []
    
#     for i in range(0, k + 1):
#         heapq.heappush(left_heap, -i)
#         temp_list.append("O")
    
#     for i in range(k+1, n):
#         heapq.heappush(right_heap, i)
#         temp_list.append("O")
    
#     for com in cmd:
#         if com[0] == "C":
#             stack.append(- heapq.heappop(left_heap))
#             if right_heap:
#                 heapq.heappush(left_heap, - heapq.heappop(right_heap))
#         elif com[0] == "Z":
#             if stack[-1] > - left_heap[0]:
#                 heapq.heappush(right_heap, stack.pop())
#             else:
#                 heapq.heappush(left_heap, - stack.pop())
#         else:
#             temp_num = int(com[-1])
#             if com[0] == "U":
#                 for _ in range(temp_num):
#                     heapq.heappush(right_heap , - heapq.heappop(left_heap))
#             elif com[0] == "D":
#                 for _ in range(temp_num):
#                     heapq.heappush(left_heap, - heapq.heappop(right_heap))

#     for i in stack:
#         temp_list[i] = "X"
    
#     return "".join(temp_list)


# import heapq

# temp=[]

# for i in range(3):
#     heapq.heappush(temp, - i)

# print(temp)
# print(temp[0])
import heapq

def solution(n, k, cmd):
    
    left_heap = []
    right_heap = []
    stack = []
    temp_list= []
    
    for i in range(0, k + 1):
        heapq.heappush(left_heap, -i)
        temp_list.append("O")
    
    for i in range(k+1, n):
        heapq.heappush(right_heap, i)
        temp_list.append("O")
    
    for com in cmd:
        #print(com, left_heap, right_heap, stack)
        if com[0] == "C":
            stack.append(-heapq.heappop(left_heap))
            if right_heap:
                heapq.heappush(left_heap, - heapq.heappop(right_heap))
        elif com[0] == "Z":
            if left_heap and stack[-1] < - left_heap[0] :
                heapq.heappush(left_heap, - stack.pop())
            else:
                heapq.heappush(right_heap, stack.pop())
        else:
            temp_num = int(list(com.split())[1])
            #print(temp_num)
            if com[0] == "U":
                for _ in range(temp_num):
                    if left_heap:
                        heapq.heappush(right_heap , - heapq.heappop(left_heap))
            elif com[0] == "D":
                for _ in range(temp_num):
                    if right_heap:
                        heapq.heappush(left_heap, - heapq.heappop(right_heap))

    for i in stack:
        temp_list[i] = "X"
    
    return "".join(temp_list)