from collections import defaultdict

def solution(record):
    
    name = defaultdict(str)
    answer = []
    
    for re in record:
        split = re.split()
        if split[0] == "Enter" or split[0] == "Change":
            name[split[1]] = split[2]
            
    for re in record:
        split = re.split()
        if split[0] == "Enter":
            input_str = name[split[1]] + "님이 들어왔습니다."
            answer.append(input_str)
        if split[0] == "Leave":
            input_str = name[split[1]] + "님이 나갔습니다."
            answer.append(input_str)
    return answer