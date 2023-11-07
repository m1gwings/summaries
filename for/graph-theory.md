---
title: Graph theory
author: Cristiano Migali
---

## Basic definitions

### Definition of Graph

- An **undirected graph** $G$ is a pair $(N, E)$ where $N$ is a set of **nodes** and $E$ is a set of **edges**, that is, unorder pairs $\{i, j\}$ with $i, j \in N$.

- A **directed graph** $G$ is a pair $(N, A)$ where $N$ is a set of **nodes** and $A \subset N \times N$ is a set of **arcs**.

### Adjacent nodes, incident edges and the degree of a node

- Two nodes are said **adjacent** if they are connected by an edge.

- An edge $e$ is **incident** in a node $n$ if $n$ is an endpoint of $e$.

- For **undirected** graphs we define the **degree** of a node $n$ as the number of edges which are incident to that node. For **directed** graphs we distinguish between the **in-degree**: the number of arcs $(i, n) \in A$ and the **out-degree**: the number of arcs $(n, j) \in A$.

### Paths

- For an **undirected** graph, a **path** of length $k$ from node $n_1$ to node $n_k$ is a sequence of nodes $n_1, n_2, ..., n_{k-1}, n_k$ s. t. $\{n_i, n_{i + 1}\} \in E$ $\forall i \in \{1, ..., k - 1\}$.

- For **directed** graphs, a **directed path** of length $k$ from node $n_1$ to node $n_k$ is a sequence of nodes $n_1, ..., n_k$ s. t. the arc $(n_i, n_{i + 1})$ belongs to $A$ $\forall i \in \{1, ..., k - 1\}$.

- A **path** is **simple** if it doesn't contain the same node twice.

### Connection

- Two nodes $u$ and $v$ are **connected** if there is a path in $G$ which starts at $u$ and ends at $v$.

- An **undirected graph** is **connected** if every two nodes of the grah are connected.

- A **directed graph** is **strongly connected** if $u$ and $v$ are connected by a direct path $\forall u, v \in N$.

### Cycles and circuits

- A **cycle** is a path (in an **undirected graph**) where $n_1 = n_k$.

- A **circuit** is a **directed** path where $n_1 = n_k$.

### Bipartite and complete graphs

- An **undirected** graph is **bipartite** if there exists a partition $N_1 \cup N_2 = N, N_1 \cap N_2 = \emptyset$ s. t. there is no edge in $E$ that connects two nodes of the same partition.

- An **undirected** graph is **complete** if $E = \{ \{n_i, n_j\} \mid n_i, n_j \in N, i < j \}$.

### Cuts

- For a **directed** graph, given $S \subset N$, we define the **outgoing cut induced by $S$** as $\delta^+(S) = \{ (n_i, n_j) \in A \mid n_i \in S, n_j \not \in S \}$ and the **incoming cut induced by $S$** as $\delta^-(S) = \{ (n_i, n_j) \in A \mid n_i \not \in S, n_j \in S \}$.

- For an **undirected** graph, given $S \subset N$, we define the **cut induced by $S$** as $\delta(S) = \{ \{i, j\} \in E \mid (i \in S \wedge j \not \in S) \vee (i \not \in S \wedge j \in S) \}$.

**Note**: cuts are subsets of the set of arcs (or edges).

### Subgraphs and trees

- Given a graph $G = (N, E)$, a **subgraph** of $G$ is a graph $G' = (N', E')$ s. t. $N' \subset N$ and $E' \subset E$.

- A **tree** $T = (N', E')$ is a connected and acyclic subgraph of $G$.

- A **spanning tree** is a tree with $N' = N$.

- The **leaves** of a tree are the nodes with degree 1.

### DAGs

- A **directed** graph is **acyclic** (we say that it is a **DAG**) if it contains no circuits.

## Basic properties

### Maximum number of edges and arcs

A **directed graph** has $m < n(n - 1)$ arcs ($m = |A|$), while an **undirected graph** has $m < \frac{n(n - 1)}{2}$ edges (we are removing the doubles).

### Properties of the trees

- Every **tree** with $n$ nodes has exactly $n - 1$ edges.

