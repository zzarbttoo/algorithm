
import collections

def solution(tickets):
    graph = collections.defaultdict(list)

    #dict 저장 
    for a, b in sorted(tickets):
        graph[a].append(b)

    #시작
    route, stack = [], ["ICN"]
    while stack:
        while graph[stack[-1]]: 
            stack.append(graph[stack[-1]].pop(0))
        route.append(stack.pop())
    
    return route[::-1]
        

tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]

tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
tickets =  [["ICN", "B"], ["B", "ICN"], ["ICN", "A"], ["A", "D"], ["D", "A"]]

tickets = [['ICN','A'],['A','B'],['A','C'],['C','A'],['B','D']]

tickets = [["ICN", "AAA"], ["ICN", "AAA"], ["ICN", "AAA"], ["AAA", "ICN"], ["AAA", "ICN"]]
tickets = [["ICN", "BOO"], ["ICN", "COO"], ["COO", "DOO"], ["DOO", "COO"], ["BOO", "DOO"], ["DOO", "BOO"], ["BOO", "ICN"], ["COO", "BOO"]]

tickets = [["ICN", "AAA"], ["ICN", "AAA"], ["ICN", "AAA"], ["AAA", "ICN"], ["AAA", "ICN"]]
tickets = [["ICN", "A"], ["A", "B"], ["A", "C"], ["C", "A"], ["B", "D"]]
tickets = [['ICN','AAA'],['ICN','AAA'],['ICN','AAA'],['AAA','ICN'],['AAA','ICN']]
tickets = [['ICN' ,'B'], ['ICN', 'C'] ,['C', 'D'], ['D', 'ICN']]
