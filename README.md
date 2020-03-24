# Small project in Flask for testing 3 search algorithms used in A.I
![result](myimage.gif)
### BFS - Breadth First Seach:
Data Structures and Introduction to Algorithms - "is one of the simplest algorithms for searching a graph and
the archetype for many important graph algorithms. Prim’s minimum-spanning-
tree algorithm and Dijkstra’s single-source shortest-paths algorithm use ideas similar to those in breadth-first search."

It computes the distance (smallest number of edges) from s
to each reachable vertex. It also produces a “breadth-first tree” with root s that
contains all reachable vertices. For any vertex v reachable from s, the simple path
in the breadth-first tree from s to v corresponds to a “shortest path” from s to 
in G, that is, a path containing the smallest number of edges.

The frontier is the list of nodes we know about, but have not visited.
We use the frontier to track of which nodes will be explored next — the ordering of the frontier controls which search algorithm we’re performing. 

--- <b> More explanations about the term frontier </b>---

To keep track of progress, breadth-first search colors each vertex white, gray, or
black. All vertices start out white and may later become gray and then black. A
vertex is discovered the first time it is encountered during the search, at which time
it becomes nonwhite.
Gray and black vertices, therefore, have been discovered, but
breadth-first search distinguishes between them to ensure that the search proceeds
in a breadth-first manner. If (u; v) -> E and vertex u is black, then vertex v
is either gray or black; that is, all vertices adjacent to black vertices have been
discovered. Gray vertices may have some adjacent white vertices; they represent
the frontier between discovered and undiscovered vertices.

Breadth-first search constructs a breadth-first tree, initially containing only its
root, which is the source vertex s.


Since a vertex is discovered at most once, it
has at most one parent. Ancestor and descendant relationships in the breadth-first
tree are defined relative to the root s

Unlike trees, graphs may contain cycles, so we may come to the same node again. 
To avoid processing a node more than once, we use a set (variable:"explored") to store the already seen nodes.



### A* :
A* is an informed search algorithm, or a best-first search, meaning that it is formulated in terms of weighted graphs: starting from a specific starting node of a graph, it aims to find a path to the given goal node having the smallest cost (least distance travelled, shortest time, etc.). It does this by maintaining a tree of paths originating at the start node and extending those paths one edge at a time until its termination criterion is satisfied.

At each iteration of its main loop, A* needs to determine which of its paths to extend. It does so based on the cost of the path and an estimate of the cost required to extend the path all the way to the goal. Specifically, A* selects the path that minimizes 

heuristic_function : h=∣xstart​−xdestination​∣+∣ystart​−ydestination​∣

fringe search is a graph search algorithm that finds the least-cost path from a given initial node to one goal node.

In essence, fringe search is a middle ground between A* and the iterative deepening A* variant (IDA*). 