def solution(n):
    memorization = [0 for _ in range(n + 1)]

    for i, _ in enumerate(memorization):
        if i == 0 or i == 1:
            continue

        memorization[i] = memorization[i-1] + 1
        
        if i % 3 == 0:
            memorization[i] = min(memorization[i], memorization[i // 3] + 1)
        
        if i % 2 == 0:
            memorization[i] = min(memorization[i], memorization[i // 2] + 1)

    return memorization[n]


print(solution(int(input())))