# https://www.acmicpc.net/problem/2174

from sys import stdin
from collections import defaultdict

def error_w(robo_num):
    return "Robot " + str(robo_num) + " crashes into the wall"

def error_r(robo_num, robo_num2):
    return "Robot " + str(robo_num) + " crashes into robot " + str(robo_num2)

def solution():

    A, B = map(int, stdin.readline().split())
    N, M = map(int, stdin.readline().split())

    location = defaultdict(lambda : defaultdict(lambda : -1)) #로봇 번호, 상태로 초기화
    robot = defaultdict(list)

    for idx in range(N):
        order = stdin.readline().split()
        X, Y, D = int(order[0]), int(order[1]), order[2]
        if  X < 0 or X > A or Y < 0 or Y > B:
            print(error_w(idx + 1)) 
            return 

        if location[X][Y] == -1:
            location[X][Y] = idx + 1 
            robot[idx + 1] = [X, Y, D]
        else:
            print(error_r(idx + 1, location[X][Y])) 
            return 
    
    order_list = []
    for _ in range(M):
        order_list.append(stdin.readline().split())

    direction = {'E' : [1, 0], 'N' : [0, -1], 'W' : [-1, 0], 'S' : [0, 1]}
    l = {'E' : 'S', 'S' : 'W', 'W' : 'N', 'N' : 'E'}
    r = {'N' : 'W', 'W' : 'S', 'S' : 'E', 'E' : 'N'}

    for order in order_list:
        #print("order ::: " + str(order))
        r_i, o, re = int(order[0]), order[1], int(order[2])
        for _ in range(re):
            if o == 'R':
                robot[r_i][2] = r[robot[r_i][2]]
            if o == 'L':
                robot[r_i][2] = l[robot[r_i][2]]
            if o == 'F':
                now = robot[r_i]
                next = [now[0] + direction[now[2]][0], now[1] + direction[now[2]][1]]
                #print("next ::: " + str(next))
                if next[0] > A or next[0] < 1 or next[1] > B or next[1] < 0:
                    print(error_w(r_i))
                    return 
                #print("location ::: " + str(location[next[0]][next[1]]))
                if location[next[0]][next[1]] != -1:
                    print(error_r(r_i, location[next[0]][next[1]]))
                    return 
                
                location[robot[r_i][0]][robot[r_i][1]] = -1
                location[next[0]][next[1]] = r_i
                robot[r_i] = [next[0], next[1], robot[r_i][2]]
            #print("robot:::" + str(robot))
    
    print("OK")


solution()