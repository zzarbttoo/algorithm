from collections import defaultdict

def solution(numbers, hand):
    print(numbers)
    #print(hand.upper())
    
    b_l, b_r = [0, 0], [2, 0]
    answer = ""
    
    c = defaultdict(int)
    c[1], c[4], c[7] = -1, -1, -1
    c[3], c[6], c[9] = 1, 1, 1
    
    n = defaultdict(list)
    n[1] = [0, 3]
    n[4] = [0, 2]
    n[7] = [0, 1]
    
    n[2] = [1, 3]
    n[5] = [1, 2]
    n[8] = [1, 1]
    n[0] = [1, 0]
    
    n[3] = [2, 3]
    n[6] = [2, 2]
    n[9] = [2, 1]
    
    for num in numbers:
        if c[num] == -1:
            answer += 'L'
            b_l = n[num]
        if c[num] == 1:
            answer += 'R'
            b_r = n[num]
        if c[num] == 0:
            left = abs(n[num][0] - b_l[0]) + abs(n[num][1] - b_l[1])
            right = abs(n[num][0] - b_r[0]) + abs(n[num][1] - b_r[1])
            
            if left < right:
                answer += 'L'
                b_l = n[num]
            if left > right:
                answer += 'R'
                b_r = n[num]
            if left == right:
                h = hand[0].upper()
                answer += h
                if h == 'R':
                    b_r = n[num]
                else:
                    b_l = n[num]
                
    return answer