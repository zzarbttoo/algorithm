from collections import defaultdict

def find_all_hobbyists(hobby, hobbies):

    hob = defaultdict(list)

    for k, v in hobbies.items():
        for h in v:
            hob[h].append(k)
    
    return sorted(list(hob[hobby]))


if __name__ == "__main__":
    hobbies = { 
        "Steve": ['Fashion', 'Piano', 'Reading'],
        "Patty": ['Drama', 'Magic', 'Pets'],
        "Chad": ['Puzzles', 'Pets', 'Yoga']
    }
    
    
    print(find_all_hobbyists('Yoga', hobbies))

