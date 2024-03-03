---
marp: true
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

We want to find expressions of $\underline{\hat{w}}$ which don't require the (expensive) computation of $(X^T X)^{-1}$.

### LS through the Gram-Schmidt process

Assume that the columns of $X$ are linearly independent. We've already seen that:
$$
\underline{\hat{w}} = (X^T X)^{-1} X^T \underline{y} \text{,}
$$
and so $\underline{\hat{y}} = X \underline{\hat{w}} = X (X^T X)^{-1} X^T \underline{y} = P_X \underline{y}$ with $P_X = X(X^T X)^{-1}X^T$.

---

$P_X$ is a projection matrix: indeed
$$
P_X^2 = X(X^T X)^{-1}X^T X(X^T X)^{-1}X^T = X (X^T X)^{-1} X^T = P_X \text{.}
$$

The idea behind LS through the Gram-Schmidt process is to use an orthogonal projection matrix $Q$ to project $\underline{y}$ onto $C(X)$.
Remember that we're assuming that the columns of $X$ are linearly independent, hence the QR factorization of $X$ is $X = QR$ where $R \in \mathbb{R}^{p \times p}$ is a full-rank upper triangular matrix. Furthermore, the columns of $Q$ form an orthonormal basis of $C(X)$, hence $Q Q^T$ is an orthogonal projection matrix onto $C(X)$.
Now observe that:
Let's substitute the $Q R$ factorization of $X$ into the expression of $P_X$:
$$
P_X = X (X^T X)^{-1} X^T = Q R (R^T Q^T Q R)^{-1} R^T Q^T = Q R (R^T R)^{-1} R^T Q^T =
$$

$$
= Q R R^{-1} (R^T)^{-1} R^T Q ^T = Q Q^T \text{.}
$$
Hence:
$$
\underline{\hat{y}} = P_X \underline{y} = Q Q^T \underline{y} \text{.}
$$

Finally:
$$
\underline{\hat{y}} = X \underline{w} = Q R \underline{w} = Q \underline{\tilde{w}} \text{ with } \underline{\tilde{w}} = R \underline{w} \text{.}
$$

By left multiplying by $Q^T$, we get:
$$
\underline{\tilde{w}} = Q^T \underline{\hat{y}} = Q^T Q Q^T \underline{y} = Q^T \underline{y} \text{.}
$$

We can make predictions through $\underline{\tilde{w}}$ in the following way:
$$
\tilde{y} = \underline{\tilde{x}}^T \underline{w} = \underline{\tilde{x}}^T R^{-1} \underline{\tilde{w}} \text{.}
$$

Observe that inverting $R$, which is a triangular matrix, is faster than inverting $X^T X$.

### LS through the pseudoinverse

- Let $A \in \mathbb{R}^{m \times n}$, we define **pseudoinverse** of $A$ the matrix
$$
A^+ = \sum_{i=1}^{r(A)}\frac{1}{\sigma_i(A)} \underline{v}_i \underline{u}_i^T \text{.}
$$

Observe that $A^+ = V \Sigma^+  U^T$. Indeed, $\Sigma = \sum_{i=1}^{r(A)} \sigma_i(A) \underline{e}_i^{(m)} (\underline{e}_i^{(n)})^T$, hence $\Sigma^+ = \sum_{i=1}^{r(A)} \frac{1}{\sigma_i(A)} \underline{e}_i^{(n)} (\underline{e}_i^{(m)})^T$, that is, we transpose $\Sigma$ and we take the reciprocal of the positive singular values on the diagonal.

Furthermore, we can derive other special expressions for $A^+$ in the case $r(A) = n$ and $r(A) = m$.

---

Assume that $r(A) = m$, that is, the **rows** of $A$ are linearly independent, then:
$$
A^+ = \sum_{i=1}^m \frac{1}{\sigma_i(A)} \underline{v}_i \underline{u}_i^T = \sum_{i=1}^m \sigma_i(A) \underline{v}_i \underline{u}_i^T \sum_{j=1}^m \frac{1}{\sigma_j^2(A)} \underline{u}_j \underline{u}_j^T =
$$

