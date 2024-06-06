# source of all pseudocode: https://arxiv.org/pdf/1510.06535.pdf
class HollowHeap:
    def __init__(self):
        """make-heap(): makes an empty heap"""
        self.root = None
        self.store = {}
        self.rank = None

    def insert(self, key, value = None):
        """insert(e,k,h): returns the heap fomed by inserting item e with value k in heap h."""
        if value == None:
            value = Item(None)
        self.root = self.meld(self.root, Node(key, value))
        return self.root

    def find_min(self):
        """find-min(h): finds the item with minimum value given a heap h."""
        if self.root == None:
            return None
        return self.root.item 

    def delete_min(self):
        """delete-min(h): returns heap formed by deleting the item with minimum value in heap h."""
        if self.find_min() != None:
            self.delete(self.find_min())
        return self.root

    def meld(self, h1, h2):
        """meld(h1, h2): returns the heap containing all items in disjoint heaps h1 and h2."""
        if h1 == None:
            return h2
        if h2 == None:
            return h1
        return self.link(h1, h2)

    def decrease_key(self, iteme, new_key):
        """decrease-key(e,k,h): decreases the value of the item e to value k in heap h."""
        u = iteme.node
        if u.key < new_key:
            return 
        
        if u.item == None:
            return

        if u == self.root:
            u.key = new_key
            return self.root
        v = Node(new_key, u.item)
        u.item = None
        if u.rank > 2:
            v.rank = u.rank - 2
        v.child = u
        u.ep = v
        return self.link(self.root, v)

    def delete(self, iteme):
        """	delete(e,h): returns the heap formed by deleting node with item e in heap h."""
        iteme.node.item = None
        iteme.node = None
        self.store = {}
        self.rank = 0

        if self.root != None and self.root.item != None:
            return 

        while self.root != None:
            a = self.root.child
            b = self.root
            self.root = self.root.next
            while a != None:
                p = a
                a = a.next
                if p.item == None:
                    if p.ep == None:
                        p.next = self.root
                        self.root = p
                    else:
                        if p.ep == b:
                            a = None
                        else:
                            p.next = None
                        p.ep = None
                else:
                    self.ranked(p)
        self.unranked()
        if self.root != None:
            self.root.next = None

    def ranked(self, node):
        """ranked(node): does the ranked links for node."""
        while node.rank in self.store and self.store[node.rank] != None:
            node = self.link(node, self.store[node.rank])
            self.store[node.rank] = None
            node.rank += 1
        self.store[node.rank] = node
        if node.rank > self.rank:
            self.rank = node.rank

    def unranked(self):
        """unranked(): does the unranked links as per the pseudocode from the paper"""
        for i in range(self.rank + 1):
            if i in self.store and self.store[i] != None:
                if self.root == None:
                    self.root = self.store[i]
                else:
                    self.root = self.link(self.root, self.store[i])
                self.store[i] = None
    
    def add_child(self, node, child):
        """add_child(node, child): adds child to node's child list."""
        node.next = child.child
        child.child = node

    def link(self, n1, n2):
        """link(n1, n2): returns the root of the heap formed by linking n1 and n2."""
        if n1.key > n2.key:
            self.add_child(n1, n1)
            return n2  
        else:
            self.add_child(n2, n1)
            return n1
class Node:
    def __init__(self, key, value):
        """"make-node(e,k): makes a node with item e and value k."""
        self.key = key
        self.item = value
        value.node = self
        self.child = None
        self.next = None
        self.ep = None
        self.rank = 0

class Item:
    """Item in the heap"""
    def __init__(self, value):
        self.node = None
        self.value = value
