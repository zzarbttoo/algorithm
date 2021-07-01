def solution(triangle):

    triangle_dict = []
    
    for i, layer in enumerate(reversed(triangle)):
        triangle_dict.append([-1] * len(layer))
    
    for height, layer in enumerate(triangle_dict):
        for index, _ in enumerate(layer):
            if height != 0:
                triangle_dict[height][index] = max(triangle_dict[height-1][index], triangle_dict[height-1][index+1]) + triangle[len(triangle)- 1 -height][index]
            else:
                triangle_dict[height][index] = triangle[-1][index]
    
    answer = triangle_dict.pop()[0]
    return answer
    







            
            



    








triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
print(solution(triangle))