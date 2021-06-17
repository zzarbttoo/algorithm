import collections

def solution(tickets):
    ticket_dict = collections.defaultdict(list)
    visited = []

    for start, end in sorted(tickets, reverse=True):
        ticket_dict[start].append(end)
    
    def dfs(node):

        nonlocal visited
        visited.append(node)

        while ticket_dict[node]:
            dfs(ticket_dict[node].pop())

    
    dfs("ICN")

    return visited



tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
tickets =  [["ICN", "B"], ["B", "ICN"], ["ICN", "A"], ["A", "D"], ["D", "A"]]
#tickets = [["ICN", "AAA"], ["ICN", "AAA"], ["ICN", "AAA"], ["AAA", "ICN"], ["AAA", "ICN"]]
print(sorted(tickets))
print(solution(tickets))