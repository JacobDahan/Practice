from typing import List, Union

class Node:
    
    def __init__(self, data : Union[list,tuple,str]):
        self.data = data
        self.next = None
        self.prev = None
        
class DubLinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
        
    def prepend(self, data : Union[list,tuple,str]):
        if not self.head: self.head = Node(data); self.tail = self.head; return
        new_node = Node(data); new_node.next = self.head; self.head.prev = new_node
        self.head = new_node
        
    def append(self, data : Union[list,tuple,str]):
        if not self.head: self.head = Node(data); self.tail = self.head; return
        new_node = Node(data); new_node.prev = self.tail; self.tail.next = new_node
        self.tail = new_node
        
    def display_iterative(self):
        if not self.head: return
        res = []; curr_node = self.head;
        while curr_node:
            res.append(curr_node.data); curr_node = curr_node.next
        return res
    
    def display_recursive(self, curr_node : "Node") -> List[Union[list,tuple,str]]:
        if not self.head: return
        if not curr_node.next: return [curr_node.data]
        return [curr_node.data] + self.display_recursive(curr_node.next)
    
    def insert(self, node : "Node", key : Union[list,tuple,str]):
        curr_node = self.head; next_node = curr_node.next
        while next_node:
            if curr_node.data == key:
                node.prev = curr_node; curr_node.next = node; node.next = next_node; next_node.prev = node; return
            curr_node = curr_node.next; next_node = next_node.next
        if curr_node.data == key: node.prev = curr_node; curr_node.next = node; self.tail = node; return
        print("Key not found & node not inserted")
    
    def insert_before(self, node : "Node", key : Union[list,tuple,str]):
        curr_node = self.head; next_node = curr_node.next
        if curr_node.data == key: self.prepend(node.data); return
        while next_node:
            if curr_node.data == key:
                node.next = curr_node; node.prev = prev_node; prev_node.next = node; curr_node.prev = node; return
            prev_node = curr_node; curr_node = curr_node.next; next_node = next_node.next
        if curr_node.data == key: node.next = curr_node; node.prev = prev_node; prev_node.next = node; curr_node.prev = node; return
        print("Key not found & node not inserted")
        
    def remove(self, key : Union[list,tuple,str]):
        if not self.head: return
        curr_node = self.head; prev_node = self.head.prev; next_node = curr_node.next
        if curr_node.data == key: next_node.prev = None; self.head = next_node; curr_node = None; return
        while next_node:
            if curr_node.data == key: 
                prev_node.next = next_node; next_node.prev = prev_node; curr_node = None; return
            prev_node = curr_node; curr_node = next_node; next_node = next_node.next
        if curr_node.data == key: prev_node.next = None; self.tail = prev_node; curr_node = None; return
        
    def reverse(self):
        if not self.head or not self.head.next: return
        curr_node = self.head; next_node = curr_node.next
        while next_node:
            next_node = curr_node.next; curr_node.next, curr_node.prev = curr_node.prev, curr_node.next
            curr_node = next_node
        self.head, self.tail = self.tail, self.head
        
    def remove_duplicates(self):
        if not self.head or not self.head.next: return
        curr_node = self.head; prev_node = curr_node.prev; next_node = curr_node.next; seen = set()
        while next_node:
            if curr_node.data in seen: 
                prev_node.next = next_node; next_node.prev = prev_node;
                next_node = next_node.next; curr_node = next_node.prev; prev_node = curr_node.prev
            else: seen.add(curr_node.data)
            prev_node = curr_node; curr_node = next_node; next_node = next_node.next
        if curr_node.data in seen: prev_node.next = None; self.tail = prev_node
                              
def append(ll : "DubLinkedList", data : List[Union[list,tuple,str]]) -> "DubLinkedList":
    for d in data: ll.append(d)
    print(ll.display_iterative())
    print(ll.display_recursive(ll.head))
    return ll

def prepend(ll : "DubLinkedList", data : List[Union[list,tuple,str]]) -> "DubLinkedList":
    for d in data: ll.prepend(d)
    print(ll.display_iterative())
    print(ll.display_recursive(ll.head))
    return ll    

def insert(ll : "DubLinkedList", data : List[Union[list,tuple,str]], keys : List[Union[list,tuple,str]]) -> "DubLinkedList":
    for d,k in zip(data,keys): ll.insert(Node(d),k)
    print(ll.display_iterative())
    print(ll.display_recursive(ll.head))
    for d,k in zip(data,keys): ll.insert_before(Node(d),k)
    print(ll.display_iterative())
    print(ll.display_recursive(ll.head))
    return ll

def delete(ll : "DubLinkedList", keys : List[Union[list,tuple,str]]) -> "DubLinkedList":
    for k in keys: ll.remove(k)
    print(ll.display_iterative())
    print(ll.display_recursive(ll.head))
    return ll   

def reverse(ll : "DubLinkedList") -> "DubLinkedList":
    ll.reverse()
    print(ll.display_iterative())
    print(ll.display_recursive(ll.head))
    return ll

def remove_dups(ll : "DubLinkedList") -> "DubLinkedList":
    ll.remove_duplicates()
    print(ll.display_iterative())
    print(ll.display_recursive(ll.head))
    return ll

def main():
    dub_llist = DubLinkedList()
    dub_llist = append(dub_llist, ['8', '9', '10', '11'])
    dub_llist = prepend(dub_llist, ['7', '6', '5', '4', '3'])
    dub_llist = insert(dub_llist, ['3.5', '9.5', '11.5'], ['3', '9', '11'])
    dub_llist = delete(dub_llist, ['5','8'])
    dub_llist = reverse(dub_llist)
    dub_llist = remove_dups(dub_llist)
    
if __name__ == "__main__":
    main()
        
        