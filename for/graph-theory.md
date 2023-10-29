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

- For **undirected** graphs we define the **degree** of a node $n$ as the number of edges which are incident to that node. For **directed** graphs we distinguish between the **in-degree**: the number of arcs $(j, n) \in A$ and the **out-degree**: the number of arcs $(n, j) \in A$.

### Paths

- For an **undirected** graph, a **path** of length $k$ from node $n_1$ to node $n_k$ is a sequence of nodes $n_1, n_2, ..., n_{k-1}, n_k$ s. t. $\{n_i, n_{i + 1}\} \in E$ $\forall i \in \{1, ..., k\}$.

- For **directed** graphs, a **directed path** of length $k$ from node $n_1$ to node $n_k$ is a sequence of nodes $n_1, ..., n_k$ s. t. the arc $(n_i, n_{i + 1})$ belongs to $A$ $\forall i \in \{1, ..., k\}$.

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

## Basic properties

### Maximum number of edges and arcs

A **directed graph** has $m < n(n - 1)$ arcs ($m = |A|$), while an **undirected graph** has $m < \frac{n(n - 1)}{2}$ edges (we are removing the doubles).

### Properties of the trees

- Every **tree** with $n$ nodes has exactly $n - 1$ edges.

- Any pair of nodes in a tree is connected by a **unique** path.

- If we add an edge to a tree we create a **unique cycle**.

- Suppose that we've added an edge to a spanning tree, creating thus a unique cycle, then if we **remove any edge in the cycle** we get again a spanning tree.

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
1. $Q \gets \{ s \}$ `// Q is a queue`
1. $M \gets \emptyset$
1. **`while`** $Q \neq \{ \}$:
1. $~~~~$ $n, Q \gets FIFOpop(Q)$
1. $~~~~$ $M \gets M \cup \{ n \}$
1. $~~~~$ **`for`** $a = (n, v) \in \delta^+(\{ n \})$:
1. $~~~~$ $~~~~$ **`if`** $v \not \in M$ **`and`** $v \not \in Q$:
1. $~~~~$ $~~~~$ $~~~~$ $Q \gets FIFOpush(Q, v)$
</div>
At the end of the computation, the reachable nodes are in $M$.
The complexity of the algorithm is $O(|N| + |A|)$.

### Minimum Cost Spanning tree

#### Prim's algorithm

The **Prim**'s algorithm allows to find a minimum cost spanning tree, given a graph $G = (N, E)$ and a cost function $c : E \rightarrow \mathbb{R}$.

Let $s \in E$.

<div class="algorithm">
1. $S \gets \{ s \}$
1. $T \gets \emptyset$
1. **`while`** $|S| \neq |N|$:
1. $~~~~$ $e = \{ i, j \} = argmin_f \{ c(f) \mid f \in \delta(S) \}$
1. $~~~~$ $T \gets T \cup \{ e \}$
1. $~~~~$ **`if`** $i \not \in S$:
1. $~~~~$ $~~~~$ $S \gets S \cup \{  i \}$
1. $~~~~$ **`else`**:
1. $~~~~$ $~~~~$ $S \gets S \cup \{ j \}$
</div>

The computed spanning tree is $G' = (S, T)$.

The **exactness** of Prim's algorithm comes from the **cut property**: given a partial tree $(S, F)$ contained in a minimum cost spanning tree of $G$, if we add to it the edge of minimum cost in $\delta(S)$, the new tree is again contained in a minimum cost spanning tree (which could differ from the previous). The proof follows by induction (at every step we have a partial tree contained in a minimum cost spanning tree, and at the last step the tree isn't partial anymore).

- **Idea behind the proof of the cut property**: let $e$ be the edge of minimum cost in $\delta(S)$ and $T^*$ the set of edges of the minimum cost spanning tree which contains the partial one ($F \subset T^*$). If $e \in T^*$ there is nothing to prove. Otherwise there exists (it can be proved) an edge $f \in T^*$ s. t. $f \in \delta(S)$, $f$ belongs to the unique cycle which we create when we add $e$ to $T^*$. Then it must be $c_f = c_e$ (otherwise the tree with edges $T^*$ would not be optimal). Then the tree of edges $T^{**} = T^* \setminus \{ f \} \cup \{ e \}$ is also optimal and contains $F \cup \{ e \}$.

Let's see how to implement the $argmin_f$ function at line `4` efficiently.

Let $G = (N, E)$.
<div class=algorithm>
1. $S \gets \{ s \}$
1. $T \gets \{ \}$
1. **`for`** $j \in S^c$:
1. $~~~~$ $K_j \gets s$
1. $~~~~$ **`if`** $\{ s, j \} \in E$:
1. $~~~~$ $~~~~$ $C_j \gets c(\{ s, j \})$ 
1. $~~~~$ **`else `**:
1. $~~~~$ $~~~~$ $C_j \gets + \infty$
1. **`while`** $|S| \neq |N|$:
1. $~~~~$ $n \gets argmin_j\{ C_j \mid j \in S^c \}$ `// O(n)`
1. $~~~~$ $S \gets \{ n \}$
1. $~~~~$ $T \gets (K_n, n)$
1. $~~~~$ **`for`** $j \in S^c$: $~~$ `// O(n)`
1. $~~~~$ $~~~~$ **`if`** $\{n, j\} \in E$ **`and`** $c(\{n, j\}) < C_j$:
1. $~~~~$ $~~~~$ $~~~~$ $K_j \gets n$
1. $~~~~$ $~~~~$ $~~~~$ $C_j \gets c(\{n, j\})$
</div>

The overall complexity is $O(n^2)$.

## More sophisticated definitions and properties

### Optimality condition for MST

- Given a spanning tree of edges $T$, an **edge** $e \not \in T$ is **cost decreasing** if when is added to $T$ it creates a cycle $C$ with $C \subset T \cup \{ e \}$ and $\exists f \in C \setminus \{ e \}$ such that $c_e < c_f$.

- A **tree is of minimum cost** $\iff$ it **has no cost decreasing edge**.
