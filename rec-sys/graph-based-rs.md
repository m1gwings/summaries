---
marp: true
theme: summary
math: mathjax
---
# Graph-based recommender systems

<div class="author">

Cristiano Migali

</div>

**Graph-based recommender systems** rely on a graph representation of the data.
In particular, we can represent a URM as a bi-partite graph between the set of users $\mathcal{U}$ and the set of items $\mathcal{I}$: there is an edge $(u, i) \in E$ iff $r_{u,i} = 1$ (_for implicit ratings_).
If we also want to represent the URM, we can turn the bi-partite graph into a tri-partite one where we add the set of attributes $\mathcal{A}$: there is an edge $(i, a) \in E$ iff $C_{i,a} = 1$ (_for binary attributes_).
The set of nodes is denoted as $N = \mathcal{U} \cup \mathcal{I} \text{ or } \mathcal{U} \cup \mathcal{I} \cup \mathcal{A}$.
We can represent a graph through an adjacency matrix $G \in \mathbb{R}^{|N| \times |N|}$, where:
$$
G_{x,y} = \begin{cases}
1 \text{ there is a connection from node } x \text{ to node } y \\
0 \text{ otherwise}
\end{cases}.
$$
If the graph is **undirected**, $G$ is symmetric, and we have $G_{x,y} = G_{y,x}$.
Otherwise, the graph is said **directed** and $G$ is not symmetric.
It is possible to generalize adjacency matrices to add weights to connections.

In a typical RS scenario:
- the graph is **undirected**;
- the edges may be **weighted or not**;
- the nodes do NOT have **self-connections**.

$G$ is usually built as a block matrix. If $N = \mathcal{U} \cup \mathcal{I}$,
$$
G = \begin{bmatrix}
O & R \\
R^T & O
\end{bmatrix}.
$$
If $N = \mathcal{U} \cup \mathcal{I} \cup \mathcal{A}$ instead, we have:
$$
G = \begin{bmatrix}
O & R & O \\
R^T & O & C \\
O & C^T & O
\end{bmatrix}.
$$

## Recommendation with random walk

The idea of **random walk** is the following: starting from a user we can "walk" on the graph by following one of the edges that exist for that node. In this way we reach an item node, we can repeat the process jumping to an user node, and then to a new item node. The item associated to this last node could be a possible recommendation (at 3 hops).

---

We need to answer the following questions:
- How to ensure that we obtained a **good** recommendation?
- How do we create a recommendation list (i.e. how do we rank the outputs of several random walks)?
- How many **hops** do we perform?

### Page rank

One way to answer to the previous questions is through the page rank algorithm.
In **page rank**, instead of running individual random walks, we model them probabilistically, computing the **probability to transition** between two nodes and a **probability distribution on being in each node**.
The items with the highest probability are the best recommendations.

We can formalize this process through:
- a **transition probability** matrix $P = (p_{x,y})_{x \in N, y \in N} \in \mathbb{R}^{|N| \times |N|}$ where $\sum_{y \in N} p_{x,y} = 1, \forall x \in N$;
- a **state probability** (row) **vector** $\Pi \in \mathbb{R}^|N|$ with $\sum_{x \in N} \Pi_x = 1$.

Let $D = (d_x)_{x \in N} \in \mathbb{R}^{|N|}$ where $d_x$ is the degree of node $x \in N$. Then we set:
$$
p_{x,y} = \frac{g_{x,y}}{d_x}.
$$

The probability of being in node $x$ can be computed, given:
- the probability distribution on being in each node in the previous hop;
- the probability to jump from it to $i$.
$$
\Pi_x^(1) = \sum_{y \in N} \Pi_y^{(0)} p_{y,x}.
$$

In matrix notation:
$$
\Pi^{(h)} = \Pi^{(h-1)} P.
$$

Once we have conducted a sufficiently long random walk, we can use the state probability of the **item nodes** as their scores and rank them.

The number of hops $h$ is a very important hyper-parameter, however, optimal values tend to be limited to 3, (sometimes) 5, and (rarely) 7.
If $h$ is large, you travel too distant from the target user, and recommendations tend to become popularity-based.

If the random walk continues for $h \rightarrow +\infty$, either:
- we will reach the steady state $\Pi = \Pi P$ regardless of the starting state;
- for $n$-partite graphs we will find a _periodic_ sequence of states.

---

Observe that the **steady state is NOT personalized** since it is independent from the initialization.

#### Random walk restart

We can model an infinite random walk with probability $1-\gamma$ to restart from the initial state as follows:
$$
\Pi^{(h)} = \gamma \Pi^{(h-1)}P + (1-\gamma) \Pi^{(0)}.
$$
The choice of $\gamma$ allows to control how **personalized** the recommendations are.
We can find the steady state of the equation above:
$$
\Pi = \gamma \Pi P + (1-\gamma) \Pi^{(0)}
$$
by solving a linear system, however this approach is expensive.

### $P^3$

A simple strategy to recommend items is based on their state probability at 3-hops:
$$
\Pi^{(1)} = \Pi^{(0)} P;
$$
$$
\Pi^{(2)} = \Pi^{(1)} P = \Pi^{(0)} P^2;
$$
$$
\Pi^{(3)} = \Pi^{(2)} P = \Pi^{(0)} P^3.
$$
The name of the method is **$P^3$** and follows from the last expression.

Computing $P^3$ is very expensive (and dense), but:
- we only need a specific meta-path: $\mathcal{U} \rightarrow \mathcal{I} \rightarrow \mathcal{U} \rightarrow \mathcal{I}$;
- $P$ is a block matrix, we can compute only the portion we need.

