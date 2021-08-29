# import sys 
# input = sys.stdin.readline

# def solution(m, n, map_list):

#     memoization = [[0 for _ in range(n)] for _ in range(m)]
#     memoization[0][0] = 1

#     for i in range(0, m):
#         for j in range(0, n):
#             if i == 0:
#                 if j!= 0 and map_list[i][j] < map_list[i][j-1]:
#                     memoization[i][j] += memoization[i][j-1]
#             elif i == m-1:
#                 if j != 0 and map_list[i][j] < map_list[i][j-1]:
#                     memoization[i][j] += memoization[i][j-1]
#                 if map_list[i-1][j] > map_list[i][j]:
#                     memoization[i][j] += memoization[i-1][j]
#             else:
#                 if map_list[i-1][j] > map_list[i][j]:
#                     memoization[i][j] += memoization[i-1][j]
#                 if map_list[i][j-1] > map_list[i][j]:
#                     memoization[i][j] += memoization[i][j-1]
#                 if j != 0 and map_list[i][j-1] < map_list[i][j]:
#                     memoization[i][j-1] += memoization[i][j]

#     print(memoization[m-1][n-1])

def solution(m, n, map_list):

    #상하좌우
    direction_list = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    memoization = [[-1 for _ in range(n)] for _ in range(m)] #-1은 도착한 적 없다는 것을 알려줌

    def dfs(x, y):
        nonlocal m, n, map_list, direction_list

        if x == m-1 and y == n-1:
            return 1

        if memoization[x][y] != -1:
            return memoization[x][y]
        else:
            memoization[x][y] = 0
        
        for direction in direction_list:
            after_x , after_y = direction[0] + x, direction[1] + y
            if 0 <= after_x < m and 0 <= after_y < n:
                if map_list[after_x][after_y] < map_list[x][y]:
                    memoization[x][y] += dfs(after_x, after_y)
        
        return memoization[x][y]
    
    print(dfs(0, 0))

m, n = map(int, input().split())

map_list = []
for i in range(m):
    map_list.append(list(map(int, input().split())))


solution(m, n, map_list)

# m, n = 4, 5
# map_list = [[50, 45 ,37 ,32 ,30], [35, 50, 40 ,20 ,25], [30, 30 ,25 ,17, 28], [27, 24, 22 ,15, 10]]
# solution(m, n, map_list)

# m, n = 1, 1
# map_list = [[1]]
# solution(m, n, map_list)


# m, n = 10, 10
# map_list = [
#     [20 ,19 ,18 ,17 ,16 ,15 ,14 ,13 ,12 ,11 ],
#     [19 ,18 ,17 ,16 ,15 ,14 ,13 ,12 ,11 ,10 ],
#     [18, 17 ,16 ,15, 14, 13, 12, 11, 10, 9],
#     [17 ,16 ,15 ,14 ,13 ,12 ,11 ,10  ,9  ,8 ],
#     [16 ,15 ,14 ,13 ,12 ,11 ,10 , 9  ,8  ,7 ],
#     [15 ,14 ,13 ,12 ,11 ,10  ,9 , 8 , 7 , 6],
#     [14 ,13 ,12 ,11 ,10 , 9 , 8  ,7 , 6  ,5 ],
#     [13 ,12 ,11 ,10 , 9  ,8  ,7 , 6 , 5  ,4 ],
#     [12 ,11 ,10 , 9  ,8 , 7  ,6  ,5 , 4  ,3 ],
#     [11 ,10  ,9  ,8  ,7  ,6 , 5 , 4 , 3  ,2 ]
#     ]

# solution(m, n, map_list)



# m, n = 4, 4

# map_list = [
# [9, 8, 7, 6],
# [8, 7, 6, 5],
# [7, 6, 5, 4],
# [6, 5, 4, 3]
# ]

# solution(m, n, map_list)