from typing import Union, List, Tuple

class Node:

    def __init__(self, data : Union[None, list, str, float] = None):
        self.next = None
        self.data = data

class LinkedList:

    def __init__(self):
        self.head = Node()
        self.tail = self.head

    def length(self) -> int:
        node_count = 0
        curr = self.head
        while curr.next:
            curr = curr.next
            if curr.data:
                node_count += 1
        return node_count
    
    def length_recursive(self, node_count : int = 0, curr : Union[None, "Node"] = None) -> int:
        if not curr:
            curr = self.head
        if curr.next:
            return self.length_recursive(node_count + 1, curr.next)
        return node_count

    def append_node(self, data : Union[list, str, float]):
        new_node = Node(data)
        self.tail.next = new_node
        self.tail = new_node

    def prepend_node(self,data : Union[list, str, float]):
        new_node = Node(data)
        old_node = self.head.next
        self.head.next = new_node
        new_node.next = old_node
        
    def insert_after_idx(self, index : int, data : Union[list, str, float]):
        new_node = Node(data)
        if index <= self.length():
            curr_idx = 0
            curr_node = self.head
            while curr_idx <= index:
                curr_node = curr_node.next
                curr_idx += 1
            next_node = curr_node.next
            curr_node.next = new_node
            new_node.next = next_node
        else:
            print("Index out of range")
            
    def insert_after_value(self, value : Union[list, str, float], data : Union[list, str, float]):
        new_node = Node(data)
        curr_node = self.head.next
        while curr_node.next:
            curr_node = curr_node.next
            if curr_node.data == value:
                next_node = curr_node.next
                curr_node.next = new_node
                new_node.next = next_node
                return
        print(f"Value [{value}] not found & node not inserted")

    def recursive_display(self, ret : Union[None, list] = None, curr : Union[None, "Node"] = None) -> str:
        if not curr and not ret:
            ret, curr = ([], self.head)
            ret = self.recursive_display(ret,curr)
            return ret
        if curr.next:
            ret = self.recursive_display(ret,curr.next)
        if curr.data:
            ret = [curr.data] + ret
        return ret

    def standard_display(self) -> List[Union[str, float]]:
        ret = []
        curr = self.head
        while curr.next:
            curr = curr.next
            if curr.data:
                ret.append(curr.data)
        return ret

    def get_value(self, index : int) -> Union[None, Union[list, str, float]]:
        if index <= self.length():
            curr_idx = 0
            curr_node = self.head
            while curr_idx <= index:
                curr_node = curr_node.next
                curr_idx += 1
            return curr_node.data
        print("Index out of range")
        return None
    
    def get_node(self, index : int) -> Union[None, "Node"]:
        if index <= self.length():
            curr_idx = 0
            curr_node = self.head
            while curr_idx <= index:
                curr_node = curr_node.next
                curr_idx += 1
            return curr_node
        print("Index out of range")
        return None
    
    def get_tail(self, index : int, ret : Union[None, List[Union[list,str,float]]] = None, curr : Union[None, "Node"] = None) -> Union[None, List[Union[list,str,float]]]:
        if index <= self.length():
            if not curr and not ret:
                curr = self.get_node(index)
                ret = []
                ret = self.get_tail(index,ret,curr)
                return ret
            if curr.next:
                ret = self.get_tail(index,ret,curr.next)
            if curr.data:
                ret = [curr.data] + ret
            return ret
        print("Index out of range")
        return None

    def delete_node(self, index : int) -> Union[None, str]:
        if index <= self.length():
            curr_idx = 0
            curr_node = self.head
            while curr_idx < index:
                curr_node = curr_node.next
                curr_idx += 1
            next_node = curr_node.next
            curr_node.next = next_node.next
            next_node = None
            return self.recursive_display()
        print("Index out of range")
        return None
    
    def swap_nodes(self, key1 : Union[list,str,float], key2 : Union[list,str,float]):
        if key1 == key2: return
        prev_node = prev_node1 = prev_node2 = None
        curr_node = self.head
        while curr_node.next:
            if curr_node.data == key1: prev_node1, swap_node1 = prev_node, curr_node
            if curr_node.data == key2: prev_node2, swap_node2 = prev_node, curr_node
            prev_node = curr_node
            curr_node = curr_node.next
        if not prev_node1 or not prev_node2: return
        prev_node1.next = swap_node2
        prev_node2.next = swap_node1
        swap_node1.next, swap_node2.next = swap_node2.next, swap_node1.next
        
    def reverse(self):
        if self.length() == 1: return
        curr_node = self.head
        prev_node = None
        self.head = Node()
        while curr_node:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node
        self.head.next = prev_node
        
    def reverse_recursive(self):
        
        def _reverse_recursive(node : "Node", prev_node : Union[None,"Node"]):
            if not node: 
                self.head = Node()
                self.head.next = prev_node
                return
            next_node = node.next
            node.next = prev_node
            return _reverse_recursive(next_node,node)
      
        _reverse_recursive(self.head, None)
        
    def merge_sorted(self, ll : "LinkedList") -> "LinkedList":
        self_head = self.head
        other_head = ll.head
        new_list = LinkedList()
        if not self_head.next.data: return ll
        if not other_head.next.data: return self
        curr_node_self = self_head.next
        curr_node_other = other_head.next
        if curr_node_self.data <= curr_node_other.data:
            new_list.append_node(curr_node_self.data)
            curr_node_self = curr_node_self.next
        else:
            new_list.append_node(curr_node_other.data)
            curr_node_other = curr_node_other.next
        while curr_node_self and curr_node_other:
            if curr_node_self.data <= curr_node_other.data: 
                new_list.append_node(curr_node_self.data)
                curr_node_self = curr_node_self.next
            else: 
                new_list.append_node(curr_node_other.data)
                curr_node_other = curr_node_other.next
        if not curr_node_self:
            while curr_node_other:
                new_list.append_node(curr_node_other.data)
                curr_node_other = curr_node_other.next
        else:
            while curr_node_other:
                new_list.append_node(curr_node_other.data)
                curr_node_other = curr_node_other.next    
        return new_list
    
    def remove_duplicates(self):
        seen = set()
        prev_node = self.head
        curr_node = prev_node.next
        while curr_node.next:
            if curr_node.data in seen: 
                curr_node = curr_node.next
                prev_node.next = curr_node
            else: 
                if curr_node.data: seen.add(curr_node.data)
                prev_node.next = curr_node
                curr_node = curr_node.next
                prev_node = prev_node.next
                
    def nth_from_end(self, n : int):
        trail_node = self.head
        lead_node = trail_node.next
        curr_gap_len = 1
        while curr_gap_len < n:
            if not lead_node.next: return None
            lead_node = lead_node.next
            curr_gap_len += 1
        while lead_node:
            lead_node = lead_node.next
            trail_node = trail_node.next
        return trail_node.data

    def count_occurrences(self, data : List[Union[list,str,float]]):
        seen = {}
        curr_node = self.head
        while curr_node.next:
            curr_node = curr_node.next
            seen[curr_node.data] = seen.get(curr_node.data,0) + 1
        return [seen.get(d,0) for d in data]
         
    def recursive_count(self, data : Union[list,str,float], node : "Node"):
        if not node: return 0
        if node.data == data:
            return 1 + self.recursive_count(data, node.next)
        return self.recursive_count(data, node.next)
    
    def rotate(self, index : int):
        if index > self.length(): return
        curr_node = self.head; curr_index = 0
        start_node = curr_node.next
        while curr_index <= index:
            prev_node = curr_node
            curr_node = curr_node.next
            curr_index += 1
        stop_node = prev_node
        stop_node.next = Node()
        self.tail = stop_node.next
        self.head.next = curr_node
        while curr_node:
            prev_node = curr_node
            curr_node = curr_node.next
        prev_node.next = start_node
        
    def tail_to_head(self):
        curr_node = self.head
        start_node = curr_node.next
        while curr_node.next and curr_node.next.data:
            prev_node = curr_node
            curr_node = curr_node.next
        self.head.next = curr_node
        curr_node.next = start_node
        prev_node.next = self.tail
        
    def sum(self, ll : "LinkedList") -> "LinkedList":
        curr_self = self.head.next
        curr_other = ll.head.next
        i = j = remainder = 0
        res = LinkedList()
        while curr_self or curr_other:
            if curr_self: i = curr_self.data; curr_self = curr_self.next
            if curr_other: j = curr_other.data; curr_other = curr_other.next
            this_sum = i + j + remainder
            remainder = this_sum // 10; this_sum = this_sum % 10
            res.append_node(this_sum)
            i = j = 0
        if remainder: res.append_node(remainder)
        return res
            
