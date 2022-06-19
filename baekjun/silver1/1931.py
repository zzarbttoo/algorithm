def solution():
    N = int(input())
    M = []

    for _ in range(N):
        M.append(list(map(int, input().split())))

    M.sort()
    stack = []
    stack.append(M[0])

    for m in M[1:]:
        print(m)
        if stack[-1]:
            before = stack[-1]
            if m[0] < before[1]:
                stack.append(m)
            else:
                if before[1] > m[1]:
                    stack.pop()
                    stack.append(m)

    print(stack)

    

solution()
