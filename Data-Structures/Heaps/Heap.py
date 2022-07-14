class MinHeap:
    
    def __init__(self, capacity):
        self.capacity = capacity
        self.heap = [0] * capacity
        self.size = 0
        
    @staticmethod
    def getParentIndex(idx : int) -> int:
        return (idx - 1) // 2 
        
    @staticmethod
    def getLeftChildIndex(idx : int) -> int:
        return 2 * idx + 1
    
    @staticmethod
    def getRightChildIndex(idx : int) -> int:
        return 2 * idx + 2
        
    def hasParent(self, idx : int) -> bool:
        return self.getParentIndex(idx) >= 0
        
    def hasLeftChild(self, idx : int) -> bool:
        return self.getLeftChildIndex(idx) < self.size
    
    def hasRightChild(self, idx : int) -> bool:
        return self.getRightChildIndex(idx) < self.size
    
    def parent(self, idx : int) -> int:
        if self.hasParent(idx): return self.heap[self.getParentIndex(idx)]
        return None
    
    def leftChild(self, idx : int) -> int:
        if self.hasLeftChild(idx): return self.heap[self.getLeftChildIndex(idx)]
        return None
    
    def rightChild(self, idx : int) -> int:
        if self.hasRightChild(idx): return self.heap[self.getRightChildIndex(idx)]
        return None

    def isFull(self) -> bool:
        return self.size == self.capacity
    
    def swap(self, idx1 : int, idx2 : int) -> None:
        tmp = self.heap[idx1]
        self.heap[idx1] = self.heap[idx2]
        self.heap[idx2] = tmp
        
    def insert(self, data : int) -> None:
        if self.isFull(): raise("Heap full")
        self.heap[self.size] = data
        self.size += 1
        self.heapifyUp(self.size - 1)
        
    def heapifyUp(self, index : int) -> None:
        if self.hasParent(index) and self.parent(index) > self.heap[index]:
            self.swap(index,self.getParentIndex(index))
            self.heapifyUp(self.getParentIndex(index))
           
    def heapifyDown(self, index : int) -> None:
        smallest = index
        if self.hasLeftChild(index) and self.leftChild(index) < self.heap[smallest]:
            smallest = self.getLeftChildIndex(index)
        if self.hasRightChild(index) and self.rightChild(index) < self.heap[smallest]:
            smallest = self.getRightChildIndex(index)
        if smallest != index:
            self.swap(index, smallest)
            self.heapifyDown(smallest)
            
    def removeMin(self) -> None:
        if self.size == 0: raise("Empty heap")
        self.storage[0] = self.storage[self.size - 1]
        self.size -= 1
        self.heapifyDown(0)
        
        
            

    