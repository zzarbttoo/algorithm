def solution(s):

    length = len(s)

    before = ""
    answer = float("INF")
    num_count = 0

    if length == 1:
        return 1
    print(length)

    for chunk_size in range(1, length // 2 + 1): #chunk_size
        temp_answer = 0
        for i in range(0, length, chunk_size):
            now = s[i: i + chunk_size]
            if before == now:
                if num_count == 1:
                    temp_answer += 1
                if num_count == 9:
                    temp_answer += 1
                if num_count == 99:
                    temp_answer += 1
                if num_count == 999:
                    temp_answer += 1
                num_count += 1

            else:
                temp_answer += len(s[i:i+chunk_size])
                num_count = 1
            before = now 
        answer = min(temp_answer, answer)
    return answer