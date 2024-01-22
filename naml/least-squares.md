---
theme: summary
---
# Least squares (LS)

<div class="author">

Cristiano Migali

</div>

The method of **least squares** allows us to solve the following problem: we are given a dataset of $n$ samples, each of which has $p$ features, organized in the rows of the matrix
$$
X = \begin{bmatrix}
\underline{x}_1^T \\
... \\
\underline{x}_n^T
\end{bmatrix} \in \mathbb{R}^{n \times p} \text{.}
$$

Each sample $\underline{x}_i$ is associated with a label $y_i$; all the labels are gouped into the vector
$$
\underline{y} = \begin{bmatrix}
y_1 \\
... \\
y_n
\end{bmatrix} \text{.}
$$

Given a new sample $\underline{\tilde{x}}$ which is not in the dataset, we want to predict its label $\tilde{y}$, and we want to do so through a linear model:
$$
\tilde{y} = \underline{x}^T \underline{w}
$$
where $\underline{w} \in \mathbb{R}^p$ is a vector of weights.

Nota that, in general:
$$
X \underline{w} = \begin{bmatrix}
\underline{x}_1^T \\
... \\
\underline{x}_n^T
\end{bmatrix} \underline{w} = \begin{bmatrix}
\underline{x}_1^T \underline{w} \\
... \\
\underline{x}_n^T \underline{w}
\end{bmatrix} \neq \underline{y} \text{.}
$$
That is, we cannot expect the linear model to produce the right label $y_i$ for every sample $\underline{x}_i$ in the dataset.
We will denote:
$$
\underline{\hat{y}} = X \underline{w} \text{.}
$$
and we want it to approximate as good as possible $\underline{y}$.
Let's formalize this concept:
$$
r_i(\underline{w}) = y_i - \hat{y}_i(\underline{w})
$$
is the error in predicting the $i$-th label in the dataset. We can group all the errors in a vector:

---

$$
\underline{r}(\underline{w}) = \begin{bmatrix}
y_1 - \hat{y}_1(\underline{w}) \\
... \\
y_n - \hat{y}_n(\underline{w})
\end{bmatrix} = \underline{y} - \underline{\hat{y}}(\underline{w}) = \underline{y} - X \underline{w} \text{.}
$$

We want to find $\underline{\hat{w}}$ such that $||\underline{r}(\underline{\hat{w}})||_2^2$ is minimum, that is
$$
\underline{\hat{w}} = \arg\min_{\underline{w} \in \mathbb{R}^p} ||\underline{r}(\underline{w})||_2^2 \text{.}
$$

## Solving LS

### Geometric approach

It is clear that $\underline{\hat{y}} = X \underline{w} \in C(X)$. If $\underline{y} \in C(X)$, we would just need to solve the linear system $X \underline{w} = \underline{y}$ in order to get $||\underline{r}(\underline{w})||_2^2 = 0$, but this is almost never the case. Then, let's assume that $\underline{y} \not \in C(X)$.

We know that the orthogonal projection of $\underline{y}$ onto $C(X)$ is the vector in $C(X)$ which is closest to $\underline{y}$, that is, it is the vector which minimizes $||\underline{r}(\underline{w})||_2^2$.
So we want to find $\underline{w}$ s.t. $\underline{\hat{y}} = X \underline{w}$ is the orthogonal projection of $\underline{y}$ onto $C(X)$.