$$
= \sum_{i=1}^m \sigma_i(A) \underline{v}_i \underline{u}_i^T (\sum_{j=1}^m \sigma_j^2(A) \underline{u}_j \underline{u}_j^T)^{-1} \text{.}
$$
The last equality follows from the fact that
$$
\sum_{j=1}^m \sigma_j^2(A) \underline{u}_j \underline{u}_j^T \sum_{i=1}^m \frac{1}{\sigma_i^2(A)} \underline{u}_i \underline{u}_i^T = \sum_{j=1}^m \underline{u}_j \underline{u}_j^T \text{.}
$$
And we've already seen (when we proved property 2 of the SVD) that
$$
\sum_{j=1}^m \underline{u}_j \underline{u}_j^T = I_m \text{.}
$$

Furthermore
$$
\sum_{i=1}^m \sigma_i(A) \underline{v}_i \underline{u}_i^T (\sum_{j=1}^m \sigma_j^2(A) \underline{u}_j \underline{u}_j^T)^{-1} = \sum_{i=1}^m \sigma_i(A) \underline{v}_i \underline{u}_i^T (\sum_{j=1}^m \sigma_j(A) \underline{u}_j \underline{v}_j^T \sum_{k=1}^m \sigma_k(A) \underline{v}_k \underline{u}_k^T) =
$$

$$
= A^T (AA^T)^{-1} \text{.}
$$

Analogously, assume that $r(A) = n$, that is, the **columns** of $A$ are linearly independent, then:

$$
A^+ = \sum_{i=1}^n \frac{1}{\sigma_i(A)} \underline{v}_i \underline{u}_i^T = \sum_{i=1}^n \frac{1}{\sigma_i^2(A)} \underline{v}_i \underline{v}_i^T \sum_{j=1}^n \sigma_j(A) \underline{v}_j \underline{u}_j^T =
$$

$$
= (\sum_{i=1}^n \sigma_i^2(A) \underline{v}_i \underline{v}_i^T)^{-1} \sum_{j=1}^n \sigma_j(A) \underline{v}_j \underline{u}_j^T =
$$

$$
= (\sum_{i=1}^n \sigma_i(A) \underline{v}_i \underline{u}_i^T \sum_{j=1}^n \sigma_j(A) \underline{u}_j \underline{v}_j^T)^{-1} \sum_{k=1}^n \sigma_i(A) \underline{v}_k \underline{u}_k^T = (A^T A)^{-1} A^T \text{.}
$$

Now let's get back to LS. We known that $||\underline{r}(\underline{w})||_2^2$ is minimum iff
$$
X^T X \underline{w} = X^T \underline{y} \text{.}
$$

We will prove that $\underline{\hat{w}} = X^+ \underline{y}$ satisfies the equation above:
$$
X^T X \underline{\hat{w}} = X^T X X^+ \underline{y} = \sum_{i=1}^{r(X)} \sigma_i^2(A) \underline{v}_i \underline{v}_i^T \sum_{j=1}^{r(X)} \frac{1}{\sigma_i(A)} \underline{v}_j \underline{u}_j^T  \underline{y} =
$$

---

$$
= \sum_{i=1}^{r(X)} \sigma_i(A) \underline{v}_i \underline{u}_i^T \underline{y} = X^T \underline{y} \text{.}
$$

Then $\underline{\hat{w}}$ solves the LS problem, no matter the rank of $X$.

#### The solution found through the pseudoinverse has the least norm

Let $\underline{w}$ be another ($\underline{w} \neq \underline{\hat{w}}$) solution to LS.

First of all observe that:
$$
\sum_{i=1}^{r(X)} \sigma_i^2(X) \underline{v}_i^T \underline{w} \underline{v}_i = X^T X \underline{w} = X^T \underline{y} = X^T X \underline{\hat{w}} = \sum_{i=1}^{r(X)} \sigma_i^2(X) \underline{v}_i^T \underline{\hat{w}} \underline{v}_i \text{.}
$$
Since $\underline{v}_1, ..., \underline{v}_{r(X)}$ are linearly independent, it must be
$$
\sigma_i^2(X) \underline{v}_i^T \underline{w} = \sigma_i^2(X) \underline{v}_i^T \underline{\hat{w}} \text{ iff } \underline{v}_i^T \underline{w} = \underline{v}_i^T \underline{\hat{w}} \text{ for every } i \in \{ 1, ..., r(X) \} \text{.}
$$

Then:
$$
(\underline{w} - \underline{\hat{w}})^T\underline{\hat{w}} = (\underline{w} - \underline{\hat{w}})^T X^+ \underline{y} = (\underline{w} - \underline{\hat{w}})^T \sum_{i=1}^{r(X)} \frac{1}{\sigma_i(X)} \underline{v}_i \underline{u}_i^T \underline{y} =
$$

