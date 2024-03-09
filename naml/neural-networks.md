---
marp: true
theme: summary
math: mathjax
---
# Neural networks

<div class="author">

Cristiano Migali

</div>

## Mathematical representation

We can represent a NN through the following parameters:
- $w_{jk}^l$ is the **weight** from the $k$-th neuron in layer $l-1$ to the $j$-th neuron in layer $l$-th;
- $b_j^l$ is the **bias** of the $j$-th neuron in layer $l$;
- $a_j^l$ is the **activation** of the $j$-th neuron in layer $l$.

The network works as follows:
$$
a_j^l = \sigma(\sum_{k=1}^{n_{l-1}} w_{jk}^l a_k^{l-1} + b_j^l)
$$
where $n_l$ is the **number of neurons in layer $l$**, and $\sigma$ is the **activation function**.

We can weite the expression above in matricial form:
$$
\underline{a}^l = \begin{bmatrix}
a_1^l \\
... \\
a_{n_l}^l
\end{bmatrix} = \begin{bmatrix}
\sigma(\sum_{k=1}^{n_{l-1}} w_{1k}^l a_k^{l-1} + b_1^l) \\
... \\
\sigma(\sum_{k=1}^{n_{l-1}} w_{n_lk}^l a_k^{l-1} + b_{n_l}^l)
\end{bmatrix} = \sigma(\begin{bmatrix}
w_{11}^l & ... & w_{1n_{l-1}}^l \\
... & ... & ... \\
w_{n_l1}^l & ... & w_{n_ln_{l-1}}^l
\end{bmatrix} \begin{bmatrix}
a_1^{l-1} \\
... \\
a_{n_{l-1}}^{l-1}
\end{bmatrix} + \begin{bmatrix}
b_1^l \\
... \\
b_{n_l}^l
\end{bmatrix}) =
$$

$$
= \sigma(W^l \underline{a}^{l-1} + \underline{b}^l) \text{.}
$$

We define $\underline{z}^l = W^l \underline{a}^{l-1} + \underline{b}^{l-1}$.

## Backpropagation

Let $J$ be the cost function which computes the error in the predictions of the network. We're intereted in computing $\frac{\partial J}{\partial w}$, and $\frac{\partial J}{\partial b}$ for every weight $w$, and bias $b$, and we want to do it efficiently.
We assume that:
> i. The cost function can be written as an average over the cost functions for each sample:
$$
J = \frac{1}{N} \sum_{i=1}^N J_i \text{.}
$$

---

> ii. The cost function of each sample can be written in terms of the output of the NN:
$$
J_i = J_i(\underline{a}_L)
$$
> (_where $L$ is the last layer of the network_).

Let's see some fundamental relationships which hold in this setting. To simplify the notation in what follows, we will omit the index $i$ from $J_i$, since it is not relevant for the treatment.

- We say
$$
\delta_j^l = \frac{\partial J}{\partial z_j^l}
$$
> the **error** of the $j$-th neuron in layer $l$. $\underline{\delta}^l$ is the **vector of errors** for layer $l$.

> **Theorem (1)**:
$$
\delta_j^L = \frac{\partial J}{\partial a_j^L} \sigma'(z_j^L) \text{, and so } \underline{\delta}^L = \nabla_{\underline{a}^L} J \cdot^* \sigma'(\underline{z}^L)
$$

> **Proof**:
$$
\delta_j^L = \frac{\partial J}{\partial z_j^L} = \frac{\partial J}{\partial a_1^L} \frac{\partial a_1^L}{\partial z_j^L} + ... + \frac{\partial J}{\partial a_j^L} \frac{\partial a_j^L}{\partial z_j^L} + ... + \frac{\partial J}{\partial a_{n_L}^L} \frac{\partial a_{n_L}^L}{\partial z_j^L} =
$$

$$
= \frac{\partial J}{\partial a_1^L} \cdot 0 + ... + \frac{\partial J}{\partial a_j^L} \sigma'(z_j^L) + ... + \frac{\partial J}{\partial a_{n_L}^L} \cdot 0 = \frac{\partial J}{\partial a_j^L} \sigma'(z_j^L) \text{.}
$$

> **Theorem (2)**:
$$
\underline{\delta}^l = [(W^{l+1})^T \underline{\delta}^{l+1}] \cdot^* \sigma'(\underline{z}^l) \text{.}
$$

