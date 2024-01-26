---
theme: summary
---
# Automatic Differentiation (AD)

<div class="author">

Cristiano Migali

</div>

**Automatic differentiation** is a technique which allows to evaluate the **exact** partial derivatives of a function specified by a computer program at **a given input**.
In order to perform AD on a function
$$
f : \mathbb{R}^n \rightarrow \mathbb{R}^m
$$
computed by a program, $f$ has to be represented as a **Wengert list**.

- A **Wengert list** for a function
$$
f : \mathbb{R}^n \rightarrow \mathbb{R}^m
$$

$$
\begin{bmatrix} x_1 \\ ... \\ x_n \end{bmatrix} \mapsto
\begin{bmatrix} y_1 \\ ... \\ y_m \end{bmatrix}
$$
> computed by a program, is a list of variables:
$$
(v_{-(n-1)}, ..., v_0, v_1, ..., v_l)
$$
> with $l \in \mathbb{N}$, $l \geq m$ s.t.
> - $v_{i-n} = x_i$ for every $i \in \{ 1, ..., n \}$;
> - $v_i = g_i(v_{-(n-1)}, ..., v_{i-1})$ for every $i \in \{ 1, ..., l \}$, where $g_i$ is a "simple" function for which we know the derivative;
> - $y_i = v_{l-m+i}$ for every $i \in \{ 1, ..., m \}$.

We can represent $f$ also with a **computational graph**, which is a DAG strictly related to the Wengert list where we have $l+n$ nodes, each one containing an element of the list $v_i$. There is an edge from node $v_i$ to node $v_j$ iff the expression of $v_j$ contains $v_i$.
Given a computational graph, we can introduce the concept of **derivative on the edge**: we can associate $\frac{\partial v_j}{\partial v_i}$ to every edge from $v_i$ to $v_j$.

## Forward Mode AD

Fix an input variable $x_i$ with $i \in \{ 1, ..., n \}$. Then we introduce the notation $\dot{v}_j$ with the meaning of
$$
\dot{v}_j = \frac{\partial v_j}{\partial x_i} \text{.}
$$

The process of computing the derivatives $\dot{v}_j$ from $j = -(n-1)$ to $j=l$ is known as **Forward Mode** (**FM**) automatic differentiation.

---

By how the Wengert list is defined, $\dot{v}_j$ depends only on $v_{-(n-1)}, ..., v_{j-1}$ and $\dot{v}_{-(n-1)}$, ..., $\dot{v}_{i-1}$, which are the values already computed at the $j$-th step.
In particular, let $P_j$ be the set of predecessors of $v_j$ in the computational graph of $f$, then
$$
\frac{\partial v_j}{\partial x_i} = \sum_{p \in P_j} \frac{\partial v_j}{\partial p} \frac{\partial p}{\partial x_i} \text{.}
$$

Of course to get the partial derivatives w.r.t. a different input, we have to repeat the process starting from $\dot{v}_{-(n-1)}$.
The process of computing all the partial derivatives $\dot{v}_{-(n-1)}$, ..., $\dot{v}_{l}$ for a given input is known as a **sweep**. The computational complexity of a sweep is the same as the one of executing the function.

To get the full jacobian of the function we need to perform $n$ sweeps in FM AD.

## Backward Mode AD

## AD Tricks
### Matrix free computation of $J \underline{r}$ through FM AD

Said $J$ the jacobian of $f$ at $\underline{x}_0 \in \mathbb{R}^n$, and $\underline{r} \in \mathbb{R}^n$ a vector, FM allows the **matrix free** (_that is, without having to explicitly compute $J$_) computation of the product $J \underline{r}$.
Let's see how this is achieved:
let
$$
f : \mathbb{R}^n \rightarrow \mathbb{R}^m
$$
$$
\begin{bmatrix} x_1 \\ ... \\ x_n \end{bmatrix} \mapsto \begin{bmatrix} y_1 \\ ... \\ y_m \end{bmatrix} \text{,}
$$

$$
\underline{x}_0 = \begin{bmatrix} x_{1,0} \\ ... \\ x_{n,0} \end{bmatrix} \in \mathbb{R}^n,
J = \begin{bmatrix}
\frac{\partial y_1}{\partial x_1}(\underline{x}_0) & ... & \frac{\partial y_1}{\partial x_n}(\underline{x}_0) \\
... & ... & ... \\
\frac{\partial y_m}{\partial x_1}(\underline{x}_0) & ... & \frac{\partial y_m}{\partial x_n}(\underline{x}_0)
\end{bmatrix} \in \mathbb{R}^{m \times n} ,
\underline{r} = \begin{bmatrix} r_1 \\ ... \\ r_n \end{bmatrix} \in \mathbb{R}^n \text{.}
$$

