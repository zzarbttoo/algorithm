from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.children = self.root.children.keys()

    #word 삽입
    def insert(self, word):
        node = self.root
        for w in word:
            node = node.children[w]
            node.count += 1

    #query 갯수 반환
    def startCount(self, word):
        node = self.root
        for w in word:
            if w == '?':
                break
            node = node.children[w]
        return node.count

def solution(words, queries):

    answer = []

    #뒤집은거, 멀쩡한 것 하나 
    #모두 물음표일 경우 count만 하나 늘려주기

    #길이에 따라 분류
    #첫번째는 정방향, 두번째는 rev
    trie_dict = defaultdict(lambda: [Trie(), Trie()])

    for word in words:
        length = len(word)
        trie_dict[length][0].insert(word)
        #rev
        trie_dict[length][1].insert(word[::-1])

    for query in queries:
        count = 0
        length = len(query)

        #뒤만 '?'
        if query[0] != '?' and query[-1] == '?':
            #print(trie_dict[length][0].startCount(query))
            answer.append(trie_dict[length][0].startCount(query))
        #앞만 '?'
        if query[0] == '?' and query[-1] != '?':
            #print(trie_dict[length][1].startCount(query[::-1]))
            answer.append(trie_dict[length][1].startCount(query[::-1]))
        #전체 '?'
        if query[0] == '?' and query[-1] =='?':
            sum = 0
            for key in trie_dict[length][0].children:
                sum += trie_dict[length][0].startCount(key)
            answer.append(sum)
    return answer