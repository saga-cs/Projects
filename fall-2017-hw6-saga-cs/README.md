# MPCS 51042-2, Python Programming

**Week 7 Assignment**

**Due**: November 12 at 11:59pm CT

For each problem, you are to submit a file named `problem<N>.py` where `<N>` is the number of the problem (e.g. `problem1.py`).

## Problem 1: Breadth-first search of an undirected graph

For this problem, you are asked to write a `Graph` class that stores the nodes and edges of an undirected graph. A [graph data structure](https://en.wikipedia.org/wiki/Graph_(abstract_data_type)) consists of a set of *nodes* together with a set of *edges*, which are unordered pairs of nodes indicating that two nodes are connected to one another. For example, the image below shows a graphical representation of a graph with 6 nodes and 7 edges.

<div align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/5/5b/6n-graf.svg" alt="undirected graph" width="200"/>
</div>

In addition to storing the nodes and edges of a graph, your `Graph` class will have methods for performing a [breadth-first search](https://en.wikipedia.org/wiki/Breadth-first_search) of the graph starting at a given node and determining the shortest distance between two nodes (the minimum number of edges that must be traversed to get from one node to another).

### Specifications: `Graph` class

- The `Graph` class stores the nodes and edges in an undirected graph. You are free to use whatever underlying data structure you wish to store the nodes and edges; you may use an [adjacency list](https://en.wikipedia.org/wiki/Adjacency_list), an [adjacency matrix](https://en.wikipedia.org/wiki/Adjacency_matrix), or any other data structure you see fit. 
- The `__init__` method should accept one optional argument called `edges` that is an iterable of 2-tuples containing the two nodes that are connected. For example, the graph pictured above could be created as:
    ```python
    edges = [
        (1, 2), (1, 5), (2, 3), (2, 5),
        (3, 4), (4, 5), (4, 6)
    ]
    g = Graph(edges)

    # ...or...
    g = Graph()
    for u, v in edges:
        g.add_edge(u, v)
    ```
- The `add_node` method accepts a single argument representing a node and adds it to the graph if it is not already present.
- The `add_edge` method accepts two arguments representing two nodes that are connected via an edge. The edge is added to the graph if it is not already present. Note that since this is an undirected graph, having an edge `(u, v)` in the graph implies that there is also an edge `(v, u)`.
- Nodes can be assumed to be immutable types suitable for use as a dictionary key (ints, floats, strings, tuples) or as items in a set.
- Iterating over a `Graph` should produce each node in the graph.
- Indexing the `Graph` with a node as a key should return a container that contains all the adjacent nodes (each adjacent node must appear only once in the container). For example:
    ```pycon
    >>> g[5]
    [1, 2, 4]
    ```
- The `in` operator should determine whether a node is present in the graph:
    ```pycon
    >>> 4 in g
    True
    >>> 20 in g
    False
    ```
- The `bfs` method takes one argument, a starting node, and returns an iterable of 2-tuples of the form (node, distance) produced by performing a breadth-first search starting at the specified node. You may implement the breadth-first search using a recursive or non-resursive algorithm. For one example of a non-recursive algorithm, see [here](https://www.hackerearth.com/practice/algorithms/graphs/breadth-first-search/tutorial/) (note that [collections.deque](https://docs.python.org/3/library/collections.html#collections.deque) is suitable as a queue). For example, for the graph above:
    ```pycon
    >>> for node, distance in g.bfs(1):
    ...     print(f'{node}, d={distance}')
    1, d=0
    2, d=1
    5, d=1
    3, d=2
    4, d=2
    6, d=3
    ```
- The `distance` method takes two arguments that are nodes and returns the length of the shortest path between them. Note that when a node is reached in a breadth-first search, it has done so via a shortest path. Example:
    ```
    >>> g.distance(2, 4)
    2
    ```
- You must write docstrings for the `Graph` class itself as well as the public methods (`add_node`, `add_edge`, `bfs`, and `distance`) that describe their purpose, their arguments, and in the case of `bfs` and `distance` how they are implemented.

### Specifications: Unit tests

In addition to writing the `Graph` class, you must also create a set of unit tests to ensure that your implementation is working as you intend. In fact, if you want to embrace "test-driven development", you can even write your tests before you implement the class itself.

- All test cases should be implemented by subclassing [unittest.TestCase](https://docs.python.org/3/library/unittest.html#unittest.TestCase).
- The following set of tests are required to receive full credit.
  - A test to ensure that nodes can be added via `add_node`.
  - A test to ensure that edges can be added via `add_edge`.
  - A test that checks whether the `in` operator works properly.
  - A test that checks that the `Graph` can be indexed using a node as the key.
  - A test that checks whether the `bfs` method produces an iterable with unique items (that is, a node should not appear twice).
  - A test that checks whether the `distance` method correctly returns the length of the shortest path between two nodes.
