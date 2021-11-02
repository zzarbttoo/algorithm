from collections import defaultdict

def solution(N, M, war_array):
    white, blue = 0, 0
    temp_dict = {'W' : 0, 'B' : 0}
    memoization = defaultdict(lambda : defaultdict(int))
    direction = [[0, 1], [1, 0], [-1, 0], [0,-1]]

    def dfs(row, col, team):
        nonlocal white, blue, memoization, war_array, N, M, temp_dict
        memoization[row][col] = -1
        temp_dict[team] += 1
        
        for direct in direction:
            next_row, next_col = row + direct[0], col + direct[1]
            if 0 <= next_row < M and 0 <= next_col < N and war_array[next_row][next_col] == team and memoization[next_row][next_col] == 0:
                dfs(next_row, next_col, team)


    for i in range(M):
        for j in range(N):
            if memoization[i][j] == 0:
                dfs(i, j, war_array[i][j])
                #print(temp_dict)
                white += temp_dict['W'] ** 2
                blue += temp_dict['B'] ** 2
                temp_dict = {'W' : 0, 'B' : 0}
        
    
    print(white, blue)
                
N, M = map(int, input().split())
war_array = []
for _ in range(M):
    war_array.append(input())

solution(N, M, war_array)

# N, M = 5, 5
# war_array = ["WBWWW", "WWWWW", "BBBBB", "BBBWW", "WWWWW"]

# solution(N, M, war_array)

