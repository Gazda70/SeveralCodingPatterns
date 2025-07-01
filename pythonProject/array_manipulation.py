def arrayManipulation(n, queries):
    # Write your code here
    arr = [0] * (n + 1)
    for q in queries:
        arr[q[0] - 1] += q[2]
        arr[q[1]] -= q[2]
    champ = float('-inf')
    suma = 0
    for a in arr:
        suma += a
        champ = max(champ, suma)
    return champ


arrayManipulation(10, [[1,5,3], [4,8,7], [6,9,1]])
arrayManipulation(5, [[1,2,100], [2,5,100], [3,4,100]])