---
theme: summary
---
# FAI's methods & algorithms

<div class="author">

Cristiano Migali

</div>

## Introudction

We will list all the methods and algorithms presented in the FAI course, which are relevant for the exam, with a focus on how to apply the algorithms on paper.

## Agents' architectures

### Simple reflex agents

The chosen action depends only on the last percept (which should represent the current state of the world).
We can implement one as a list of `if` statements.

### Model-based agents

They use a model of the world to build a representation of the current state from the sequence of percepts and actions performed. Then they choose the action in function of the current state.
We can implement one by specifying:
- a **transition model**: specifies the next state given the current state and the performed action;
- a **sensor model**: specifies how the current state of the world reflects in the agent's percepts;
- a set of **rules** to choose the action according to the current state.

### Goal-based agents

They are like model based agents, but the chosen actions depends not only on the current state, but also on a goal that we want to reach (we can model the goal as a predicate satisfied by certain states).


### Utility-based agents

They are like model-based agenets, but the chosen actions depends not only on the current state, but also on a utility function that the agent tries to maximize.

### Learning agents

Learning is orthogonal to the chosen agents architecture. In every case it consists of "imrpoving" the elements which constitute the agents from experience (through algorithms).

---

We can define a learning agent through 4 macro-components:
- a **learning element**: it is responsible for making improvements;
- a **performance element**: it selects external actions;
- a **critic element**: it provides feedback on how the agent is doing and determins how the performance element should be modified to improve future performance;
- a **problem generator**: it suggests explanatory actions that will lead to new and informative experiences.

The **performance element** contains all the components that we listed in the various agent architectures.

## Search

### Problem formulation

To formulate a seach problem, we need to specify:
- how we represent the **states**;
- a function **`actions(s)`** which returns the list of functions that we can perform in state `s`;
- a function **`result(s, a)`** which returns the next state when the current state is `s` and we perform action `a`;
- a function **`goal_test(s)`** which returns true if the state `s` satisfies the goal.
- a function **`c(s, a, s')`** which is the cost of performing action `a` in state `s`, ending in state `s'`;
- an **initial state** `s0`.

The **state space** is a graph induced by the elements listed above.

The **solution to a search problem** is a path (in the state space) from `s0` to a state `g` s. t. `goal_test(g)` is `True`.
An **optimal solution to a search problem** is a solution with minimum cost (where the cost is the sum of `c(s, a, s')` for all `(s, a, s')` in the path).

### Solving search problems

**Solutions** to a search problem are **found by building a search tree** from the space state graph.

A **search tree** is composed of **search nodes**.
**Each node corresponds to a path from the initial state to a state in the state space**.
**Each state of the space state can correspond to multiple nodes, when a state can be reacahed from the initial state, following multiple paths**.
If the states can be visited multiple times, then the search tree can be infinite even if the state space is finite.

---

Every node is represented by:
- a **state** which is the last state of the path corresponding to the node;
- a **parent node** which is the node which corresponds to the path of the current node excepts for the last state (the node with no parent represents the path with only one state `s0` and no actions);
- an **action** which is the action which led to the last state;
- a **cost** which is the cost of going to the last state according to the performed action.
To every node we can associate the corresponding **depth** in the search tree.

#### Tree search

1. We initialize the search by drawing a node corresponding to the path with only the `s0` state and no action;
2. At every step:
> 3. Select (_see the "Search strategies" paragraph_) a node which hasn't been expanded yet (a node with no children):
> 4. If the node corresponds to the goal state:
>> 5. Return the solution;
> 6. Else:
>> 7. Expand the selected node.

We call **frontier** the set of nodes not yet expanded. It is implemented as a priority queue.
A **search strategy** determines the ordering of nodes in the frontier: we select the first node in the frontier.

**Remark**: tree search can lead to visiting the same state more than once.

#### Graph search

Graph search avoids visiting the same state more than once. We do so with a so-called closed list:

1. We initialize the closed list with an empty list;
2. We initialize the search by drawing a node corresponding to the path with only the `s0` state and no action;
3. At every step:
> 4. Select (_see the "Search strategies" paragraph_) a node which hasn't been expanded yet (a node with no children):
> 4. If the node corresponds to the goal state:
>> 5. Return the solution;

---

> 6. Else, if the node is not yet in the closed list:
>> 7. Add the node to the closed list;
>> 8. Expand the node.

#### Search strategies

Let $b$ be the branching factor (assuming its finite) and $d$ the depth of the shallowest solution.

We say that a **search strategy** is **complete** if, when there is a solution to the problem, it finds at least one.

- **BFS**

The priority queue is a queue.
Temporal and spatial complexity are $O(b^{d+1})$. In the worst case the solution is the "last" (according to the order in which we select nodes) node of the $d$ layer, hence, before reaching it, we will have built almost all the $d+1$ layer.

