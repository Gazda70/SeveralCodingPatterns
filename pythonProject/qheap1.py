from heapq import heappush, heapify, heappop

q = []
q2 = []

for _ in range(int(input())):
    op = list(map(int, input().split()))

    if op[0] == 1:
        heappush(q, op[1])
    elif op[0] == 2:
        heappush(q2, op[1])
    elif op[0] == 3:
        while len(q2) > 0 and q[0] == q2[0]:
            heappop(q)
            heappop(q2)
        print(q[0])
