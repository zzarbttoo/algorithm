

#in 연산자 list, tuple (O(n))
#set, dictionary : O(1), O(n)
#dict from keys

import collections


def solution(participant:list, completion:list) -> str:

    person = collections.Counter(participant) - collections.Counter(completion)

    return list(person.keys())[0]

print(solution(["leo", "kiki", "eden"], ["leo", "eden"]))