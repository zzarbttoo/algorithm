from collections import defaultdict
import string

def solution():

    num = input()

    alpha = set([str(i + 1) for i in range(len(string.ascii_lowercase))])
    cnt = defaultdict(int)

    if num[0] in alpha: cnt[0] = 1

    if cnt[0] == 0: 
        print(0)
        return 
    
    if len(num) == 1: 
        print(1)
        return 

    if num[1] in alpha: cnt[1] = 1 
    if num[0] + num[1] in alpha: cnt[1] += 1

    if cnt[1] == 0: 
        print(0)
        return 
    

    for i in range(2, len(num)):
        if num[i] in alpha: cnt[i] += cnt[i-1]
        if num[i -1] + num[i] in alpha: cnt[i] += cnt[i - 2]
        if cnt[i] == 0:
            print(0)
            return 

    print(cnt[len(num) - 1] % 1000000)

solution()

