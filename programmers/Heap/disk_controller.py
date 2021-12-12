from collections import deque
from queue import PriorityQueue

def solution(jobs):
    
    answer = 0
    length = len(jobs)
    jobs.sort(key= lambda x : (x[0], x[1]))
    
    queue = PriorityQueue()
    jobs = deque(jobs) #시간순이라는 가정이 돼있음 #들어온 시간, 지속 시간
    now, fin = jobs.popleft()
    queue.put([0, now, fin]) #우선순위, 들어온 시간, 지속시간
    
    while queue.qsize() != 0: #처리할 일이 남아있나
        now_job = queue.get() 
        now += now_job[2]
        
        answer += now - now_job[1]
        
        while jobs:
            if jobs[0][0] < now:
                add_job = jobs.popleft()
                queue.put([(add_job[1], add_job[0]), add_job[0], add_job[1]])
            else:
                if queue.qsize() == 0: #끊어져 있을 경우에 대비
                    add_job = jobs.popleft()
                    queue.put([(add_job[1], add_job[0]), add_job[0], add_job[1]])
                break
        
    return int(answer / length)