def fill_linked_list(ll : "LinkedList", data : List[Union[list,str,float]] = [5,8,12,4,2,7,4], randint : int = 4) -> "LinkedList":
    for d in data:
        ll.append_node(d)
    print(f"{ll.length()} elements found in this linked list")
    print(f"Linked list: {ll.recursive_display()}")
    print(f"Linked list: {ll.standard_display()}")
    print(f"Element at index [{randint}] has value [{ll.get_value(randint)}]")
    print(f"Linked list from element [{randint}]: {ll.get_tail(randint)}")
    print(f"Nth [{randint}] element from end of linked list: {ll.nth_from_end(randint)}")
    print(f"[{ll.count_occurrences([randint,randint+1])}] occurrences of value(s) [[{randint},{randint+1}]]")
    print(f"[{ll.recursive_count(randint,ll.head)}] occurrences of value [{randint}]")
    ll.remove_duplicates()
    print(f"Linked Lists without duplicates: {ll.recursive_display()}")
    ll.rotate(randint)
    print(f"Rotated Linked List about position [{randint}]: {ll.recursive_display()}")
    ll.tail_to_head()
    print(f"Linked List with head to tail: {ll.recursive_display()}")
    return ll

def delete_element(ll : "LinkedList", randint : int = 2) -> "LinkedList":
    ll.delete_node(randint)
    print(f"Deleted element {randint} from this linked list")
    print(f"{ll.length()} elements found in this linked list")
    print(f"{ll.length_recursive()} elements found recursively in this linked list")
    print(f"Linked list: {ll.recursive_display()}")
    print(f"Linked list: {ll.standard_display()}")
    print(f"Element at index [{randint}] has value [{ll.get_value(randint)}]")
    print(f"Linked list from element [{randint}]: {ll.get_tail(randint)}")
    return ll

