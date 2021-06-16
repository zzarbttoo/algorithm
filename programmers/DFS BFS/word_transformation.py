def solution(begin, target, words):

    answer = 51 #최대 단어 갯수 이상 

    def dfs(begin, now_depth):

        nonlocal answer

        if begin == target:
            answer = min(now_depth, answer)

        if now_depth == len(words):
            return 

        for i in range(len(target)):
            startwith = begin[:i]
            endwith = begin[i+1:]

            for word in words:
                if startwith == "" and word.endswith(endwith):
                    dfs(word, now_depth + 1)
                elif endwith == "" and word.startswith(startwith):
                    dfs(word, now_depth + 1)
                elif word.startswith(startwith) and word.endswith(endwith):
                    dfs(word, now_depth + 1)

    
    dfs(begin, 0)
    if answer == 51:
        return 0

    return answer
   

#begin = "hit" 
#target = "cog"
#words = ["hot", "dot", "dog", "lot", "log", "cog"]
#words = ["hot", "dot", "dog", "log", "log"]

begin = "hit"
target = "hhh"
words = ["hhh", "hht"]

print(solution(begin, target, words))