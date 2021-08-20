
def solution(n):
    temp_list = [0 for _ in range(0, n + 1)]
    temp_list[0], temp_list[1] = 0, 1

    for i, _ in enumerate(temp_list):
        if i >=2:
            temp_list[i] = temp_list[i-1] + temp_list[i-2]
        
    
    return temp_list[n]
    





    


    


n = input()
print(solution(int(n)))