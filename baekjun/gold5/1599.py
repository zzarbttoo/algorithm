from collections import defaultdict
from string import ascii_uppercase

def solution():
    num_hash = defaultdict(int)
    N = int(input())
    answer = []

    for i, word in enumerate("a b k d e g h i l m n ng o p r s t u w y".split(" ")):
        num_hash[word] = ascii_uppercase[i]

    for _ in range(N):
        minsick_word = input()
        replace_word = minsick_word.replace("ng", 'L')
        for key, val in num_hash.items():
            replace_word = replace_word.replace(key, val)

        answer.append([minsick_word, replace_word])
    
    answer.sort(key = lambda x:x[1])

    for word in answer:
        print(word[0])

solution()

