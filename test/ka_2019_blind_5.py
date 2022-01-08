# from collections import defaultdict

# def solution(nodeinfo):
    
#     node_idx = defaultdict(lambda : defaultdict(int))
#     parent_node = defaultdict(lambda : defaultdict(list))
#     left_node = defaultdict(lambda : defaultdict(list))
#     right_node = defaultdict(lambda : defaultdict(list))
#     y_hash = defaultdict(list)
    
#     for idx, node in enumerate(nodeinfo):
#         node_idx[node[0]][node[1]] = idx + 1
#         y_hash[node[1]].append(node)
    
#     for key in y_hash.keys():
#         y_hash[key].sort()
        
#     root = []
    
#     length = len(y_hash.keys())
#     sort_y_key = sorted(y_hash.keys(), reverse= True)
#     for idx, key in enumerate(sort_y_key):
#         if idx == 0:
#             root = y_hash[key][0]
        
#         if idx + 1 < length:
#             first, last = 0, len(y_hash[sort_y_key[idx + 1]])
#             for parent in y_hash[key]:
#                 for i, t in enumerate(range(first, first + 2)):
#                     if t < last:
#                         if i == 0 and parent[0] 
#                         print(parent)
#                         print(i)
#                         print(y_hash[sort_y_key[idx + 1]][t])
                        
#                         #print(y_hash[sort_y_key[idx + 1]])
            
# from collections import defaultdict

# def solution(nodeinfo):
    
#     node_idx = defaultdict(lambda : defaultdict(int))
#     parent_node = defaultdict(lambda : defaultdict(list))
#     left_node = defaultdict(lambda : defaultdict(list))
#     right_node = defaultdict(lambda : defaultdict(list))
#     y_hash = defaultdict(list)
    
#     for idx, node in enumerate(nodeinfo):
#         node_idx[node[0]][node[1]] = idx + 1
#         y_hash[node[1]].append(node)
    
#     key_sorted = sorted(y_hash.keys(), reverse = True)
#     idx = 0
#     root = y_hash[key_sorted[idx]][0] #root는 제약 없음
#     left_re = -float('inf') #커야함
#     right_re = float('inf') #작아야함
    
    
#     #restriction
#     def search(parent ,idx, left_re, right_re):
#         nonlocal y_hash, left_node, right_node, key_sorted
        
#         if idx + 1 < len(key_sorted):
#             for node in y_hash[key_sorted[idx + 1]]:
#                 print("node ::: " + str(node) + " left :::" + str(left_re) + " right ::: " + str(right_re) + " parent ::: " + str(parent))
#                 if node[0] > left_re and node[0] < parent[0]:
#                     left_node[parent[0]][parent[1]] = node
#                     if left_re < parent[0]:
#                         next_left_re = parent[0]
#                         next_right_re = right_re
#                         search(node, idx + 1, next_left_re, next_right_re)
                    
#                 if node[0] < right_re and node[0] > parent[0]:
#                     right_node[parent[0]][parent[1]] = node
#                     if right_re > parent[0]:
#                         next_right_re = parent[0]
#                         next_left_re = left_re
#                         search(node, idx + 1, next_left_re, next_right_re)
                        
                    
#     search(root, idx, left_re, right_re)
    
#     print(left_node)
    
#     for val in left_node.values():
#         for v in val.values():
#             print(v)
#     print(right_node)
     
#     for val in right_node.values():
#         for v in val.values():
#             print(v)
    
                
            
            
            
            
            
            
            
            
    
#     print(root)
            
            
from collections import defaultdict

def solution(nodeinfo):
    
    node_idx = defaultdict(lambda : defaultdict(int))
    parent_node = defaultdict(lambda : defaultdict(list))
    left_node = defaultdict(lambda : defaultdict(list))
    right_node = defaultdict(lambda : defaultdict(list))
    y_hash = defaultdict(list)
    
    for idx, node in enumerate(nodeinfo):
        node_idx[node[0]][node[1]] = idx + 1
        y_hash[node[1]].append(node)
    
    key_sorted = sorted(y_hash.keys(), reverse = True)
    idx = 0
    root = y_hash[key_sorted[idx]][0] #root는 제약 없음
    left_re = -float('inf') #커야함
    right_re = float('inf') #작아야함
    
    #restriction
    #def search(parent ,idx, left_re, right_re):
    def search(parent ,idx):
        nonlocal y_hash, left_node, right_node, key_sorted
        if idx + 1 < len(key_sorted):
            for node in y_hash[key_sorted[idx + 1]]:
                if idx == 0:
                    if node[0] < parent[0]:
                        left_node[parent[0]][parent[1]] = node
                    else:
                        right_node[parent[0]][parent[1]] = node
                    parent_node[node[0]][node[1]] = parent
                    search(node, idx + 1)
                    
                if idx > 0:
                    if node[0] < parent[0]:
                        if parent_node[parent[0]][parent[1]][0] < parent[0]: #부모가 우측노드
                            if node[0] < parent_node[parent[0]][parent[1]][0]:
                                continue
                            left_node[parent[0]][parent[1]] = node
                    if node[0] > parent[0]:
                        if parent_node[parent[0]][parent[1]][0] > parent[0]: #부모가 좌측노드
                            if node[0] > parent_node[parent[0]][parent[1]][0]:
                                continue
                            right_node[parent[0]][parent[1]] = node
                    parent_node[node[0]][node[1]] = parent
                    search(node, idx + 1)
                        
    
    search(root, idx)
    print(parent_node)
    
    print(left_node)
    
    for val in left_node.values():
        for v in val.values():
            print(v)
    print(right_node)
     
    for val in right_node.values():
        for v in val.values():
            print(v)