- Any pair of nodes in a tree is connected by a **unique** path.

- If we add an edge to a tree we create a **unique cycle**.

- Suppose that we've added an edge to a spanning tree, creating thus a unique cycle, then if we **remove any edge in the cycle** we get again a spanning tree.

## More sophisticated definitions and properties

### Optimality condition for MST

- Given a spanning tree of edges $T$, an **edge** $e \not \in T$ is **cost decreasing** if when is added to $T$ it creates a cycle $C$ with $C \subset T \cup \{ e \}$ and $\exists f \in C \setminus \{ e \}$ such that $c_e < c_f$.

- A **tree is of minimum cost** $\iff$ it **has no cost decreasing edge**.

### Optimal paths for graphs with $c(a) \geq 0$

- If $c(a) \geq 0 \forall a \in A$, then there exists **at least one simple optimal (shortest) path** between the nodes $s$ and $t$.

### Topological ordering

For every **DAG** it is possible to define an **order relation** between its nodes such that $i < j \forall (i, j) \in A$.

For doing so there exists a simple procedure:

- Any DAG has (at least) one node $n$ with in-degree equal to 0 (otherwise there would be at least a circuit): $n$ is the first in the topological ordering.

- We remove $n$ from the DAG and all its outgoing arcs ($n$ has only outgoing arcs), the result is again a DAG (by removing arcs and nodes we can't introduce circuits).

- We repeat the process finding the second node in the topological ordering and iterate until we have removed all the nodes.

We can translate this procedure in an algorithm as follows:

<div class="algorithm">
1. $FindNodeWithNoPredecessors(n, A)$:
1. &emsp; **while** $Predecessors(n, A) \neq \emptyset$:
1. &emsp; &emsp; $n \gets RandomNode(Predecessors(n, A))$
1. &emsp; **return** $n$
</div>

<div class="algorithm">
1. $u \gets RandomNode(N)$
1. $i \gets 1$
1. $R \gets \emptyset$
1. **while** $N \neq \emptyset$:
1. &emsp; $u \gets FindNodeWithNoPredecessors(u, A)$
1. &emsp; $s \gets RandomNode(Successors(u, A))$
1. &emsp; $N \gets N \setminus \{ u \}$
1. &emsp; $A \gets A \setminus \{ (u, j) \mid (u, j) \in A \}$
1. &emsp; $R \gets R \cup \{ (u, i) \}$
1. &emsp; $i \gets i + 1$
1. &emsp; $u \gets s$
</div>

At the end, the ordering can be derived from the couples in $R$. The algorithm considers every node and every arc at mosts twice (one time in the _"backward step"_ of finding a node with no predecessors and one time in the _"forward step"_ of deleting the node), then the overall complexity is $O(|N| + |A|)$.

### Recursive equation for shortest paths

Let $L_j$ be the length of a shortest path from node $s$ to node $j$.
Then the following **recursive** equation must hold $\forall t \in N$: $L_t = min_{(i, t) \in \delta^-(S)}\{L_i + c(i, t)\}$.

If the graph is a **DAG** we can exploit the **topological ordering** to rewrite the equation: $L_t = min_{i < t \wedge (i, t) \in \delta^-(S)}\{ L_i + c(i, t) \}$.

### Network flows

- A **network** is a **directed** and **connected** graph $G = (N, A)$ with a **source** $s \in N$ and a **sink** $t \in N$, with $s \neq t$ and a **capacity** $k_{ij} \geq 0$ for each arc $(i, j) \in A$.

- A **feasible flow** is a vector $\underline{x}$ with a component $x_{ij}$ for every arc $(i, j) \in A$ s. t.
    - $0 \leq x_{ij} \leq k_{ij} \forall (i, j) \in A$;
    - $\sum_{(i, u) \in \delta^-(\{ u \})} x_{iu} = \sum_{(u, j) \in \delta^+(\{ u \})} x_{uj} \forall u \in N \setminus \{ s, t \}$.

- The **value of the flow** is $\phi = \sum_{(s, j) \in \delta^+(\{ s \})} x_{sj}$.

- We say that an arc $(i, j)$ is **saturated** if $x_{ij} = k_{ij}$, **empty** if $x_{ij} = 0$.

- A **cut seprating $s$ from $t$** is a cut **induced by** $S \subset N \mid s \in S \wedge t \not \in S$.

- The **capacity of a cut $\delta(S)$** is $k(S) = \sum_{(i, j) \in \delta^+(S)} k_{ij}$.

- The **value of the flow through the cut $\delta(S)$ separating $s$ from $t$** is $\phi(S) = \sum_{(i, j) \in \delta^+(S)} x_{ij} - \sum_{(i, j) \in \delta^-(S)} x_{ij}$.

- It is possible to prove that **$\phi(S) = \phi(\{ s \})$** for every cut $\delta(S)$ separating $s$ from $t$. _(The proof follows very easily by induction once we have demonstrated the following identity: $\phi(R \cup \{ u \}) = \phi(R) + \phi(\{ u \})$ $\forall R \subset N$, $u \in N$, $u \not \in R$ which comes from splitting the sums in $\phi(R \cup \{ u \})$ over different subsets of $\delta^+(R \cup \{ u \})$ and $\delta^-(R \cup \{ u \})$ plus the usual adding and subtracting trick involving the arcs in $\{ (i, u) \in A \mid i \in R \}$ and $\{ (u, j) \in A \mid j \in R \}$)._

- It is clear that $\phi(S) \leq k(S)$ for every cut $\delta(S)$ separating $s$ from $t$: this implies that if we find a **feasible flow** $\underline{x}$ and a **cut separating $s$ from $t$ $\delta(S)$** s. t. $\phi(S) = k(S)$, then the **value** of $\underline{x}$ is **maximum** (**weak duality**).

## Algorithms

There are 3 usual data structures used to represent graphs:

- the **adjacency matrix**;

- the **adjacency list**;

- the **edge list**.

The algorithms that we will present are agnostic with respect to the various representations.

### Graph reacahability problem

Given a node $s$ in a directed graph $G = (N, A)$, we want to find all the nodes $n \in N$ that are reachable from $s$ (connected to $s$).

We can solve this problem through the so-called **Breadth First Search (BFS)** algorithm:
<div class="algorithm">
1. $Q \gets \{ s \}$ // Q is a queue
1. $M \gets \emptyset$
1. **while** $Q \neq \{ \}$:
1. &emsp; $n, Q \gets FIFOpop(Q)$
1. &emsp; $M \gets M \cup \{ n \}$
1. &emsp; **for** $a = (n, v) \in \delta^+(\{ n \})$:
1. &emsp; &emsp; **if** $v \not \in M$ **and** $v \not \in Q$:
1. &emsp; &emsp; &emsp; $Q \gets FIFOpush(Q, v)$
</div>
At the end of the computation, the reachable nodes are in $M$.
The complexity of the algorithm is $O(|N| + |A|)$ (we process every node and every arc at most once).

### Minimum Cost Spanning tree

#### Prim's algorithm

The **Prim**'s algorithm allows to find a minimum cost spanning tree, given a graph $G = (N, E)$ and a cost function $c : E \rightarrow \mathbb{R}$.

Let $s \in E$.

<div class="algorithm">
1. $S \gets \{ s \}$
1. $T \gets \emptyset$
1. **while** $|S| \neq |N|$:
1. &emsp; $e = \{ i, j \} \gets argmin_f \{ c(f) \mid f \in \delta(S) \}$
1. &emsp; $T \gets T \cup \{ e \}$
1. &emsp; **if** $i \not \in S$: $S \gets S \cup \{  i \}$
1. &emsp; **else**: $S \gets S \cup \{ j \}$
</div>

The computed spanning tree is $G' = (S, T)$.

The **exactness** of Prim's algorithm comes from the **cut property**: given a partial tree $(S, F)$ contained in a minimum cost spanning tree of $G$, if we add to it the edge of minimum cost in $\delta(S)$, the new tree is again contained in a minimum cost spanning tree (which could differ from the previous). The proof follows by induction (at every step we have a partial tree contained in a minimum cost spanning tree, and at the last step the tree isn't partial anymore).

