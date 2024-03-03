---
marp: true
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

---

## Constraint Satisfaction Problems (CSP)

In search problems considered so far, the state representation is generic.
When the strucutre of the state is fixed, more efficient solving techniques could be developed. In **Constratint Satisfaction Problems**, the state has a **factored representation**, namely it is represented by a pair (variable, value).

### CSP formulation

A **CSP** is a triple $(X, D, C)$ where:
- $X = \{ x_1, ..., x_n \}$ is a set of **variables**;
- $D = \{ D_1, ..., D_n \}$ is a set of **domains**;
- $C = \{ C_1, ..., C_m \}$ is a set of **contraints**.

Every domain $D_i$ is the set of values that the variable $x_i$ can assume.
Every constraint $C_j = (S_j, R_j)$ where:
- $S_j = (x_{h_1}, ..., x_{h_{k_j}})$ is the **scope** of the constraint (that is, the tuple of variables involved in the constraint);
- $R_j \subset D_{h_1} \times ... \times D_{h_{k_j}}$ is the set of value that the tuple $S_j$ can assume.
$k_j$ is the **arity** of the constaint $C_j$:
- if $k_j = 1$, the constraint is unary;
- if $k_j = 2$, the constraint is binary.

**Remark**: it is possible to show that, for every CSP, we can find an equivalent CSP with only binary constraints (by adding variables).

An **assignment** is a set of pairs $A = \{ (x_i, v_i) \}$ where $x_i \in X, v_i \in D_i$, and, if $(x_i, v_{i_1}), (x_i, v_{i_2}) \in A$, then $v_{i_1} = v_{i_2}$.

We say that an **assignment** is:
- **partial** if there exists $x_{\hat{i}}$ s.t. $(x_{\hat{i}}, v_i) \not \in A$ for every $v_i \in D_i$, **complete** otherwise;
- **consistent** if for every $C_j \in C$, the fact that for every $x_i \in S_j$ there exists $(x_i, v_i) \in A$ for some $v_i \in D_i$ implies that $(v_1, ..., v_{k_j}) \in R_j$, **inconsistent** otherwise.

The **goal** of a CSP is to find a complete and consistent assignment.

**For every CSP we can find an equivalent CSP involving only binary constraints** (by adding additional variables).

---

### Solving CSPs

We can solve CSPs as search problems where the states are consistent assignments (and domain of variables if we restrict them during the search). With every action we assign a value to an unassigned variable. We can reduce the branching factor by fixing the order by which we assign values to variables. The goal test is that the number of assigned variables is equal to the number of variables. The step cost is unitary.

**Remark**: every solution is at depth $n$ of the search tree (where $n$ is the number of varibales of the CSP). Then, since we use unitary step cost, every solution has the same cost (we just need to find one). Then, we can use **DFS with backtracking** (the DFS recursive implementation) to solve the problem.

The algorithm can be implemented on paper as follows:
1. Inside every node we put the current assignment $x_1 = v_1, x_2 = v_2, ...$, next to the node we put the domains of the variables if they change during the search.
2. We start from the root node with represents the empty assignment.
3. We run a DFS, for every node (according to the depth), we choose which variable to assign and try every possible assignment, until either we reach a complete and consistent assignment (and so we stop) or a in inconsistent assignment/assignment where some variable has empty domain (in that case we go back to the parent).

We can improve the backtrcking search by exploiting the factored representation.

#### Forward checking

It is a technique for reducing the domains of varibales during the search, eliminating inconsistent assignments:
1. When we assign a variable $x$;
2. We consider every unassgined variable $y$ which is in a constraint $C$ with $x$;
3. We remove the values of $y$ from $D_y$ which do not satisfy $C$ (given the value of $x$).

We can do forward checking right after the assignment in the backtracking search.

Let $n$ be the number of variables, $s$ the maximum number of constraints that involve any given variable, $d$ the maximum size of a domain. Then FC is: $O(n s d)$.

#### Heuristics for choosing the order of assignment of variables

