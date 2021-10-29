
# def solution(koong_list):
#     memoization = defaultdict(lambda : defaultdict(int))
#     memoization[0][0] = 0
#     memoization[1][0] = koong_list[0][0]
#     memoization[0][1] = koong_list[0][1]

#     N = len(koong_list)

#     def dfs(idx, white, black):
#         #print("idx ::: " + str(idx) + " N ::: " + str(N))
#         #print("white ::: " + str(white) + "black ::: " + str(black))
#         #print("memoization ::: " + str(memoization[white][black]))

#         if black < 15 and white < 15 and idx < N - 1:
#             dfs(idx + 1, black, white)
#             if white < 15: 
#                 #memoization[white + 1][black] = max(memoization[white + 1][black], memoization[white][black] + koong_list[idx][0])
#                 #print(memoization[white + 1][black])
#                 dfs(idx + 1, black, white + 1)
#             if black < 15:
#                 #memoization[white][black + 1] = max(memoization[white][black + 1], memoization[white][black] + koong_list[idx][1])
#                 #print(memoization[white + 1][black])
#                 dfs(idx + 1, black + 1, white)

#     dfs(0, 0, 0)
#     print(memoization[14][14])

from collections import defaultdict

def solution(koong_list):
    N = len(koong_list)
    memoization = defaultdict(lambda : defaultdict(lambda : defaultdict(int)))

    def dfs(idx, white, black):
        if idx >= N:
            return
        if white == 14 and black == 14:
            return 
        memoization[idx + 1][white][black] = memoization[idx][white][black]
        if white < 14:
            memoization[idx + 1][white + 1][black] = max(memoization[idx][white][black] + koong_list[idx][0], memoization[idx + 1][white + 1][black])
            dfs(idx + 1, white + 1, black)
        if black < 14:
            memoization[idx + 1][white][black + 1] = max(memoization[idx][white][black] + koong_list[idx][1], memoization[idx + 1][white][black + 1])
            dfs(idx + 1, white, black + 1)


    dfs(0, 0, 0)

    answer = 0   

    for idx in range(N):
        answer = max(memoization[idx][14][14], answer)
    
    print(answer)

    



koong_list = [
[87, 84],
[66, 78],
[86, 94],
[93, 87],
[72 ,100],
[78, 63],
[60, 91],
[77, 64],
[77, 91],
[87, 73],
[69, 62],
[80, 68],
[81, 83],
[74, 63],
[86, 68],
[53, 80],
[59, 73],
[68, 70],
[57, 94],
[93, 62],
[74, 80],
[70, 72],
[88, 85],
[75, 99],
[71, 66],
[77, 64],
[81, 92],
[74, 57],
[71, 63],
[82, 97],
[76, 56]]

solution(koong_list)