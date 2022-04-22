def solution():
    string = input()
    bomb = input()
    length = len(bomb)

    stack = []

    for st in string:
        stack.append(st)
        while len(stack) >= length:
            if ''.join(stack[-length:]) == bomb: 
                for _ in range(length):
                    stack.pop()
            else : break

    answer = ''.join(stack)
    if answer == '':
        answer = 'FRULA'
    
    print(answer)

solution()

# def solution():
#     string = input()
#     bomb = input()

#     while True: 
#         temp = string.split(bomb)
#         string = "".join(temp)

#         if len(temp) == 1:
#             break
    
#     if string == "":
#         print("FRULA")
#     else:
#         print(string)

# solution()
