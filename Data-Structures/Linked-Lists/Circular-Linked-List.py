from typing import List, Union

class Node:
    
    def __init__(self, data : Union[None,list,tuple,str] = None):
        self.data = data
        self.next = None
        
class CircularLinkedList:
    
    def __init__(self):
        self.head = None
        
    def prepend(self, data : Union[list,tuple,str]):
        if not self.head: self.head = Node(data); self.head.next = self.head; return
        new_node = Node(data)
        curr_node = self.head; next_node = curr_node.next
        while next_node is not self.head:
            curr_node = curr_node.next; next_node = next_node.next
        curr_node.next = new_node
        new_node.next = next_node
        self.head = new_node
        
    def append(self, data : Union[list,tuple,str]):
        if not self.head: self.head = Node(data); self.head.next = self.head; return
        new_node = Node(data)
        curr_node = self.head; next_node = curr_node.next
        while next_node is not self.head:
            curr_node = curr_node.next; next_node = next_node.next
        curr_node.next = new_node
        new_node.next = self.head
        
    def display_iterative(self) -> List[Union[list,tuple,str]]:
        res = []
        if not self.head: return None
        curr_node = self.head; next_node = curr_node.next
        while next_node is not self.head:
            res.append(curr_node.data)
            curr_node = curr_node.next; next_node = next_node.next
        res.append(curr_node.data)
        return res
    
    def display_recursive(self, curr_node : "Node", next_node : "Node") -> List[Union[list,tuple,str]]:
        if next_node is self.head: return [curr_node.data]
        return [curr_node.data] + self.display_recursive(next_node, next_node.next)
    
    def remove(self, key : Union[list,tuple,str]):
        if len(self) == 1: self.head = None; return
        if len(self) == 0: return
        curr_node = self.head; next_node = curr_node.next
        if curr_node.data == key:
            while next_node is not self.head: next_node = next_node.next
            next_node.next = curr_node.next
            self.head = next_node.next
        while next_node is not self.head:
            if next_node.data == key: 
                curr_node.next = next_node.next
                next_node = next_node.next
            curr_node = curr_node.next; next_node = next_node.next
          
    def __len__(self) -> int:
        if not self.head: return 0
        curr_node = self.head; next_node = curr_node.next; nodes = 1
        while next_node is not self.head:
            curr_node = curr_node.next; next_node = next_node.next
            nodes += 1
        return nodes
            
    def split_list(self):
        length = len(self); half_length = length // 2; curr_index = 0
        if length == 0: return
        if length == 1: return self.head
        curr_node = self.head; next_node = curr_node.next;
        while curr_index < half_length:
            prev_node = curr_node
            curr_node = curr_node.next; next_node = next_node.next
            curr_index += 1
        prev_node.next = self.head
        split_circular_llist = CircularLinkedList(); split_circular_llist.head = curr_node
        while next_node is not self.head:
            curr_node = curr_node.next; next_node = next_node.next
        curr_node.next = split_circular_llist.head
        return [self,split_circular_llist]
    
    def remove_node(self, node : "Node"):
        curr_node = self.head; next_node = curr_node.next
        if curr_node == node:
            while next_node is not self.head: next_node = next_node.next
            next_node.next = curr_node.next
            self.head = next_node.next
        while next_node is not self.head:
            if next_node == node: 
                curr_node.next = next_node.next
                next_node = next_node.next
            curr_node = curr_node.next; next_node = next_node.next
    
    def josephus(self, step : int) -> Union[list,tuple,str]:
        curr_node = self.head; next_node = curr_node.next
        while len(self) > 1: 
            counter = 1
            while counter < step:
                prev_node = curr_node; curr_node = curr_node.next; next_node = next_node.next
                counter += 1
            prev_node.next = curr_node.next
            if curr_node is self.head: self.head = next_node
            self.remove_node(curr_node); curr_node = next_node; next_node = next_node.next
        return next_node.data
            
def append(ll : "CircularLinkedList", data : List[Union[list,tuple,str]]) -> "CircularLinkedList":
    for d in data: ll.append(d)
    print(ll.display_iterative())
    print(ll.display_recursive(ll.head,ll.head.next))
    return ll

def prepend(ll : "CircularLinkedList", data : List[Union[list,tuple,str]]) -> "CircularLinkedList":
    for d in data: ll.prepend(d)
    print(ll.display_iterative())
    print(ll.display_recursive(ll.head,ll.head.next))
    return ll

def remove(ll : "CircularLinkedList", data : List[Union[list,tuple,str]]) -> "CircularLinkedList":
    for d in data: ll.remove(d)
    print(ll.display_iterative())
    if ll.head: print(ll.display_recursive(ll.head,ll.head.next))
    return ll

def split_list(ll : "CircularLinkedList") -> "CircularLinkedList":
    split_l, split_r = ll.split_list()
    print(f"Split at midpoint: {split_l.display_iterative(),split_r.display_iterative()}")
    print(f"Split at midpoint: {split_l.display_recursive(split_l.head,split_l.head.next),split_r.display_recursive(split_r.head,split_r.head.next)}")
    return split_l

def josephus(ll : "CircularLinkedList", step : int = 2) -> "CircularLinkedList":
    print(f"Josephus value with step [{step}]: [{ll.josephus(step)}]")
    return ll

def main():
    circular_llist = CircularLinkedList()
    circular_llist = append(circular_llist, ['A', 'BC', 'D', 'EFG'])
    circular_llist = prepend(circular_llist, ['3', '12', '0', 'BC', 'A'])
    circular_llist = remove(circular_llist, ['A', 'E'])
    circular_llist = split_list(circular_llist)
    circular_llist = remove(circular_llist, ['BC', '12', '0'])
    circular_llist = append(circular_llist, ['1', '2', '3', '4'])
    circular_llist = josephus(circular_llist)
    
if __name__ == "__main__":
    main()