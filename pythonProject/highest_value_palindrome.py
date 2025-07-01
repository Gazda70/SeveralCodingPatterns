def highestValuePalindrome(n, k, s):
    # Write your code here
    if k == n:
        return ''.join(['9'] * n)
    arr = list(s)
    lefts = []
    for i in range(n // 2):
        if arr[i] != arr[n - i - 1]:
            if k == 0:
                return '-1'
            val = max(arr[i], arr[n - i - 1])
            arr[i] = val
            arr[n - i - 1] = val
            lefts.append(i)
            k-=1
    lefts_idx = 0
    while k >= 1 and lefts_idx < len(lefts):
        arr[lefts[lefts_idx]] = '9'
        arr[n - lefts[lefts_idx] - 1] = '9'
        lefts_idx+=1
        k-=1
    l = 0
    r = n-1
    while k >= 2 and l < r:
        if arr[l] != '9' and arr[r] != '9':
            arr[l] = '9'
            arr[r] = '9'
            k-=2
        l+=1
        r-=1
    if k == 1 and len(arr) % 2 == 1:
        arr[len(arr) // 2] = '9'
    return ''.join(arr)


highestValuePalindrome(5, 2, '44534')
