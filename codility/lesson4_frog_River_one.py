    
def solution(A):
    length_A = len(A)
    perm_set = set()
    diff_set = set([i for i in range(1, length_A + 1)])
    #print(diff_set)

    for i in A:
        perm_set.add(i)

    if list(diff_set.difference(perm_set)) == []:
        return 1   
    return 0
