def dfs(node, graph, visited, cycles):
    if node in cycles:
        raise Exception
    if node in visited:
        return
    visited.add(node)
    cycles.add(node)

    for neighbor in graph[node]:
        dfs(neighbor, graph, visited, cycles)
    cycles.remove(node)


graph = {}
while True:
    line = input()
    if line == 'End':
        break
    sours, destination = line.split('-')
    if sours not in graph:
        graph[sours] = []
    if destination not in graph:
        graph[destination] = []
    graph[sours].append(destination)


try:
    visited = set()
    for node in graph:
        dfs(node, graph, visited, set())
    print('Acyclic: Yes')
except Exception:
    print('Acyclic: No')
