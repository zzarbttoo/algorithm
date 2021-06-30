def solution(routes):

    routes.sort(key =lambda x : x[1], reverse = True)

    now_min_out = routes.pop()
    count = 1

    while routes:
        compare_num = routes.pop()
        if now_min_out[1] < compare_num[0]:
            count += 1
            now_min_out = compare_num

    return count



routes = [[-20,15], [-14,-5], [-18,-13], [-5,-3]]	
print(solution(routes))