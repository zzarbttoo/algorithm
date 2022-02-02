from collections import deque

def solution(priorities, location):
    
    q = deque([i for i in range(len(priorities))])
    
    count = 0
    
    while q:
        temp = [priorities[idx] for idx in q]
        if temp[0] == max(temp):
            num = q.popleft()
            count += 1
            if num == location:
                return count
        else:
            q.append(q.popleft())
        