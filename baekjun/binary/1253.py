from sys import stdin

def solution():
    N = int(stdin.readline())
    A = list(map(int, stdin.readline().split()))

    #N, A = 10, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    A.sort()
    count = 0

    for i, a in enumerate(A):
        left, right = 0, len(A) - 1

        while True:

            if left == i:
                left += 1
            if right == i:
                right -= 1
            
            if left >= right:
                break

            sum = A[left] + A[right]

            if sum == a:
                count += 1
                break
            if sum > a:
                right -= 1
            else:
                left += 1

    print(count)

solution()