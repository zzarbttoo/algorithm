from collections import defaultdict
import sys

#recursion limit 
sys.setrecursionlimit(10 ** 6)

def solution(k, num, links):
    
    left = defaultdict(lambda : -1) #우측 노드 번호
    right = defaultdict(lambda : -1) #좌측 노드 번호
    parent = defaultdict(lambda : -1) #부모 노드 번호
    head_count = defaultdict(int) #노드별 인원수
    
    all_sum = 0
    
    for i, (link, weight) in enumerate(zip(links, num)):
        head_count[i] = weight
        left[i], right[i] = link[0], link[1]
        if link[0] != -1: parent[link[0]] = i
        if link[1] != -1: parent[link[1]] = i
        all_sum += weight
    
    root = 0
    
    #root 찾기
    for i in range(len(num)):
        if parent[i] == -1:
            root = i
            break
    
    
    def calculate(limit):
        nonlocal left, right, parent, head_count, root
        
        count = 0 
        dp = defaultdict(int)
        
        def dfs(node, limit):
            
            nonlocal count, dp
            
            #왼쪽 자식
            if left[node] != -1: 
                dp[left[node]] = dfs(left[node], limit)
            if right[node] != -1:
                dp[right[node]] = dfs(right[node], limit)
                
            if dp[left[node]] + dp[right[node]]+ head_count[node] <= limit:
            	return dp[left[node]] + dp[right[node]] + head_count[node]
            
            if min(dp[left[node]], dp[right[node]]) + head_count[node] <= limit:
                count += 1
                return min(dp[left[node]], dp[right[node]]) + head_count[node]
            
            count += 2
            return head_count[node]
        
        dfs(root, limit)
        count += 1
        return count
    
    # 전체 가중치의 합 / k <= L <= 전체 가중치의 합 
    #R = all_sum #최대 
    R = all_sum 
    L = int(all_sum / k) #최소        
    
    #파라메트릭 서치
    while L < R:
        mid = (L + R) // 2 #최대 최소의 중간값
        if calculate(mid) <= k: R = mid 
        else: L = mid + 1
    
    return L 
        
    
        
        