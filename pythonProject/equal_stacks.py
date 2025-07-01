def equalStacks(h1, h2, h3):
    l1 = sum(h1)
    l2 = sum(h2)
    l3 = sum(h3)
    # Write your code here
    r1 = r2 = r3 = 0  # Indices of which cylinder to remove

    # Use a greedy approach to make heights equal
    while not (l1 == l2 == l3):
        if l1 >= l2 and l1 >= l3:
            l1 -= h1[r1]
            r1 += 1
        elif l2 >= l1 and l2 >= l3:
            l2 -= h2[r2]
            r2 += 1
        else:
            l3 -= h3[r3]
            r3 += 1
    return l1

equalStacks([3, 2, 1, 1, 1], [4, 3, 2], [1, 1, 4, 1])