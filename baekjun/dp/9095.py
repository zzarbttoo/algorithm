def solution(n):

    count_array = [0 for _ in range(n+1)]
    count_array[0] = 1

    for i in range(n+2):

        if i+1 <= n:
            count_array[i+1] += count_array[i]
        if i+2 <= n:
            count_array[i+2] += count_array[i]
        if i+3 <= n:
            count_array[i+3] += count_array[i]     
        
    return count_array[n]

n = int(input())
answer = []
for i in range(n):
    answer.append(int(input()))

for num in answer:
    print(solution(num))






# n=4
# print(solution(n))

# n=7
# print(solution(n))

# n = 10
# print(solution(n))

# n = 2 
# print(solution(n))

# n = 1
# print(solution(n))

