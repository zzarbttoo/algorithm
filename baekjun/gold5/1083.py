#https://www.acmicpc.net/problem/1083



# N, A, S = 5, [3, 5, 1, 2, 4], 2
# N, A, S = 10, [19, 20, 17, 18, 15, 16, 13, 14, 11, 12], 5

N = int(input())
A = list(map(int, input().split()))
S = int(input())


idx = 0


while True:
    max_value = max(A[idx: idx + S + 1])
    max_value_index = A[0:idx + S + 1].index(max_value)
    used = max_value_index - idx    

    A.pop(max_value_index)
    A.insert(idx, max_value)

    S -= used 
    idx += 1 

    if S == 0 or idx >= len(A):
        break

print(' '.join(map(str, A)))




# idx = 0
# max_value = max(A[idx:idx + S])
# max_value_index = A[0:idx + S].index(max_value)
# used = max_value_index - idx

# A.pop(max_value_index)
# A.insert(idx, max_value)

# S = S - used
# idx += 1 

# print(A)
# print(idx, S)


# max_value = max(A[idx:idx + S])
# max_value_index = A[0:idx + S].index(max_value)
# used = max_value_index - idx

# print(max_value, max_value_index, used)

# A.pop(max_value_index)
# A.insert(idx, max_value)

# S = S - used
# idx += 1 


# max_value = max(A[idx:idx + S])
# max_value_index = A[0:idx + S].index(max_value)
# used = max_value_index - idx

# print(max_value, max_value_index, used)

# A.pop(max_value_index)
# A.insert(idx, max_value)

# S = S - used
# idx += 1 













