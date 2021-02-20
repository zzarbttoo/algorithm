def solution(arr:list, n:int)->bool:

    arr.sort()

    left, right = 0, len(arr)-1

    while not left == right:
        if arr[left] + arr[right] > n:
            right -= 1
        elif arr[left] + arr[right] < n:
            left += 1
        elif arr[left] + arr[right] == n:
            return True

    return False

print(solution([5, 3, 9, 13], 8))
print(solution([5, 3, 9, 13], 7))