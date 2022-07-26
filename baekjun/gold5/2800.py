# def solution():
#     form = input()

#     stack = []

#     for st in form:
#         if st == ')':
#             substitution = []
#             while stack:
#                 tmp = stack.pop()
#                 if tmp == '(':
#                     break
#                 substitution.append(tmp)
#             stack.append(substitution)
#         else:
#             stack.append(st)
            
    
#     #뒤 -> 앞으로 pop 해야한다 
#     def dfs(sub):
#         for s in sub[::-1]:
#             print(s)
    

#     dfs(stack)

from itertools import combinations

def solution():
    form = input()

    stack = []
    sub = []

    for idx, st in enumerate(form):
        if st == ')':
            while True:
                tmp = stack.pop()
                if tmp[0] == '(':
                    sub.append([tmp[1], idx])
                    break
        else:
            stack.append([st, idx])

    # print(sub)
    
    combs = []

    for i in range(1, len(sub) + 1):
        combs.append(list(combinations(sub, i)))
    
    # print(combs)

    answer_set = set()

    for comb in combs:
        for lst in comb:
            target = list(form)
            for l in lst:
                target[l[0]], target[l[1]] = '', ''
            answer_set.add(''.join(target))

    for ans in sorted(list(answer_set)):
        print(ans)

solution()