$$
= \sum_{i=1}^{r(X)} \frac{\underline{w}^T \underline{v}_i - \underline{\hat{w}}^T \underline{v}_i}{\sigma_i(X)} \underline{u}_i^T \underline{y} = \sum_{i=1}^{r(X)} 0 \cdot \underline{u}_i^T \underline{y} = 0 \text{.}
$$

Finally:
$$
||\underline{w}||_2^2 = ||\underline{\hat{w}} + (\underline{w} - \underline{\hat{w}})||_2^2 = ||\underline{\hat{w}}||_2^2 + ||\underline{w} - \underline{\hat{w}}||_2^2 - 2 (\underline{w} - \underline{\hat{w}})^T \underline{\hat{w}} =  
$$

$$
= ||\underline{\hat{w}}||_2^2 + ||\underline{w} - \underline{\hat{w}}||_2^2 > ||\underline{\hat{w}}||_2^2 \text{.}
$$

This property is useful since sometimes, if $||\underline{w}||_2^2$ is big, the noise in the measured values of the features of $\underline{\tilde{x}}$ are amplified when we compute $\tilde{y} = \underline{\tilde{x}}^T \underline{w}$.

## Ridge regression

**Ridge regression** is a regularization technique useful when we want to solve the LS problem in the following scenario:
$$
\underline{y} = X \underline{w}^* + \underline{\epsilon}
$$
where $X \underline{w}^*$ are the "true" labels (thus $\underline{w}^*$ is the "true" model), and $\underline{\epsilon}$ represents the noise in the measurements.

---

Let's see how the noise propagates into the pseudoinverse LS solution (which we'll denote with $\underline{w}_{\text{LS}}$):
$$
\underline{w}_{\text{LS}} = X^+ \underline{y} = \sum_{i=1}^{r(X)} \frac{1}{\sigma_i(X)} \underline{v}_i \underline{u}_i^T (X \underline{w}^* + \underline{\epsilon}) =
$$

$$
= \sum_{i=1}^{r(X)} \frac{1}{\sigma_i(X)} \underline{v}_i \underline{u}_i^T (\sum_{j=1}^{r(X)} \sigma_j(X) \underline{u}_i \underline{v}_i^T \underline{w}^* + \underline{\epsilon}) =
$$

$$
= (\sum_{i=1}^{r(X)} \underline{v}_i \underline{v}_i^T) \underline{w}^* +
\sum_{i=1}^{r(X)} \frac{\underline{u}_i^T \underline{\epsilon}}{\sigma_i(X)} \underline{v}_i \text{.}
$$

If $r(X) = p$, then $\sum_{i=1}^{r(X)} \underline{v}_i \underline{v}_i^T = \sum_{i=1}^p \underline{v}_i \underline{v}_i^T = I_p$, hence
$$
\underline{w}_{\text{LS}} = \underline{w}^* + \sum_{i=1}^p \frac{\underline{u}_i^T \underline{\epsilon}}{\sigma_i(X)} \underline{v}_i .
$$

Observe that $\sigma_p$ can be quite small, that is $0 \approx \sigma_p \leq ... \leq \sigma_1$. If this is the case, $\underline{u}_i^T \underline{\epsilon}$ gets amplified in $\underline{w}_{\text{LS}}$, and the norm of the "propagated" error is:
$$
\sqrt{\sum_{i=1}^p (\frac{\underline{u}_i^T \underline{\epsilon}}{\sigma_i(X)})^2} \gg 0 \text{.}
$$

That is $\underline{w}_{\text{LS}} \not \approx \underline{w}^*$.

Ridge regression aims at solving this issue by modifying the functional that we're minimizing through the introduction of a penalty term on the 2-norm of the model:
$$
F_{\text{R}}(\underline{w}) = ||\underline{y} - X \underline{w}||_2^2 + \lambda ||\underline{w}||_2^2
$$
where $\lambda > 0$ is an hyperparameter.
Observe that $F_{\text{R}}$ is still a quadratic functional:
$$
F_{\text{R}}(\underline{w}) = \underline{y}^T \underline{y} -2\underline{y}^T X \underline{w} + \underline{w}^T X^T X \underline{w} + \lambda \underline{w}^T \underline{w} =
$$