- **Idea behind the proof of the cut property**: let $e$ be the edge of minimum cost in $\delta(S)$ and $T^*$ the set of edges of the minimum cost spanning tree which contains the partial one ($F \subset T^*$). If $e \in T^*$ there is nothing to prove. Otherwise there exists (it can be proved) an edge $f \in T^*$ s. t. $f \in \delta(S)$, $f$ belongs to the unique cycle which we create when we add $e$ to $T^*$. Then it must be $c_f = c_e$ (otherwise the tree with edges $T^*$ would not be optimal). Then the tree of edges $T^{**} = T^* \setminus \{ f \} \cup \{ e \}$ is also optimal and contains $F \cup \{ e \}$.

Let's see how to implement the $argmin_f$ function at line 4 efficiently.

Let $G = (N, E)$.

<div class="algorithm">
1. $S \gets \{ s \}$
1. $T \gets \{ \}$
1. **for** $j \in S^c$:
1. &emsp; $K_j \gets s$
1. &emsp; **if** $\{ s, j \} \in E$:
1. &emsp; &emsp; $C_j \gets c(\{ s, j \})$ 
1. &emsp; **else **:
1. &emsp; &emsp; $C_j \gets + \infty$
1. **while** $|S| \neq |N|$:
1. &emsp; $n \gets argmin_j\{ C_j \mid j \in S^c \}$ // $O(n)$
1. &emsp; $S \gets S \cup \{ n \}$
1. &emsp; $T \gets T \cup \{ (K_n, n) \}$
1. &emsp; **for** $j \in S^c$: &ensp; // $O(n)$
1. &emsp; &emsp; **if** $\{n, j\} \in E$ **and** $c(\{n, j\}) < C_j$:
1. &emsp; &emsp; &emsp; $K_j \gets n$
1. &emsp; &emsp; &emsp; $C_j \gets c(\{n, j\})$
</div>

