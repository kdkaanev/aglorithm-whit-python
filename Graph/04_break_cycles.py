def dfs(node,destination, graph, visited):
    if node in visited:
        return
    visited.add(node)
    if node == destination:
        return
    for child in graph:
        dfs(child,destination, graph, visited)



def path_exist(source, destination, graph):
    visited = set()

    dfs(source,destination, graph, visited)

    return destination in visited

graph = {}
eges = []
remove_eges = []
nodes = int(input())
for _ in range(nodes):
    node, children_str = input().split(" -> ")
    children = children_str.split()
    graph[node] = children

    for child in children:
        eges.append((node, child))

for source, destination in sorted(eges, key=lambda x: (x[0], x[1])):
    if destination not in graph[source] or source not in graph[destination]:
        continue
    graph[source].remove(destination)
    graph[destination].remove(source)

    if path_exist(source, destination, graph):
        remove_eges.append((source, destination))
    else:
        graph[source].append(destination)
        graph[destination].append(source)
print(f"Edges to remove: {len(remove_eges)}")
for first,second in remove_eges:
    print(f"{first} - {second}")

