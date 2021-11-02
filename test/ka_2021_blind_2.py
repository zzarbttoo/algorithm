from itertools import combinations 
from collections import defaultdict
def solution(orders, course):
    
    course_hash = defaultdict(int)
    
    for i, order in enumerate(orders):
        for co in course:
            for co_maden in list(combinations(sorted(list(order)), co)):
                course_hash[''.join(co_maden)] += 1
    
    answer_hash = defaultdict(lambda : defaultdict(list))
    answer = []
    
    for key, value in course_hash.items():
        if value >= 2: answer_hash[len(key)][value].append(key)
    
    for co in course:
        if len(answer_hash[co].keys()) != 0:
            answer += answer_hash[co][max(answer_hash[co].keys())]
    
    return sorted(answer)




import collections
import itertools

def solution(orders, course):
    result = []

    for course_size in course:
        order_combinations = []
        for order in orders:
            order_combinations += itertools.combinations(sorted(order), course_size)

        most_ordered = collections.Counter(order_combinations).most_common()
        result += [ k for k, v in most_ordered if v > 1 and v == most_ordered[0][1] ]

    return [ ''.join(v) for v in sorted(result) ]