Now consider the function
$$
h : \mathbb{R} \rightarrow \mathbb{R}^n \text{ defined as }
$$
$$
h(t) = \underline{r}t + \underline{x}_0 \text{.}
$$

Observe that
$$
\frac{d}{dt}h(t) = \underline{r} \text{ and } h(0) = \underline{x}_0 \text{.}
$$

---

Let
$$
g : \mathbb{R} \rightarrow \mathbb{R}^m
$$
$$
t \mapsto \begin{bmatrix} z_1 \\ ... \\ z_m \end{bmatrix} \text{ defined as }
$$
$$
g(t) = f(h(t)) \text{.}
$$

As we know, since $g$ has a single input, we can compute its jacobian at $t = 0$ with **one single sweep of FM**. Furthermore, by the chain rule,
$$
Dg(0) = Df(h(0)) \cdot Dh(0) = Df(\underline{x}_0) \cdot \underline{r} = J \underline{r}
$$
which is exactly what we were looking for.
Observe that **computing $J$ explicitly** would have required **$n$ sweeps of FM**.
But one could say: maybe computing one sweep of FM on $g$ has the same cost of computing $n$ sweeps of FM on $f$. We will see that it is not the case, one sweep of FM on $g$ has the same cost of one sweep on $f$. Furthermore it is not necessary to compute $g$ explicitly (we used it only for proving the theoretical result): we just need to "seed" (_we will specify what we mean in a moment_) the FM on $f$ with $\underline{r}$ instead of $\underline{e}_i$.

**First remark**: as the dot notation for derivatives suggests, FM is completely agnostic w.r.t. the variable by which we are differentiating. That is, assume that the variable $v_1$ is the sum of the inputs $v_{-1}$ and $v_0$. Then $\dot{v}_1 = \dot{v}_{-1} + \dot{v}_0$. Now the fact that $\dot{v}_{1} = \frac{\partial v_1}{\partial v_{-1}}$ or $\dot{v}_1 = \frac{\partial v_1}{\partial v_0}$ depends only on the values that we have previously assigned to $\dot{v}_{-1}$ and $\dot{v}_0$:
- if $\dot{v}_{-1} = 1$ and $\dot{v}_0 = 0$, then $\dot{v}_1 = \frac{\partial v_1}{\partial v_{-1}}$;
- otherwise, if $\dot{v}_{-1} = 0$ and $\dot{v}_0 =1$, then $\dot{v}_1 = \frac{\partial v_1}{\partial v_0}$.

These values are what we call the **seed**. In the example we compared the seeds $\underline{e}_1$ and $\underline{e}_2$.

**Second remark**: let $[v_{-(n-1)}, ..., v_0, v_1, ..., v_l]$ be a Wengert list for $f$. Then, since $g(t) = f(r_1 t + x_{1,0}, ..., r_n t + x_{n,0})$, the Wengert list for $g$ has:
- one input: $w_0 = t$;
- $l + 2n$ non-input variables:
$$
\begin{matrix}
w_1 = r_1 w_0 \text{,} \\
w_2 = w_1 + x_{1,0} = x_1 = v_{-(n-1)} \text{,} \\
... \text{,} \\
w_{2n-1} = r_n w_0 \text{,} \\
w_{2n} = w_{2n-1} + x_{n,0} = x_n = v_0 \text{,} \\
w_{2n+i} = v_i \text{ for } i \in \{ 1, ..., l \} \\
\text{ where we substitute } v_{-(n-j)} = x_j \text{ with } w_{2j} = x_j \\
\text{ in the expression of } v_i \text{.}
\end{matrix}
$$

---

Then, when we apply FM on $g(t)$ for $t = 0$:
1. $w_0 = t = 0$ implies $w_{2i-1} = 0$ for $i \in \{ 1, ..., n \}$ and so $w_{2i} = x_{i,0}$;
2. $\dot{w}_0 = 1$ implies $\dot{w}_{2i-1} = r_i$ for $i \in \{ 1, ..., n \}$, and so $\dot{w}_{2i} = \dot{w}_{2i-1} + 0 = r_i$;
3. By how we have defined $w_{2n+i}$ for $i \in \{ 1, ..., l \}$, remembering that $w_{2i} = x_i$, the remaining part of the computation is equivalent to applying the FM of $f$ with the seed
$$
\dot{\underline{x}} = \begin{bmatrix}
\dot{x}_1 \\
... \\
\dot{x}_n
\end{bmatrix} = \begin{bmatrix}
r_1 \\
... \\
r_n
\end{bmatrix} \text{.}
$$

