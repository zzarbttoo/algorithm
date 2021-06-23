import string
import collections

def solution(name):
    upper_alpha = string.ascii_uppercase
    alpha_dict = collections.defaultdict(int)

    for i, alpha in enumerate(upper_alpha):
        alpha_dict[alpha] = i

    answer = 0
    answer_list = [] 

    #상하에 대한 최적화 
    for alpha in name:
        alpha_number = alpha_dict[alpha] if alpha_dict[alpha] < 26 - alpha_dict[alpha] else 26 - alpha_dict[alpha]
        answer += alpha_number
        answer_list.append(alpha_number)
    
    print(answer_list)
        

    return answer

name = "JEROEN"
name = "JAN"
name = "AAAAABBBBBAAAAAABBAA"
name = "AZAAAZ"
name = "AAAZAAZA"
name = "ABABAAAAAAABA"
print(solution(name))