def prepend_data(ll : "LinkedList", data : List[Union[list,str,float]] = ["a", "b", "c"], randint : int = 1) -> "LinkedList":
    for d in data:
        ll.prepend_node(d)
    print(f"{ll.length()} elements found in this linked list")
    print(f"Linked list: {ll.recursive_display()}")
    print(f"Linked list: {ll.standard_display()}")
    print(f"Element at index [{randint}] has value [{ll.get_value(randint)}]")
    print(f"Linked list from element [{randint}]: {ll.get_tail(randint)}")
    return ll

def insert_by_idx(ll : "LinkedList", data : List[Union[list,str,float]] = ["x", "y", "z"], indices : List[int] = [2, 4, 5], randint : int = 5) -> "LinkedList":
    for i,d in zip(indices,data):
        ll.insert_after_idx(i,d)
    print(f"{ll.length()} elements found in this linked list")
    print(f"Linked list: {ll.recursive_display()}")
    print(f"Linked list: {ll.standard_display()}")
    print(f"Element at index [{randint}] has value [{ll.get_value(randint)}]")
    print(f"Linked list from element [{randint}]: {ll.get_tail(randint)}")
    return ll
   
def insert_by_val(ll : "LinkedList", data : List[Union[list,str,float]] = [9, 14, 29], values : List[Union[list,str,float]] = ["a", "M", 7], randint : int = 8) -> "LinkedList":
    for v,d in zip(values,data):
        ll.insert_after_value(v,d)
    print(f"{ll.length()} elements found in this linked list")
    print(f"Linked list: {ll.recursive_display()}")
    print(f"Linked list: {ll.standard_display()}")
    print(f"Element at index [{randint}] has value [{ll.get_value(randint)}]")
    print(f"Linked list from element [{randint}]: {ll.get_tail(randint)}")
    return ll
    
def swap_nodes(ll : "LinkedList", data : List[Union[list,str,float]] = [9, 'z']) -> "LinkedList":
    ll.swap_nodes(*data)
    print(f"Swapped elements with values: {data}")
    print(f"Linked list: {ll.recursive_display()}")
    print(f"Linked list: {ll.standard_display()}")
    return ll

def reverse(ll : "LinkedList") -> "LinkedList":
    ll.reverse()
    print(f"Linked list: {ll.recursive_display()}")
    print(f"Linked list: {ll.standard_display()}")
    ll.reverse_recursive()
    print(f"Linked list: {ll.recursive_display()}")
    print(f"Linked list: {ll.standard_display()}")
    return ll
    
def main():
    ll = fill_linked_list(LinkedList())
    ll = delete_element(ll)
    ll = prepend_data(ll)
    ll = insert_by_idx(ll)
    ll = insert_by_val(ll)
    ll = swap_nodes(ll)
    ll = reverse(ll)

def operations(data : List[Tuple[int,int,int]] = [(1,9,2),(2,6,1)]):
    ll = LinkedList(); ll2 = LinkedList()
    for d in range(*data[0]):
        ll.append_node(d)
    for d in range(*data[1]):
        ll2.append_node(d)
    ll3 = ll.merge_sorted(ll2)
    print(f"Linked List 1: {ll.recursive_display()}")
    print(f"Linked List 1: {ll.standard_display()}")
    print(f"Linked List 2: {ll2.recursive_display()}")
    print(f"Linked List 2: {ll2.standard_display()}")
    print(f"Sorted/Merged Linked Lists: {ll3.recursive_display()}")
    print(f"Sum of Linked Lists: {ll.sum(ll2).recursive_display()}")

if __name__ == "__main__":
    main()
    operations()
