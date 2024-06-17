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
**Important remark**: dealing with the case $\lambda = 0$ gets messy and I haven't found any source online which does it (_and I've no time for it_). In principle one as to define the dual objective function by cases, finding the minimizer of the lagrangian when $\lambda = 0$. Unfortunately the optimality conditions for $\lambda = 0$ require $\Phi^T \underline{\beta} = 0$, which is a somewhat hard condition to deal with because we don't have the guarantee that the rows of $\Phi$ are linearly independent. Hence, in what follows, we will assume $\lambda > 0$. Furthermore, at the end, instead of solving for $\lambda$, we will fix a value for $B$ s.t. the optimization problem has the solution $\lambda^*$ chosen by us. Anyway, in principle, we should also check that the obtained dual objective function value (for the chosen $\lambda^*$) is greater or equal than the case $\lambda = 0$, but we can't since I have no time to solve that case.

We can plug the expression for $\underline{w}$ and $\underline{\xi}$ to get the objective function of the lagrangian dual problem:
$$
\max_{\underline{\beta}, \lambda} \frac{1}{2} \underline{\beta}^T \underline{\beta} - \underline{\beta}^T \underline{\beta} + \underline{\beta}^T \underline{t} - \frac{1}{\lambda} \underline{\beta}^T \Phi \Phi^T \underline{\beta} + \frac{1}{2 \lambda} \underline{\beta}^T \Phi \Phi^T \underline{\beta} - \lambda \frac{B^2}{2} = - \frac{1}{2} \underline{\beta}^T \underline{\beta} - \frac{1}{2\lambda} \underline{\beta}^T \Phi \Phi^T \underline{\beta} + \underline{\beta}^T \underline{t} - \lambda \frac{B^2}{2}
$$
$$
\text{s.t.}
$$
$$
\lambda \geq 0 \text{ (actually the expression is valid only for } \lambda > 0 \text{)}.
$$

Observe that, as we know from the theory, the dual objective function is concave. Hence again we have a NS condition for the optimality of the unconstrained objective function. Remember that, because of the important remark, the global optimum will be such that $\lambda > 0$ (_we choose it_), hence it will also solve the constrained optimization problem.
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

---

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


Let's find the global minimizer of the unconstrained dual objective function by enforcing the NS optimality condition (stationarity):
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

Finally, thanks to Slater's conditions, we have strong duality. Hence, by p. 242, 248 _Convex Optimization by Boyd, Vandenberghe: complementary slackness, solving the primal problem via the dual_, we know that every optimal solution of the primal problem is a minimizer of $\mathcal{L}(\underline{w}, \underline{\xi}, \underline{\alpha}^*, \lambda^*)$ (_where $\underline{\alpha}^*, \lambda^*$ are fixed_).
Furthermore, $\mathcal{L}$ is strictly convex in $\underline{w}, \underline{\xi}$ for every fixed $\underline{\alpha}, \lambda$, hence, the minimizer is UNIQUE.
The primal problem is clearly feasible hence at least a solution exits, which thus must correspond to the minimizer of $\mathcal{L}(\underline{w}, \underline{\xi}, \underline{\alpha}^*, \lambda^*)$ because of the uniqueness.
We know the expression of the minimizer of $\mathcal{L}(\underline{w}, \underline{\xi}, \underline{\alpha}^*, \lambda^*)$ since we used it to build the dual objective function:
$$
\begin{cases}
\underline{w}^* = \Phi^T \underline{\alpha}^* \\
\underline{\xi}^* = - \lambda \underline{\alpha}^*
\end{cases}.
$$

This means that $\underline{w}^* = \Phi^T \underline{\alpha}^*$ are the optimal parameters for the primal problem.

Observe that $\underline{\alpha}^*$ depends only on the targets and the Gram matrix: the features completely disappeared. We want to do the same with the expression for the **prediction**:
$$
y(\underline{x}) = {\underline{w}^*}^T \underline{\phi}(\underline{x}) = {\underline{\alpha}^*}^T \Phi \underline{\phi}(\underline{x}) = {\underline{\alpha}^*}^T \begin{bmatrix} \underline{\phi}^T(\underline{x}_1) \\ \vdots \\ \underline{\phi}^T(\underline{x}_N) \end{bmatrix} \underline{\phi}(\underline{x}) = {\underline{\alpha}^*}^T \begin{bmatrix} k(\underline{x}_1, \underline{x}) \\ \vdots \\ k(\underline{x}_N, \underline{x}) \end{bmatrix} = {\underline{\alpha}^*}^T \underline{k}(\underline{x})
$$
where $\underline{k}(\underline{x}) = \begin{bmatrix} k(\underline{x}_1, \underline{x}) & \cdots & k(\underline{x}_N, \underline{x}) \end{bmatrix}^T$. Hence we can do also predictions without explicitly computing the features.

