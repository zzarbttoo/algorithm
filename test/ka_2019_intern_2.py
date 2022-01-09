from itertools import permutations
import re

def solution(expression):

    orders = permutations(['*', '-', '+'], 3)

    p_list = re.findall("\D", expression)
    n_list = re.findall("\d+", expression)
    answer = 0

    for order in orders:
        n_p = p_list[:]
        n_n = n_list[:]
        for o in order:
            idx = 0
            while len(n_p) > idx:
                if n_p[idx] == o:
                    del n_p[idx]
                    new = eval(n_n[idx] + o + n_n[idx + 1])
                    n_n[idx] = str(new)
                    del n_n[idx + 1]
                    idx = 0
                else:
                    idx += 1
        if abs(int(n_n[0])) > answer:
            answer = abs(int(n_n[0]))
    return answer

# def solution(expression):
#     operations = [('+', '-', '*'),('+', '*', '-'),('-', '+', '*'),('-', '*', '+'),('*', '+', '-'),('*', '-', '+')]
#     answer = []
#     for op in operations:
#         a = op[0]
#         b = op[1]
#         temp_list = []
#         for e in expression.split(a):
#             temp = [f"({i})" for i in e.split(b)]
#             temp_list.append(f'({b.join(temp)})')
#         answer.append(abs(eval(a.join(temp_list))))
#     return max(answer)