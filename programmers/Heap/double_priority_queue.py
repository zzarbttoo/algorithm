from queue import PriorityQueue

def solution(operations):
    
    ascending_sort = PriorityQueue()
    descending_sort = PriorityQueue() 
    length_1 = 0
    length_2 = 0
    
    for operation in operations:
        #print(operation)
        com, str_num = operation.split()
        num = int(str_num)
        
        if com == 'D': #삭제
            if length_1 > 0 and length_2 > 0: #큐 길이 고려
                if num == -1: #앞에서 제거
                    ascending_sort.get()
                elif num == 1: #뒤에서 제거
                    -descending_sort.get()
                length_1 -= 1
                length_2 -= 1
        else: #추가
            ascending_sort.put(num)
            descending_sort.put(-num)
            length_1 += 1
            length_2 += 1
        if length_1 == 0 and length_2 == 0:
            ascending_sort = PriorityQueue()
            descending_sort = PriorityQueue() 
            
    #print(ascending_sort.queue)
    #print(descending_sort.queue)

    if length_1 > 0 and length_2 > 0:
        return [-descending_sort.get(), ascending_sort.get()]
    return [0, 0]