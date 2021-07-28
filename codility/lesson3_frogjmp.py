import math

def solution(X, Y, D):
    distance = Y - X
    return math.ceil(distance / D)


X , Y, D= 10, 85, 30
print(solution(X, Y, D))