def solution(n, stair_array):

    count_array = [0 for _ in range(n)]

    if n == 1:
        return stair_array[0]
    
    if n == 2:
        return stair_array[0] + stair_array[1]

    count_array[0] = stair_array[0]
    count_array[1] = stair_array[0] + stair_array[1]
    count_array[2] = max((stair_array[0] + stair_array[2]), (stair_array[1] + stair_array[2]))

    for i, _ in enumerate(count_array):
        if i == 0 or i==1 or i==2:
            continue
        count_array[i] = max((count_array[i-3] + stair_array[i-1] + stair_array[i]), (count_array[i-2] + stair_array[i]))
    
    return count_array[n-1]

n = int(input())
stair_array = []

for i in range(n):
    stair_array.append(int(input()))

print(solution(n, stair_array))




