import collections
def solution(n, k, cmd):
    
    idx = collections.defaultdict(int)
    stack = []
    
    for i in range(n):
        idx[i] = i
    
    for com in cmd:
        if com == 'C':
            idx[k] = -1
            stack.append(k)
        elif com == 'Z':
            pop_num = stack.pop()
            idx[pop_num] = pop_num
        else:
            if com[0] == 'D':
                pass
            else:
                pass
         