
def dfs(node, graph,visited):
    if node in visited:
        return
    visited.add(node)
    for child in graph[node]:
        dfs(child, graph,visited)

    print(node, end= ' ')


graph = {
    1: [19, 21, 14],
    19: [21, 7, 12, 31],
    21: [14, ],
    14: [23, 6],
    7: [1, ],
    12: [],
    31: [21, ],
    23: [21, ],
    6: [],

}

visited = set()


for node in graph:
    dfs(node, graph, visited)
