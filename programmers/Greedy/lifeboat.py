def solution(people, limit):

    now_count, first_index, last_index = 0, 0, len(people) -1 
    people.sort()

    while first_index <= last_index:
        #print("first_index ::: " + str(first_index))
        #print("last_index ::: "+ str(last_index))

        if people[first_index] + people[last_index] > limit:
            last_index -= 1
            now_count += 1
        else:
            last_index -= 1
            first_index += 1
            now_count += 1

    return now_count


people = [70, 50, 80, 50]
limit = 100

print(solution(people, limit))

people = [70, 80, 50]
limit = 100

print(solution(people, limit))