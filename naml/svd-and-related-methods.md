---
theme: summary
---
# SVD & related methods

<div class="author">

Cristiano Migali

</div>

## Singular value decomposition (SVD)

We want to extend the factorization provided for real symmetric matrices by the spectral theorem, that is
$$
A = Q \Lambda Q^T
$$
to any matrix $A \in \mathbb{R}^{m \times n}$.
The **SVD** allows us to factorize $A$ as
$$
A = U \Sigma V^T
$$
where:
- $U \in \mathbb{R}^{m \times m}$ is an orthogonal matrix;

- $\Sigma = \begin{bmatrix} \text{diag}\{ \sigma_1, ..., \sigma_r \} & O_{r \times (n-r)} \\ O_{(m-r) \times r} & O_{(m-r) \times (n-r)} \end{bmatrix}$ with $\sigma_1 \geq ... \geq \sigma_r > 0$ and $r = r(A)$;

- $V \in \mathbb{R}^{n \times n}$ is an orthogonal matrix.

### The reduced form of the SVD

The one that we already presented ($A = U \Sigma V^T$) is known as the **full form** of the SVD. We will introduce an equivalent expression where we keep only the first $r$ columns of $U$ and $V$ that is known as the **reduced** (or **economy**) **form**:
let $U_r = \begin{bmatrix} \underline{u}_1 & ... & \underline{u}_r \end{bmatrix}$, $V_r = \begin{bmatrix} \underline{v}_1 & ... & \underline{v}_r \end{bmatrix}$, $\Sigma_r = \text{diag} \{ \sigma_1, ..., \sigma_r \}$.
Then:
$$
U_r \Sigma_r V_r^T = \begin{bmatrix} \underline{u}_1 & ... & \underline{u}_r \end{bmatrix}
\begin{bmatrix}
\sigma_1 & 0 & ... & 0 \\
0 & ...  & ... & ... \\
... & ... & ... & 0 \\
0 & ... & 0 & \sigma_r
\end{bmatrix}
\begin{bmatrix}
\underline{v}_1^T \\
... \\
\underline{v}_r^T
\end{bmatrix} = 
\begin{bmatrix} \underline{u}_1 & ... & \underline{u}_r \end{bmatrix} \begin{bmatrix}
\sigma_1 \underline{v}_1^T \\
... \\
\sigma_r \underline{v}_r^T
\end{bmatrix} =
$$

$$
= \sum_{i=1}^r \sigma_i \underline{u}_i \underline{v}_i^T \text{.}
$$

Now it is just a matter of proving that $A = U \Sigma V^T = \sum_{i=1}^r \sigma_i \underline{u}_i \underline{v}_i^T$. This expression will be used quite often.

---

$$
A = U \Sigma V^T =
\begin{bmatrix}
\underline{u}_1 & ... & \underline{u}_r & \begin{bmatrix} \underline{u}_{r+1} & ... & \underline{u}_m \end{bmatrix}
\end{bmatrix}

\begin{bmatrix}
\begin{bmatrix}
\sigma_1 & 0 & ... & 0 \\
0 & ...  & ... & ... \\
... & ... & ... & 0 \\
0 & ... & 0 & \sigma_r
\end{bmatrix} & O_{r \times (n - r)} \\

O_{(m - r) \times n} & O_{(m-r) \times (n-r)}
\end{bmatrix}
\begin{bmatrix}
\underline{v}_1^T \\
... \\
\underline{v}_r^T \\
\begin{bmatrix}
\underline{v}_{r+1}^T \\
... \\
\underline{v}_{n}^T
\end{bmatrix}
\end{bmatrix} =
$$

$$
= \begin{bmatrix}
\underline{u}_1 & ... & \underline{u}_r & \begin{bmatrix} \underline{u}_{r+1} & ... & \underline{u}_m \end{bmatrix}
\end{bmatrix}
\begin{bmatrix}
\sigma_1 \underline{v}_1^T \\
... \\
\sigma_r \underline{v}_r^T \\
O_{(m-r) \times n}
\end{bmatrix} = \sigma_1 \underline{u}_1 \underline{v}_1^T + ... + \sigma_r \underline{u}_r \underline{v}_r^T + O_{m \times n} =
$$

$$
= \sum_{i=1}^r \sigma_i \underline{u}_i \underline{v}_i^T \text{.}
$$