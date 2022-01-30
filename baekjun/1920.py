
from sys import stdin

def input_nums():
    N = int(stdin.readline())
    A = list(map(int, stdin.readline().split()))
    M = int(stdin.readline())
    D = list(map(int, stdin.readline().split()))

    return N, A, M, D

# def solution():
#     N, A, M, D = input_nums()

#     A = set(A)

#     for d in D:
#         if d in A: print(1)
#         else: print(0)
    
def solution():
    N, A, M, D = input_nums()
    A.sort()

    def binary(num):
        nonlocal N, A

        left, right = 0, len(A) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if A[mid] == num: return 1
            if A[mid] < num: left = mid + 1
            elif A[mid] > num: right = mid - 1

        return 0

    for num in D:
        print(binary(num))

solution()