The overall complexity is $O(n^2)$.

### Shortest path problem

We want to determine a path of minimum cost (shortest) starting at node $s$ and ending at node $t$.

#### Dijkstra's algorithm

The algorithm works for graphs where $c(a) \geq 0 \forall a \in A$.
The main idea is to consider the nodes in increasing order of length of the shortest path from $s$. If a node $u$ precedes a node $v$ in such ordering, then there must exist a shortest path from $s$ to $u$ which doesn't go through $v$ (remember the assumption above).

Let $G = (N, A)$.

<div class="algorithm">
1. $S \gets \{ s \}$
1. **for** $j \in S^c$:
1. &emsp; **if** $(s, j) \in A$:
1. &emsp; &emsp; $L_j \gets c(s, j)$
1. &emsp; **else**:
1. &emsp; &emsp; $L_j \gets + \infty$
1. &emsp; $P_j \gets s$
1. **while** $|S| \neq |N|$:
1. &emsp; $n \gets argmin_j\{L_j \mid j \in S^c\}$
1. &emsp; $S \gets S \cup \{ n \}$
1. &emsp; **for** $j \in S^c$: &ensp;
1. &emsp; &emsp; **if** $(n, j) \in A$ **and** $L_n + c(n, j) < L_j$:
1. &emsp; &emsp; &emsp; $L_j \gets L_n + c(n, j)$
1. &emsp; &emsp; &emsp; $P_j \gets n$
</div>

The overall complexity is $O(n^2)$.

The algorithm **exactness** follows (through induction) by the following statement: at every step $L_j$ is **the cost of the shortest path** from $s$ to $j$ $\forall j \in S$, and it is **the cost of the shortest path** from $s$ to $j$ **with all intermediate nodes in $S$** $\forall j \in S^c$.

To prove the inductive step just split every path $\pi$ from $s$ to **the chosen** $v \in S^c$ in $\pi_1 \cup (i, j) \cup \pi_2$ with $(i, j) \in \delta^+(S)$. Then $\pi_1 \geq L_i$ ($i \in S \implies L_i$ minimum cost of a path from $s$ to $i$), $\pi_2 \geq 0$ and so $c(\pi) \geq L_i + c(i, j) \geq min_{(k, l) \in \delta^+(S)}\{ L_k + c(k, l) \} = L_u + c(u, v) = c(\phi)$ where $\phi$ is the path from $s$ to $v$ picked by the algorithm.

