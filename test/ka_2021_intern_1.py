# def solution(s):
#     answer = ''

#      num_dict = {'one' : '1', 'two' : '2', 'three' : '3', 'four' : '4'
#                , 'five' : '5', 'six' : '6', 'seven' : '7', 'eight' : '8'
#                , 'nine' : '9', 'zero' : '0'}


#     length = len(s)
#     count = 0

#     while count < length:

#         if s[count].isnumeric():
#             answer += s[count]
#             count += 1
#             continue
#         elif s[count : count + 3] in num_dict:
#             answer += num_dict[s[count:count+3]]
#             count += 3
#             continue
#         elif s[count : count + 4] in num_dict:
#             answer += num_dict[s[count : count + 4]]
#             count += 4
#             continue
#         elif s[count : count + 5] in num_dict:
#             answer += num_dict[s[count : count + 5]]
#             count += 5
#             continue


#     return int(answer)


#answer1
def solution(s):

    num_dict = {'one' : '1', 'two' : '2', 'three' : '3', 'four' : '4'
               , 'five' : '5', 'six' : '6', 'seven' : '7', 'eight' : '8'
               , 'nine' : '9', 'zero' : '0'}

    answer = s
    for key, value in num_dict.items():
        answer = answer.replace(key, value)

    return int(answer)

print(solution('one34two'))
print(solution('two0'))
print(solution('0'))