It is **complete** (if $b$ is finite).
It is **optimal** when the cost function is a non-decreasing function of the depth of the node.

If we do **early goal checking** (that is, we check if a node's state satisfies the goal test when we add it to the frontier and not when we select it from the frontier) the algorithm is still optimal and complete (if the hypotheses cited before are met), .

- **Uniform-cost search**

It generalizes breadth-first search. It sorts the nodes in the frontier according to their increasing path cost from the root. It selects the node $n$ with the smallest path cost from the root.

Let $\epsilon > 0$ be the smallest step cost and $C^*$ be the cost of an optimal solution. Then, the temporal and spatial complexity of UCS is $O(b^{1+C^*/\epsilon})$.

Uniform cost search is **optimal** and **complete**.

- **DFS**

The priority queue is a stack.
It is **not complete** (it can follow paths of infinite depth), **nor optimal**.

It has spatial complexity of $O(bm)$ where $m$ is the maximum depth of the search tree (only a single path of the search tree is stored in memory).
The spatial complexity is $O(b^m)$ in the worst case (often $m \gg d$).

---

- **Depth limited search**

Like DFS but we limit the depth of the tree to $L$. Nodes at depth $L$ are assumed to not have successors.
It is not complete, nor optimal in general.
It is **complete if $d \leq L$**.
Time complexity is $O(b^L)$. Space complexity is $O(bL)$

- **Iterative deeepening search**

It perform depth limited searches for increasing values of $L$.
It has $O(bd)$ spatial complexity and $O(b^d)$ temporal complexity.
It is **complete** and **optimal** (assuming the same hypotheses of BFS).

- **Greedy best first search**

Uses an evaluation function that is equal to a heuristic function $h(n)$.
An **heuristic function** provides an under estimate of the cost of reaching the goal from the given state.

Greedy best first searach is **not complete** when the heuristic makes it follow an infinite path with no goal states.

Greedy best first search is in general, **not optimal**.

It has  both temporal and spatial complexity of $O(b^m)$, where $m$ is the maximum depth of the search tree.

- **A\* search**

The evaluation function is $f(n) = g(n) + h(n)$, where $g(n)$ is the cost of reaching node $n$.

**First optimality theorem**: **A\*** search is **complete and optimal for tree-search** for admissible heuristics.

> **Proof**: 
> - **Completeness**
>>> Assume that the step costs are at least $\epsilon > 0$. Then $f(n) \geq g(n) \geq d(n) \epsilon$ where $d(n)$ is the depth of node $n$. Let $C^*$ be the cost of an optimal solution. Hence, A* won't expand any node at depth $\lceil \frac{C^*}{\epsilon} \rceil$ before having expanded the goal. Since the number of nodes with $d(n) < \lceil \frac{C^*}{\epsilon} \rceil$ is finite (assuming finite branching factor), A* is complete.
> - **Optimality**
>>> Let $g'$ be a suboptimal goal. Then $g(g') > C^*$. Let $n$ be a node on the path for an optimal goal $g^*$, then, $f(n) \leq C^*$.

---

>>> Hence, every node in the path to $g^*$ will be expanded before $g'$ (including $g^*$). SO the first goal which we expand must be an optimal goal. It follows that A* is optimal.

**Second optimality theorem**: **A\*** search is **complete and optimal for graph-search** for consistent heuristics.

> **Proof**:
> - **Completeness**
>>> (_Same proof as the first optimality theorem_).
> - **Optimality**
>>> Consider the node $n$ and its successor $n'$: $f(n') = g(n') + h(n') = g(n) + c(n, n') + h(n') \geq g(n) + h(n) = f(n).$ That is, A* with a consistent heuristic expands nodes in order of increasing $f(n)$. Hence, the first time we expand a node with a certain state, the path for reaching that state must be optimal (otherwise, since $h$ does not depend on the path, there would be another node with the same state and smaller $f$). So the first time we reach a goal, the path to that goal is optimal and the cost of reaching every other goal must be greater or equal that the one found.

It has worst case temporal and spatial complexity exponential in the length of the solution.

A heuristic is **admissible** when, for each node $n$, $0 \leq h(n) \leq h^*(n)$ where $h^*(n)$ represents the actual cost from node $n$ to the solution (following an optimal path).
When $g$ is a goal node, $h(g)$ should be $0$.

We usually define admissible heuristics by solving a relaxed version of the problem.

A heuristic function si **consistent** iff:
- $h(n) \leq c(n, n') + h(n')$ for every successor $n'$ of $n$;
- $h(g) = 0$ for every goal $g$.


**A\*** is **optimally efficient**:
- it expands all nodes with $f(n) < C^*$;
- it expands some nodes with $f(n) = C^*$;
- it expands no nodes with $f(n) > C^*$.

---

- **Weighted A\***

Like A*, but the heuristic is weighted by $1 leq w < + \infty$:

