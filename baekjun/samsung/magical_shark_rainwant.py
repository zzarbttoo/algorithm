

#배열 받기

def array_input() -> list:
    n, m = map(int, input().split())

    bucket_list = list()
    move_list = list()

    for i in range(n):
        temp_list = list(map(int, input().split()))
        bucket_list.append(temp_list)

    for j in range(m):
        temp_list = list(map(int, input().split()))
        move_list.append(temp_list)
    
    now_cloud_info = [[n, 1], [n, 2], [n-1, 1], [n-1, 2]]
    
    return bucket_list, move_list, now_cloud_info


def move(move_info_list, bucket_list):

    if now_cloud_info is none:
        print("hello")

    #상/하 좌/우
    info_list = [[0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1]]

    #info_list[n-1] 이런 식
    

    #넘어갈 경우 뒤에서 빼준다



    #




def main():
    #init_bucket_list, move_list, now_cloud_info = array_input()
    bucket_list = [[0, 0, 1, 0, 2], [2, 3, 2, 1, 0], [4, 3, 2, 9, 0], [1, 0, 2, 9, 0], [8, 8, 2, 1, 0]]
    move_list = [[1, 3], [3, 4], [8, 1], [4, 8]]
    now_cloud_info = [[5,1], [5,2], [4,1], [4,2]]

    for move_array in move_list:
        bucket_list = move_list(move_array,bucket_list, now_cloud_info)
    


main()

