def solution(number, k):

    answer_list = []
    now = 0
    now_max = number

    while True:
        for i in range(len(now_max)):
            temp_answer = now_max[:i] + now_max[i+1:]
            #print(temp_answer)
            answer_list.append(temp_answer)
        now_max = str(max(list(map(int, answer_list))))
        answer_list = []
        now += 1
        if now == int(k):
            break

    return now_max


number = "1924"
k = "2"

number = "1231234"
k = "3"

number = "4177252841"
k = "4"

print(solution(number, k))