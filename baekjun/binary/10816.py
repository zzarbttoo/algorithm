
from sys import stdin

def input_nums():
    N = int(stdin.readline())
    A = list(map(int, stdin.readline().split()))
    M = int(stdin.readline())
    D = list(map(int, stdin.readline().split()))

    return N, A, M, D

from collections import Counter

def solution():
    N, A, M, D = input_nums()
    a_l = []

    counter = Counter(A)

    for num in D:
        if num not in counter:
            a_l.append('0')
        else:
            a_l.append(str(counter[num]))
    
    print(' '.join(a_l))

solution()