> **Proof**:
$$
\delta_j^l = \frac{\partial J}{\partial z_j^l} = \frac{\partial J}{\partial z_1^{l+1}} \frac{\partial z_1^{l+1}}{\partial z_j^l} + ... + \frac{\partial J}{\partial z_{n_{l+1}}^{l+1}} \frac{\partial z_{n_{l+1}}^{l+1}}{\partial z_j^l} \text{.}
$$

> Since $z_k^{l+1} = \sum_{i=1}^{n_l} w_{ki}^{l+1} a_i^l + b_k^{l+1} = \sum_{i=1}^{n_l} w_{k_i}^{l+1} \sigma(z_i^l) + b_k^{l+1}$. Then
$$
\frac{\partial z_k^{l+1}}{\partial z_j^l} = w_{kj}^{l+1} \sigma'(z_j^l) \text{.}
$$

> Then $\delta_j^l = \delta_1^{l+1} w_{1j}^{l+1} \sigma'(z_j^l) + ... + \delta_{n_{l+1}}^{l+1} w_{n_{l+1}j}^{l+1} \sigma'(z_j^l)$.

---

> The result follows.

> **Theorem (3)**:
$$
\frac{\partial J}{\partial b_j^l} = \delta_j^l \text{.}
$$

> **Proof**:
$$
\frac{\partial J}{\partial b_j^l} = \frac{\partial J}{\partial z_j^l} \cdot \frac{\partial z_j^l}{\partial b_j^l} \text{.}
$$

> Furthermore, since $z_j^l = \sum_{k=1}^{n_{l-1}} w_{jk}^l a_k^{l-1} + b_j^l$, then $\frac{\partial z_j^l}{\partial b_j^l} = 1$, hence:
$$
\frac{\partial J}{\partial b_j^l} = \delta_j^l \text{.}
$$

> **Theorem (4)**:
$$
\frac{\partial J}{\partial w_{jk}^l} = a_k^{l-1} \delta_j^l \text{.}
$$

> **Proof**:
$$
\frac{\partial J}{\partial w_{jk}^l} = \frac{\partial J}{\partial z_j^l} \frac{\partial z_j^l}{\partial w_{jk}^l} = \delta_j^l a_k^{l-1} \text{.}
$$

> **Remarks**:
>> i. By theorem (2), it follows that $(W^{l+1})^T$ "backpropagates" the error from the last layer to the first. With theorem (1) and (2), we can compute the error for every layer;

>> ii. Every $\underline{z}^l$ is computed in the "forward procedure";

>> iii. By theorem (4), it follows that if $a_k^{l-1} \approx 0$, then $\frac{\partial J}{\partial w_{jk}^l} \approx 0$ for every $j \in \{ 1, ..., n_{l+1} \}$. We will see that this implies that neuron $k$ at layer $l-1$ will learn slowly;

>> iv. By theorem (1), if $\sigma'(z_j^L) \approx 0$, then $\delta_j^L \approx 0$. Again, this will imply slow learning. If we use the sigmoid as activation function, $\sigma'(x) \rightarrow 0$ for $x \rightarrow \pm \infty$. Since
$$
z_j^L = \sum_{k=1}^{n_{L-1}} w_{jk}^L a_k^{L-1} + b_j^L \text{, }
$$

---

>> if $a_k^{L-1} \gg 1$, or $a_k^{L-1} \ll -1$, then same will be true for $z_j^L$, hence, $\sigma'(z_j^L) \approx 0$.

Let's summarize everything into a procedure for calculating $\frac{\partial J}{\partial w_{jk}^l}$, and $\frac{\partial J}{\partial b_j^l}$ for every $w_{jk}^l$, and $b_j^l$.
1. Let $\underline{x}$ be the input vector, compute $\underline{a}^1$ (_the input layer_);
2. Feedforward: for each $l = 2, 3, ..., L$, compute
$$
\underline{z}^l = W^l \underline{a}^{l-1} + \underline{b}^l \text{, and} \underline{a}^l = \sigma(\underline{z}^l) \text{;}
$$
3. Output error: compute
$$
\underline{\delta}^L = \nabla_{\underline{a}_L} J \cdot^* \sigma'(\underline{z}^L) \text{;}
$$
4. Backpropagation: for each $l = L-1, L-2, ..., 2$, compute
$$
\underline{\delta}^L = [(W^{l+1})^T \underline{\delta}^{l+1}] \cdot^* \sigma'(\underline{z}^l) \text{,}
$$
5. Output values of the derivatives. Compute
$$
\frac{\partial J}{\partial w_{jk}^l} = a_k^{l-1} \delta_j^l \text{ and } \frac{\partial J}{\partial b_j^l} = \delta_j^l \text{.}
$$