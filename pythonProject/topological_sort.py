def topological_sort_util(v, visited, adj, stack):
    visited[v] = True

    for i in adj[v]:
        if not visited[i]:
            topological_sort_util(i, visited, adj, stack)
    stack.append(v)

def topological_sort(adj, V):
    stack = []

    visited = [False] * V

    for i in range(V):
        if not visited[i]:
            topological_sort_util(i, visited, adj, stack)

    while len(stack) > 0:
        print(stack.pop(), end=" ")

# # Number of nodes
# V = 4
#
# # Edges
# edges = [[0, 1], [1, 2], [3, 1], [3, 2]]
#
# # Graph represented as an adjacency list
# adj = [[] for _ in range(V)]
#
# for i in edges:
#     adj[i[0]].append(i[1])
#
# topological_sort(adj, V)


def top_sort_util(v, adj, visited, stack):
    visited[v] = True
    for i in adj[v]:
        if not visited[i]:
            top_sort_util(i, adj, visited, stack)
    stack.append(v)

    return True


def top_sort_util(v, adj, visited, stack, cycle):
    if v in cycle:
        return False
    cycle.append(v)
    visited[v] = True
    correct = True
    for i in adj[v]:
        if i in cycle:
            return False
        if not visited[i]:
            correct = correct and top_sort_util(i, adj, visited, stack, cycle)
    stack.append(v)
    return correct


def findOrder(numCourses, prerequisites):
    """
    :type numCourses: int
    :type prerequisites: List[List[int]]
    :rtype: List[int]
    """
    schedule = []

    if numCourses <= 0:
        return []
    steps = [0 for _ in range(numCourses)]
    graph = [[] for _ in range(numCourses)]

    for pre in prerequisites:
        parent = pre[0]
        child = pre[1]

        graph[parent].append(child)
        steps[child]+=1

    sources = []

    for s in steps:
        if s == 0:
            sources.append(s)

    while len(sources) > 0:

        vertex = sources.pop()
        schedule.append(vertex)

        for child in graph[vertex]:
            steps[child] -= 1
            if steps[child] == 0:
                sources.append(child)

    if len(schedule) != numCourses:
        return[]

    return schedule

findOrder(3, [[0,1],[0,2],[1,2]])


def top_sort_util(v, adj, visited, stack):
    visited[v] = True

    for i in adj[v]:
        if not visited[i]:
            top_sort_util(i, adj, visited, stack)
    stack.append(v)

def top_sort(edges, n):
    visited = [False] * n

    adj = [[] for _ in range(n)]

    for edge in edges:
        adj[edge[0]].append(edge[1])

    stack = []

    for i in range(n):
        if visited[i] is False:
            top_sort_util(i, adj, visited, stack)

def top_sort_util(v, adj, visited, stack):
    visited[v] = True

    for i in adj[v]:
        if not visited[i]:
            top_sort_util(i, adj, visited, stack)
    stack.append(v)

def top_sort(edges, n):
    visited = [False] * n

    adj = [[] for _ in range(n)]
    for edge in edges:
        adj[edge[0]].append(edge[1])
    stack = []
    for i in range(n):
        if visited[i] is False:
            top_sort_util(i, adj, visited, stack)








def top_sort_util(i, adj, visited, stack):
    visited[i] = False
    for a in adj[i]:
        if not visited[a]:
            top_sort_util(i, adj, visited, stack)
    stack.append(i)


def top_sort(edges, n):
    visited = [False] * n
    adj = [[] for _ in range(n)]
    for edge in edges:
        adj[edge[0]].append(edge[1])
    stack = []
    for i in range(n):
        if visited[i] is False:
            top_sort_util(i, adj, visited, stack)


def top_sort_util(i, adj, visited, stack):
    visited[i] = False
    for a in adj[i]:
        if visited[a] is False:
            top_sort_util(a, adj, visited, stack)
    stack.append(a)


def top_sort(edges, n):
    visited = [False] * n
    adj = [[] for _ in range(n)]
    for edge in edges:
        adj[edge[0]].append(edge[1])
    stack = []
    for i in range(n):
        if visited[i] is False:
            top_sort_util(i, adj, visited, stack)