Let's prove that this is equivalent to $X^T \underline{r}(\underline{w}) = \underline{0}$.
First of all, if $\underline{\hat{y}}$ is the orthogonal projection of $\underline{y}$ onto $C(X)$, then $\underline{r}(\underline{w}) = \underline{y} - \underline{\hat{y}} \perp C(X)$ because of the properties of the orthogonal projection, hence $X^T \underline{r}(\underline{w}) = \underline{0}$.
The converse is also true: assume that $X^T \underline{r}(\underline{w}) = \underline{0}$. Let $P$ be the composition of (column) permutation matrices, such that the first $r(X)$ columns of $X P$ are linearly independent. Let $Q R$ be the QR factorization of $X P$. Then
$$
Q \in \mathbb{R}^{n \times r(X)}, R = [ B C ] \text{ with } B \in \mathbb{R}^{r(X) \times r(X)} \text{ upper triangular}, C \in \mathbb{R}^{r(X) \times p-r(X)} \text{.}
$$
Hence
$$
X^T \underline{r}(\underline{w}) = \underline{0} \text{ iff } (X P P^{-1})^T \underline{r}(\underline{w}) = \underline{0} \text{ iff } (P^{-1})^T \begin{bmatrix}
B^T \\ C^T\end{bmatrix} Q^T (\underline{y} - \underline{\hat{y}}) = \underline{0} \text{ iff }
$$

$$
\text{ iff } \begin{bmatrix}
(P^{-1})^T B^T Q^T (\underline{y} - \underline{\hat{y}}) \\
(P^{-1})^T C^T Q^T (\underline{y} - \underline{\hat{y}})
\end{bmatrix} = \underline{0}
$$
which implies
$$
(P^{-1})^TB^TQ^T\underline{y} = (P^{-1})^T B^T Q^T \underline{\hat{y}} = (P^{-1})^TB^TQ^T X \underline{w} = (P^{-1})^T B^T Q^T Q \begin{bmatrix} B & C \end{bmatrix} P^{-1} \underline{w} \text{.}
$$
Since $(P^-1)^T$ and $B^T$ are clearly invertible, this is equivalent to:
$$
Q^T \underline{y} = Q^T Q \begin{bmatrix} B & C \end{bmatrix} P^{-1} \underline{w} = \begin{bmatrix} B & C \end{bmatrix} P^{-1} \underline{w} \text{.}
$$

---

The last equality implies (by premultiplying both sides with $Q$) that:
$$
Q Q^T \underline{y} = Q \begin{bmatrix} B & C \end{bmatrix} P^{-1} \underline{w} = XPP^{-1} \underline{w} = X \underline{w} = \underline{\hat{y}} \text{.}
$$
Since the columns of $Q$ form an orthonormal basis of $C(X)$, it follows that $\underline{\hat{y}}$ is the orthogonal projection of $\underline{y}$ onto $C(X)$.

Then, we reduced the problem to finding $\underline{w}$ s.t.
$$
X^T \underline{r}(\underline{w}) = X^T (\underline{y} - X \underline{w}) = \underline{0} \text{ iff }
$$
$$
X^T X \underline{w} = X^T \underline{y} \text{.}
$$

Now, if we assume that $r(X) = p$ (that is, the columns of $X$ are linearly independent), since in the construction of the SVD we proved that $r(X^T X) = r(X)$, it follows that $X^T X$ is invertible, hence:
$$
\underline{\hat{w}} = (X^T X)^{-1} X^T \underline{y} \text{.}
$$

### Analytic approach

Solving LS boils down to minimizing
$$
F(\underline{w}) = ||\underline{r}(\underline{w})||_2^2 = ||\underline{y} - X \underline{w}||_2^2 = \underline{y}^T \underline{y} -2\underline{y}^T X \underline{w} + \underline{w}^T X^T X \underline{w} \text{.} 
$$
$F$ is a quadratic functional, hence it is convex, so $\nabla_{\underline{w}}F(\underline{w}) = \underline{0}$ is a necessary and sufficient condition for $\underline{w}$ to be a minimizer.
Finally
$$
\nabla_{\underline{w}}F(\underline{w}) = 2 X^T X \underline{w} - 2 X^T \underline{y} = \underline{0} \text{ iff }
$$

$$
X^T X \underline{w} = X^T \underline{y} \text{.}
$$
That is, we rediscovered the same equation.

## Better expressions for the LS solution

We want to find expressions of $\underline{\hat{w}}$ which don't require the (expensive) computation of $X^T X$.

### LS through the Gram-Schmidt process
