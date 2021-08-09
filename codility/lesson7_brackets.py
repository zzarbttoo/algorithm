def solution(S):

    temp_stack = []


    for bracket in S:
        if bracket == '('  or bracket == '{' or  bracket == '[': 
            temp_stack.append(bracket)
        elif len(temp_stack) == 0:
            return 0

        if bracket == ')':
            if temp_stack.pop() != '(':
                return 0
        if bracket == '}':
            if temp_stack.pop() !=  '{':
                return 0
        if bracket ==  ']':
            if temp_stack.pop() != '[':
                return 0

    if len(temp_stack) == 0:
        return 1
    else:
        return 0 
    