$$
= \underline{y}^T \underline{y} - 2 \underline{y}^T X \underline{w} + \underline{w}^T (X^T X + \lambda I_p) \underline{w} \text{.}
$$

Hence $\underline{w}$ is a minimizer of $F_{\text{R}}$ iff
$$
\nabla_{\underline{w}} F_{\text{R}}(\underline{w}) = 2 (X^T X + \lambda I_p) \underline{w} - 2 X^T \underline{y} = \underline{0} \text{ iff }
$$

$$
(X^T X + \lambda I_p) \underline{w} = X^T \underline{y} \text{.}
$$

---

Remember that $X^T X$ has non-negative eigenvalues, hence

$$
X^TX + \lambda I_p = V (\Lambda + \lambda I_p) V^T
$$

has strictly positive eigenvalues. Thus it is invertible.
It follows that the solution to the Ridge regression is:
$$
\underline{w}_{\text{R}} = (X^T X + \lambda I_p)^{-1} X^T \underline{y} \text{.}
$$

Let's see how the noise propagates into $\underline{w}_{\text{R}}$.
First of all observe that:
$$
X^TX + \lambda I_p = \sum_{i=1}^{r(X)} \sigma_i^2(X) \underline{v}_i \underline{v}_i^T + \lambda \sum_{i=1}^{r(X)} \underline{v}_i \underline{v}_i^T \text{.}
$$
Then, if we define $\sigma_{r(X)+1}(X) = ... = \sigma_p(X) = 0$,
$$
X^T X + \lambda I_p = \sum_{i=1}^p (\sigma_i^2(X) + \lambda) \underline{v}_i \underline{v}_i^T \text{.}
$$

It is easy to check (by multiplying the two expressions) that
$$
(X^T X + \lambda I_p)^{-1} = \sum_{i=1}^p \frac{1}{\sigma_i^2(X) + \lambda} \underline{v}_i \underline{v}_i^T \text{.}
$$

Then:
$$
(X^T X + \lambda I_p)^{-1} X^T = \sum_{i=1}^p \frac{1}{\sigma_i^2(X) + \lambda} \underline{v}_i \underline{v}_i^T \sum_{j=1}^p \sigma_j(X) \underline{v}_j \underline{u}_j^T =
$$

$$
= \sum_{i=1}^p \frac{\sigma_i(X)}{\sigma_i^2(X) + \lambda} \underline{v}_i \underline{u}_i^T \text{.}
$$

Observe that:
- if $\sigma_i(X) \gg \lambda$, then
$$
\frac{\sigma_i(X)}{\sigma_i^2(X) + \lambda} = \frac{1}{\sigma_i(X) + \frac{\lambda}{\sigma_i(X)}} \approx \frac{1}{\sigma_i(X)} \text{;}
$$
- if $\sigma_i(X) \ll \lambda$, then
$$
\frac{\sigma_i(X)}{\sigma_i^2(X) + \lambda} = \frac{1}{\sigma_i(X) + \frac{\lambda}{\sigma_i(X)}} \approx \frac{1}{\frac{\lambda}{\sigma_i(X)}} = \frac{\sigma_i(X)}{\lambda} \approx 0 \text{.}
$$

---

Finally:
$$
\underline{w}_{\text{R}} = \sum_{i=1}^p \frac{\sigma_i(X)}{\sigma_i^2(X) + \lambda} \underline{v}_i \underline{u}_i^T (X \underline{w}^* + \underline{\epsilon}) = 
\sum_{i=1}^p \frac{\sigma_i(X)}{\sigma_i^2(X) + \lambda} \underline{v}_i \underline{u}_i^T (\sum_{j=1}^p \sigma_j(X) \underline{u}_j \underline{v}_j^T \underline{w}^* + \underline{\epsilon}) =
$$

$$
= (\sum_{i=1}^p \frac{\sigma_i^2(X)}{\sigma_i^2(X) + \lambda} \underline{v}_i \underline{v}_i^T ) \underline{w}^* + \sum_{i=1}^p \frac{\sigma_i(X)}{\sigma_i^2(X) + \lambda}(\underline{u}_i^T \underline{\epsilon}) \underline{v}_i \text{.}
$$

