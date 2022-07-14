from typing import List

def dfs(mat: List[List[int]], r: int, c: int, visited: set) -> bool:
    
    def r_inbounds() -> bool:
        if r >= 0 and r < len(mat): return True
        return False
    
    def c_inbounds() -> bool:
        if c >= 0 and c < len(mat[0]): return True
        return False
    
    if (r,c) in visited: return False
    if not r_inbounds() or not c_inbounds(): return False
    if not mat[r][c]: return False
    visited.add((r,c))
    neighbors = [(r-1,c),(r+1,c),(r,c-1),(r,c+1)]
    for r,c in neighbors:
        dfs(mat,r,c,visited)
    return True

def island_count(mat: List[List[int]]) -> int:
    visited = set()
    islands = 0
    for r in range(len(mat)):
        for c in range(len(mat[0])):
            if dfs(mat,r,c,visited): islands += 1
    return islands    

def dfs_count(mat: List[List[int]], r: int, c: int, visited: set) -> int:
    
    def r_inbounds() -> bool:
        if r >= 0 and r < len(mat): return True
        return False
    
    def c_inbounds() -> bool:
        if c >= 0 and c < len(mat[0]): return True
        return False
    
    island_size = 0
    if (r,c) in visited: return island_size
    if not r_inbounds() or not c_inbounds(): return island_size
    if not mat[r][c]: return island_size
    visited.add((r,c))
    neighbors = [(r-1,c),(r+1,c),(r,c-1),(r,c+1)]
    for r,c in neighbors:
        island_size += dfs_count(mat,r,c,visited)
    return 1 + island_size

def smallest_island(mat: List[List[int]]) -> int:
    smallest = float("inf"); visited = set()
    for r in range(len(mat)):
        for c in range(len(mat[0])):
            size = dfs_count(mat,r,c,visited)
            if size: smallest = min(smallest,size)
    return smallest

grid = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 1, 1, 0],
    [1, 0, 0, 1, 1],
    [1, 1, 0, 0, 0]
]

if __name__ == "__main__":
    print(f"[{island_count(grid)}] island(s) found in our grid")
    print(f"Smallest island contains [{smallest_island(grid)}] elements")