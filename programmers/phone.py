def solution(phone_book:list)->bool:

    hash = {}

    for phone_number in phone_book:
        hash[phone_number] = 0

    for phone_number in phone_book:
        temp = ""
        for phone in phone_number:
            temp += phone 
            if temp in hash and temp != phone_number:
                return False
       
    return True



print(solution(["12", "123", "1235", "567", "88"]))