In conclusion:
- if $\underline{\epsilon}$ is NOT negligible, suitable values of $\lambda$ prevent the "propagated" error to blow up in the expression of $\underline{w}_{\text{R}}$ by putting the terms $\frac{\sigma_i(X)}{\sigma_i^2(X) + \lambda} \approx 0$ for small $\sigma_i(X)$;
- if $\underline{\epsilon} \approx \underline{0}$ then, with $\lambda = 0$, assuming $r(X) = p$, we would get $\underline{w}_{\text{R}} \approx \underline{w}^*$. So the term $\lambda$ is worsening the performance of our method.

## Least Absolute Shrinkage and Selection Operator (LASSO)

The linear model produced by solving LS not only allows to predict a label given a sample:
$$
\tilde{y} = \underline{\tilde{x}}^T \underline{\hat{w}}
$$
but also to identify the features which are more relevant for the prediction: that is, the ones whose values are multiplied by larger coefficients in $\underline{\hat{w}}$. This process is known as **features selection** and is relevant for the explainability of the model.
Features selection is straightforward when the model $\underline{\hat{w}}$ is sparse (that is, it has many zeros): the relevant features are the ones which are multiplied by a non-zero coefficient, and we can discard the others. For this reason we're interested in methods which provide sparse solutions to the LS problem. Neither solving LS through the pseudoinverse, nor Ridge regression has this property: we need to introduce a different kind of regularization.

First of all, let's understand the impact of regularization on the "shape" of the solution.
Remember that we want to find $\underline{w}$ s.t.
$$
X^T X \underline{w} = X^T \underline{y} \text{.}
$$
Let's assume that $r(X^T X) = r(X) < p$ ortherwise the solution to LS is unique, and there is no solution sparser than another that we can choose. If $p = 2$ (we have two features) $X^T X \underline{w} = X^T \underline{y}$ is a system of two linear equations whose unkwowns are $w_1$, and $w_2$ (with $\underline{w}^T = \begin{bmatrix} w_1 & w_2 \end{bmatrix}$). Furthermore if $r(X) = 1$, the two equations are equivalent, hence we can get rid of one. It follows that the locus of solutions to LS is a line.
Now suppose that we add a penalty term $\lambda ||\underline{w}||_2^2$ with $\lambda > 0$. Then, among all points on the line of solutions to LS, we want to find the one with least 2-norm.

---

(_Observe that we're making an approximation here: if we want to minimize $F(\underline{w}) + \lambda ||\underline{w}||_2^2$ it may be convenient, depending on the value of $\lambda$, to not satisfy $F(\underline{w}) = 0$ in favor of a solution with least 2-norm_).
Under this assumption, the point we're looking for has a peculiar property: it must have a 2-norm $c$ such that there is exactly one point on the line of solutions which has 2-norm $c$ (which is the solution we're looking for), and every other point with 2-norm less than or equal to $c$ doesn't lie on the line of solutions.
Furthermore, the locus of points $\{ ||\underline{w}||_2^2 \leq c \}$ is a circle. Hence, we're looking for a circle which is tangent to the line of solutions, and in particular, the solution we're interested in, is the point of intersection between this circle and the line of solutions.

<p align="center">
    <img src="http://localhost:8080/naml/static/2-norm-penalty.png" width="420mm" />
</p>

The locus of points with 1-norm equal to $c$ has instead another shape (a square roatated of 45 degrees in 2d) which favors sparse solutions:

<p align="center">
    <img src="http://localhost:8080/naml/static/1-norm-penalty.png" width="420mm" />
</p>

---

These observations lead to **LASSO**: a type of regression in which we introduce a penalty term on the 1-norm of the model.
That is:
$$
F(\underline{w}) = ||X \underline{w} - \underline{y}||_2^2 + \lambda ||\underline{w}||_1 \text{.}
$$

## Elastic net

**Elastic net** is a generalization of LASSO and Ridge regression, where we introduce a penalty term on both the 2-norm and the 1-norm of the model:
$$
F(\underline{w}) = ||X \underline{w} - \underline{y}||_2^2 + \lambda_1 ||\underline{w}||_1 + \lambda_2 ||\underline{w}_2||_2^2 \text{.}
$$

## Non-linear models and the kernel trick

