def solution():
    N = int(input())
    nums  = list(map(int, input().split()))
    st = [N-1]

    answer = ['0' for _ in range(N)]

    for idx in range(N - 2, -1, -1):
        print(idx)
        while st:
            if nums[st[-1]] <= nums[idx]:
                answer[st.pop()] = str(idx + 1)
            else:
                break
        st.append(idx)

    print(' '.join(answer))









solution()
