size = [0] * 100001
parent = [0] * 100001

def find(a):
    if a == parent[a]:
        return a
    parent[a] = find(parent[a])
    return parent[a]

def group(a, b):
    a = find(a)
    b = find(b)

    if a == b:
        return

    if size[a] < size[b]:
        swap(a, b)

    parent[b] = a
    size[a] += size[b]


def swap(a, b):
    temp = size[a]
    size[a] = size[b]
    size[b] = temp


def roads_and_libraries(n, c_lib, c_road,  cities):
    if c_lib < c_road:
        return n * c_lib
    
    for i in range(n):
        size[i] = 1
        parent[i] = i

    for c in cities:
        group(c[0], c[1])

    umap = {}
    cost = 0

    for i in range(n):
        p = find(i)
        if not (p in umap and umap[p] is True):
            cost += c_lib
            cost += (size[p] - 1) * c_road
            umap[p] = 1

    return cost


def roadsAndLibraries(n, c_lib, c_road, cities):
    # Write your code here
    graph = {}
    for city in cities:
        if city[0] not in graph.keys():
            graph[city[0]] = []
        if city[1] not in graph.keys():
            graph[city[1]] = []
        graph[city[0]].append(city[1])
        graph[city[1]].append(city[0])

    visited = [False] * (n + 1)
    group_sizes = []
    for i in range(n):
        if i in graph.keys() and len(graph[i]) > 0 and not visited[i]:
            group_sizes.append(dfs(graph, i, visited))
        elif i not in graph.keys() or len(graph[i]) == 0:
            group_sizes.append(1)
    cost = 0
    for group_size in group_sizes:
        cost += min((group_size - 1) * c_road + c_lib, group_size * c_lib)

    return cost


def dfs(graph, source_vertex, visited):
    visited[source_vertex] = True
    ans = 1
    for vertex in graph[source_vertex]:
        if not visited[vertex]:
            ans += dfs(graph, vertex, visited)
    return ans

roadsAndLibraries(5, 6, 1, [[1, 2], [1, 3], [1, 4]])