from heapq import heapify, heappop, heappush

def cookies(k, A):
    # Write your code here
    count = 0
    heapify(A)
    while A[0] < k and len(A) >= 2:
        count += 1
        least = heappop(A)
        sleast = heappop(A)
        new = least + 2 * sleast
        heappush(A, new)
    if min(A) < k:
        return -1
    return count

cookies(7, [1, 2, 3, 9, 10, 12])