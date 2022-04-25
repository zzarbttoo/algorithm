from itertools import permutations

def solution(user_id, banned_id):
    
    answer = []
    p_l = list(permutations(user_id, len(banned_id)))
    
    for p in p_l:
        t = True
        for (u, b) in zip(p, banned_id):
            if len(u) != len(b):
                t = False
                break
            for (u_c, u_b) in zip(u, b):
                if u_b == '*':
                    continue
                if u_c != u_b:
                    t = False
                    break
        if t:
            p = set(p)
            if p not in answer:
                answer.append(p)
                
    return len(answer)