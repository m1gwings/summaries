---
marp: true
theme: summary
math: mathjax
---
# Introduction to ML

<div class="author">

Cristiano Migali
(_adapted from the slides of Prof. Marcello Restelli_)

</div>

Kernel methods are _memory-based methods_: the **training data** are used in the **prediction phase**. For this reason they are **fast to train** and **slow to predict**. They require the definition of a metric which captures the "distance" between two input samples w.r.t. to the learning task.

There are Kernel methods both for regression and classification.
In particular, Kernel methods are used when we want to **capture non-linear relationships** in the data:
- in a regression task the input-output relationship may be not linear (_nonlinear regression_);
- in a classification task the decision boundary may be not linear (_nonlinear classification_).

As we know from linear regression, this is achieved by _mapping data to an higher dimension space_ where it exhibits linear patterns. Then we apply a linear model in the new input space. Mapping consists in changing the **feature representation**. This operation can be **expensive** to compute if we do it in the "naive" way illustrated when we talked about linear regression. Instead, in Kernel methods such mapping is (almost) free thanks to se-called Kernel trick!

To understand the Kernel trick and how Kernel methods work, we need to define **kernel functions**.
- A **kernel function** is a function $k(\underline{x}, \underline{x}')$ s.t. there exists a feature mapping $\underline{\phi}$ which satisfies:
$$
k(\underline{x}, \underline{x}') = \underline{\phi}^T(\underline{x}) \underline{\phi}(\underline{x}') \ \forall \underline{x}, \underline{x}'.
$$
Many linear **parametric** models can be re-cast into an equivalent **dual representation** where the predictions are based ona **kernel function** evaluated at **training points**.

- Observe that the definition implies that a **kernel function** is **symmetric**:
$$
k(\underline{x}, \underline{x}') = \underline{\phi}^T(\underline{x}) \underline{\phi}(\underline{x}') = \underline{\phi}^T(\underline{x}') \underline{\phi}(\underline{x}) = k(\underline{x}', \underline{x}) \ \forall \underline{x}, \underline{x}'.
$$

Kernel function can be interpreted as a **similarity value** between $\underline{x}$, and $\underline{x}'$ w.r.t. the learning task to solve.

- The simplest kernel function is the scalar product where the feature mapping is the identity mapping (it is also called _linear kernel_):
$$
k(\underline{x}, \underline{x}') = \underline{x}^T \underline{x}'.
$$

---

There are some other very common **shapes of kernel functions**.

- A **stationary kernel** is a function of the difference between arguments:
$$
k(\underline{x}, \underline{x}') = k_\text{stat}(\underline{x} - \underline{x}').
$$
> The names comes from the fact that it is invariant to translations in the input space.

- An **homogeneous kernel**, also known as a **radial basis function** has the shape:
$$
k(\underline{x}, \underline{x}') = k_\text{rad}(||\underline{x} - \underline{x}'||).
$$
> It depends only on the magnitude of the distance between the arguments.

Note tat the kernel function is a **scalar** value while $\underline{x}$ is an $M$-dimensional vector.

## Kernel trick on ridge regression

[_I will adopt a slightly different treatment than that on the slides/book in order to apply duality in a clearer (at least to me) way_].
We can express the Ridge regression problem in constrained form (_remember the "equivalence" with penalty form which can be obtained by comparing the optimality conditions: KKT/stationarity_) as follows:
$$
\min_{\underline{w}, \underline{\xi}} \frac{1}{2} || \underline{\xi} ||_2^2
$$
$$
\text{s.t.}
$$
$$
\underline{\xi} = \Phi \underline{w} - \underline{t}
$$
$$
\frac{1}{2}|| \underline{w} ||_2^2 \leq \frac{B^2}{2}
$$
where $B \in \mathbb{R}$ is a parameter.

The lagrangian of this problem is:
$$
\mathcal{L}(\underline{w}, \underline{\xi}, \underline{\beta}, \lambda) = \frac{1}{2} \underline{\xi}^T \underline{\xi} + \underline{\beta}^T(\underline{\xi} + \underline{t} - \Phi \underline{w}) + \lambda (\frac{1}{2} ||\underline{w}||_2^2 - \frac{B^2}{2} ).
$$
Observe that, if we fix $\underline{\beta}$ and $\lambda \geq 0$, the function is convex in $\underline{w}$ and $\underline{\xi}$. We can find the corresponding global minimum thanks to the NS optimality condition:
$$
\begin{cases}
\nabla_{\underline{w}} \mathcal{L}(\underline{w}, \underline{\xi}, \underline{\beta}, \lambda) = \lambda \underline{w} - \Phi^T \underline{\beta} = \underline{0} \\
\nabla_{\underline{\xi}} \mathcal{L}(\underline{w}, \underline{\xi}, \underline{\beta}, \lambda) = \underline{\xi} + \underline{\beta} = \underline{0}
\end{cases}.
$$

---

Hence:
$$
\begin{cases}
\underline{w} = \frac{1}{\lambda} \Phi^T \underline{\beta} \\
\underline{\xi} = - \underline{\beta}
\end{cases}.
$$
**Important remark**: it is not a problem that we're dividing by $\lambda$, as we will see later, we will fix $B$ s.t. at optimality $\lambda$ has a value chosen by us, which we'll choose strictly positive. Hence, in what follows, we will assume $\lambda > 0$.

We can plug the expression for $\underline{w}$ and $\underline{\xi}$ to get the objective function of the lagrangian dual problem:
$$
\max_{\underline{\beta}, \lambda} \frac{1}{2} \underline{\beta}^T \underline{\beta} - \underline{\beta}^T \underline{\beta} + \underline{\beta}^T \underline{t} - \frac{1}{\lambda} \underline{\beta}^T \Phi \Phi^T \underline{\beta} + \frac{1}{2 \lambda} \underline{\beta}^T \Phi \Phi^T \underline{\beta} - \lambda \frac{B^2}{2} = - \frac{1}{2} \underline{\beta}^T \underline{\beta} - \frac{1}{2\lambda} \underline{\beta}^T \Phi \Phi^T \underline{\beta} + \underline{\beta}^T \underline{t} - \lambda \frac{B^2}{2}
$$
$$
\text{s.t.}
$$
$$
\lambda \geq 0.
$$

Observe that, as we know from the theory, the dual objective function is concave. Hence again we have a NS condition for the optimality of the unconstrained objective function. Remember that, because of the important remark, the global optimum will be such that $\lambda > 0$, hence it will also solve the constrained optimization problem.
Before solving the dual problem, let's introduce some notation.
- We define **Gram matrix** $K = \Phi \Phi^T$ the matrix:
$$
K = \Phi \Phi^T = \begin{bmatrix} \underline{\phi}^T(\underline{x_1}) \\ \vdots \\ \underline{\phi}^T(\underline{x_N}) \end{bmatrix} \begin{bmatrix} \underline{\phi}(\underline{x_1}) & \cdots & \underline{\phi}(\underline{x_N}) \end{bmatrix} = \begin{bmatrix} \underline{\phi}^T(\underline{x}_1) \underline{\phi}(\underline{x}_1) & \cdots & \underline{\phi}^T(\underline{x}_1) \underline{\phi}(\underline{x}_N) \\
\vdots & \vdots & \vdots \\
\underline{\phi}^T(\underline{x}_N) \underline{\phi}(\underline{x}_1) & \cdots & \underline{\phi}^T(\underline{x}_N) \underline{\phi}(\underline{x}_N) \end{bmatrix} =
$$
$$
= \begin{bmatrix} k(\underline{x}_1, \underline{x}_1) & \cdots & k(\underline{x}_1, \underline{x}_N) \\ \vdots & \vdots & \vdots \\ k(\underline{x}_N, \underline{x}_1) & \cdots & k(\underline{x}_N, \underline{x}_N) \end{bmatrix}.
$$

Furthermore, let:
$$
\underline{\alpha} = \frac{1}{\lambda} \underline{\beta},
$$
which implies: $\underline{w} = \Phi^T \underline{\alpha}$. The dual problem becomes ($\underline{\beta} = \lambda \underline{\alpha}$):
$$
\max_{\underline{\alpha},\lambda} - \frac{\lambda^2}{2} \underline{\alpha}^T \underline{\alpha} - \frac{\lambda}{2} \underline{\alpha}^T K \underline{\alpha} + \lambda \underline{\alpha}^T \underline{t} - \lambda \frac{B^2}{2}
$$
$$
\text{s.t.}
$$
$$
\lambda \geq 0.
$$

---

Let's solve find the global minimizer of the unconstrained dual objective function by enforcing the NS optimality condition (stationarity):
$$
\begin{cases}
- \lambda^2 \underline{\alpha} - \lambda K \underline{\alpha} + \lambda \underline{t} = \underline{0} \\
- \lambda \underline{\alpha}^T \underline{\alpha} - \frac{\alpha^T K \underline{\alpha}}{2} + \underline{t}^T \underline{\alpha} - \frac{B^2}{2} = 0
\end{cases} \text { iff }
\begin{cases}
\underline{\alpha}^* = (K + \lambda^* I)^{-1} \underline{t} \\
{\underline{\alpha}^*}^T K {\underline{\alpha}^*} - {\underline{\alpha}^*}^T( \lambda \underline{\alpha}^* + K \underline{\alpha}^* - \underline{t}) - \frac{{\underline{\alpha}^*}^T K \underline{\alpha}^*}{2} = \frac{B^2}{2}
\end{cases} \text{ iff }
$$
$$
\text{ iff } \begin{cases}
\underline{\alpha}^* = (K + \lambda^* I)^{-1} \underline{t} \\
\frac{{\underline{\alpha}^*}^T K {\underline{\alpha}^*}}{2} - {\underline{\alpha}^*}^T( \underline{t} - \underline{t}) = \frac{B^2}{2}
\end{cases} \text{ iff } \begin{cases}
\underline{\alpha}^* = (K + \lambda^* I)^{-1} \underline{t} \\
{\underline{\alpha}^*}^T K {\underline{\alpha}^*} = B^2
\end{cases} \text{ iff }
\begin{cases}
\underline{\alpha}^* = (K + \lambda^* I)^{-1} \underline{t} \\
B = \sqrt{{\underline{\alpha}^*}^T K {\underline{\alpha}^*}}
\end{cases}.
$$
Observe that $K$ is positive semi-definite by construction, hence $B$ is well defined. As you can see, we can choose the $\lambda^* > 0$ that we prefer.

[Check KKTs, resume...].
