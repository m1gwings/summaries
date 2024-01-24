---
theme: summary
---
# Automatic Differentiation (AD)

<div class="author">

Cristiano Migali

</div>

---

## Wengert lists

(_What follows is my reinterpretation of Wengert lists with the purpose of proving the "fundamental recursive equations" of FM and BM AD_).
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

Then, if we fix $i \in \{ 1, ..., n \}$, we can compute $D_i f_j(v_1, ..., v_n)$ for every $j \in \{ 1, ..., l \}$ through dynamic programming.

### Backward mode recursive equation

Let's consider a function, described with a Wengert list, with just one output. As we will see we can apply BM AD "one output at the time", hence this assumption doesn't compromise the generality of the treatment.

To introduce the BM recursive equation, we need to define a list of helper functions first.
Let:
$$
\begin{matrix}
b_l(v_1, ..., v_l) = v_l \text{;} \\
b_i(v_1, ..., v_i) = b_{i+1}(v_1, ..., v_i, \hat{\phi}_{i+1}(v_1, ..., v_i)) \text{ for } i \in \{ n, ..., l-1 \} \text{.}
\end{matrix}
$$

Let's prove by induction that:
$$
b_i(f_1(v_1, ..., v_n), ..., f_i(v_1, ..., v_n)) = f_l(v_1, ..., v_n) = g(v_1, ..., v_n) \text{.}
$$

First of all observe that $f_l(v_1, ..., v_n) = g(v_1, ..., v_n)$ by definition (_remember that we're working with the assumption that $m = 1$_), then, we just need to prove that $b_i(f_1(v_1, ..., v_n), ..., f_i(v_1, ..., v_n)) = f_l(v_1, ..., v_n)$.

Base case: let $i = l$, it is straightforward by looking at how $b_l$ is defined.

Inductive step: let $n \leq i < l$, then
$$
b_i(f_1(v_1, ..., v_n), ..., f_i(v_1, ..., v_n)) =
$$

$$
= b_{i+1}(f_1(v_1, ..., v_n), ..., f_i(v_1, ..., v_n), \hat{\phi}_{i+1}(f_1(v_1, ..., v_n), ..., f_i(v_1, ..., v_n))) =
$$

$$
= b_{i+1}(f_1(v_1, ..., v_n), ..., f_i(v_1, ..., v_n), f_{i+1}(v_1, ..., v_n)) = f_l(v_1, ..., v_n) \text{.}
$$

The last equality follows from inductive hypothesis.

---

A consequence of this property is that:
$$
b_n(v_1, ..., v_n) = b_n(f_1(v_1, ..., v_n), ..., f_n(v_1, ..., v_n)) = g(v_1, ..., v_n) \text{.}
$$
Then, out objsective is to compute $D_i b_n(v_1, ..., v_n)$ for $i \in \{ 1, ..., n \}$.

Now we're ready to introduce the recursive equation. Let $j \in$, then
$$

$$