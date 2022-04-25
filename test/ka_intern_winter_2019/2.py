from collections import Counter

def solution(s):
    
    s = s.replace("{", '').replace("}", '')
    s_l = list(map(int, s.split(',')))
    
    count = Counter(s_l).most_common()
    answer = [k for (k, v) in count]
    
    return answer