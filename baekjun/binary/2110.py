from sys import stdin

def input_num():
    N, C = map(int, stdin.readline().split())
    X = []

    for _ in range(N):
        X.append(int(stdin.readline()))
    return N, C, X
 
def solution():
   
    N, C, X = input_num()
    #N, C, X = 5, 3, [1, 2, 8, 4, 9]
    #N, C, X = 4, 3, [11, 13, 16, 18]

    answer = 0

    X.sort()

    left, right = 1, X[-1] - X[0]
    #print(left, right)

    while left <= right:
        mid = left + (right - left) // 2
        #print("mid  ::: " + str(mid))

        count = 1 
        now = X[0]
        
        for x in X[1:]:
            #print(mid, now, count)
            if now + mid <= x:
                count += 1
                now = x
        

        if count >= C:
            answer = mid
            left = mid + 1
        else:
            right = mid - 1

    print(answer)

solution()

    
