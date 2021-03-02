def solution(citations):

    citations = sorted(citations, reverse = True)

    length = len(citations)
    print(length)

    for i, m in enumerate(citations, start = 1):
        print(i, m)

    for i in (map(min, enumerate(citations, start = 1))):
        print(i)

    temp = []

    for i, num in enumerate(citations):
        if num >= i + 1: 
            temp.append(i+1)

    if len(temp) == 0:
        return 0
        
    return max(temp)

'''
def solution(citations):
    citations.sort(reverse=True)
    answer = max(map(min, enumerate(citations, start=1)))
    return answer
'''
        
    

#print(solution([3,0,6,1,5]))
#print(solution([6, 5, 4, 1, 0]))
print(solution([ 0]))
