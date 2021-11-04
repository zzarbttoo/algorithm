from collections import defaultdict

def solution():

    N = int(input())
    crane_limit = list(map(int, input().split()))
    M = int(input())
    box_weight = list(map(int, input().split()))
    box_weight.sort(reverse = True)
    crane_limit.sort(reverse = True)

    visited = defaultdict(int)
    count = 0

    while M > 0:
        now_crane = 0
        for i, num in enumerate(box_weight):
            if now_crane == N: break
            if visited[i] == 0 and crane_limit[now_crane] >= num:
                M -= 1
                visited[i] = -1
                now_crane += 1
            if now_crane == 0 and crane_limit[now_crane] < num:
                return -1
        count += 1
    return count
            
print(solution())


# 3
# 6 8 9
# 9
# 1 2 3 4 5 6 7 8 9







    # print("box weight :: " + str(box_weight))
    # print("crane limit :: " + str(crane_limit))

    # while box_weight:

    #     for idx, crane in enumerate(crane_limit):
    #         if idx == N - 1 and box_weight and box_weight[-1] > crane:
    #             if idx == N - 1: return -1
    #             break
    #         if box_weight and box_weight[-1] <= crane:
    #             box_weight.pop()

    #         #print(box_weight.pop())
    #     answer += 1
    