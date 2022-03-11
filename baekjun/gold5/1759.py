from sys import stdin

def input_():
    L, C = map(int, stdin.readline().split())
    W = list(stdin.readline().split())
    return L, C, W

from collections import defaultdict
import itertools

def solution():
    #L, C, W = 4, 6, ['a', 't', 'c', 'i', 's', 'w']
    L, C, W = input_()
    vo = set(['a', 'i', 'e', 'o', 'u'])
    n_v, n_c = [], []
    t_v, t_c = [], []

    for w in W:
        if w in vo:
            n_v.append(w)
        else:
            n_c.append(w)

    for i in range(1, len(n_v) + 1):
        t_v += list(itertools.combinations(n_v, i))

    for j in range(2, len(n_c) + 1):
        t_c += list(itertools.combinations(n_c, j))
    
    answer = []

    print(t_v)
    print(t_c)

    for v in t_v:
        for c in t_c:
            temp = ''.join(sorted(v + c))
            if len(temp) == L: answer.append(temp)

    answer.sort()   

    for a in answer:
        print(a)
    
solution()