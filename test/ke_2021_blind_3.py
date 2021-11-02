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
                        
                        
if []:
    print('es')