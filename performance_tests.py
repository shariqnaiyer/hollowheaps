import random
import heapq
import timeit
from hollowheap import HollowHeap, Item
import random

def hollow_heap_basic_operations():
    test_heap = HollowHeap()
    test_heap.insert(4)
    test_heap.insert(8)
    test_heap.insert(3, Item("A"))
    test_heap.insert(2, Item("B"))
    test_heap.find_min()

def hollow_heap_insert_operations():
    test_heap = HollowHeap()
    itemA = Item("A")
    itemB = Item("B")
    itemC = Item("C")
    itemD = Item("D")
    test_heap.insert(1, itemA)
    test_heap.insert(2, itemB)
    test_heap.insert(3, itemC)
    test_heap.insert(4, itemD)

def hollow_heap_heavy_insert_operations():
    test_heap = HollowHeap()
    items = [Item(str(random.random())) for _ in range(10000)]
    for item in items:
        test_heap.insert(random.randint(1, 100000), item)

def hollow_heap_delete_operations():
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

def hollow_heap_delete_min_operations():
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

def hollow_heap_decrease_key_operations():
    test_heap = HollowHeap()
    itemA = Item("A")
    itemB = Item("B")
    itemC = Item("C")
    itemD = Item("D")
    test_heap.insert(4, itemA)
    test_heap.insert(8, itemB)
    test_heap.insert(3, itemC)
    test_heap.insert(2, itemD)
    test_heap.find_min()
    test_heap.decrease_key(test_heap.find_min(), 1)

def heavy_hollow_heap_delete_operations():
    test_heap = HollowHeap()
    items = [Item(str(random.random())) for _ in range(10000)]
    for item in items:
        test_heap.insert(random.randint(1, 100000), item)
    for item in items:
        test_heap.delete(item)

def heavy_hollow_heap_delete_min_operations():
    test_heap = HollowHeap()
    items = [Item(str(random.random())) for _ in range(10000)]
    for item in items:
        test_heap.insert(random.randint(1, 100000), item)
    for _ in range(10000):
        test_heap.delete_min()

def heavy_hollow_heap_decrease_key_operations():
    test_heap = HollowHeap()
    items = [Item(str(random.random())) for _ in range(10000)]
    for item in items:
        test_heap.insert(random.randint(1, 100000), item)
    for _ in range(5000): 
        test_heap.decrease_key(random.choice(items), random.randint(1, 100000))

def heapq_basic_operations():
    heap = []
    heapq.heappush(heap, 4)
    heapq.heappush(heap, 8)
    heapq.heappush(heap, 3)
    heapq.heappush(heap, 2)
    heapq.heappop(heap)

def heapq_insert_operations():
    heap = []
    heapq.heappush(heap, 1)
    heapq.heappush(heap, 2)
    heapq.heappush(heap, 3)
    heapq.heappush(heap, 4)

def heavy_heapq_insert_operations():
    heap = []
    for _ in range(10000):
        heapq.heappush(heap, random.randint(1, 100000))

def heapq_delete_operations():
    heap = []
    heapq.heappush(heap, (1, "A"))
    heapq.heappush(heap, (2, "B"))
    heapq.heappush(heap, (3, "C"))
    heapq.heappush(heap, (4, "D"))
    heap.remove((1, "A"))

def heapq_delete_min_operations():
    heap = []
    heapq.heappush(heap, (2, "A"))
    heapq.heappush(heap, (4, "B"))
    heapq.heappush(heap, (5, "C"))
    heapq.heappush(heap, (8, "D"))
    heapq.heappop(heap)

def heavy_heapq_delete_operations():
    heap = []
    items = [(random.randint(1, 100000), str(random.random())) for _ in range(10000)]
    for item in items:
        heapq.heappush(heap, item)
    for item in items:
        heap.remove(item)

def heavy_heapq_delete_min_operations():
    heap = []
    items = [(random.randint(1, 100000), str(random.random())) for _ in range(10000)]
    for item in items:
        heapq.heappush(heap, item)
    for _ in range(10000):
        heapq.heappop(heap)

heapq_basic_time = timeit.timeit(heapq_basic_operations, number=10)
heapq_delete_time = timeit.timeit(heapq_delete_operations, number=10)
heapq_delete_min_time = timeit.timeit(heapq_delete_min_operations, number=10)
heavy_heapq_delete_time = timeit.timeit(heavy_heapq_delete_operations, number=1)
heavy_heapq_delete_min_time = timeit.timeit(heavy_heapq_delete_min_operations, number=1)
hollow_heap_basic_time = timeit.timeit(hollow_heap_basic_operations, number=10)
hollow_heap_delete_time = timeit.timeit(hollow_heap_delete_operations, number=10)
hollow_heap_delete_min_time = timeit.timeit(hollow_heap_delete_min_operations, number=10)
hollow_heap_decrease_key_time = timeit.timeit(hollow_heap_decrease_key_operations, number=10)
heavy_hollow_heap_delete_time = timeit.timeit(heavy_hollow_heap_delete_operations, number=1)
heavy_hollow_heap_delete_min_time = timeit.timeit(heavy_hollow_heap_delete_min_operations, number=1)
heavy_hollow_heap_decrease_key_time = timeit.timeit(heavy_hollow_heap_decrease_key_operations, number=1)

print("Non-heavy HollowHeap operations time:")
print("Basic operations time: ", hollow_heap_basic_time)
print("Delete operations time: ", hollow_heap_delete_time)
print("Delete min operations time: ", hollow_heap_delete_min_time)
print("Decrease key operations time: ", hollow_heap_decrease_key_time)
print("----------------------------------------")
print("Non-heavy heapq operations time:")
print("Basic operations time: ", heapq_basic_time)
print("Delete operations time: ", heapq_delete_time)
print("Delete min operations time: ", heapq_delete_min_time)
print("----------------------------------------")
print("Heavy HollowHeap operations time:")
print("Delete operations time: ", heavy_hollow_heap_delete_time)
print("Delete min operations time: ", heavy_hollow_heap_delete_min_time)
print("Decrease key operations time: ", heavy_hollow_heap_decrease_key_time)
print("----------------------------------------")
print("Heavy heapq operations time:")
print("Delete operations time: ", heavy_heapq_delete_time)
print("Delete min operations time: ", heavy_heapq_delete_min_time)
print("----------------------------------------")
