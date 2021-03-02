def solution(num:int)->str:

    number_hash = {'1':'one', '2': 'two', '3':'three', '4':'four', '5':'five', '6':'six', '7':'seven', '8':'eight', '9':'nine', '10':'ten'}
    print(number_hash)
    answer = ""

    for number in str(num):
        answer += number_hash[number]

    return answer

print(solution(147))
