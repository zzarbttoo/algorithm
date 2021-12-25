def time_to_second(time):
    time_list = list(map(int, time.split(":")))
    second = time_list[0] * 60 * 60 + time_list[1] * 60 + time_list[2]
    return second

def second_to_time(time):
    
    hour, minute = divmod(time, 60 * 60)
    minute, second = divmod(minute, 60)
    hour_str, minute_str, second_str = str(hour), str(minute), str(second)
    
    if len(str(hour)) == 1: hour_str = "0" + str(hour)
    if len(str(minute)) == 1: minute_str = "0" + str(minute)
    if len(str(second)) == 1: second_str = "0" + str(second)
        
    answer = hour_str + ":" + minute_str + ":" + second_str
    return answer
    

    
from collections import defaultdict

def solution(play_time, adv_time, logs):
    
    count = defaultdict(int)
    play_second = time_to_second(play_time)
    adv_second = time_to_second(adv_time)
    
    for log in logs:
        start, end = log.split("-")
        start_second = time_to_second(start)
        end_second = time_to_second(end)
        
        count[start_second] += 1
        count[end_second] -= 1
        
    # 각 time에 몇개의 프로그램이 있는 지 확인(누적)
    for time in range(play_second + 1):
        count[time] = count[time - 1] + count[time]
    	
    for time in range(play_second + 1):
        count[time] = count[time - 1] + count[time]
    
    answer_count = -float("INF")
    answer = 0
    
    for time in range(adv_second - 1, play_second):
        if count[time] - count[time - adv_second] > answer_count:
            answer_count = count[time] - count[time - adv_second]
            answer = time - adv_second + 1
            
    
    return second_to_time(answer)
    
    
        
    