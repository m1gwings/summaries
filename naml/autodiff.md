---
theme: summary
---
# Automatic Differentiation (AD)

<div class="author">

Cristiano Migali

</div>

---

## Wengert lists

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

**Remark**: the way in which the functions in the list are composed, which is described by $\mathcal{P}$, can be represented through the so-called **computational graph**. In particular, a computational graph is a DAG which represents a function as the composition of elementary functions. The nodes of the computational graph are the variables $v_1, ..., v_l$, and $v_i$ is a predecessor of $v_j$ iff $i \in P_j$.

To simplify what follows in the treatment, let:
$$
\hat{\phi}_i(v_1, ..., v_{i-1}) = \phi_i(v_{P_i[1]}, ..., v_{P_i[|P_i|]}) \text{ for } i \in \{ n+1, ..., l \} \text{.}
$$

---

It follows that:
$$
f_i(v_1, ..., v_n) = \hat{\phi}_i(f_1(v_1, ..., v_n), ..., f_{i-1}(v_1, ..., v_n)) \text{ for } i \in \{ n+1, .., l \} \text{.}
$$

We want to compute $D_i g_j(v_1, ..., v_n)$ for $i \in \{ 1, ..., n \}$, $j \in \{ 1, ..., m \}$. We will do so through a dynamic programming approach. The recursive equation that we will solve depends on the kind of AD that we'll implement.

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

We will assume that the function represented by the Wengert list has just one output ($m = 1$). Since, as it will be evident, BM AD works "one output at the time", this is without loss of generality.

Let's define a family of functions $\{ \phi^*_{i,j}(v_1, ..., v_j) \}$ with $i, j \in \{ n, ..., l \}$, $i \leq j$ with a set of recursive equations:
$$
\tag{1}\label{1} \phi_{i,i}^*(v_1, ..., v_i) = v_i \text{ for every } i \in \{ n, ..., l \} \text{;}
$$

$$
\tag{2}\label{2} \phi^*_{i,i+1}(v_1, ..., v_i) = \hat{\phi}_{i+1}(v_1, ..., v_i) \text{ for every } i \in \{ n, ..., l-1 \} \text{;}
$$

---

$$
\tag{3}\label{3} \phi^*_{j,i}(v_1, ..., v_j) = \phi^*_{j+1,i}(v_1, ..., v_j, \hat{\phi}_{j+1}(v_1, ..., v_j))
$$

$$
\text{ for every } j \in \{ n, ..., l-1 \}, i \in \{ j+1, ..., l \} \text{.}
$$

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

Let $i \in \{ 1, ..., l \}$, we define the set of successors of $v_i$ as
$$
S_i = \{ j \in \{ 1, ..., l \} | i \in P_j \} \text{.}
$$

_The desired result I wished to prove is the following_:
$$
D_j \phi_{j,l}^*(v_1, ..., v_j) = \sum_{k=j+1}^{l-1} D_j \phi_k(v_1, ..., v_j, \phi_{j,j+1}^*(v_1, ..., v_j), ..., \phi_{j,k-1}^*(v_1, ..., v_j)) \cdot
$$

$$
\cdot D_k \phi_{k,l}^*(v_1, ..., v_j, \phi_{j,j+1}^*(v_1, ..., v_j), \phi_{j,k-1}^*(v_1, ..., v_j)) =
$$

$$
= \sum_{k \in S_j} D_j \phi_k(v_1, ..., v_j, \phi_{j,j+1}^*(v_1, ..., v_j), ..., \phi_{j,k-1}^*(v_1, ..., v_j)) \cdot
$$

$$
\cdot D_k \phi_{k,l}^*(v_1, ..., v_j, \phi_{j,j+1}^*(v_1, ..., v_j), \phi_{j,k-1}^*(v_1, ..., v_j)) \text{.}
$$