Indeed, remember that:
$$
P = \begin{bmatrix}
O & P_{\mathcal{U}\mathcal{I}} \\
P_{\mathcal{I}\mathcal{U}} & O
\end{bmatrix}
$$
where
$$
P_{\mathcal{U}\mathcal{I}} = \text{diag}\left[\frac{1}{D_\mathcal{U}}\right] R;
$$
$$
P_{\mathcal{I}\mathcal{U}} = \text{diag}\left[\frac{1}{D_\mathcal{I}}\right] R^T.
$$

---

From this block representation, we get:
$$
P^2 = \begin{bmatrix}
P_{\mathcal{U}\mathcal{I}} P_{\mathcal{I}\mathcal{U}} & O \\
O & P_{\mathcal{I}\mathcal{U}} P_{\mathcal{U}\mathcal{I}}
\end{bmatrix};
$$
$$
P^3 = \begin{bmatrix}
O & P_{\mathcal{U}\mathcal{I}} P_{\mathcal{I}\mathcal{U}} P_{\mathcal{U}\mathcal{I}} \\
P_{\mathcal{I}\mathcal{U}} P_{\mathcal{U}\mathcal{I}} P_{\mathcal{I}\mathcal{U}} & O
\end{bmatrix}.
$$

In our case, we're interested only on the top-right block.

In the following we will denote with $\Pi_\mathcal{I}$ the state probability for item nodes, and with $\Pi_\mathcal{U}$ the state probability for user nodes.
We have that:
$$
\Pi_\mathcal{I}^{(3)} = \Pi_\mathcal{U}^{(0)} P_{\mathcal{U} \mathcal{I}} P_{\mathcal{I} \mathcal{U}} P_{\mathcal{U} \mathcal{I}}.
$$
We can rewrite the expression above as:
$$
\Pi_\mathcal{I}^{(3)} = \Pi_\mathcal{U}^{(0)} P_{\mathcal{U} \mathcal{I}} S
$$
where
$$
S_{i,j} = [ P_{\mathcal{I} \mathcal{U}} P_{\mathcal{U} \mathcal{I}} ]_{i,j} = \sum_{u \in \mathcal{U}} \frac{r_{u,i} r_{u,j}}{d_i d_j}.
$$

Thus, for implicit interactions, <u>$P^3$ is the cosine similarity without shrinkage</u>.

### $P^3_\alpha$

In **$P^3_\alpha$**, the transition probabilities are elevated to a power $\alpha$:
$$
P_{\mathcal{U} \mathcal{I}} = \left( \text{diag}\left[\frac{1}{D_\mathcal{U}}\right] R \right)^\alpha;
$$
$$
P_{\mathcal{I} \mathcal{U}} = \left( \text{diag}\left[\frac{1}{D_\mathcal{I}}\right] R^T \right)^\alpha.
$$
Thus, the similarity matrix becomes:
$$
S_{i,j} = \sum_{u \in \mathcal{U}} \left( \frac{r_{u,i} r_{u,j}}{d_i d_j} \right)^\alpha.
$$
If $\alpha > 1$ is small, the transition probabilities and the similarities are attenuated.

$P^3_\alpha$ tends to exhibit a <u>strong popularity bias</u>.
Indeed, if the small probabilities are attenuated too much, we will only consider items that are "very likely" (i.e. popular).

---

### $RP^3_\beta$

**$RP^3_\beta$** tries to reduce the popularity bias.
In particular, the **problem** is that it is too easy for a random walk to end up in items with high degree.
The **idea** is to penalize the similarity of items with high degree. We divide the similarity by the popularity of the destination item elevated to a power $\beta$:
$$
S_{i,j} = \frac{1}{d_j^\beta} \sum_{u \in \mathcal{U}} \left( \frac{r_{u,i} r_{u,j}}{d_i d_j} \right)^\alpha.
$$

### Adding side information

As explained before, we can add information about items attributes in a tri-partite graph.
If we run a $3$-hop random walk, we have two possible meta-paths which end in the set of items:
- $\mathcal{U} \rightarrow \mathcal{I} \rightarrow \mathcal{U} \rightarrow \mathcal{I}$;
- $\mathcal{U} \rightarrow \mathcal{I} \rightarrow \mathcal{A} \rightarrow \mathcal{I}$,

It will be possible to use the methods described earlier, but we may need to weight the edges $\mathcal{I} \rightarrow \mathcal{A}$ to control how frequently we use them.

We can also add both item attributes $\mathcal{A}_\mathcal{I}$ and user attributes $\mathcal{A}_\mathcal{U}$. But in this way we encounter problematic meta-paths.
In particular we have a new (desired) meta-path:
$$
\mathcal{U} \rightarrow \mathcal{A}_\mathcal{U} \rightarrow \mathcal{U} \rightarrow \mathcal{I};
$$
but there are also some meta-paths which do NOT end in the right node:
$$
\mathcal{U} \rightarrow \mathcal{I} \rightarrow \mathcal{U} \rightarrow \mathcal{A}_\mathcal{U} \text{, and}
$$
$$
\mathcal{U} \rightarrow \mathcal{A}_\mathcal{U} \rightarrow \mathcal{U} \rightarrow \mathcal{A}_\mathcal{U}.
$$

The **solution** is simply to change the $P$ matrix used in the third hop to remove that $\mathcal{U} \rightarrow \mathcal{A}_\mathcal{U}$ edges.
