from typing import List, Union
from collections import deque

class SearchNode:
    
    def __init__(self, data : Union[str,float]):
        self.data = data
        self.left = None
        self.right = None
        
    def add_child(self, child_data : Union[str,float]):
        if child_data == self.data: return
        if child_data < self.data:
            if self.left is None: self.left = SearchNode(child_data)
            else: self.left.add_child(child_data)
        else: 
            if self.right is None: self.right = SearchNode(child_data)
            else: self.right.add_child(child_data)
            
    def dfs_inorder(self, node : "SearchNode") -> List[Union[str,float]]:
        if not node: return []
        if not node.left and not node.right: return [node.data]
        return [*self.dfs_inorder(node.left), node.data, *self.dfs_inorder(node.right)]
    
    def dfs_preorder(self, node : "SearchNode") -> List[Union[str,float]]:
        if not node: return []
        if not node.left and not node.right: return [node.data]
        return [node.data, *self.dfs_preorder(node.left), *self.dfs_preorder(node.right)]
    
    def dfs_postorder(self, node : "SearchNode") -> List[Union[str,float]]:
        if not node: return []
        if not node.left and not node.right: return [node.data]
        return [*self.dfs_postorder(node.left), *self.dfs_postorder(node.right), node.data]
    
    def search(self, val : Union[str,float]) -> bool:
        if self.data == val: return True
        if self.data > val: 
            if self.left: return self.left.search(val)
            else: return False
        if self.right: return self.right.search(val)
        return False
    
    def find_min(self) -> Union[str,float]:
        if not self.left: return self.data
        return min(self.data, self.left.find_min())
    
    def find_max(self) -> Union[str,float]:
        if not self.right: return self.data
        return max(self.data, self.right.find_max())
    
    def sum(self) -> int:
        if not self.left and not self.right: return self.data
        if not self.right: return self.data + self.left.sum()
        if not self.left: return self.data + self.right.sum()
        return self.data + self.left.sum() + self.right.sum()
        
    def delete(self, key) -> "SearchNode":
        if self.data > key: self.left = self.left.delete(key)
        elif self.data < key: self.right = self.right.delete(key)
        else: # node found
            if not self.left and not self.right: return None # leaf node condition; set to null
            if self.left: # at least left branch
                self.data = self.left.find_max() # maximum value of the left branch; > all left, < all right
                self.left = self.left.delete(self.data) # search left branch to recursively push node to leaf; delete
            else:
                self.data = self.right.find_min() # minimum value of right branch; > all left, < all right
                self.right = self.right.delete(self.data) # search right branch to recursively push node to leaf; delete
        return self
        
    def findNextBiggest(self) -> int:
        next_node = self.right
        while next_node.left:
            next_node = next_node.left
        return next_node.data
      
    def findNextSmallest(self) -> int:
        next_node = self.left
        while next_node.right:
            next_node = next_node.right
        return next_node.data

def build_tree(numbers : List[Union[str,float]]) -> "SearchNode":
    nodes = deque(numbers)
    root = SearchNode(nodes.popleft())
    while nodes:
        root.add_child(nodes.popleft())
    return root

def traverse_tree(tree : "SearchNode") -> "SearchNode":
    print(f"Inorder tree traversal: {tree.dfs_inorder(tree)}")
    print(f"Preorder tree traversal: {tree.dfs_preorder(tree)}")
    print(f"Postorder tree traversal: {tree.dfs_postorder(tree)}")
    return tree

def search_tree(tree : "SearchNode", keys : List[Union[str,float]]) -> "SearchNode":
    for k in keys: print(f"[{k}] in tree: {tree.search(k)}")
    return tree

def minmax(tree : "SearchNode") -> "SearchNode":
    print(f"Min of tree: [{tree.find_min()}]")
    print(f"Max of tree: [{tree.find_max()}]")
    return tree

def tree_sum(tree : "SearchNode") -> "SearchNode":
    print(f"Sum of tree elements: [{tree.sum()}]")
    return tree

def delete(tree : "SearchNode", key : int) -> "SearchNode":
    tree = tree.delete(key)
    print(f"Tree with deletion of element [{key}]: {tree.dfs_inorder(tree)}")
    return tree

def main(numbers = [5,3,6,2,4,7]):
    tree = build_tree(numbers)
    tree = traverse_tree(tree)
    tree = search_tree(tree, [20, 6, 34])
    tree = minmax(tree)
    tree = tree_sum(tree)
    tree = delete(tree, 3)

if __name__ == "__main__":
    main()