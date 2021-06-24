def solution(number, k):

    stack, num, count, pop_num = [], 0, 0, 0 

    if int(k) == len(number):
        return "0"

    while True:
        while stack and stack[-1] and int(stack[-1]) < int(number[num]) and int(k) > count:
            stack.pop()
            pop_num += 1
            count += 1
        
        stack.append(number[num])
        num += 1

        if int(k) == pop_num and len(stack) == len(number) - int(k):
            break
        elif num == len(number):
            stack = stack[:-int(k)]
            break

    answer = "".join(stack)
    return answer
    

# number = "1924"
# k = "2"

# print(solution(number, k))

# number = "1231234"
# k = "3"

# print(solution(number, k))


# number = "4177252841"
# k = "4"

# print(solution(number, k))

# number = "1111117"
# k = "5"

#print(solution(number, k))

number = "1000"
k = "1"

print(solution(number, k))