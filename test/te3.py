from collections import defaultdict

def solution():
    N = int(input())
    S = input()
    me = defaultdict(lambda : defaultdict(int))
    E_cnt = 0
    E_nums = 0
    E_idx = -1
    W, H, E = 'W', 'H', 'E'

    for i, s in enumerate(S):
        me[i][W] = me[i-1][W]
        me[i][H] = me[i-1][H]
        me[i][E] = me[i-1][E]

        if s == 'W':
            me[i][s] = me[i - 1][s] + 1
        if s == 'H':
            me[i][s] = (me[i - 1][s] + 1) * (me[i - 1][W])
        if s == 'E':
            E_nums += 1
            if E_cnt == 0:
                E_idx = i
                E_cnt += 1
            elif E_cnt == 1:
                E_cnt += 1
            else:
                me[i][s] = (me[i - 1][s] + 1) * (me[i - 1][H])

    print(me[E_idx][H] * (E_nums - 1) + me[N - 1][E])



solution()