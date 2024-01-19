---
theme: summary
---
# Numerical analysis basics

<div class="author">

Cristiano Migali

</div>

---

## Methods

### Power method

- Let $A \in \mathbb{R}^{n \times n}$. Let $\lambda_1, ..., \lambda_k$ be the (distinct) eigenvalues of $A$. We say the $\lambda_1$ is the **dominant eigenvalue of $A$** iff $|\lambda_1| > |\lambda_i|$ for every $i \in \{ 2, ..., k \}$.
The eigenvectors related to $\lambda_1$ are called **dominant eigenvectors of $A$**.

> **Remark**: not every matrix has a dominant eigenvector. For example:
$$
A = \begin{bmatrix}
1 & 0 \\
0 & -1
\end{bmatrix} \text{.}
$$

The **power method** allows to approximate numerically a dominant eigenvector of $A$ (given that some hypotheses are satisfied). The iteration rule is:
$$
\underline{x}^{(k)} = \frac{A \underline{x}^{(k-1)}}{||A \underline{x}^{(k-1)}||} \text{.}
$$

1. $\underline{x}^{(k)} = \frac{A^k \underline{x}^{(0)}}{||A^k \underline{x}^{(0)}||}$.

> **Proof**: the base case follows directly from the iteration rule.

> Inductive step: let $k > 1$.
$$
\underline{x}^{(k)} = \frac{A \underline{x}^{(k-1)}}{||A \underline{x}^{(k-1)}||} = \frac{A \frac{A^{k-1} \underline{x}^{(0)}}{||A^{k-1} \underline{x}^{(0)}||}}{||A \frac{A^{k-1} \underline{x}^{(0)}}{||A^{k-1} \underline{x}^{(0)}||}||} = \frac{||A^{k-1} \underline{x}^{(0)}||}{||A^{k-1} \underline{x}^{(0)}||} \frac{A^k \underline{x}^{(0)}}{||A^k \underline{x}^{(0)}||} = \frac{A^k \underline{x}^{(0)}}{||A^k \underline{x}^{(0)}||} \text{.}
$$

2. Let $A \in \mathbb{R}^{m \times n}$ be a diagonalizable matrix. Let $\underline{v}_1, ..., \underline{v}_n$ be a basis of eigenvectors of $A$ with **norm 1**. Let $\underline{x}^{(0)} = \alpha_1 \underline{v}_1 + ... + \alpha_n \underline{v}_n$ with $\alpha_1 \neq 0$. Assume that $\underline{v}_1$ is a dominant eigenvector and no other $\underline{v}_i$ with $i \in \{ 2, ..., n \}$ is. (_Observe that, if the dimension of the eigenspace to which $\underline{v}_1$ belongs is greater than 1, then there will be at least another dominant eigenvector in the basis. For the purpose of the proof we can sum all these eigenvectors together with the relative coefficients $\alpha$ and consider them as one: $\underline{v}_1' = \alpha_1 \underline{v}_1 + ... + \alpha_h \underline{v}_h, \alpha_1' = 1$_).
Then $\underline{x}^{(k)}$ "approaches" (it can oscillate without converging to any vector) $\underline{v}_1$.

> **Proof**: From 1:
$$
\underline{x}^{(k)} = \frac{A^k \underline{x}^{(0)}}{||A^k \underline{x}^{(0)}||} = \frac{\alpha_1 \lambda_1^k \underline{v}_1 + ... + \alpha_n \lambda_n^k \underline{v}_k}{|| \alpha_1 \lambda_1^k \underline{v}_1 + ... + \alpha_n \lambda_n^k \underline{v}_k ||} =
$$

---

$$
= \frac{\alpha_1 \lambda_1^k}{|\alpha_1 \lambda_1^k|} \frac{\underline{v}_1 + ... + \frac{\alpha_n}{\alpha_1} (\frac{\lambda_n}{\lambda_1})^k \underline{v}_n}{||\underline{v}_1 + ... + \frac{\alpha_n}{\alpha_1} (\frac{\lambda_n}{\lambda_1})^k \underline{v}_n||} \text{.}
$$

> Since $\lambda_1$ is a dominant eigenvector: $(\frac{\lambda_i}{\lambda_1})^k \underline{v}_i \rightarrow \underline{0}_n$ for every $i \in \{ 2, ..., k \}$.
Then $\underline{v}_1 + ... + \frac{\alpha_n}{\alpha_1} (\frac{\lambda_n}{\lambda_1})^k \underline{v}_n \rightarrow \underline{v}_1$, and $||\underline{v}_1 + ... + \frac{\alpha_n}{\alpha_1} (\frac{\lambda_n}{\lambda_1})^k \underline{v}_n|| \rightarrow ||\underline{v}_1|| = 1$.
Finally $\frac{\alpha_1 \lambda_1^k}{|\alpha_1 \lambda_1^k|} \in \{ -1, 1 \}$. Note that both $\underline{v}_1$ and $-\underline{v}_1$ are dominant eigenvectors.

