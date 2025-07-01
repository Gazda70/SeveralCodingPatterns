def hackerlandRadioTransmitters(x, k):
    # Write your code here
    i = 0
    count = 0
    n = len(x)
    x.sort()
    while i < n:
        loc = x[i] + k
        while i < n and x[i] <= loc:
            i += 1

        i -= 1
        count += 1

        loc = x[i] + k
        while i < n and x[i] <= loc:
            i += 1

    return count


hackerlandRadioTransmitters([7, 2, 4, 6, 5, 9, 12, 11], 2)