---

## A more formal approach to Wengert lists

(_What follows is my reinterpretation of Wengert lists with the purpose of proving the "fundamental recursive equations" of FM and BM AD [I failed with BM :D]_).
- A **Wengert list** is a tuple $(n, m, l, \mathcal{P}, \Phi)$ where:
> - $n, m, l \in \mathbb{N}^+$, $l \geq n+m$;
> - $\mathcal{P}$ is a list of $l-n$ sets $P_{n+1}, ..., P_l$ s.t. $\emptyset \neq P_i \subseteq \{ 1, ..., i-1 \}$ for every $i \in \{ n+1, ..., l \}$ and $\cup_{i=l-m+1}^l P_i \cap \{ l-m+1, ..., l \} = \emptyset$;
> - $\Phi$ is a list of $l-n$ "elementary" (_the definition of which function is elementary and which is not depends on the context, anyways, it doesn't affect the treatment_) functions
$$
\phi_i : \mathcal{D}_i \subseteq \mathbb{R}^{|P_i|} \rightarrow \mathbb{R} \text{ with } i \in \{ n+1, ..., l \} \text{.}
$$

Each Wengert list represents a function
$$
\underline{g} : \mathcal{D} \subseteq \mathbb{R}^n \rightarrow \mathbb{R}^m \text{.}
$$

The semantics is the following, let:
$$
\begin{matrix}
f_1(v_1, ..., v_n) = v_1 \text{;} \\
... \\
f_n(v_1, ..., v_n) = v_n \text{;} \\
f_{n+1}(v_1, ..., v_n) = \phi_{n+1}(f_{P_{n+1}[1]}(v_1, ..., v_n), ..., f_{P_{n+1}[|P_{n+1}|]}(v_1, ..., v_n)) \text{;} \\
... \\
f_l(v_1, ..., v_n) = \phi_l(f_{P_l[1]}(v_1, ..., v_n), ..., f_{P_l[|P_l|]}(v_1, ..., v_n))
\end{matrix}
$$
where $P_i[j]$ is the $j$-th element of $P_i$ according to the natural ordering.
Then
$$
\underline{g}(v_1, ..., v_n) = \begin{bmatrix}
g_1(v_1, ..., v_n) \\
... \\
g_m(v_1, ..., v_n)
\end{bmatrix} = \begin{bmatrix}
f_{l-m+1}(v_1, ..., v_n) \\
... \\
f_l(v_1, ..., v_n)
\end{bmatrix} \text{.}
$$

To simplify what follows in the treatment, let:
$$
\hat{\phi}_i(v_1, ..., v_{i-1}) = \phi_i(v_{P_i[1]}, ..., v_{P_i[|P_i|]}) \text{ for } i \in \{ n+1, ..., l \} \text{.}
$$

It follows that:
$$
f_i(v_1, ..., v_n) = \hat{\phi}_i(f_1(v_1, ..., v_n), ..., f_{i-1}(v_1, ..., v_n)) \text{ for } i \in \{ n+1, .., l \} \text{.}
$$

We want to compute $D_i g_j(v_1, ..., v_n)$ for $i \in \{ 1, ..., n \}$, $j \in \{ 1, ..., m \}$. We will do so through a dynamic programming approach. The recursive equation that we will solve depends on the kind of AD that we'll implement.

---

### Forward mode recursive equation

Let $i \in \{ 1, ..., n \}$, $j \in \{ n+1, ..., l \}$. Then, from the chain rule (_see Theorem 2-9 in Spivak's Calculus on Manifolds_):
$$
D_i f_j(v_1, ..., v_n) = \sum_{k=1}^{j-1} D_k \hat{\phi}_j(f_1(v_1, ..., v_n), ..., f_{j-1}(v_1, ..., v_n)) D_if_k(v_1, ..., v_n) \text{.}
$$

Let $j \in \{ 1, ..., n \}$ instead, then:
$$
D_i f_j(v_1, ..., v_n) = \begin{cases}
1 \text{ if } i = j \\
0 \text{ otherwise }
\end{cases} \text{.}
$$

Finally, observe that
$$
D_k \hat{\phi}_j(v_1, ..., v_{j-1}) \neq 0 \text{ implies } k \in P_j \text{.}
$$
Hence, we can rewrite the recursive equation as:
$$
D_i f_j(v_1, ..., v_n) = \sum_{k \in P_j} D_k \hat{\phi}_j(f_1(v_1, ..., v_n), ..., f_n(v_1, ..., v_n)) D_i f_k(v_1, ..., v_n) \text{.}
$$

### Backward mode recursive equation

I failed in the derivation of the recursive equation for BM AD. I developed a "supporting framework" which I think is inconclusive since it doesn't capture the structure of the computational graph and doesn't make it easy to prove the desired result. I will write it down here anyway. (_At the end I will put the result I wished to prove_).

We will assume that the function represented by the Wengert list has just one output ($m = 1$). Since, BM AD works "one output at the time", this is without loss of generality.

Let's define a family of functions $\{ \phi^*_{i,j}(v_1, ..., v_j) \}$ with $i, j \in \{ n, ..., l \}$, $i \leq j$ with a set of recursive equations:
$$
\tag{1}\label{1} \phi_{i,i}^*(v_1, ..., v_i) = v_i \text{ for every } i \in \{ n, ..., l \} \text{;}
$$

$$
\tag{2}\label{2} \phi^*_{i,i+1}(v_1, ..., v_i) = \hat{\phi}_{i+1}(v_1, ..., v_i) \text{ for every } i \in \{ n, ..., l-1 \} \text{;}
$$

$$
\tag{3}\label{3} \phi^*_{j,i}(v_1, ..., v_j) = \phi^*_{j+1,i}(v_1, ..., v_j, \hat{\phi}_{j+1}(v_1, ..., v_j))
$$

$$
\text{ for every } j \in \{ n, ..., l-1 \}, i \in \{ j+1, ..., l \} \text{.}
$$

---

> **Theorem (*)**: Let $j \in \{ n, ..., l-1 \}$, $i \in \{ j+1, ..., l \}$ then
$$
\phi_{j,i}^*(v_1, ..., v_j) = \hat{\phi}_i(v_1, ..., v_j, \phi^*_{j,j+1}(v_1, ..., v_j), ..., \phi^*_{j,i-1}(v_1, ..., v_j)) \text{.}
$$

> **Proof**: base case, let $i-j = 1$, the result follows from $(2)$.

> Inductive step: let $i-j > 1$ and assume that the result is true if $n-m < i-j$ for $m \in \{ n, ..., l-1 \}, n \in \{ m+1, ..., l \}$.

$$
\phi^*_{j,i}(v_1, ..., v_j) =^{(3)} \phi_{j+1,i}(v_1, ..., v_j, \hat{\phi}_{j+1}(v_1, ..., v_j)) =^{\text{ind. hp.}}
$$

$$
=^{\text{ind. hp.}} \hat{\phi}_i(v_1, ..., v_j, \hat{\phi}_{j+1}(v_1, ..., v_j), \phi_{j+1,j+2}^*(v_1, ..., v_j, \hat{\phi}_{j+1}(v_1, ..., v_j)),
$$

$$
..., \phi^*_{j+1,i-1}(v_1, ..., v_j, \hat{\phi}_{j+1}(v_1, ..., v_j))) =^{(2)}
$$

$$
=^{(2)} \hat{\phi}_i(v_1, ..., v_j, \phi^*_{j,j+1}(v_1, ..., v_j), \phi_{j+1,j+2}^*(v_1, ..., v_j, \hat{\phi}_{j+1}(v_1, ..., v_j)),
$$

$$
..., \phi^*_{j+1,i-1}(v_1, ..., v_j, \hat{\phi}_{j+1}(v_1, ..., v_j))) =^{(3)}
$$

$$
=^{(3)} \hat{\phi}_i(v_1, ..., v_j, \phi^*_{j,j+1}(v_1, ..., v_j), \phi^*_{j,j+2}(v_1, ..., v_j), ..., \phi^*_{j,i-1}(v_1, ..., v_j)) \text{.}
$$

> **Theorem (<3)**: Let $j \in \{ n, ..., l-2 \}$, $k \in \{ j+1, ..., l-1 \}$, $i \in \{ i+1, ..., l \}$ then
$$
\phi_{j,i}^*(v_1, ..., v_j) = \phi_{k,i}^*(v_1, ..., v_j, \phi_{j,j+1}^*(v_1, ..., v_j), ..., \phi_{j, k}^*(v_1, ..., v_j)) \text{.}
$$

> **Proof**: base case, let $k-j = 1$:
$$
\phi_{j,i}^*(v_1, ..., v_j) =^{(3)} \phi_{j+1,i}^*(v_1, ..., v_j, \hat{\phi}_{j+1}(v_1, ..., v_j)) =^{(2)}
$$

$$
=^{(2)} \phi_{j+1,i}^*(v_1, ..., v_j, \phi_{j,j+1}^*(v_1, ..., v_j)) =^{k=j+1} \phi^*_{k,i}(v_1, ..., v_j, \phi_{j,k}^*(v_1, ..., v_j)) \text{.}
$$

> Inductive step: let $k-j > 1$, then:
$$
\phi_{j,i}^*(v_1, ..., v_j) =^{\text{ind. hp.}} \phi_{k-1, i}^*(v_1, ..., v_j, \phi_{j,j+1}^*(v_1, ..., v_j), ..., \phi_{j,k-1}^*(v_1, ..., v_j)) =^{(3)}
$$

$$
=^{(3)} \phi_{k,i}^*(v_1, ..., v_j, \phi_{j,j+1}^*(v_1, ..., v_j), ..., \phi_{j,k-1}^*(v_1, ..., v_j),
$$

$$
\hat{\phi}_k(v_1, ..., v_j, \phi_{j,j+1}^*(v_1, ..., v_j), ..., \phi_{j,k-1}^*(v_1, ..., v_j))) =^{(*)}
$$

$$
=^{(*)} \phi_{k,i}^*(v_1, ..., v_j, \phi_{j,j+1}^*(v_1, ..., v_j), ..., \phi_{j,k}^*(v_1, ..., v_j)) \text{.}
$$

---

> **Theorem (<>)**: $\phi_{j,l}^*(f_1(v_1, ..., v_n), ..., f_j(v_1, ..., v_n)) =$ $= f_l(v_1, ..., v_n) = g(v_1, ..., v_n)$ for every $j \in \{ n, ..., l \}$.

> **Proof**: base case, let $j = l$:
$$
\phi_{l,l}^*(f_1(v_1, ..., v_n), ..., f_l(v_1, ..., v_n)) =^{(1)} f_l(v_1, ..., v_n) = g(v_1, ..., v_n) \text{.}
$$

> Inductive step: let $j < l$:
$$
\phi_{j,l}^*(f_1(v_1, ..., v_n), ..., f_j(v_1, ..., v_n)) = \phi_{j+1,l}^*(f_1(v_1, ..., v_l), ..., f_j(v_1, ..., v_n),
$$

$$
\hat{\phi}_{j+1}(f_1(v_1, ..., v_l), ..., f_j(v_1, ..., v_n))) =
$$

$$
= \phi_{j+1,l}^*(f_1(v_1, ..., v_n), ..., f_{j+1}(v_1, ..., v_n)) =^{\text{ind. hp.}} f_l(v_1, ..., v_n) \text{.}
$$

Let $i \in \{ 1, ..., l \}$, we define the set of **successors** of $v_i$ as
$$
S_i = \{ j \in \{ 1, ..., l \} | i \in P_j \} \text{.}
$$

_The desired result I wished to prove is the following_:
$$
D_j \phi_{j,l}^*(v_1, ..., v_j) = \sum_{k=j+1}^{l-1} D_j \phi_k(v_1, ..., v_j, \phi_{j,j+1}^*(v_1, ..., v_j), ..., \phi_{j,k-1}^*(v_1, ..., v_j)) \cdot
$$

$$
\cdot D_k \phi_{k,l}^*(v_1, ..., v_j, \phi_{j,j+1}^*(v_1, ..., v_j), ..., \phi_{j,k}^*(v_1, ..., v_j)) =
$$

$$
= \sum_{k \in S_j} D_j \phi_k(v_1, ..., v_j, \phi_{j,j+1}^*(v_1, ..., v_j), ..., \phi_{j,k-1}^*(v_1, ..., v_j)) \cdot
$$

$$
\cdot D_k \phi_{k,l}^*(v_1, ..., v_j, \phi_{j,j+1}^*(v_1, ..., v_j), ..., \phi_{j,k}^*(v_1, ..., v_j)) \text{.}
$$

(_In particular what has to be proven is the first equality; I believe it holds, but I don't know how to prove it_).