from heapq import heappop, heappush
from hollowheap import HollowHeap, Item

# Python implementation of Dijkstra's algorithm: https://github.com/cheran-senthil/PyRival/blob/master/pyrival/graphs/dijkstra.py
def dijkstra(graph, start):
    """ 
        Uses Dijkstra's algortihm to find the shortest path from node start
        to all other nodes in a directed weighted graph.
    """
    n = len(graph)
    dist, parents = [float("inf")] * n, [-1] * n
    dist[start] = 0

    queue = [(0, start)]
    while queue:
        path_len, v = heappop(queue)
        if path_len == dist[v]:
            for w, edge_len in graph[v]:
                if edge_len + path_len < dist[w]:
                    dist[w], parents[w] = edge_len + path_len, v
                    heappush(queue, (edge_len + path_len, w))

    return dist, parents

# Python implementation of Dijkstra's algorithm with hollow heaps modified from the above
def dijkstra_hollow(graph, start):
    """ 
    Uses Dijkstra's algorithm to find the shortest path from node start
    to all other nodes in a directed weighted graph.
    """
    n = len(graph)
    dist, parents = [float("inf")] * n, [-1] * n
    dist[start] = 0

    heap = HollowHeap()
    heap.insert(0, Item(start))

    while heap.root is not None:
        path_len, v = heap.find_min().node.key, heap.find_min().value
        heap.delete_min()
        for w, edge_len in graph[v]:
            if edge_len + path_len < dist[w]:
                dist[w], parents[w] = edge_len + path_len, v
                heap.insert(edge_len + path_len, Item(w))

    return dist, parents

# make a very dense graph with 10000 nodes and all possible edges
import random
n = 10000
graph = [[] for i in range(n)]
for i in range(n):
    for j in range(n):
        if i != j:
            graph[i].append((j, random.randint(1, 100)))

# run dijkstra's algorithm on the graph
import time
start = time.time()
dijkstra(graph, 0)
end = time.time()
print("Dijkstra's algorithm on a dense graph with 10000 nodes and all possible edges took", end - start, "seconds.")

# run dijkstra's algorithm on the graph
start = time.time()
dijkstra_hollow(graph, 0)
end = time.time()
print("Dijkstra's with hollow heaps on a dense graph with 10000 nodes and all possible edges took", end - start, "seconds.")
