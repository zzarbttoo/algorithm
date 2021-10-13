def solution(N, L):

    #print(N // L)
    now = L

    while now <= 100:

        #짝수 -> 
        point = N // now

        if now % 2 == 0:
            if point - (now / 2) < 0:
                break
            if 2 * point + 1 == N / (now / 2):
                #print("even porint ::: " + str(point))
                start = point - (now // 2)
                return " ".join([num for num in range(start , start + now)])
        # 홀수
        else:
            if (point - 1) - (now - 1) / 2 < 0:
                break
            if point == N // now:
                start = int(point - (now - 1) // 2)
                return " ".join([num for num in range(start ,start + now)])
        now += 1 

    return -1

def solution(N, L):

    for length in range(L, 101):
        start = (N - length * (length -1) / 2) / length
        int_start = int(start)

        if start == int_start and int_start >= 0:
            return " ".join(map(str, [num for num in range(int_start, int_start + length)]))

    return -1 



N , L = map(int, input().split())
print(solution(N, L))

#k 5050 99