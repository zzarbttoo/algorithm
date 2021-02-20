import collections
def solution(answers:list)->list:
    
    answer_list = answers * 10000
    
    first_score, second_score, third_score = 0, 0, 0
    
    first = [1, 2, 3, 4, 5] * 10000
    second = [ 2, 1, 2, 3, 2, 4, 2, 5 ] * 10000
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 10000
    
    for i in range(len(answers)):
        if first[i] == answer_list[i]: first_score+=1
        if second[i] == answer_list[i]: second_score+=1
        if third[i] == answer_list[i]: third_score+=1

    print(collections.Counter([first_score, second_score, third_score]))
    


    
    
   
    return []

solution([1,2,3,4,5])
