def solution(N, r, c):

    direction = [[0, 1], [2, 3]]

    def dfs(n, row, col):

        row_div, row_mod = divmod(row, 2 ** (n - 1))
        col_div, col_mod = divmod(col, 2 ** (n - 1))

        temp_num = ((2 ** (n - 1)) ** 2) * direction[row_div][col_div]
        #print("temp_num ::: " + str(temp_num))

        if n > 1:
            return temp_num + dfs(n-1, row_mod, col_mod)
        else:
            return temp_num



    answer = dfs(N, r, c)
    print(answer)


N, r, c = map(int, input().split())
solution(N, r, c)