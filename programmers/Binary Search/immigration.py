def solution(n, times):

    left= 0
    right = n * min(times)

    while left <= right:

        medium = left + (right - left) // 2
        fin_num = sum([medium // time for time in times])

        print("midium ::: " + str(medium))
        print("fin_num ::: " + str(fin_num))

        if fin_num >= n: #fin_num 과 n이 같지 않을 경우가 있다
            answer = medium
            right = medium - 1
            print("answer ::: " + str(answer))
        elif fin_num < n:
            left = medium + 1

    return answer


n = 6
times = [7, 10]

n = 2
times = [2, 1]

print(solution(n, times))

