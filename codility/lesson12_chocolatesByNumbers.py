def solution(N, M):

    if N == 1: return 1 

    gcf = gcd(N, M)

    return N // gcf 


def gcd(N, M):
    if M == 0:
        return N 
    return gcd(M, N % M)