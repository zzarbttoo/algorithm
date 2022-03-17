def input_():
    str = input()
    num = int(input())
    nums = input()[1:-1].split(',')
    if nums == "".split(','): nums = []

    return str, num, nums

def main():
    N = int(input())
    answer = []
    for _ in range(N):
        answer.append(solution())
    
    for a in answer:
        print(a)

from collections import deque

def solution():
    str, num, nums = input_()
    #str, num ,nums = "RDD", 4, ["1", "2", "3", "4"]
    nums = deque(nums)

    n_r = True

    for s in str:
        if s == 'R':
            if n_r: n_r = False
            else: n_r = True
            continue

        if len(nums) == 0: return "error"

        if n_r:
            nums.popleft()
        else:
            nums.pop()
    
    nums = list(nums)

    if not n_r:
        nums = nums[::-1]

    return "[" + ','.join(nums) + "]"

main()



# def solution():

#     def inner():
#         str, num ,nums = input_()

#         orders = []   
#         before = 0

#         for s in str:
#             if s == 'R':
#                 if before != 0:
#                     orders.append(before)
#                     before = 0
#                 orders.append(s)
#             else:
#                 before += 1
        
#         if before != 0: orders.append(before)
#         if len(nums) == 0 and len(orders) != 0: return "error"

#         sw = True
        
#         for o in orders:
#             if o == 'R':
#                 if len(nums) == 0: return "error"
#                 if sw: sw = False
#                 else: sw = True
#                 continue
            
#             if o > len(nums): return "error"
            
#             if sw:
#                 nums = nums[o:]
#             else:
#                 nums = nums[:o][::-1]
        
#         if orders and orders[-1] == "R" and not sw: nums = nums[::-1]
            
#         return "[" + ','.join(nums) + "]"


#     N = int(input())
#     answer = []

#     for _ in range(N):
#         answer.append(inner())
#     for a in answer:
#         print(a)



# solution()
