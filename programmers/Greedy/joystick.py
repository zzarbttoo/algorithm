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

    
    #좌우 거리를 구한 후 가까운 쪽으로 간다 
    now_index = 0

    while len(answer_list) != answer_list.count(0):

        answer += answer_list[now_index]
        answer_list[now_index] = 0
        left, right = 1, 1

        print("now_index ::: " + str(now_index))

        while answer_list[now_index + right] == 0:

            print("right_num ::: " + str(answer_list[now_index + right]))
            right += 1
            if now_index + right > len(answer_list):
                

        while answer_list[now_index - left] == 0:
            print("left_num ::: " + str(answer_list[now_index - left]))
            left += 1

        print("left :::" + str(left) + "  right ::: " +  str(right))

        if left >= right:
            now_index = now_index + right
            print("right ::: " + str(right))
            print("now_index ::: " + str(now_index))
            print("now_num ::: " + str(answer_list[now_index]))
        else:
            now_index = now_index - left
            print("left ::: " + str(left))


    return answer

name = "JEROEN"

print(solution(name))
name = "JAN"

print(solution(name))
name = "AAAAABBBBBAAAAAABBAA"
name = "AZAAAZ"
name = "AAAZAAZA"
name = "ABABAAAAAAABA"
name = "ABAAB"
name = "AAAA"
print(solution(name))