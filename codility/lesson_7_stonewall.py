def solution(H):

    stack = []
    count = 0

    for hei in H:
        while stack and stack[-1] > hei:
            stack.pop()

        if not stack or stack[-1] < hei:
            stack.append(hei)        
            count += 1

    return count
