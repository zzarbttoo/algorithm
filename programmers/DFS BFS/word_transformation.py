def solution(begin, target, words):

    answer = 51 #최대 단어 갯수 이상 

    def dfs(now_word, now_depth, new_words):

        nonlocal answer

        if now_word == target:
            answer = min(now_depth, answer)

        if now_depth == len(words):
            return 

        for i in range(len(target)):
            startwith = now_word[:i]
            endwith = now_word[i+1:]

            for word in new_words:
                new_words = new_words[:] #다른 배열로 copy
                if (startwith == "" and word.endswith(endwith)) or  (endwith == "" and word.startswith(startwith)) or (word.startswith(startwith) and word.endswith(endwith)):
                    new_words.remove(word)
                    dfs(word, now_depth + 1, new_words)

    
    dfs(begin, 0, words)
    if answer == 51:
        return 0

    return answer
   

begin = "hit" 
target = "cog"
#words = ["hot", "dot", "dog", "lot", "log", "cog"]
words = ["hot", "dot", "dog", "log", "log"]

#begin = "hit"
#target = "hhh"
#words = ["hhh", "hht"]

print("solution ::: " + str(solution(begin, target, words)))