def solution(S, P, Q):
    hash_alpha = {'A' : 1, 'C' : 2, 'G' : 3, 'T': 4 }
    answer_list = list()

    for i, (p , q) in enumerate(zip(P, Q)):
        if 'A' in S[p:q+1]:
            answer_list.append(hash_alpha['A']) 
        elif 'C' in S[p:q+1]:
            answer_list.append(hash_alpha['C'])
        elif 'G' in S[p:q+1]:
            answer_list.append(hash_alpha['G'])
        else:
            answer_list.append(hash_alpha['T'])
    
    return answer_list