- **Minimum Remaining Values** (**MRV**) heuristic:
choose the variable with the fewest legal values ramaining in its domain.
The reationale is: if we have to fail, it is better to fail fast. And, since at the end we have to assign a value to every variable, we should start from those that are most likely to lead to fail (thos with less legal values).

---

- **Degree** heuristic:
choose the variable which is involve in the highest number of constraints  with unassigned variables (the degree of the constraints graph).

#### Heuristics for choosing the value to assign to $x$

- **Least-constraining-value** heuristic:
choose the value which leads to the minimum reduction of the domains of unassigned values. At the end we want to find a solution, so it is better to consider more promising values first.

#### Arc consistency

Given a CSP with binary constraints, we say that the current assignment is **arc consistent** iff:
- for every constraint $C_j$ let $S_j = (X_{h_1}, X_{h_2})$,
>> then for every $v_1 \in D_{h_1}$, there exists $v_2 \in D_{h_2}$ s. t. $(v_1, v_2) \in R_j$;
>> and, for every $v_2 \in D_{h_2}$, there exists $v_1 \in D_{h_1}$ s. t. $(v_1, v_2) \in R_j$.

We can enforce arc consistency through the **AC3** algorithm:
1. Initialize an empty set;
2. For every constraint involving $x_i$ and $x_j$, add $x_i \rightarrow x_j$ and $x_j \rightarrow x_i$ to the set;
3. While the set is not empty;
> 4. Remove the first (according to some ordering) value $x_i \rightarrow x_j$ from the set:
> 5. Check that for every value of $x_i$ in $D_i$ there is an appropriate value in $x_j$, otherwise remove the value from $D_i$;
> 7. If $D_i = \emptyset$: return failure;
> 6. If $D_i$ has been modified add all $x_k \rightarrow x_i$ to the set.

Each arc is inserted in the set at most $d$ time, hence, the complexity of AC3 is $O(d n s d^2) = O(n s d^3)$.

**AC3** is more powerful than forward checking.

We can run AC3 inside the bracktracking algorithm after every assignment (and at the beginning).

