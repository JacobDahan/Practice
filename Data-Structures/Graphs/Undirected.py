from typing import Union, Dict, List
from collections import deque, defaultdict

def has_connection(graph: Dict[str,List[str]], source: str, dest: str) -> bool:
    seen = set(); stack = [source]
    while stack:
        node = stack.pop()
        if node in seen: continue
        if node == dest: return True
        seen.add(node)
        for neighbor in graph[node]: stack.append(neighbor)
    return False

def has_connection_recursive(graph: Dict[str,List[str]], source: str, dest: str, visited: set) -> bool:
    if source == dest: return True
    if source not in visited:
        visited.add(source)
        for neighbor in graph[source]:
            if has_connection_recursive(graph,neighbor,dest,visited): return True
    return False

def dfs(graph: Dict[str,List[str]], node: str, visited: set) -> bool:
    if node in visited: return False
    visited.add(node)
    for neighbor in graph[node]: dfs(graph, neighbor, visited)
    return True

def count_connected_components(graph: Dict[str,List[str]]) -> int:
    visited = set(); connected_components = 0
    for node in graph:
        if dfs(graph,node,visited):
            connected_components += 1
    return connected_components

def dfs_count(graph: Dict[str,List[str]], node: str, visited: set) -> int:
    if node in visited: return 0
    visited.add(node); count = 0
    for neighbor in graph[node]:
        count += dfs_count(graph,neighbor,visited)
    return 1 + count

def largest_component(graph: Dict[str,List[str]]) -> int:
    visited = set(); largest = 0
    for node in graph:
        if node in visited: continue
        largest = max(largest, dfs_count(graph,node,visited))
    return largest

def shortest_path(graph: Dict[str,List[str]], source: str, dest: str) -> int:
    count = 0; queue = deque([(source,count)]); visited = set([source])
    while queue:
        node, count = queue.popleft()
        if node == dest: return count
        visited.add(node)
        for neighbor in graph[node]:
            if not neighbor in visited:
                queue.append((neighbor,count + 1))
    return -1

def graph_from_edges(edges: List[List[str]]) -> Dict[str,List[str]]:
    graph = defaultdict(list)
    for node1,node2 in edges:
        if node1 == node2: graph[node1] = []; continue
        graph[node1].append(node2)
        graph[node2].append(node1)
    return graph

edges = [
    ['w','x'],
    ['w','v'],
    ['v','z'],
    ['x','y'],
    ['z','y']
]

def main():
    a, b = 'j','m'
    graph = graph_from_edges(edges)
    print(graph)
    #print(f"Graph has connection between [{a}], [{b}]: {has_connection(graph,'j','m')}")
    #print(f"Graph has connection between [{a}], [{b}]: {has_connection_recursive(graph,'j','m',set())}")
    #print(f"[{count_connected_components(graph)}] components in graph")
    #print(f"Largest component in graph contains [{largest_component(graph)}] elements")
    print(shortest_path(graph,'w','z'))

if __name__ == "__main__":
    main()