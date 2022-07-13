from typing import List, Union
from collections import deque

class Node:
    
    def __init__(self, data : Union[list,tuple,str]):
        self.data = data
        self.left = self.right = None
       
       
def dfs(node : "Node") -> List[Union[None,list,tuple,str]]:
    if not node: return []
    stack = [node]; visited = []
    while stack:
        curr_node = stack.pop()
        visited.append(curr_node.data)
        if curr_node.right: stack.append(curr_node.right)
        if curr_node.left: stack.append(curr_node.left)
    return visited

def dfs_recursive(node : "Node") -> List[Union[None,list,tuple,str]]:
    if not node: return []
    return [node.data, *dfs_recursive(node.left), *dfs_recursive(node.right)] 

def bfs(node : "Node") -> List[Union[None,list,tuple,str]]:
    if not node: return []
    queue = deque([node]); visited = []
    while queue:
        curr_node = queue.popleft(); visited.append(curr_node.data)
        if curr_node.left: queue.append(curr_node.left)
        if curr_node.right: queue.append(curr_node.right)
    return visited

def dfs_includes(node : "Node", target : Union[list,tuple,str]) -> bool:
    if not node: return False
    stack = [node]
    while stack:
        curr_node = stack.pop()
        if curr_node.data == target: return True
        if curr_node.right: stack.append(curr_node.right)
        if curr_node.left: stack.append(curr_node.left)
    return False

def dfs_recursive_includes(node : "Node", target : Union[list,tuple,str]) -> bool:
    if not node: return False
    if node.data == target: return True
    return dfs_recursive_includes(node.left,target) or dfs_recursive_includes(node.right,target)

def bfs_includes(node : "Node", target : Union[list,tuple,str]) -> bool:
    if not node: return False
    queue = deque([node])
    while queue:
        curr_node = queue.popleft()
        if curr_node.data == target: return True
        if curr_node.left: queue.append(curr_node.left)
        if curr_node.right: queue.append(curr_node.right)
    return False

def dfs_sum(node : "Node") -> int:
    if not node: return 0
    stack = [node]; running_sum = 0
    while stack:
        curr_node = stack.pop()
        running_sum += curr_node.data
        if curr_node.right: stack.append(curr_node.right)
        if curr_node.left: stack.append(curr_node.left)
    return running_sum

def dfs_recursive_sum(node : "Node") -> int:
    if not node: return 0
    return node.data + dfs_recursive_sum(node.left) + dfs_recursive_sum(node.right)

def bfs_sum(node : "Node") -> int:
    if not node: return 0
    queue = deque([node]); running_sum = 0
    while queue:
        curr_node = queue.popleft()
        running_sum += curr_node.data
        if curr_node.left: queue.append(curr_node.left)
        if curr_node.right: queue.append(curr_node.right)
    return running_sum

def dfs_min(node : "Node") -> float:
    if not node: return float("inf")
    stack = [node]; running_min = float("inf")
    while stack:
        curr_node = stack.pop()
        running_min = min(curr_node.data,running_min)
        if curr_node.right: stack.append(curr_node.right)
        if curr_node.left: stack.append(curr_node.left)
    return running_min
 
def dfs_recursive_min(node : "Node") -> float:
    if not node: return float("inf")
    return min(node.data, dfs_recursive_min(node.left), dfs_recursive_min(node.right))

def bfs_min(node : "Node") -> float:
    if not node: return float("inf")
    queue = deque([node]); running_min = float("inf")
    while queue:
        curr_node = queue.popleft()
        running_min = min(curr_node.data,running_min)
        if curr_node.left: queue.append(curr_node.left)
        if curr_node.right: queue.append(curr_node.right)
    return running_min
 
def max_root_to_leaf(node : "Node") -> float:
    if not node: return float("-inf")
    if not node.left and not node.right: return node.data
    return max((node.data + max_root_to_leaf(node.left)),(node.data + max_root_to_leaf(node.right)))
        
a = Node('a'); b = Node('b'); c = Node('c'); d = Node('d'); e = Node('e'); f = Node('f')

a.left = b; a.right = c
b.left = d; b.right = e
c.right = f

print(dfs(a))
print(dfs_recursive(a))
print(bfs(a))
print(dfs_includes(a,'d'))
print(dfs_includes(a,'f'))
print(dfs_includes(a,'j'))
print(dfs_recursive_includes(a,'d'))
print(dfs_recursive_includes(a,'f'))
print(dfs_recursive_includes(a,'j'))
print(bfs_includes(a,'d'))
print(bfs_includes(a,'a'))
print(bfs_includes(a,'j'))


a = Node(3); b = Node(11); c = Node(4); d = Node(4); e = Node(-2); f = Node(1)

a.left = b; a.right = c
b.left = d; b.right = e
c.right = f

print(dfs_sum(a))
print(dfs_recursive_sum(a))
print(bfs_sum(a))
print(dfs_min(a))
print(dfs_recursive_min(a))
print(bfs_min(a))
print(max_root_to_leaf(a))