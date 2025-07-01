def waiter(number, q):
    # Write your code here
    answers = []
    primes = generate_n_primes(q)
    counter = 1
    A = number
    B = []
    for i in range(q):
        prime = primes.pop(0)
        newA = []
        for a in range(len(A)):
            if A[a] % prime == 0:
                B.append(A[a])
            else:
                newA.append(A[a])
        A = newA
        if counter % 2 == 0:
            # A.reverse()
            answers += A
        else:
            # B.reverse()
            answers += B
        counter+=1
    answers += A
    return answers

def generate_n_primes(n):
    primes = []
    counter = 0
    number = 2
    while counter < n:
        isPrime = True
        for i in range(1, number):
            if i != 1 and (number % i) == 0:
                isPrime = False
        if isPrime:
            primes.append(number)
            counter += 1
        number += 1
    return primes

waiter([3, 4, 7, 6, 5], 1)