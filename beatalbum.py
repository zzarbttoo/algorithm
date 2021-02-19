import collections

def solution(genres:list, plays:list)->list:

    answer_list = []
    genre_hash = collections.defaultdict(list)

    for i, (genre, play_time) in enumerate(zip(genres, plays)):
        genre_hash[genre].append((i, play_time))
        
    #map의 key를 정렬하는 것이 아니라 list에 key들을 담아서 정렬
    #print(sum(list(map(lambda y:y[1], genre_hash['pop']))))
    sorted_key = sorted(list(genre_hash.keys()), key = lambda x : sum(map(lambda y:y[1], genre_hash[x])), reverse = True)
    print(sorted_key)

    for key in sorted_key:
        #temp = sorted(genre_hash[key], key = lambda x:x[1],reverse = True)[:min(len(genre_hash), 2)]
        temp = list(map(lambda y: y[0], sorted(genre_hash[key], key = lambda x:x[1],reverse = True)[:min(len(genre_hash), 2)]))
        #appendlist 는 이중리스트 됨 
        answer_list += temp
       
    return answer_list


print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))