The idea that we will explot in order to adapt LS to non-linear models is very simple: we enrich the features of each sample by adding new features computed starting from the old ones, through non-linear functions.
For example, if the features of the sample $\underline{x}_i$ are $y_i$ and $z_i$, we could compute the new features $y_i^2$, $z_i^2$, and $y_i z_i$.
In general, we will enrich a sample vector $\underline{x}_i$ (which we can also call **feature vector**) through a **feature map** $\phi : \mathbb{R}^p \rightarrow \mathbb{R}^d$ (with $d > p$). At the end this boils down to applying LS to the matrix
$$
\Phi = \begin{bmatrix}
\phi(\underline{x}_1)^T \\
... \\
\phi(\underline{x}_n)^T
\end{bmatrix}
$$
instead of $X$. (_Of course, labels are not affected_).
Usually $d$ is huge, making the computation of $\Phi^+$ infeasible. For this reason, we will introduce the so-called **kernel trick** which will allow us to make labels predictions without having to compute $\Phi^+$.
Before introducing the trick, we have to rewrite the expression of the Ridge regression formula (applied to $\Phi$):
$$
\underline{w}_{\text{R}} = \sum_{i=1}^p \frac{\sigma_i(X)}{\sigma_i^2(X) + \lambda} \underline{v}_i \underline{u}_i^T \underline{y} = \sum_{i=1}^p \sigma_i(X) \underline{v}_i \underline{u}_i^T \sum_{j=1}^p \frac{1}{\sigma_j^2(X) + \lambda} \underline{u}_j \underline{u}_j^T \underline{y} = 
$$

$$
= \sum_{i=1}^p \sigma_i(X) \underline{v}_i \underline{u}_i^T (\sum_{j=1}^p (\sigma_j^2(X) + \lambda) \underline{u}_j \underline{u}_j^T )^{-1} \underline{y} =
$$

$$
= \sum_{i=1}^p \sigma_i(X) \underline{v}_i \underline{u}_i^T (\sum_{j=1}^p \sigma_j^2(X) \underline{u}_j \underline{u}_j^T + \lambda \sum_{j=1}^p \underline{u}_j \underline{u}_j^T)^{-1} \underline{y} = \Phi^T (\Phi \Phi^T + \lambda I_p)^{-1} \underline{y} = \Phi^T \underline{\alpha}
$$

---

where $\underline{\alpha} = (\Phi \Phi^T + \lambda I_p)^{-1} \underline{y}$.
As we remarked before, the computation of $\Phi \Phi^T$ is often infeasible.
Let's inspect what this matrix is like:
$$
\Phi \Phi^T = \begin{bmatrix}
\phi(\underline{x}_1)^T \\
... \\
\phi(\underline{x}_n)^T
\end{bmatrix} \begin{bmatrix}
\phi(\underline{x}_1) & ... & \phi(\underline{x}_n)
\end{bmatrix} = \begin{bmatrix}
\phi(\underline{x}_1)^T \phi(\underline{x}_1) & ... & \phi(\underline{x}_1)^T \phi(\underline{x}_n) \\
... & ... & ... \\
\phi(\underline{x}_n)^T \phi(\underline{x}_1) & ... & \phi(\underline{x}_n)^T \phi(\underline{x}_n)
\end{bmatrix} \text{.}
$$
We're ready to introduce the kernel trick: a **kernel function** is a function
$$
k(\underline{x}_i, \underline{x}_j) = f(g(\underline{x}_i, \underline{x}_j))
$$
where $g : \mathbb{R}^p \times \mathbb{R}^p \rightarrow \mathbb{R}$ has complexity $O(p)$, $f : \mathbb{R} \rightarrow \mathbb{R}$, and such that $k(\underline{x}_i, \underline{x}_j) = \phi(\underline{x}_i)^T \phi(\underline{x}_j)$.
Once we've a kernel function which matches out feature map, it is easy to compute $\Phi \Phi^T$:
$$
\Phi \Phi^T = \begin{bmatrix}
k(\underline{x}_1, \underline{x}_1) & ... & k(\underline{x}_1, \underline{x}_n) \\
... & ... & ... \\
k(\underline{x}_n, \underline{x}_1) & ... & k(\underline{x}_n, \underline{x}_n)
\end{bmatrix} = K \text{.}
$$

Some well-known kernel functions are:
- $k(\underline{x}_i, \underline{x}_j) = (\underline{x}_i^T \underline{x}_j)^q$ where the corresponding feature map is given by all the monomials of degree $q$ in the values of the features;
- $k(\underline{x}_i, \underline{x}_j) = (\underline{x}_i^T \underline{x}_j + 1)^q$ where the corresponding feature map is given by all the monomials of degree $q$ or less in the values of the features;
- $k(\underline{x}_i, \underline{x}_j) = \exp\{ -\frac{||\underline{x}_i - \underline{x}_j||_2^2}{2 \sigma} \}$, known as the gaussian kernel, whose feature map produces a vector of infinite dimension.

