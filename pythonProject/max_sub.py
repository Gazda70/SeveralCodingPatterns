def maxSubarray(arr):
    # Write your code here
    max_sub = 0
    for i in range(len(arr)):
        for j in range(i, len(arr) + 1):
            max_sub = max(max_sub, sum(arr[i:j]))

    max_subseq = sum(arr)
    for i in range(len(arr)):
        if (sum(arr) - arr[i]) > max_subseq:
            max_subseq = sum(arr[:i]) + sum(arr[i:])

    return [max_sub, max_subseq]

maxSubarray([1, 2, 3, 4])
maxSubarray([2, -1, 2, 3, 4, -5])