---

**Remark**: we can write the prediction as:
$$
y(\underline{x}) = \underline{k}^T(\underline{x}) (K + \lambda^* I)^{-1} \underline{t}.
$$
Hence the prediction is a **linear combination** of the **target** values from the training set, where the coefficients depend on the kernel. This gives an hint on why we must choose the kernel function as a metric of similarity between the inputs w.r.t. the learning task.

**Final remarks**: instead of inverting an $M \times M$ matrix ($\Phi^T \Phi + \lambda I$) as in standard ridge regression, we're inverting an $N \times N$ matrix ($K + \lambda I$). This could seem a disadvantage. But, in this way:
- we can avoid to compute the features explicitly (_which can be very expensive in some cases_);
- we can work in infinite dimensional feature spaces (_as we will see_);
- we can work with inputs which aren't necessarily vectors of real numbers: kernel functions can be defined also over **objects** as diverse as graphs, sets, string, and text documents.

Of course all of this relies on the assumption that we have a **valid kernel function**, i.e. which can be decomposed as the scalar product between the feature maps.

## Constructing kernels

The most intuitive way to construct a kernel is to apply directly the definition. We can **choose a feature space mapping** $\underline{\phi}(\underline{x})$ and use it to find the corresponding kernel:
$$
k(\underline{x}, \underline{x}') = \underline{\phi}^T(\underline{x}) \underline{\phi}(\underline{x}').
$$
Of course computing the kernel function in this way cancels all the advantages of kernel methods since we have to explicitly compute the features.
Indeed, there are smarter ways to compute kernels. Consider the following kernel function in a two dimensional space ($\underline{x}, \underline{z} \in \mathbb{R}^2$):
$$
k(\underline{x}, \underline{z}) = (\underline{x}^T \underline{z})^2 = (x_1 z_1 + x_2 z_2)^2 = x_1^2 z_1^2 + 2 x_1 z_1 x_2 z_2 + x_2^2 z_2^2 =
$$
$$
= \begin{bmatrix} x_1^2 & \sqrt{2} x_1 x_2 & x_2^2 \end{bmatrix} \begin{bmatrix} z_1^2 \\ \sqrt{2} z_1 z_2 \\ z_2^2 \end{bmatrix} = \underline{\phi}^T(\underline{x}) \underline{\phi}(\underline{z})
$$
where $\underline{\phi}(\underline{x}) = \begin{bmatrix} x_1^2 & \sqrt{2} x_1 x_2 & x_2^2 \end{bmatrix}^T$.
In this case the computation of the kernel function requires 2 multiplications, a sum, and a squaring, while the scalar product between the feature maps requires 2+2+3 multiplications (considering also the multiplication by $\sqrt{2}$), 4 squarings and 2 sums.

---

It is possible to **generalize this result**:
$$
k(\underline{x}, \underline{z}) = (\underline{x}^T \underline{z} + c)^p
$$
has an associated feature map with all the monomial terms up to degree $p$.

### Necessary and sufficient conditions

Now we're going to provide some conditions to test if a generic function is a kernel, without having to find explicitly a corresponding feature map.

