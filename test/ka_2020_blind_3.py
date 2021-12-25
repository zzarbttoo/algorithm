import copy

def solution(key, lock):
    
    #회전 로직
    key_90 = [k[::-1] for k in zip(*key)]
    key_180 = [k[::-1] for k in zip(*key_90)]
    key_270 = [k[::-1] for k in zip(*key_180)]
    
    keys = [key, key_90, key_180, key_270]
    
    N = len(lock)
    M = len(key)
    
    new_lock = []
    
    for i in range(N):
        temp_lock = [0 for _ in range(3 * N)]
        new_lock.append(temp_lock)
        
    
    for i in range(N):
        temp_lock = [0 for _ in range(N)]
        temp_lock += lock[i]
        temp_lock += [0 for _ in range(N)]
        new_lock.append(temp_lock)
        
    for i in range(N):
        temp_lock = [0 for _ in range(3 * N)]
        new_lock.append(temp_lock)
    
    for i in range(3 * N - M + 1):
        for j in range(3 * N - M + 1):
            for rev_key in keys:
                temp_lock = copy.deepcopy(new_lock)
                for x in range(M):
                    for y in range(M):
                        if x + M < 3 * N - 1 and y + M < 3 * N - 1:
                            temp_lock[x + i][y + j] += rev_key[x][y]
                            
                    answer = True
                    
                    for t in range(N):
                        if temp_lock[N + t][N : N + N] != [1]* N:
                            answer = False
                    if answer == True:
                        return True
    return False
            
            
            
            
        
        