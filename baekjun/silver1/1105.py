def solution(L, R):

    count = 0

    if len(R) == len(L):
        for (i, j) in zip(L, R):
            if i != j:
                break
            if i == "8" and j == "8":
                count += 1


    return count


L, R = input().split()
print(solution(L, R))

#1888 1887
