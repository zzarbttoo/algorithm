def solution(phone_number:str)->int:

    if phone_number.startswith('010-'):
        return 1
    
    elif phone_number.startswith('010'):
        return 2
    
    elif phone_number.startswith('+82-10-'):
        return 3
    else:
        return -1
    

print(solution("01012345678"))
print(solution("010-1212-333"))
print(solution("+82-10-3434-2323"))
print(solution("+82-010-3434-2323"))

