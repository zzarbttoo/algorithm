from collections import defaultdict
import sys

input = sys.stdin.readline

def solution():

    N = int(input())
    A = list(map(int, input().split()))

    memo_b = defaultdict(int) #before
    memo_a = defaultdict(int) #after

    for idx in range(N):
        for b_idx in range(0, idx):
            if A[b_idx] < A[idx] and memo_b[b_idx] + 1>= memo_b[idx]:
                memo_b[idx] = memo_b[b_idx] + 1
    
    for idx in range(N - 1, -1, -1):
        for a_idx in range(N - 1, idx - 1, -1): 
            if A[a_idx] < A[idx] and memo_a[a_idx] + 1 >= memo_a[idx]:
                memo_a[idx] = memo_a[a_idx] + 1


    answer = -1
    for idx in range(N):
        t = memo_a[idx] + memo_b[idx] + 1
        if answer < t:
            answer = t

    print(answer)

solution()




