
def input_():
    N = int(input())
    nums = []

    for _ in range(N):
        nums.append(list(map(int, input().split())))
    
    return N, nums
    

from collections import defaultdict

def solution():
    N, nums = input_()
    me = defaultdict(lambda : defaultdict(bool))

    coor = {0 : [1, 0], 1 : [0, -1], 2 : [-1, 0], 3 : [0, 1]}
    dire = {0 : 1, 1: 2, 2 : 3, 3 : 0}

    for num in nums:
        x, y, d, c = num
        b_d = [d]
        me[x][y] = True
        x, y = x + coor[d][0], y + coor[d][1]
        me[x][y] = True

        for _ in range(c):
            a_d = []
            for before in b_d[::-1]:
                a_d.append(dire[before])
                x, y = x + coor[dire[before]][0], y + coor[dire[before]][1]
                me[x][y] = True
            b_d += a_d

    points = []

    for k, v in me.items():
        for k_k, k_v in v.items():
            if k_v: points.append([k, k_k])

    answer = 0

    for point in points:
        x, y = point
        if me[x][y + 1] and me[x + 1][y] and me[x + 1][y + 1]: answer += 1
    
    print(answer)
                
    
        

















        

    


    



solution()
