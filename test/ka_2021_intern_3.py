
# from collections import defaultdict

# def solution(n, k, cmd):
    
#     d = defaultdict(bool)
#     b = []
    
#     for c in cmd:
#         cnt = 0
#         if c[0] == 'D':
#             while cnt < int(c[2:]):
#                 k += 1
#                 if not d[k]:
#                     cnt += 1
#         if c[0] == 'U':
#             while cnt < int(c[2:]):
#                 k -= 1
#                 if not d[k]:
#                     cnt += 1
#         if c[0] == 'C':
#             b.append(k)
#             d[k] = True
#             m = False
#             for t in range(k + 1, n):
#                 if not d[t]:
#                     m = True
#                     k = t 
#                     break
#             if not m:
#                 for t in range(k, 0, -1):
#                     if not d[t]:
#                         k = t
#                         break
#         if c[0] == 'Z':
#             d[b.pop()] = False
            
#     answer = ""
#     for i in range(n):
#         if d[i]:
#             answer += "X"
#         else:
#             answer += "O"
    
#     return answer

class Node:
    def __init__(self):
        self.removed = False
        self.prev = None
        self.next = None

def solution(n, k, cmd):
    
    arr = [Node() for _ in range(n)]
    stack = []
	
    for i in range(1, n):
        arr[i].prev = arr[i - 1]
        arr[i - 1].next = arr[i]
    
    now = arr[k]
    
    for c in cmd:
        if c[0] == 'D':
            for _ in range(int(c[2:])):
                now = now.next
        if c[0] == 'U':
            for _ in range(int(c[2:])):
                now = now.prev
        if c[0] == 'C':
            stack.append(now)
            now.removed = True
            up = now.prev
            down = now.next
            if up:
                up.next = down
                now = up
            if down:
                down.prev = up
                now = down 
        if c[0] == 'Z':
            alive = stack.pop()
            alive.removed = False
            up = alive.prev
            down = alive.next
            if up:
                up.next = alive
            if down:
                down.prev= alive
                
    answer = ''
    
    for node in arr:
        if node.removed:
            answer += 'X'
        else:
            answer += 'O'
            
    return answer