- A **necessary and sufficient** for a function $k(\underline{x}, \underline{x}')$ to be a kernel is that the Gram matrix $K$ is positive semi-definite for all possible choices of the set $\{ \underline{x}_1, \ldots, \underline{x}_N \}$.

- **Mercer's theorem**: **any** continuous, symmetric, positive semi-definite kernel function $k(\underline{x}, \underline{y})$ can be expressed as a **dot product** in a high-dimensional space. In particular, with $k(\underline{x}, \underline{y})$ positive semi-definite, we mean that the associated Gram matrix is positive definite for any set of inputs.

### Composing kernels

There are also some theorems which allow us to construct new kernels from other simpler kernels.

- **Theorem**: given valid kernels $k_1(\underline{x}, \underline{x}')$, $k_2(\underline{x}, \underline{x}')$, $k_3$, $k_a$, $k_b$, the following new kernels will be valid.
> 1. $k(\underline{x}, \underline{x}') = c k_1(\underline{x}, \underline{x}')$ where $c \geq 0$;
> 2. $k(\underline{x}, \underline{x}') = f(\underline{x}) k_1(\underline{x}, \underline{x}')f(\underline{x}')$ where $f$ is any function;
> 3. $k(\underline{x}, \underline{x}') = q(k_1(\underline{x}, \underline{x}'))$, where $q$ is a polynomial with non-negative coefficients;
> 4. $k(\underline{x}, \underline{x}') = \exp(k_1(\underline{x}, \underline{x}'))$;
> 5. $k(\underline{x}, \underline{x}') = k_1(\underline{x}, \underline{x}') + k_2(\underline{x}, \underline{x}')$;
> 6. $k(\underline{x}, \underline{x}') = k_1(\underline{x}, \underline{x}') k_2(\underline{x}, \underline{x}')$;
> 7. $k(\underline{x}, \underline{x}') = k_3(\underline{\phi}(\underline{x}), \underline{\phi}(\underline{x}'))$, where $\underline{\phi}(\underline{x})$ is a function from $\underline{x}$ to $\mathbb{R}^M$;
> 8. $k(\underline{x}, \underline{x}') = \underline{x}^T A \underline{x}'$, where $A$ is a symmetric positive semi-definite matrix;
> 9. $k(\underline{x}, \underline{x}') = k_a(\underline{x}_a, \underline{x}_a') + k_b(\underline{x}_b, \underline{x}_b')$, where $\underline{x}_a$ and $\underline{x}_b$ are variables with $\underline{x} = \begin{bmatrix} \underline{x}_a^T & \underline{x}_b^T \end{bmatrix}^T$;
> 10. $k(\underline{x}, \underline{x}') = k_a(\underline{x}_a, \underline{x}_a')k_b(\underline{x}_b, \underline{x}_b')$.

A kernel which is often used it the **Gaussian kernel**:
$$
k(\underline{x}, \underline{x}') = \exp(-\frac{||\underline{x} - \underline{x}'||_2^2}{2 \sigma^2}).
$$
Let's prove that it is a valid kernel:
$$
||\underline{x} - \underline{x}'||_2^2 = \underline{x}^T \underline{x} + \underline{x}'^T \underline{x} - 2 \underline{x}^T \underline{x}'.
$$

---

Let $f(\underline{x}) = \exp(-\frac{\underline{x}^T \underline{x}}{2 \sigma^2})$. Then:
$$
k(\underline{x}, \underline{x}') = f(\underline{x}) \exp\left(\frac{\underline{x}^T \underline{x}'}{\sigma^2}\right) f(\underline{x}')
$$
is valid because of: the validity of the linear kernel, property 1, property 4, and, finally, property 2.

It can be extended to non-euclidean distances:
$$
k(\underline{x}, \underline{x}') = \exp\left(-\frac{1}{2 \sigma^2}\left( k(\underline{x}, \underline{x}) + k(\underline{x}', \underline{x}'-2k(\underline{x}, \underline{x}')) \right)\right).
$$

### Kernels for symbolic data

As we remarked before, kernels can be extended to inputs that are **symbolic**, rather than simply vectors of real numbers. For example, a simple kernel over sets could be:
$$
k(A_1, A_2) = 2^{|A_1 \cap A_2|}.
$$

### Kernels based on Generative models

Given a generative model $p(\underline{x})$, we define a kernel by:
$$
k(\underline{x}, \underline{x}') = p(\underline{x}) p(\underline{x}').
$$
It is a valid kernel since it is an inner product in the one-dimensional feature space defined by the mapping $p(\underline{x})$.
In particular, two inputs $\underline{x}$ and $\underline{x}'$ are similar if they have high probabilities.

## Gaussian processes

We have seen how to apply kernel methods to linear regression.
Now we will see how to apply kernel methods to Bayesian linear regression.
In the standard Bayesian linear regression setting we introduced a prior over the parameters $\underline{w}$. This prior induced a posterior distribution over the (_parameters of the_) regression functions, which allowed at the end to compute the predictive distribution for the target given the input. [_See Linear regression, p. 13_].

In this case we will directly define a **prior** probability distribution over the space of regression functions. Since it is hard to deal with distributions over the uncountable infinite space of functions, we will define the probability distribution for the output of such functions after fixing the input. In particular the inputs will correspond to the points $\underline{x}_1, \ldots, \underline{x}_N$ in the training set. In this way we get back to work in a finite dimensional space.

In particular we defined the prior $p(\underline{w}) = \mathcal{N}(\underline{w}|\underline{0}, \tau I)$.

---

The output of the corresponding regression functions, for fixed parameters $\underline{w}$ and inputs $\underline{x}_1, \ldots, \underline{x}_N$ is:
$$
\underline{y} = \Phi \underline{w}.
$$
Hence:
$$
p(\underline{y}) = \mathcal{N}(\underline{y}|\Phi \underline{0}, \tau \Phi I \Phi^T) = \mathcal{N}(\underline{y}|\underline{0},K)
$$
where $K = \tau \Phi \Phi^T$ is the Gram matrix (observe that, if we multiply by $\tau \geq 0$ we still have a kernel).

