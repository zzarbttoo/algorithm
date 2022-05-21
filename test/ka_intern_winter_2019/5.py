def solution(stones, k):
    
    start, end = 0, max(stones)
    answer = 0
    
    while start <= end:
        mid = (start + end) // 2
        cnt = 0
        pos = True
        for s in stones:
            if s - mid + 1 <= 0:
                cnt += 1
                if cnt >= k:
                    pos = False
                    break
            else:
                cnt = 0
        if pos:
            start = mid + 1
            if answer < mid:
                answer = mid
        else:
            end = mid - 1
    return answer