#### Floyd-Warshall's algorithm

Conversely to Dijkstra's, **Floyd-Warshall**'s algorithm allows to find shortest paths even when $\exists a \in A \mid c(a) < 0$.

**Note**: sometimes when working with graphs with negative cost arcs, the shortest path problem could be ill-defined: think about negative net cost cycles! Even in such a case, **Floyd-Warshall**'s algorithm allows to detect the issue.

It is based on two data structures:

- $D_{ij}$ is the cost of the (current) shortest path from $i$ to $j$;

- $P_{ij}$ is the predecessor of $j$ in the (current) shortest path from $i$ to $j$.

It works by applying iteratively the **triangular operation**: fixed a node $u$, $\forall i, j \mid i \neq u, j \neq u$ if $D_{iu} + D_{uj} < D_{ij} \implies D_{ij} \gets D_{iu} + D_{uj}$ and $P_{ij} \gets P_{uj}$.

Let $G = (N, A)$.

<div class="algorithm">
1. **for** $i \in N$:
1. &emsp; **for** $j \in N$:
1. &emsp; &emsp; **if** $i = j$:
1. &emsp; &emsp; &emsp; $D_{ij} \gets 0$
1. &emsp; &emsp; **else if** $(i, j) \in A$:
1. &emsp; &emsp; &emsp; $D_{ij} \gets c(i, j)$
1. &emsp; &emsp; **else**:
1. &emsp; &emsp; &emsp; $D_{ij} \gets + \infty$
1. **for** $u \in N$:
1. &emsp; **for** $i \in N \setminus \{ u \}$:
1. &emsp; &emsp; **for** $j \in N \setminus \{ u \}$:
1. &emsp; &emsp; &emsp; **if** $D_{iu} + D_{uj} < D_{ij}$:
1. &emsp; &emsp; &emsp; &emsp; **if** $i = j$:
1. &emsp; &emsp; &emsp; &emsp; &emsp; **error**: Negative cost cycle!
1. &emsp; &emsp; &emsp; &emsp; $D_{ij} \gets D_{iu} + D_{uj}$
1. &emsp; &emsp; &emsp; &emsp; $P_{ij} \gets P_{uj}$
</div>

At the end we can retrieve the shortest path between any two nodes through $P_{ij}$. The overall complexity is $O(n^3)$.

#### Shortest path in DAGs

We can find shortest paths in a DAG by **exploiting the recursive equation**.

In particular we can solve it easily through **dynamic programming**: $L_0 = 0$, $L_1 = L_0 + c(0, 1)$, $L_2 = min\{ L_0 + c(0, 2), L_1 + c(1, 2) \}$, ... .

**Important note**: an analogous recursive equation holds for longest pahts. Then we can exploit the same approach to solve that problem too. For graphs in general the longest path problem could be ill-defined (when there are cycles of positive net cost) and adding the constraint of finding the longest simple path leads to a very hard problem.

### Project planning

A **project** consists of a set of **activities** $A, B, C, D, ...$ with a duration $d_A, d_B, d_C, d_D, ...$ and a set of **precedence constraints** between the activities: $A \propto B, B \propto D, ...$ .

We can represent every project through a **directed graph** where the **activities** are the **arcs**, every **node** $n$ represent the **event**: "end of all the activities in $\delta^-(\{ n \})$" and in particular there is a node for the event "beginning of the project" and a node for the event "end of the project". There is a **precedence constraint** between activity $A$ and activity $B$ $\iff$ there exists a **directed path where $A$ precedes $B$**.

**Note**: such directed graph must be a **DAG** (otherwise there would be a logical inconsistency in the precedence constraints).

The **cost** of each arch is the duration of the activity.

Let $s$ be the "beginning of the project" node and $t$ be the "end of the project" node. The cost of a path from $s$ to a node $n$ is a lower bound to the time at which the event represented by $n$ can occur (remember that **all** the activities in $\delta^-(\{ n \})$ must end). Then we can compute:

- $T_{min,h}$: _the minimum time at which the event associated to node $h$ can occur_ as **the length of the longest path from $s$ to $h$** (which we can compute through dynamic programming as we've seen before).

- $T_{max,h}$: _the maximum time at which the event associated to node $h$ can occur without delaying the completion of the project beyond $T_{min,t}$_ as $T_{min,t} - d_{h,t}$ where $d_{h,t}$ is **the length of the longest path from $t$ to $h$ in the DAG with reverse arcs** and can be interpreted as _the minimum time interval between the occurrence of the event $h$ and the occurrence of the event $t$_.

Finally for every activity $(i, j)$ we can calculate its **slack** $\sigma_{ij} = T_{max,j} - d_{ij} - T_{min,i}$ that is _the maximum time interval by which we can delay the start of activity $(i, j)$ without delaying the completion of the project (beyond $T_{min,t}$)_ (in this case $d_{ij}$ is the **duration** of the activity $(i, j)$).

We say that an activity $(i, j)$ is **critical** if $\sigma_{ij} = 0$.

The complexity of the algorithm is $O(|N| + |A|)$: the computations of $T_{min,h}$ and $T_{max,h}$ require each to consider each node and arc once.

Finally we can represent a **project schedule** through **Gantt charts**:

- **at earliest**: every activity $(i, j)$ starts at $T_{min,i}$;

- **at latest**: every activity $(i, j)$ ends at $T_{max,j}$.

### Maximum flow

Given a network we want to determine a **feasible flow of maximum value**.

#### Ford-Fulkerson's algorithm

The algorithm works as follows:

- Let $G = (N, A)$ be a **network** and $\underline{x}$ a **feasible flow** (we can always start with $\underline{x} = \underline{0}$).

- From $G$ we can build the **so called** residual network $\bar{G}$ = $(N, \bar{A})$ as follows:
    - if $(i, j) \in A \wedge x_{ij} < k_{ij} \implies (i, j) \in \bar{A}$ with **residual capacity** $\bar{k}_{ij} = k_{ij} - x_{ij}$;
    - if $(j, i) \in A \wedge x_{ji} > 0 \implies (i, j) \in \bar{A}$ with **residual capacity** $\bar{k}_{ij} = x_{ji}$.

- If we find a path $s$, $n_1$, ..., $n_u$, $t$ in $\bar{G}$, then we can increase the flow from $s$ to $t$ either by increasing the flow in $(n_i, n_{i + 1})$ or by decreasing the flow in $(n_{i + 1}, n_i)$: we have found a so-called **augmenting path** (of course we also have to increase the flow in both $(s, n_1)$ and $(n_u, t)$). The amount by which we can increase the flow is $min_{i \in \{ 1, ..., u-1 \}}\{ \bar{k}_{s, n_1}, \bar{k}_{n_i, n_{i + 1}}, \bar{k}_{n_u, t} \}$.

- We keep iterating this process until there is no path in $\bar{G}$ from $s$ to $t$: this means that there must be a cut $\delta(S)$ separating $s$ from $t$ that has every outgoing arc **saturated** and every incoming arc **empty**. Hence $\phi(S) = k(S)$, and so, by **weak duality**, the **value of $\underline{x}$** is **maximum**.

The overall complexity is $O(m^2 k_{max})$ (it is exponential in the size of the instance with respect to $k_{max}$):

- $\phi(\{ s \}) \leq m k_{max}$;

- **At every step** the value of the **flow increases**;

- If all $k_{ij}$ and $x_{ij}$ are integers, then the same is true for all the $\bar{k}_{ij}$ and so for the increase of the flow, which must be at least 1 (then the algorithm takes at most $m k_{max}$ steps);

- Every step is $O(n + m) = O(m)$: we have to build $\bar{G}$ ($O(n + m)$) and find a path from $s$ to $t$ (for example with an $O(n + m)$ DFS).

**Note**: there are some variations of **Ford-Fulkerson**'s algorithm that are polynomial in the size of the instance and work by looking for augmenting paths **with a minimum number of arcs** (**Edmond-and-Karp**'s $O(nm^2)$, **Dinic**'s $O(n^2m)$).
