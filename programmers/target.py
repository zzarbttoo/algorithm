def targetTree(targetArray:list, target:int) -> int:
    
    root:list = [0]

    for i in targetArray:
        appendList = []
        for j in root:
            appendList.append(j + i)
            appendList.append(j - i)
        root = appendList
    
    #print(root)
    answer:int = root.count(target)
    return answer

print(targetTree([1,2,3], 1))