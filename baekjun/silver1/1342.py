from collections import defaultdict
from email.policy import default

def solution():

    word = input()
    answer = 0
    alpha = defaultdict(int)

    for c in word:
        alpha[c] += 1

    def dfs(depth, be_word):
        nonlocal alpha, word, answer

        if depth == len(word):
            answer += 1
        
        for key in alpha.keys():
            if alpha[key] <= 0:
                continue
            if be_word and be_word[-1] == key:
                continue

            alpha[key] -= 1
            dfs(depth + 1, be_word + key)
            alpha[key] += 1
    
    dfs(0, "")
    print(answer)


solution()



# #메모리 초과
# from collections import defaultdict

# def solution():
#     #word = input()
#     #word = "aabbbaa"
#     #word = "ab"
#     #word = "aaab"
#     word = "abcdefghij"
#     alpha = defaultdict(int)
#     visited = defaultdict(int)
#     answer = 0

#     for c in word:
#         alpha[c] += 1
#     #print(alpha)

#     def dfs(now, al):
#         nonlocal visited, alpha, answer
#         #print(now , al)
#         for key in al.keys():
#             if key != now[-1] and al[key]>=1:
#                 next_al = al.copy()
#                 next_al[key] -= 1
#                 next = now + key
#                 if visited[next] != 0: continue
#                 visited[next] += 1
#                 if len(next) == len(word):
#                     answer += 1
#                     continue 
#                 dfs(next, next_al)

#     for key in alpha.keys():
#         next_al = alpha.copy()
#         next_al[key] -= 1
#         next_word = key
#         dfs(next_word, next_al)
    
#     print(answer)

# solution()

