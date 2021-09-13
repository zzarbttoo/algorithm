def solution(places):

    answer = []

    for place in places:
        answer.append(isSuccess(place))

    return answer

def isSuccess(place):
    add_list = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    for i, row in enumerate(place):
        for j, col in enumerate(row):
            if col == 'P':
                for idx, add in enumerate(add_list):
                    if add[0] + i >= 0 and add[0] + i<= 4 and  add[1] + j >= 0 and add[1] + j <= 4:
                        temp_row = add[0] + i
                        temp_col = add[1] + j
                        if place[temp_row][temp_col] == 'X':
                            continue
                        elif place[temp_row][temp_col] == 'P':
                            print(i, j, temp_row, temp_col)
                            return 0
                        else:
                            for next_idx, next_add in enumerate(add_list):
                                next_row, next_col = temp_row + next_add[0] , temp_col + next_add[1]
                                if next_row >= 0 and next_row <= 4 and next_col >= 0 and next_col <= 4:
                                    if next_row == i and next_col == j :
                                        continue
                                    elif place[next_row][next_col] == 'P':
                                        print(i, j, temp_row, temp_col, next_row, next_col)
                                        return 0
    return 1