In particular a **Gaussian process** is defined as a **probability distribution over functions $\underline{y}(\underline{x})$** such that the set of values of $\underline{y}(\underline{x})$ evaluated at an arbitrary set of points $\underline{x}_1, \ldots, \underline{x}_N$ **jointly have a Gaussian distribution**.
As we know this distribution is completely specified by the second-order statistics: the mean and the covariance matrix. In particular we will choose mean $\underline{0}$ and covariance matrix $K$ as shown before.

Furthermore, as in the usual Bayes linear regression setting, we assume that:
$$
p(t|y(\underline{x})) = \mathcal{N}(t|y(\underline{x}), \sigma^2).
$$

Because the noise is **independent** on each data point, the joint distribution of the targets is still Gaussian:
$$
p(\underline{t}|\underline{y}) = \mathcal{N}(\underline{t}|\underline{y}, \sigma^2 I_N).
$$
Because of property $(A)$ of Gaussian vectors [_see Linear regression, p. 12_]:
$$
p(\underline{t}) = \mathcal{N}(\underline{t}|\underline{0}, K + \sigma^2 I_N) = \mathcal{N}(\underline{t}|\underline{0}, C)
$$
where $C = K + \sigma^2 I_N$.

Now let's understand how we can derive the predictive distribution.
But before we need another property of Gaussian vectors.

- **Theorem**: given a joint Gaussian distribution $\mathcal{N}(\underline{x}|\underline{\mu}, \Sigma)$ with:
$$
\underline{x} = \begin{bmatrix} \underline{x}_a \\ \underline{x}_b \end{bmatrix}, \underline{\mu} = \begin{bmatrix} \underline{\mu}_a \\ \underline{\mu}_b \end{bmatrix},
\Sigma = \begin{bmatrix}
\Sigma_{aa} & \Sigma_{ab} \\
\Sigma_{ba} & \Sigma_{bb}
\end{bmatrix}
$$
> we have that:
$$
p(\underline{x}_a|\underline{x}_b) = \mathcal{N}(\underline{x}|\underline{\mu}_{a|b}, \Sigma_{a|bss})
$$
> with $\underline{\mu}_{a|b} = \underline{\mu}_a + \Sigma_{ab} \Sigma_{bb}^{-1} (\underline{x}_b - \underline{\mu}_b)$, $\Sigma_{a|b} = \Sigma_{aa} - \Sigma_{ab} \Sigma_{bb}^{-1} \Sigma_{ba}.$

---

Now, let $\underline{t}_{N+1} = \begin{bmatrix} t_{N+1} \\ t_1 \\ \vdots \\ t_N \end{bmatrix}$. Then, because of the previous expression for $p(\underline{t})$ and the usual definition for $\underline{k} = \begin{bmatrix} k(\underline{x}_1, \underline{x}_{}N+1) & \cdots & k(\underline{x}_N, \underline{x}_{N+1}) \end{bmatrix}^T$. Then:
$$
p(\underline{t}_{N+1}) = \mathcal{N}(\underline{t}_{N+1}|\underline{0}, C_{N+1})
$$
where:
$$
C_{N+1} = \begin{bmatrix} k(\underline{x}_{N+1}, \underline{x}_{N+1}) + \sigma^2 & \underline{k}^T \\ \underline{k} & C_N \end{bmatrix} = \begin{bmatrix} c & \underline{k}^T \\ \underline{k} & C_N \end{bmatrix}
$$
with $c = k(\underline{x}_{N+1}, \underline{x}_{N+1}) + \sigma^2, C_N = K_N + \sigma^2 I_N$.

Then, because of the property of Gaussian vectors which we just refreshed:
$$
p(t_{N+1}|\underline{t}_N) = \mathcal{N}(t_{N+1}, 0+\underline{k}^T C_N^{-1}(\underline{t}_N - \underline{0}), c - \underline{k}^T C_N^{-1} \underline{k}) = \mathcal{N}(t_{N+1}|\underline{k}^T C_N^{-1} \underline{t}_N, c-\underline{k}^T C_N^{-1} \underline{k}).
$$

Hence we can make predictions by computing: $\underline{k}^T C_N^{-1} \underline{t}_N$. We need to invert the matrix $C_N$, with a cost of $O(N^3)$, but this inversion has to be done only one for the given training set.
Then, the computation of the mean has a cost $O(N)$, while the computation of the variance costs $O(N^2)$. For large training sets this computations are carried out through **approximated methods**.

The performance of a GP is strongly affected by the choice of **parameters** for the kernels. The choice of the kernel parameters is a **model selection** problem:
- we can consider a discrete grid of values and use **cross-validation** (it is robust, but slow);
- we can maximize the **marginal likelihood** using gradient optimization.
