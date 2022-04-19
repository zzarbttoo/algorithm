class Node(object):
    def __init__(self) :
        self.children = {}

class Trie:
    def __init__(self):
        self.head = Node()

    def insert(self, string):
        cur = self.head

        for c in string:
            if c not in cur.children:
                cur.children[c] = Node()
            cur = cur.children[c]

    def is_prefix(self, string):
        cur = self.head

        for c in string:
            cur = cur.children[c]
        
        if not cur.children:
            return False 
        return True


def solution():
    n = int(input())
    words = []
    trie = Trie()

    for _ in range(n):
        word = input()
        words.append(word)
        trie.insert(word)

    for w in words:
        if trie.is_prefix(w):
            return "NO"
    
    return "YES"
        

t = int(input())
answer = []

for _ in range(t):
    answer.append(solution())

for a in answer:
    print(a)
    