Let's make a concrete example. Let $p = 2$,
$$
\phi(\begin{bmatrix} x_1 \\ x_2 \end{bmatrix}) = \begin{bmatrix}
x_1^2 \\
\sqrt{2} x_1 x_2 \\
x_2^2
\end{bmatrix} \text{.}
$$

Then
$$
\phi(\begin{bmatrix} x_{i1} \\ x_{i2} \end{bmatrix})^T \phi(\begin{bmatrix} x_{j1} \\ x_{j2} \end{bmatrix}) = \begin{bmatrix}
x_{i1}^2 & \sqrt{2}x_{i1}x_{i2} & x_{i2}^2
\end{bmatrix} \begin{bmatrix}
x_{j1}^2 \\
\sqrt{2}x_{j1}x_{j2} \\
x_{j2}^2
\end{bmatrix} =
$$

$$
= x_{i1}^2 x_{j1}^2 + 2 x_{i1}x_{i2}x_{j1}x_{j2} + x_{i2}^2x_{j2}^2 = (x_{i1}x_{j1} + x_{i2}x_{j2})^2 = (\begin{bmatrix} x_{i1} \\ x_{i2} \end{bmatrix}^T \begin{bmatrix} x_{j1} \\ x_{j2} \end{bmatrix})^2 = k(\underline{x}_i, \underline{x}_j) \text{.}
$$

---

We got rid of $\Phi$ from the expression of
$$
\underline{\alpha} = (K + \lambda I_p)^{-1} \underline{y}
$$
but it still appears in the expression of $\underline{w}_{\text{R}}$:
$$
\underline{w}_{\text{R}} = \Phi^T \underline{\alpha} \text{.}
$$

Fortunately, there is a way of making predictions without having to compute explicitly $\underline{w}_{\text{R}}$:
$$
\tilde{y} = \phi(\underline{\tilde{x}})^T \underline{w}_{\text{R}} = \underline{w}_{\text{R}}^T \phi(\underline{\tilde{x}}) = \underline{\alpha}^T \Phi \phi(\underline{\tilde{x}}) = \underline{\alpha}^T \begin{bmatrix}
\phi(\underline{x}_1)^T \\
... \\
\phi(\underline{x}_n)^T
\end{bmatrix} \phi(\underline{\tilde{x}}) =
\underline{\alpha}^T \begin{bmatrix}
k(\underline{x}_1, \underline{\tilde{x}}) \\
... \\
k(\underline{x}_n, \underline{\tilde{x}})
\end{bmatrix} \text{.}
$$

## Issues of LS for binary classification

Consider a binary classification problem with $n$ samples $\underline{x}_1, ..., \underline{x}_n \in \mathbb{R}^p$ and $n$ labels $y_1, ..., y_n \in \{ -1, 1 \}$.
Imagine to a have a **perfect** linear affine model $(\underline{w}^*, b^*)$ with $\underline{w}^* \in \mathbb{R}^p, b^* \in \mathbb{R}$, which predicts the labels in the following way:
$$
\hat{y} = \begin{cases}
1 \text{ if } \underline{\tilde{x}}^T \underline{w}^* + b^* \geq 0 \\
-1 \text{ if } \underline{\tilde{x}}^T \underline{w}^* + b^* < 0
\end{cases} \text{.}
$$
Now let's do the contrary w.r.t. what we usually do: instead of trying to look for the "best" model by minimizing the squared errors, let's compute the sum of the squared errors for a model we already know that is perfect:
$$
\sum_{i=1}^n [ y_i - (\underline{x}_i^T \underline{w}^* + b^*) ]^2 =
\sum_{i=1}^n y_i^2 [1 - \frac{1}{y_i} (\underline{x}_i^T \underline{w}^* + b^*)]^2 = 
\sum_{i=1}^n 1 \cdot [1 - y_i (\underline{x}_i^T \underline{w}^* + b^*)]^2 \text{.}
$$
The last equality follows from the fact that $y_i \in \{ -1, 1 \}$.
Now let $\underline{x}_P \in \mathbb{R}^p$ s.t. $\underline{x}_P^T \underline{w}^* = - b^*$. Then the separation boundary of the classifier is:
$$
H = \{ \underline{x} \in \mathbb{R}^p | \underline{x}^T \underline{w}^* + b^* = 0 \} = \{ \underline{x}_P + \underline{p} | \underline{p} \in \mathbb{R}^p \land \underline{p}^T \underline{w}^* = 0 \} \text{.}
$$
$\underline{w}^*$ is the direction perpendicular to $H$.
Hence, the distance of a generic point from $H$ is:
$$
|(\underline{\tilde{x}} - \underline{x}_P)^T \underline{w}^*| = |\underline{\tilde{x}}^T \underline{w}^* - \underline{x}_P^T \underline{w}^*| = |\underline{\tilde{x}}^T \underline{w}^* + b^*| \text{.}
$$

