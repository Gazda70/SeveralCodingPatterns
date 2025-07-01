def solve(arr, queries):
    # Write your code here
    res_arr = []
    for q in queries:
        maxnum = max(arr[:q])
        minimum = maxnum
        for i in range(q, len(arr) + 1):
            if i % q == 0:
                maxnum = max(arr[i-q:i])
            if maxnum < minimum:
                minimum = maxnum
        res_arr.append(minimum)
    return res_arr

solve([33, 11, 44, 11, 55], [1, 2, 3, 4, 5])