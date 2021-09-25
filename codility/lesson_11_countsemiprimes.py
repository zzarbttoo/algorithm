def solution(N, P, Q):

    sieve = [1 for _ in range(N + 1)]
    sieve[0]=sieve[1] = 0

    i = 0 
    while i * i <= N:
        if sieve[i]:
            k = i * i
            while k <= N:
                sieve[k] = 0 
                k += i
        i+= 1

    prime = []

    for i, is_prime in enumerate(sieve):
        if is_prime:
            prime.append(i)
    
    #print(prime)

    semi_prime = [0 for _ in range(N + 1)]

    for num in prime:
        for next_num in prime:
            if num * next_num > N:
                break 
            else:
                #print(num * next_num)
                semi_prime[num * next_num] = 1 
    #print(semi_prime)

    answer = []

    semi_count = 0 
    semi_prime_count = [0 for _ in range(N + 1)]

    for i, num in enumerate(semi_prime):
        if num:
            semi_count += 1 
        semi_prime_count[i] = semi_count
    
    #print(semi_prime_count)
    for (start, end) in zip(P, Q):
        answer.append(semi_prime_count[end] - semi_prime_count[start - 1])
    
    #print(answer)
    return answer 