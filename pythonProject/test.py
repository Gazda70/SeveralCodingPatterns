def lca(root, v1, v2):
    # Enter your code here
    return recursive(root, v1, v2)


def recursive(root, v1, v2):
    if v1 < root.info and v2 > root.info:
        return root
    if v1 < root.info and v2 < root.info:
        return recursive(root.left, v1, v2)
    elif v1 > root.info and v2 > root.info:
        return recursive(root.right, v1, v2)


N = 3

grid = [".X.", ".X.", "..."]

a, b,  = 0, 0
c, d = 0,2

moves = [[[a, b]]]
visited = [[False for i in range(N)] for j in range(N)]
visited[a][b] = True

while [c, d] not in moves[-1]:
    nxt = []

    for m in moves[-1]:
        i = m[0] + 1
        j = m[1]
        while i < N and grid[i][j] != 'X':
            if not visited[i][j]:
                nxt.append([i, j])
                visited[i][j] = True
            i += 1

        i = m[0] - 1
        j = m[1]
        while i >= 0 and grid[i][j] != 'X':
            if not visited[i][j]:
                nxt.append([i, j])
                visited[i][j] = True
            i -= 1

        i = m[0]
        j = m[1] + 1
        while j < N and grid[i][j] != 'X':
            if not visited[i][j]:
                nxt.append([i, j])
                visited[i][j] = True
            j += 1

        i = m[0]
        j = m[1] - 1
        while j >= 0 and grid[i][j] != 'X':
            if not visited[i][j]:
                nxt.append([i, j])
                visited[i][j] = True
            j -= 1
    moves.append(nxt)

print(len(moves) - 1)


def minimumMoves(grid, startX, startY, goalX, goalY):
    N = len(grid)
    a, b = startX, startY
    c, d = goalX, goalY

    moves = [[[a, b]]]

    visited = [[False for i in range(N)] for j in range(N)]
    visited[a][b] = True

    while [c, d] not in moves[-1]:
        nxt = []

        # m - aktualna pozycja
        for m in moves[-1]:
            i = m[0] + 1
            j = m[1]
            while i < N and grid[i][j] != 'X':
                if not visited[i][j]:
                    nxt.append([i, j])
                    visited[i][j] = True
                i += 1

            i = m[0] - 1
            j = m[1]
            while i >= 0 and grid[i][j] != 'X':
                if not visited[i][j]:
                    nxt.append([i, j])
                    visited[i][j] = True
                i -= 1

            i = m[0]
            j = m[1] + 1
            while j < N and grid[i][j] != 'X':
                if not visited[i][j]:
                    nxt.append([i, j])
                    visited[i][j] = True
                j += 1

            i = m[0]
            j = m[1] - 1
            while j >= 0 and grid[i][j] != 'X':
                if not visited[i][j]:
                    nxt.append([i, j])
                    visited[i][j] = True
                j -= 1
        moves.append(nxt)
    return len(moves) - 1

minimumMoves(["...", ".X.", ".X."], 2, 0, 2, 2)

def findZigZagSequence(a, n):
    a.sort()
    mid = int((n + 1)/2)

    st = mid
    ed = n - 1
    while(st <= ed and ed < len(a)):
        a[st], a[ed] = a[ed], a[st]
        st = st + 1
        ed = ed + 1

    for i in range (n):
        if i == n-1:
            print(a[i])
        else:
            print(a[i], end = ' ')
    print("End of function")

findZigZagSequence([1, 2, 3, 4, 5, 6, 7], 7)