import re 

def solution(new_id):
    
    level1 = new_id.lower()
    level2 = ''.join(char for char in level1 if char not in '~!@#$%^&*()=+[{]}:?,<>/')
    
    level3 = re.sub('[.]{1,}', '.', level2)
    level4 = level3
    
    while level4 and level4.startswith('.'): level4 = level4.lstrip('.')
    while level4 and level4.endswith('.'): level4 = level4.rstrip('.')
    
    level5 = level4
    if not level4: level5 = 'a'
        
    level6 = level5
    
    if len(level6) >= 16: 
        level6 = level6[:15]
        while level6 and level6.endswith('.'): level6 = level6.rstrip('.')
            
    level7 = level6
    length_7 = len(level7)
    
    if length_7 <= 2:
        level7 += level7[-1] * (3 - length_7)
    
    answer = level7
    return answer

import re

def solution(new_id):
    st = new_id
    st = st.lower()
    st = re.sub('[^a-z0-9\-_.]', '', st)
    st = re.sub('\.+', '.', st)
    st = re.sub('^[.]|[.]$', '', st)
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
    return st


