from typing import Union, Dict, List
from collections import deque

def print_dfs(graph: Dict[Union[str,float],List[Union[str,float]]], source: Union[str,float]):
    stack = [source]
    while stack:
        node = stack.pop(); print(node)
        if not graph[node]: continue
        for neighbor in graph[node]: stack.append(neighbor)

def print_dfs_recursive(graph: Dict[Union[str,float],List[Union[str,float]]], source: Union[str,float]):
    print(source)
    for neighbor in graph[source]: print_dfs_recursive(graph,neighbor)
    
def print_bfs(graph: Dict[Union[str,float],List[Union[str,float]]], source: Union[str,float]):
    queue = deque([source])
    while queue:
        curr_node = queue.popleft()
        print(curr_node)
        for neighbor in graph[curr_node]: queue.append(neighbor)

def has_path(graph: Dict[str,List[str]], source: str, dest: str) -> bool:
    stack = [source]
    while stack:
        node = stack.pop()
        if node == dest: return True
        for neighbor in graph[node]: stack.append(neighbor)
    return False

def has_path_recursive(graph: Dict[str,List[str]], source: str, dest: str) -> bool:
    if source == dest: return True
    for neighbor in graph[source]:
        if has_path_recursive(graph,neighbor,dest): return True
    return False

graph = {
    'f': ['g','i'],
    'g': ['h'],
    'h': [],
    'i': ['g','k'],
    'j': ['i'],
    'k': [],
}

def main():
    #print_dfs_recursive(graph,'a')
    #print_bfs(graph,'a')
    print(has_path_recursive(graph,'f','k'))

if __name__ == "__main__":
    main()