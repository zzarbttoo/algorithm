from sys import stdin 
from collections import defaultdict

def input_nums():


    d, o = stdin.readline().split()
    d = int(d)
    w = defaultdict(bool)

    for _ in range(d):
        w[stdin.readline().strip()] = True
    return d, o, w

from string import ascii_lowercase

def solution():

    d, o, w = input_nums()
    visited = defaultdict(bool)

    def dfs(now):
        nonlocal d, o, w, visited

        for c in ascii_lowercase:
            for i in range(len(now) + 1):
                next = now[0:i] + c + now[i:]

                if w[next] == True and visited[next] == False:
                    visited[next] = True
                    dfs(next)

    visited[o] = True
    dfs(o)

    answer = o

    for key, val in visited.items():
        if val and  len(answer) < len(key):
            answer = key

    print(answer)

solution()


            # next1 = c + now
            # next2 = now[0:len(now) // 2] + c + now[len(now) // 2:]
            # next3 = now + c

            # if w[next1] == True and visited[next1] == False:
            #     visited[next1] = True
            #     dfs(next1)

            # if w[next2] == True and visited[next2] == False:
            #     visited[next2] = True
            #     dfs(next2)

            # if w[next3] == True and visited[next3] == False:
            #     visited[next3] = True
            #     dfs(next3)

