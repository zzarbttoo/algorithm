
from collections import defaultdict
import re
import bisect

def solution(info, query):
    
    answer = []
    score = defaultdict(lambda : defaultdict(lambda : defaultdict(lambda : defaultdict(list))))
    
    for person in info:
        p = list(person.split())
        for lang in [p[0], '-']:
            for pos in [p[1], '-']:
                for car in [p[2], '-']:
                    for food in [p[3], '-']:
                        score[lang][pos][car][food].append(int(p[4]))
                        
    lang_list = ['cpp', 'java', 'python', '-']
    pos_list = ['backend', 'frontend', '-']
    carr_list = ['junior', 'senior', '-']
    food_list = ['chicken', 'pizza', '-']
                        
    for lang in lang_list:
        for pos in pos_list:
            for car in carr_list:
                for food in food_list:
                    score[lang][pos][car][food].sort()
        
    for qu in query:
        parse = re.sub(" +", " ", qu.replace("and", "")).split()
        temp_list = score[parse[0]][parse[1]][parse[2]][parse[3]]
        lower_bound = bisect.bisect_left(temp_list, int(parse[4]))
        #print(temp_list, lower_bound, parse[4])
        answer.append(len(temp_list) - lower_bound)
        
    return answer


# from collections import defaultdict
# import re

# def solution(info, query):
    
#     info_hash = defaultdict(lambda : defaultdict(lambda:defaultdict(lambda:defaultdict(list))))
#     answer = []
    
#     for person in info:
#         temp = person.split()
#         info_hash[temp[0]][temp[1]][temp[2]][temp[3]].append(int(temp[4]))
        
#     for qu in query:
#         temp = re.sub(" +", " ", qu.replace("and", "")).split()
#         first_key = ["cpp", "java", "python"] if temp[0] == "-" else [temp[0]]
#         second_key = ["backend", "frontend"] if temp[1] == "-" else [temp[1]]
#         third_key = ["junior", "senior"] if temp[2] == "-" else [temp[2]]
#         fourth_key = ["chicken", "pizza"] if temp[3] == "-" else [temp[3]]
#         count = 0
#         #print("key ::: " + temp[4])
        
        
#         for f_k in first_key:
#             for s_k in second_key:
#                 for t_k in third_key:
#                     for fo_k in fourth_key:
#                         for num in info_hash[f_k][s_k][t_k][fo_k]:
#                             if num >= int(temp[4]):
#                                 count += 1
#         answer.append(count)
        
#     return answer

# from collections import defaultdict
# import re

# def solution(info, query):
    
#     info_hash = defaultdict(lambda : defaultdict(lambda:defaultdict(lambda:defaultdict(list))))
#     answer = []
#     visited = defaultdict(lambda : defaultdict(lambda:defaultdict(lambda:defaultdict(int))))
    
#     for person in info:
#         parse = person.split()
#         now_num = int(parse[4])
#         info_hash[parse[0]][parse[1]][parse[2]][parse[3]].append(now_num)
        
#         info_hash['-'][parse[1]][parse[2]][parse[3]].append(now_num)
#         info_hash[parse[0]]['-'][parse[2]][parse[3]].append(now_num)
#         info_hash[parse[0]][parse[1]]['-'][parse[3]].append(now_num)
#         info_hash[parse[0]][parse[1]][parse[2]]['-'].append(now_num)
        
#         info_hash['-']['-'][parse[2]][parse[3]].append(now_num)
#         info_hash['-'][parse[1]]['-'][parse[3]].append(now_num)
#         info_hash['-'][parse[1]][parse[2]]['-'].append(now_num)
#         info_hash[parse[0]]['-']['-'][parse[3]].append(now_num)
#         info_hash[parse[0]]['-'][parse[2]]['-'].append(now_num)
#         info_hash[parse[0]][parse[1]]['-']['-'].append(now_num)
        
#         info_hash[parse[0]]['-']['-']['-'].append(now_num)
#         info_hash['-'][parse[1]]['-']['-'].append(now_num)
#         info_hash['-']['-'][parse[2]]['-'].append(now_num)
#         info_hash['-']['-']['-'][parse[3]].append(now_num)
        
#         info_hash['-']['-']['-']['-'].append(now_num)
        
#     for qu in query:
#         parse = re.sub(" +", " ", qu.replace("and", "")).split()
        
#         sort_list = info_hash[parse[0]][parse[1]][parse[2]][parse[3]]
        
#         if visited[parse[0]][parse[1]][parse[2]][parse[3]] == 0: 
#             sort_list = sorted(info_hash[parse[0]][parse[1]][parse[2]][parse[3]])
#             visited[parse[0]][parse[1]][parse[2]][parse[3]] = -1
        
#         if sort_list:
#             start , end = 0, len(sort_list)
#             while start != end and start != len(sort_list):
#                 if sort_list[(start + end) // 2] >= int(parse[4]):
#                     end = (start + end) // 2
#                 else:
#                     start = (start + end) // 2 + 1
#             answer.append(len(sort_list) - start)
#         else:
#             answer.append(0)
            
#     return answer


# def solution(info, query):

# from collections import defaultdict
# import re
# import bisect

# def solution(info, query):
    
#     answer = []
    
#     lang_list = ['cpp', 'java', 'python']
#     pos_list = ['backend', 'frontend']
#     carr_list = ['junior', 'senior']
#     food_list = ['chicken', 'pizza']
    
#     score = defaultdict(lambda : defaultdict(lambda : defaultdict(lambda : defaultdict(list))))
    
#     for person in info:
        
#         p = list(person.split())
#         for lang in [p[0], '-']:
#             for pos in [p[1], '-']:
#                 for car in [p[2], '-']:
#                     for food in [p[3], '-']:
#                         score[lang][pos][car][food].append(int(p[4]))
        
#     for qu in query:
#         parse = re.sub(" +", " ", qu.replace("and", "")).split()
#         temp_list = sorted(score[parse[0]][parse[1]][parse[2]][parse[3]])
#         lower_bound = bisect.bisect_left(temp_list, int(parse[4]))
#         #print(temp_list, lower_bound, parse[4])
#         answer.append(len(temp_list) - lower_bound)
        
#     return answer

    