AC3 does not detect all the inconsistencies among binary constraints (for example 3 variables must be all different but they all have the same domain with two values: this is not satisfiable but AC3 can't detect it).

---

## Local search

**Optimization** is the problem of coosing the best option from a set of options.
Search algorithms solve optimization problems by maintaining a set of different paths (options) that they are simultaneously exporing.
Local search algorithms maintain a single state (option) and search by moving to a neighboring state.

To formulate a local search problem we need to define:
- a state space;
- a neighbor relation;
- an objective function (to minimize or maximize).

Local search algorithms can get stuck in local optima.

We can formulate CSPs as local search problem: the state space is the set of complete assignments, the neighbor function is modifying the assignment to each variable, for every variable, the objective function is the number of unsatisfied constraints, and we want to minimize it.

## Logic

### Model checking

We want to prove that a logical sentence entails another by checking that in all the models where the first sentence is true, the second is also true.

#### Reasoning with truth tables

We have to compute a thruth table of size $O(2^n M)$ where $n$ is the number of variables and $M$ is the number of sentences.

#### Propositional satisfiabiliy

The goal is to verify if a set of logical sentences is or is not satisfiable.

- **DPLL**

1. We put every formula in CNF.
2. We stop when either all clause are satisfied or one clause is falsified.
3. At every step we assign a thruth value to a variable. In general we have to branch and consider both the thruth values.
4. Except for: **pure literals** (they appear always positive or always negative in the current set of sentences) and we satisfy them; or **unit clauses** (which must be satisfied).

---

We represent the algorithm with a table, where in each row we have the current set of sentences (considering the assignments made). On the right we write the applied criteria; on the left we write the literal that we made true in the last step.
We can call three blocks of column of the table: "Assignment", "Clauses", and "Rule".

We can use popositional satisfiability to check entailment thanks to the refutation theorem: $\alpha \models \beta \iff \alpha \land \lnot \beta$ is unsatisfiable.

### Theorem proving

In theorem proving we use an algorithm $\mathcal{A}$ which builds a proof leading from $\alpha$ to $\beta$ and we write $\alpha \vdash_\mathcal{A} \beta$.

An algorithm is **sound** if:
- $\alpha \vdash_\mathcal{A} \beta \implies \alpha \models \beta$.

An algorithm is **complete** if:
- $\alpha \models \beta \implies \alpha \vdash_\mathcal{A} \beta$.

#### Resolution

Resolution is applied to sentences in CNF. It proves that $KB \models \alpha$ by showing that $KB \land \lnot \alpha$ is unsatisfiable.

The inference rule is the following: from $C_1$, $C_2$ s.t. $l_1 \in C_1$, $\lnot l_1 \in C_2$, we resolve $C_3 = (C_1 \setminus \{ l_1 \}) \cup (C_2 \setminus \{ \lnot l_1 \})$.

When we reach the empty clause, we can conclue that the set of sentences is unsatisfiable.

When applying it on paper:
1. We add all the formulas one above the other (in CNF) and we draw an horizontal line after the last;
2. We compare every pair of formulas and we try to resolve them; we add the results below the horizontal line; when we have compared all the formulas above the horizontal line, we draw another horizontal line;
3. We keep comparing all the sentences in the last block (blocks are identified by horizontal lines) with all the sentences in the other blocks; when we stop adding new sentences, we have reached the fixed point.

The resolution rule is **sound** and **complete**.

There are some variations of the standard resolution rule:
- **unit resolution**: at least one parent clause is a unit clause (complete only for Horn clauses);
- **input resolution**: at least one parent clause is a member of the initial set (complete only for Horn clauses);

---

- **linear resolution**: at least one parent is a member of the initial set or one parent is an ancestor of the other parent (it is complte).

A **horn clause** is a special sentence with the structure:
- (conjunction of symbols) $\rightarrow$ symbol, or;
- symbol.

Another characherization is:
- a **horn clause** is a sentence which in CNF has **at most one positive** literal;
- a **definite clause** is a sentence which is CNF has **exactly one positive** literal.

Horn clauses represent:
- **rules**: $C \land D \rightarrow B$;
- **facts**: $C$;
- **goals**: $A \land B \rightarrow \bot$;
- **empty clause**: $\top \rightarrow \bot$.

#### Forward chaining

**Forward chaining** considers **definite clauses** and applies modus ponens to generate new facts: given $X_1 \land ... \land X_n \rightarrow Y$ and $X_1 \land ... \land X_n$, infer $Y$.
Forward chaining keeps applying this rule, adding new facts, until nothing more can be added.

We can represent the set of clauses used in forward chaining with an AND-OR graph:
- normal predecessors $p_1, ..., p_n$ of $s$ represent that $p_1 \rightarrow s, ..., p_n \rightarrow s \in KB$;
- multiple predecessors whose $p_1, ..., p_n$ of $s$ whose arrows are linked by an arc representf that $p_1 \land .... \land p_n \implies s \in KB$.

The algorithm works as follows:
- we keep two arrays: count and inferred, and a queue;
- count is initialized (for every clause) with the number of symbols in the premise of that clause;
- inferred is initialized to false for every clause;
- we put onto the queue all the unit clauses;
- while the queue is not empty;
> - we pop an element from the queue;
> - if this element was not already inferred:
>> - we set inferred to true and decrement the count of all the clauses which have this symbol in their premise;
>> - if count gets to 0 for a clause during this step, we push it onto the queue.

---

We iterate until the formula that we want to entail becomes inferred or we empty the queue.

Forward chaining is **sound** and **complete** for KBs compose of definite clauses.
The soundness follows from the soundness of modus ponens, the completeness follows from the fact that we reach a fixed point from which we can't derive no new formula.

#### Backward chaining

**Backward chaining** works like forward chaining but backward.

When we apply it, we can build a search tree, starting from the symbol that we want to prove and going back through implications. Each node is known as a subgoal.

Furthermore, we want to avoid loops by checking if the new subgoal is already in the goal stack, and avoid repeated work checking if new subgoal has already beeen proved true, or has already failed.

## Planning

The implicit assumptions of planning:
- **Unique Name Assumption** (**UNA**): different **constants** (not variables) always denote different obejcts;
- **Domain Closure Assumption** (**DCA**): the environment includes only those objects that are denoted by a constant;
- **Closed World Assumption** (**CWA**): all literals that are not explicitly mentioned in the description of the state are assumed to be false.

### Planning problem formulation

A **STRIPS planning problem** is a tuple $(Cond, Actions, Init, Goal)$
where
- $Cond$ is a finite set of **ground** (no variables), **functionless** (no functions), **atomic** (no connectives) formulas (e. g. $Q(c_1, ..., c_n)$ where $c_i$ is a constant);
- a $state$ is a conjuenction of conditions (the elements of $Cond$) (e. g. $S = \{ p_1, ..., p_n \}$ where $p_i$ are conditions);
- $Actions$ is a finite set of actions, each action is a pair $a = (Precond, Effect)$;
- action $a$ is **applicable** in state $S$ iff $Precond \subset S$;
- $Effect = Effect^+ \cup Effect^-$;
- $result(S, a) = (S \setminus Effect^-) \cup Effect^+$;
- $Init \subset Cond$ is the initial state;
- $Goal$: specifies the goal condition, it is a set of **functionless atomic** formulas (they can have variables); a state satisfies the goal condition if there is at least one assignment to the variables inside the conditions of $Goal$ s. t., after the assignment $Gaol \rvert_{\underline{x} = \underline{a}} \subset S$.

---

A **solution** in a planning problem is a sequence of actions leading to a goal state (it is also known as a plan).

**PDDL** $\equiv$ **STRIPS + $\lnot$** in preconditions and goals.

### Solving planning problems

#### Forward planning

We do a search in the state space from the initial state to a state satisfying the goal. It is formulated as a classical search problem.

#### Backward planning

We do a search in the **goal space** (goals are not states) back to the initial state.

We say that an action $a$ is **relevant** for a goal $G$ if at least one of the positive effects of $a$ satisfies $G$.

We say that an action $a$ is **inconsistent** for a goal $G$ if at least one of the effects in the delete list of $a$ is a subgoal of $G$.

Given a goal $G$ and an action $a$ **relevant and consistent** (not inconsistent) for $G$, we define the **regression of goal $G$ through $a$** as: a goal $G'$ which contains the precondtions of $a$ and all the subgoals of $G$ which are not in the add list of $a$.

During the search we keep applying regressions until we find a regressed goal which is satisfied by the initial state.

Backward planning is usually more efficient than forward planning (because we have a smaller branching factor).

#### SAT planning

In SAT planning a planning problem is solved by reducing it to model checking. In particular incremental model checking.
Starting from a PDDL representation of the agent's initial state and actions (the knowledge base KB) and of the goal $\gamma$, the plan is built as follows:
- SATPlan tries to build a plan of length $L$ starting with $L = 0$ and then incrementing $L$ by 1 at each attempt (a strategy analogous to iterative deepening search strategy);
- for every value of $L = 0, 1, 2, ...$ a (partially) different propositional representation of $KB \land \gamma$ is generated and the attempt to build a model of such representation is carried out (for example using the DPLL algorithm);
- if for some value of $L$ a model of $KB$ is found, a plan of length $L$ is extracted from the model;
- if the available time and/or space resources are xhausted before a model is found, the planning effort fails.

---

The symbols in the propositional model are:
- **one symbol for every $Cond$** (so if we have a predicate which takes a variable, we need one symbol for each possible variable that can be put inside that predicate);
- **one symbol for every instance of an action** (we have variables also in actions).

We say that actions are **reified** (they are represented as propositional symbols).

Furthermore, every symbol has a superscript $t$ with values from $0$ to $L$, hence, actually, for every symbol identified in the previous step, we have $L + 1$ symbols.

The sentences in the propositional model are:
- a sentence for the **initial state**, **important** remember that in propositional logic the CWA doesn't hold, hence we need to specify at time $t = 0$ all the predicates which are true and all the ones that are false;
- a sentence for the **goal**: it is a disjunction of the possible ways in which we can achieve the goal (if the goal includes variables); it must be satisfied at time $t = L$;
- sentences for the **preconditions** of an action (**preconditions axioms**): $a^t \rightarrow p^t \land ... \land q^t$;
- sentences to link $p^t$ and $p^{t+1}$ (**fluent axioms**), with the sturcture: $p^(t+1)$ is true iff $p^t$ was true and no action which makes $p$ false has been applied or an action which makes $p$ true has been applied;
- sentences to force the plan to execute one action at the time (**actions exclusion axioms**): they are of the form $\lnot a^t_i \lor \lnot a^t_j$ for all $t$, for all $i \neq j$.

## Uncertainty

### Bayesian network

A **Bayesian network** is a data structure that represents the dependencies among random variables. 

- It is a Directed Acyclic Graph (DAG);
- Each node represents a random variable;
- A direct edge from X to Y means X is a parent of Y;
- **Each node X has probability distribution P(X|Parents(X))**.

The **joint distribution** "induced" by a Bayesian network is **defined** as:
$$
P(X_1, ..., X_n) = \prod_i P(X_i | Parents(X_i)) \text{.}
$$

#### Inference in bayesian networks

Given a set of evidence variables $E$ and the variable $X$ in which we are interested, we want to compute the probability distribution $P(X | e)$ (where $e$ is an assignment to the variables in $E$).

---

We can combine the probability distributions that are represented by the Bayesian network through:

- **Chain rule**
$$
P(X_1, ..., X_n, Y_1, ..., Y_m | W_1, ..., W_l) = P(X_1, ..., X_n | Y_1, ..., Y_m, W_1, ..., W_l) P(Y_1, ..., Y_m | W_1, ..., W_l)
$$

- **Marginalization**
$$
P(X_1, ..., X_n | W_1, ..., W_l) = \sum_{y_1, ..., y_m} P(X_1, ..., X_n, Y_1 = y_1, ..., Y_m = y_m | W_1, ..., W_l) 
$$
(we can use marginalization and the chain rule together).

**When can X influence Y?**

|                                 | Can X influence Y?     |
|---------------------------------|------------------------|
| $X \rightarrow Y$               | Yes (causal)           |
| $X \leftarrow Y$                | Yes (evidential)       |
| $X \rightarrow W \rightarrow Y$ | Yes (causal chain)     |
| $X \leftarrow W \leftarrow Y$   | Yes (evidential chain) |
| $X \leftarrow W \rightarrow Y$  | Yes                    |
| $X \rightarrow W \leftarrow Y$  | No                     |

We say that a **trail** $X_1, ..., X_k$ is active if **it has no v-structure**.

**When can X influence Y given Z?**

|                                 | Can X influence Y given Z?                                                                       |                 |
|---------------------------------|--------------------------------------------------------------------------------------------------|-----------------|
|                                 | $W \not \in Z$                                                                                   | $W \in Z$       |
| $X \rightarrow W \rightarrow Y$ | Yes                                                                                              | No ($W$ blocks) |
| $X \leftarrow W \leftarrow Y$   | Yes                                                                                              | No ($W$ blocks) |
| $X \leftarrow W \rightarrow W$  | Yes                                                                                              | No ($W$ blocks) |
| $X \rightarrow W \leftarrow Y$  | Yes, but only if one successor of $W$ is in $Z$ (then we can reach $W$ with an evidential chain) | Yes             |

We can reformulate the concept of active trail: a trail $X_1, ..., X_k$ is **active given $Z$** if, for any v-structure $X_{i-1} \rightarrow X_i \leftarrow X_{i+1}$, $X_i$ or one of its descendent is in $Z$ and no other $X_i$ in v-structures is in $Z$.

#### Approximate inference

We can do approximate inference through sampling.

---

That is, we sample from the distribution of nodes with no predecessors, and then we use the sampled values to sample from conditional distributions.

In **rejection sampling** to approximate a conditional distribution we do standard sampling as we described before and then we consider only the samples "which respect the condtion".

If the evidence we are looking for is a fairly unlikely event, then we're going to reject many samples. This can become quite inefficient since we might need to generate a huge number of samples.