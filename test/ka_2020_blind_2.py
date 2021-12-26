def is_balanced(word):
    
    stack = []
    
    for wo in word:
        if len(stack) == 0 and wo == ')':
            return False
        if wo == '(':
            stack.append(wo)
        if stack and wo == ')':
            stack.pop()
            
    if len(stack) == 0:
        return True
    else:
         return False

def split(word):
    
    if len(word) == 0:
        return "", ""
    
    stack = [word[0]]
    u, v = "", ""
    
    for idx, bracket in enumerate(word[1:]):
        
        if stack and bracket == ')' and stack[-1] == '(':
            stack.pop()
        if stack and bracket == '(' and stack[-1] == ')':
            stack.pop()
        if stack and bracket == ')' and stack[-1] == ')':
            stack.append(')')
        if stack and bracket == '(' and stack[-1] == '(':
            stack.append('(')
        if not stack:
            u, v = word[0: idx + 2], word[idx + 2:]
            break    
    return u, v
    

def new_words(word):
    u, v = split(word)
    
    while v != "" and is_balanced(v) == False:
        v = new_words(v)
    
    new_u = ""
    
    if len(u) >= 2 and is_balanced(u) == False:
        for bracket in u[1:-1]:
            if bracket == ')':
                new_u += '('
            if bracket == '(':
                new_u += ')'
    else:
        return u + v
    
    return "(" + v + ")" + new_u
    

def solution(p):
    return new_words(p)



#다른 사람 풀이..
#...ㅎㅎㅎㅎ 미친거 아닐까?
def other_solution(p):
    if p=='': return p
    r=True; c=0
    for i in range(len(p)):
        if p[i]=='(': c-=1
        else: c+=1
        if c>0: r=False
        if c==0:
            if r:
                return p[:i+1]+other_solution(p[i+1:])
            else:
                return '('+other_solution(p[i+1:])+')'+''.join(list(map(lambda x:'(' if x==')' else ')',p[1:i]) ))