$$
f(n) = g(n) + wh(n)
$$

- **IDA\***

It stands for **Iterative Deepening A\***, it is similar to IDS, but instead of limiting the depth, it limits the value of $f(n)$. It reduces the memory requirement of A* search. It requires a consistent heuristic function.

In practice we do a **DFS** for all the nodes such that $f(n) \leq k$, where $k$ is a cutoff.

**IDA\*** is **complete** when $h(n)$ is **admissible**.

**IDA\*** is also **optimal** when $h(n)$ is **consistent**.

#### Bidirectional search

It performs two searchs in parallel: a "forward" search from the initial state to a goal state, a "backward" search from a goal state to the initial state.

### Adversarial search

Games can be formulated as search problems with an element of uncertainty due to the actions (moves) of the opponent.

We can **formulate a search problem for a game** by specifying:
- the players (usually two players, MIN and MAX, which takes turn);
- an initial state;
- the function `actions`;
- the function `result(s, a)`;
- a function `goal_test(s)`,
- a function `utility(s, p)`: returns the numerical value to player p in terminal state `s`.

#### Minimax

1. We draw the max node;
2. We expand the game tree in a depth-first manner, max and min nodes alternate;
3. When we reach the leaf, the corresponding value is given by a utility function (if they correspond to terminal states) or by an evaluation function (if it is not the case).
4. Then we propagate up the values of the nodes: min takes the minimum among the values of its children, max does the contrary.

---

#### Alpha beta pruning

Reduces the compelxity of the minimax search by not considering branches of the game tree that cannot influence the final decision.

To very node we associate a value $\alpha$ and a value $\beta$. $\alpha$ is a lowerbound to the value of the node for it to potentially have influence on the final decision. $\beta$, instead, is an upperbound

The root node has $\alpha = - \infty$ and $\beta = + \infty$.
Values of $\alpha$ and $\beta$ propagates from parents to children.
A min node updates its $\beta$ value (it tells the children the best value that it has already found).
A max node updates its $\alpha$ value (it tells the children)

Let $h$ be the maximum height of the search tree.
Minimax expands $O(b^h)$ nodes.
In the best case, alpha-beta pruning expands $O(b^{h/2})$ nodes.
On the average case, it expands $O(b^{3/4 h})$ nodes.
On the worst case, it expands $O(b^h)$ nodes.

**If we sort the moves such that the first move is always the best both for MAX and MIN, we have the best complexity**.

#### Expected minimax

To model stochastic games we can use **expected minimax** where we add to minimax a third kind of node which performs the weighted average (depending on the probabilities) of the values of the children.

We can apply alpha beta pruning also to stochastic games.

In stochastic games, an **order preserving transformation** that changes the values in the leaves can **affect the optimal move** (there are examples of this). This does not happen in deterministic game since the values in the second last layer are completely determined by the order, and the same happens as we go above by induction.

#### Monte Carlo Tree Search (MCTS)

Monte Carlo Tree Seacrh (MCTS) develops an asymmetric game tree whhile evaluating states using random simulations.

The algorithms works as follows:
1. Until we have time:
> 2. Until the current node is not a leaf or a node with unexpanded children:
>> 3. We select a child using a selection policy and make it the current node;

---

> 4. We expand the current node (if it is not terminal) by adding **one child**;
> 5. We perform a simulation for that child.
> 6. We backpropagate the result of the simulation to the parents.

In particular every node stores: the number of wins and the number of simulations.

At the end we return the move **with the heighest number of playout** (which, because of the selection policy, correlates with the move with the highest number of wins).

We say that MCTS is an **anytime method**: it can provide an answer if stopped at any time.

A typical selection policy is:
$$
UCB1(n) = \frac{U(n)}{N(n)} + C \sqrt{\frac{\log N(parent(b))}{N(n)}}
$$

$C$ is known as **exploration parameter**.

---


## Reinforcement learning

### Q-learning

The **update rule** for Q-learning is:

$$
Q(s_t, a_t) \leftarrow Q(s_t, a_t) + \beta ( r_{t+1} + \gamma \max_{a \in \mathcal{A}}Q(s_{t+1}, a) - Q(s_t, a_t) ) \text{ .}
$$

Let's decompose the formula:
$$
Q(s_t, a_t) \leftarrow Q(s_t, a_t) + \beta \epsilon
$$
where $\epsilon$ is the error in the prediction:
$$
\epsilon = r_{t+1} + \gamma \max_{a \in \mathcal{A}} Q(s_{t+1}, a) - Q(s_t, a_t) \text{ .}
$$
Indeed $Q(s_t, a_t)$ is the predicted value for the expected reward (at $+ \infty$), and $r_{t+1} + \gamma \max_{a \in \mathcal{A}} Q(s_{t+1}, a)$ is the prediction updated by taking into account the last reward.