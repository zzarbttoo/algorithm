def solution(S):

    length = len(S)

    for i ,word in enumerate(S[:-1]):
        if word == S[-1]: 
            if S[i:] == S[::-1][:length-i]: return length + i
    if length == 1: return 1 
    return 2 * (length - 1) + 1
            
    
S = input()
print(solution(S))

    # length = len(S)
    # rev_idx = S[::-1].find(S[-1] ,1)
    # start = length - rev_idx - 1
    # end = length - 1

    # if rev_idx != -1:
    #     if S[start : end + 1] == S[::-1][length - end - 1: length - start]:
    #         pal_length = len(S[start : end + 1])
    #         return pal_length + 2 * (length - pal_length)
    # else:
    #     if length == 1: return 1
    #     return 1 + 2 * (length - 1)


#S = "abdfhdyrbdbsdfghjkllkjhgfds"
#S = "abab"
#S = "abacaba"
#S = "qwerty"