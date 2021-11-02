from collections import defaultdict

def solution(N):
    left_lion , right_lion, no_lion = defaultdict(int), defaultdict(int), defaultdict(int)
    left_lion[1], right_lion[1], no_lion[1] = 1, 1, 1

    for row in range(2, N + 1):
        left_lion[row] = (right_lion[row - 1] + no_lion[row - 1]) % 9901
        right_lion[row] = (left_lion[row - 1] + no_lion[row - 1]) % 9901
        no_lion[row] = (no_lion[row-1] + left_lion[row - 1] + right_lion[row - 1]) % 9901

    print((left_lion[N] + right_lion[N] + no_lion[N]) % 9901)


solution(int(input()))