Since $\underline{w}^*$ is the model of a perfect classifier:
$$
y_i = -1 \text{ iff } \underline{x}_i^T \underline{w}^* + b^* < 0 \text{.}
$$
Then $y_i(\underline{x}_i^T \underline{w}^* + b^*) = |\underline{x}_i^T \underline{w}^* + b^*| = \text{dist}(H, \underline{x}_i)$.

---

If we substitute this result in the expression we found before for the sum of the squared errors we get:
$$
\sum_{i=1}^n [1 - \text{dist}(H, \underline{x}_i)]^2 \text{.}
$$
Hence, if a sample is **far away** from the separation boundary, the **squared error** of the perfect classifier **gets big**.
This is **bad news** since we're trying to find $\underline{w}^*$ by minimizing the sum of the squared errors, but if there are samples far from the separation boundary (which is likely and desired), $\underline{w}^*$ has an high squared error in the first place.

It is clear that the sum of the squared errors isn't a good loss function for classifications problems: we need to use other loss functions.
Some alternatives are:
- the **ideal loss**:
$$
\mathcal{I}(y_i, \underline{x}_i, \underline{w}, b) = \begin{cases}
0 \text{ if } y_i (\underline{x}_i^T \underline{w} + b) > 0 \\
1 \text{ otherwise }
\end{cases}
$$
> (_it counts the number of bad predictions_);
- the **hinge loss**:
$$
\mathcal{H}(y_i, \underline{x}_i, \underline{w}, b) = (1 - y_i (\underline{x}_i^T \underline{w} + b))_+
$$
> where
$$
(a)_+ = \begin{cases}
a \text{ if } a > 0 \\
0 \text{ otherwise}
\end{cases} \text{ for every } a \in \mathbb{R} \text{.}
$$

<p align="center">
    <img src="http://localhost:8080/naml/static/loss-functions.png" width="450mm" />
</p>

---

In the picture, we plotted the loss functions for the $i$-th sample with respect to the variable
$$
d = y_i(\underline{x}_i^T \underline{w} + b) \text{.} 
$$

In particular:
- the expression for the LS loss becomes $\mathcal{L}(d) = (1-d)^2$;
- the expression for the ideal loss becomes $\mathcal{I}(d) = \text{step}(-d)$;
- the expression for the hinge loss becomes $\mathcal{H}(d) = (1-d)_+$.

Observe that:
- if $d > 0$, then the sample is correctly classified (as we have seen before);
- if $d > 1$ both $\mathcal{H}$ and $\mathcal{I}$ have value 0 (as it should be), whereas $\mathcal{L}$ increases (it is the phenomenon that we have seen before);
- if $d < 0$, then the sample has been classified incorrectly: $\mathcal{I}$ gives a contribution of 1, $\mathcal{H}$ gives a contribution linear in $d$ and $\mathcal{L}$ gives a contribution quadratic in $d$;
- if $d \in (0, 1)$, then $\mathcal{I}$ gives no contribution but $\mathcal{H}$ still does. Remember that, **for a perfect classifier**, $d$ is the **distance from the separation boundary**. This is very important, since it is the reason why $\mathcal{H}$ penalizes models that classify correctly the samples but where there are samples close to the separation boundary. Hence a model obtained by minimizing the hinge loss is more robust since there are no samples close to the sepration boundary: then small perturbations do not alter the classification.
This is the idea that leads to **SVM** (Suppoer Vector Machines) (_usually in conjunction with kernel functions_).

Finally, the hinge loss is usually preferred over the ideal one because the discontinuity in the ideal loss leads to problems in the minimization technique which has to be numerical.
