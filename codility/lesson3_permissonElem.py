# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import collections

def solution(A):

    count_hash = collections.defaultdict(int)

    for count in A:
        count_hash[count] += 1
    
    for num in range(1, len(A) + 2):
        if count_hash[num] == 0:
            return num



    
