def solution(n, time, price):

    memoization = [0 for _ in range(n)]
    max_num = 0

    for i in range(n):
        max_num = max(max_num, memoization[i])

        if i + time[i] > n:
            continue
        
        memoization[i + time[i]] = max(max_num + price[i], memoization[i])
    
    return max(memoization)
        

n = int(input())

time = []
price = []

for i in range(n):

    temp_1, temp_2= map(int, input().split())
    time.append(temp_1)
    price.append(temp_2)


print(solution(n, time, price))

# n = 7
# time = [3, 5, 1, 1, 2, 4, 2]
# price = [10, 20, 10, 20, 15, 40, 200]
# print(solution(n, time, price))

# n = 10
# param_array = [[1, 1], [1, 2], [1, 3], [1, 4], [1,5], [1,6], [1,7], [1,8], [1,9],[1,10]]

# print(solution(n, param_array))
