def solution(rows, columns, queries):

    answer = []
    before = []
    count = 0

    for row in range(rows):
        temp = []
        for col in range(columns):
            count += 1
            temp.append(count)
        before.append(temp)

    for query in queries:

        m = float('inf')
        y1, x1, y2, x2 = query[0] - 1, query[1] - 1, query[2] - 1, query[3] - 1
        next = before[:]

        #left
        n_l = [before[col][x1] for col in range(y1 + 1, y2 + 1)]
        #right
        n_r = [before[col][x2] for col in range(y1, y2)]
        #top 
        n_t = [before[y1][row] for row in range(x1, x2)]
        #bottom
        n_b = [before[y2][row] for row in range(x1 + 1, x2 + 1)]

        for i, col in enumerate(range(y1, y2)):
            next[col][x1] = n_l[i]
            if n_l[i] < m: m = n_l[i]

        for i, col in enumerate(range(y1 + 1, y2 + 1)):
            next[col][x2] = n_r[i]
            if n_r[i] < m: m = n_r[i]

        for i, row in enumerate(range(x1 + 1, x2 + 1)):
            next[y1][row] = n_t[i]
            if n_t[i] < m: m = n_t[i]

        for i, row in enumerate(range(x1, x2)):
            next[y2][row] = n_b[i]
            if n_b[i] < m: m = n_b[i]

        before = next[:]
        answer.append(m)

    return answer
