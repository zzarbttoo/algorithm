from sys import stdin
import heapq

def solution():

    N  = int(stdin.readline())
    nums = []

    for _ in range(N):
        nums.append(int(stdin.readline()))
    
    #N, nums= 7, [1, 5, 2, 10, -99, 7, 5]
    #N, nums = 6, [5, 4,4, 4, 3, 3]
    #N, nums = 1, [-1]
    #N, nums = 5, [1, 2, 3, 4, 5]


    left = []
    right = []
    count = 0



    for now in nums:
        #heapq.heappush(left, -now) #일단 좌측에 넣음

        if len(left) == 0 or len(right) == 0 or right[0] > now:
            heapq.heappush(left, -now) #일단 좌측에 넣음
        else:
            heapq.heappush(right, now) #일단 좌측에 넣음


        count += 1

        if count % 2 == 0: #짝수개
            if len(left) < len(right):
                heapq.heappush(left, - heapq.heappop(right))
            elif len(left) > len(right):
                heapq.heappush(right, -heapq.heappop(left))
        else: #홀수개
            if len(left) < len(right):
                while len(left) != len(right) + 1:
                    heapq.heappush(left, - heapq.heappop(right))
            else:
                while len(left) != len(right) + 1:
                    heapq.heappush(right, -heapq.heappop(left))
        print(-left[0])
            
solution() 