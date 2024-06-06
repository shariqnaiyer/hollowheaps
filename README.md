# Hollow Heaps 💡

## Description

A heap is a tree-based data structure that follows the heap property, i.e., the value of each node is either greater than or equal to the value stored in the node’s children (max-heap) or the value of each node is less than or equal to the value stored in the nodes' children (min-heap). These structures are commonly used to implement priority queues. Hollow heaps combine the use of lazy deletion and re-insertion for decrease-key operations and Directed Acyclic Graphs (DAGs) instead of trees to represent the heap. The use of lazy deletion leads to there being nodes that hold no value called hollow nodes. Hollow heaps support most heap operations such as insert and decrease-key operations with O(1) time worst-case complexity compared to the O(logn) time worst-case complexity of binary heaps. On all other heap operations such as delete and delete-min, they are on par with Fibonacci heaps that are faster than binary heaps.

### Operations:

- `make-heap()`: makes an empty heap
- `find-min(h)`: finds the item with minimum value given a heap h.
- `insert(e,k,h)`: returns the heap formed by inserting item e with value k in heap h.
- `delete-min(h)`: returns heap formed by deleting the item with minimum value in heap h.
- `meld(h1, h2)`: returns the heap containing all items in disjoint heaps h1 and h2.
- `decrease-key(e,k,h)`: decreases the value of the item e to value k in heap h.
- `delete(e,h)`: returns the heap formed by deleting item e in heap h.

## Resources

Research Paper on Hollow heaps by Thomas Dueholm Hansen, Haim Kaplan, Robert E. Tarjan, Uri Zwick: [Hollow Heaps Paper](https://arxiv.org/pdf/1510.06535.pdf)
The pseudocode provided in the paper served as a great reference for the implementation of the hollow heap.
Pyrival's implementation of Djikstra's algorithm using hollow heaps: [Pyrival's Djikstra Implementation](https://github.com/cheran-senthil/PyRival/blob/master/pyrival/graphs/dijkstra.py)

## Time Bounds

- `find-min(h)`: O(1) time worst case as it just returns the min attribute
- `insert(e,k,h)`: O(1) time worst case, uses meld which is O(1)
- `delete-min(h)`: O(log n), getting min is O(1) and then deleting is O(logn)
- `meld(h1, h2)`: O(1) time worst case
- `decrease-key(e,k,h)`: O(1) time worst case
- `delete(e,h)`: O(log n) time worst case

## Instructions

The code is modelled as a python package. To run use the hollow heap, run the following command:

```
from hollow_heap import HollowHeap, Node, Item
```

Available methods are:

- `make_heap()`: makes an empty heap
Example usage:
```
h = HollowHeap()
```

- `find_min()`: finds the item with minimum value given a heap h.

Example usage:
```
h.find_min()
```

- `insert(key, value)`: returns the heap formed by inserting item e with value k in heap h.

Example usage:
```
h.insert(1, Item(1))
```

- `delete_min()`: returns heap formed by deleting the item with minimum value in heap h.

Example usage:
```
h.delete_min()
```

- `meld(h1, h2)`: returns the heap containing all items in disjoint heaps h1 and h2.

Example usage:
```
h1 = HollowHeap()
h2 = HollowHeap()
h1.insert(1, Item(1))
h2.insert(2, Item(2))
h3 = h1.meld(h2)
```

- `decrease_key(iteme, new_key)`: decreases the value of the item e to value k in heap h.

Example usage:
```
h = HollowHeap()
item = h.insert(1, Item(1))
h.decrease_key(item, 0)
```

- `delete(iteme)`: returns the heap formed by deleting item e in heap h.

Example usage:
```
h = HollowHeap()
item = Item(1)
h.insert(1, item)
h.delete(item)
```

In the main directory, run the following command to run the operation tests:

```
python3 operation_tests.py
```

These tests test the basic functionality of insert, find-min, delete, delete-min, decrease-key on the hollow heap for correctness. I have used assert functions so the tests will fail if the output is not as expected. The tests also give output to show the results of the operations. 

Up next, run the following command to run the performance tests:

```
python3 performance_tests.py
```

These tests test the performance of the Hollow Heaps against python's Heapq implementation. The tests are run on the following operations: insert, find-min, delete, delete-min, decrease-key. The tests are run on smaller input and then on more complex larger inputs. These tests are then timed using python's time it module. The results are outputted to the terminal. We use the random module of python to generate the test input. This leads to the program taking about a minute to run. My performance tests were focused on the delete-min and delete operations as well as the 
A sample output of the performance tests yields the following results:
```
Non-heavy HollowHeap operations time:
Basic operations time:  4.609999814420007e-05
Delete operations time:  7.560000085504726e-05
Delete min operations time:  7.129999721655622e-05
Decrease key operations time:  0.00012599999899975955
----------------------------------------
Non-heavy heapq operations time:
Basic operations time:  5.000001692678779e-06
Delete operations time:  4.999998054699972e-06
Delete min operations time:  4.699999408330768e-06
----------------------------------------
Heavy HollowHeap operations time:
Delete operations time:  0.027734199997212272
Delete min operations time:  0.021488900001713773
Decrease key operations time:  0.02788409999993746
----------------------------------------
Heavy heapq operations time:
Delete operations time:  0.35263790000317385
Delete min operations time:  0.016366099996957928
----------------------------------------
```
As we can see from the results, hollow heap outperforms heapq on the delete-min and delete operations. However, heapq is efficiently optimized so it is on par with hollow heaps on the delete operations. 

For further testing, as recommended by Zac, I have implemented a test with Djikstra on a very dense graph with 10000 nodes and all possible edges. The initial code for Djikstra's Algorithm was taken from Pyrival's implementation of Djikstra's algorithm using python's heapq. I have modified the code to use hollow heaps instead of heapq. 
To run the test, run the following command:
```
python3 dijkstra_test.py
```

The results are as follows:
```
Dijkstra's algorithm on a dense graph with 10000 nodes and all possible edges took 4.454363584518433 seconds.
Dijkstra's with hollow heaps on a dense graph with 10000 nodes and all possible edges took 1.6050024032592773 seconds.
```

## Assumptions
- Decrease key is only called on items that are already in the heap
- Delete is only called on items that are already in the heap

## Interpretation of the Results

The results are clearly printed to the console and can be tinkered around with in the files. The results comply with the faster O(1) time complexity of the insert and decrease key functions of hollow heaps compared to the O(logN) time complexity of binary heaps. The results also show that hollow heaps are faster than heapq on the delete operations.

## Included Files

- `hollow_heap.py`: Contains the implementation of the hollow heap
- `operation_tests.py`: Contains the tests for the correctness of basic operations of the hollow heap
- `performance_tests.py`: Contains the tests for the performance of the hollow heap
- `dijkstra_test.py`: Contains the implementation of Djikstra's algorithm using hollow heaps
- `report.md`: Contains the report for the project
