def solution(board, moves):
    
    stack = []
    answer = 0
    
    for move in moves:
        for b in board:
            if b[move - 1] != 0:
                stack.append(b[move - 1])
                b[move - 1] = 0
                break
        if len(stack) >= 2 and stack[-2] == stack[-1]:
            stack.pop()
            stack.pop()
            answer += 2
            
    return answer