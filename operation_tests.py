from hollowheap import HollowHeap, Item, Node

# Create a HollowHeap instance
test_heap = HollowHeap()

# check root is None
# initial test
print("Test 1: check root is None on Initialization")
print("root is None: ", test_heap.root == None)
assert test_heap.root == None
print("Test 1 Passed")
print("----------------------------------------")

# insert a key
print("Test 2: insert a key, we will insert 4, and check that root is not None and root.key is 4")
test_heap.insert(4)
print("root is not None: ", test_heap.root != None)
print("root.key is 4: ", test_heap.root.key == 4)
assert test_heap.root.key == 4
print("Test 2 Passed")
print("----------------------------------------")

# insert another key larger
print("Test 3: insert a key larger than root, we will insert 8, and check that root.key is 4")
test_heap.insert(8)
print("root.key is 1: ", test_heap.root.key == 4)
assert test_heap.root.key == 4
print("Test 3 Passed")
print("----------------------------------------")

# insert a key with value 
print("Test 4: insert a key with value, we will insert 3 with value A, and check that root.item.value is A")
test_heap.insert(3, Item("A"))
print("root.item.value is A: ", test_heap.root.item.value)
assert test_heap.root.item.value == "A"
print("Test 4 Passed")
print("----------------------------------------")

# insert a smaller key with value
print("Test 5: insert a key with value, we will insert 2 with value B, and check that root.item.value is B")
test_heap.insert(2, Item("B"))
print("root.item.value is B: ", test_heap.root.item.value)
assert test_heap.root.item.value == "B"
print("Test 5 Passed")
print("----------------------------------------")

# find min
# currently min is 2 with value B
print("Test 6: find min, we will call findmin and check that the min is 2 with value B")
print("find_min is 2: ", test_heap.find_min().node.key == 2)
assert test_heap.find_min().node.key == 2
print("Test 6 Passed")
print("----------------------------------------")

print("Test 7: decrease_key, we will decrease the key of the root to 1 and check that the min is 1")
test_heap.decrease_key(test_heap.root.item, 1)
print("find_min is 1: ", test_heap.find_min().node.key == 1)
assert test_heap.find_min().node.key == 1
print("Test 7 Passed")
print("----------------------------------------")

print("Test 8: decrease_key, we will create a new heap with 9 and 7 decrease_key on the node with key 7 and decrease it to 4")
# Given that e is an item in heap h with key greater than k, return a heap formed from h by changing the key of e to k.
test_heap = HollowHeap()
test_heap.insert(9, Item("A"))
test_heap.insert(7, Item("B"))
# decrease key of 2 to 1
test_heap.decrease_key(test_heap.find_min(), 4)
print("find_min is 4: ", test_heap.find_min().node.key == 4)
assert test_heap.find_min().node.key == 4
print("Test 8 Passed")

print("----------------------------------------")
print("Test 9: decrease_key, we will call decrease_key on the root with key 4 and increase it to 11")
print("This should not change as the key is larger than the current key")
test_heap.decrease_key(test_heap.find_min(), 11)
print("find_min is 4: ", test_heap.find_min().node.key == 4)
assert test_heap.find_min().node.key == 4
print("Test 9 Passed")
print("----------------------------------------")


print("Test 10: delete, we will create heaps with 1, 2, 3 and 4 with values A, B, C, and D respectively")
print("We will delete item A and check that the min is 2")
test_heap = HollowHeap()
itemA = Item("A")
itemB = Item("B")
itemC = Item("C")
itemD = Item("D")
test_heap.insert(1, itemA)
test_heap.insert(2, itemB)
test_heap.insert(3, itemC)
test_heap.insert(4, itemD)
test_heap.delete(itemA)
print("find_min is 2: ", test_heap.find_min().node.key == 2)
assert test_heap.find_min().node.key == 2
print("Test 10 Passed")
print("----------------------------------------")

print("Test 11: delete min, we will create heaps with 2, 4, 5 and 8 with values A, B, C, and D respectively")
print("We will delete min and check that the min is 4")
test_heap = HollowHeap()
itemA = Item("A")
itemB = Item("B")
itemC = Item("C")
itemD = Item("D")
test_heap.insert(2, itemA)
test_heap.insert(4, itemB)
test_heap.insert(5, itemC)
test_heap.insert(8, itemD)
test_heap.delete_min()
print("find_min is 4: ", test_heap.find_min().node.key == 4)
assert test_heap.find_min().node.key == 4
print("Test 11 Passed")
print("----------------------------------------")

print("Test 12: meld, we will create 2 heaps")
print("We will meld them and check that the min is 1")
test_heap = HollowHeap()
test_heap2 = HollowHeap()
test_heap.insert(2, itemA)
test_heap.insert(4, itemB)
test_heap.insert(5, itemC)
test_heap.insert(8, itemD)
test_heap2.insert(1, itemA)
m = test_heap.meld(test_heap.root, test_heap2.root)
print("find_min is 1: ", test_heap.find_min().node.key == 1)
assert test_heap.find_min().node.key == 1
print("Test 12 Passed")
print("----------------------------------------")
