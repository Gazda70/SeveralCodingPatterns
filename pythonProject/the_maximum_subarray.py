def maxSubarray(arr):
    # Write your code here
    greater_than_zero = [i for i in arr if i > 0]
    if len(greater_than_zero) == 0:
        return [max(arr), max(arr)]
    else:
        max_sub = arr[0]
        maxEnding = arr[0]
        for i in range(1, len(arr)):
            maxEnding = max(maxEnding + arr[i], arr[i])
            max_sub = max(max_sub, maxEnding)
        return [max_sub, sum(greater_than_zero)]

maxSubarray([2, -1, 2, 3, 4, -5])