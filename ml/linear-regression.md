---
marp: true
theme: summary
math: mathjax
---
# Linear regression

<div class="author">

Cristiano Migali
(_adapted from the slides of Prof. Marcello Restelli_)

</div>

**Remember**: the goal of _regression_ is to learn a _mapping_ from the input $\underline{x}$ to the output $t$ (_usually_) continuous, which belongs to a metric space.

- We define **linear model** a function $y(\underline{x}, \underline{w})$ which is _linear in the parameters_. That is, fixed any input $\underline{\overline{x}}$, the function $y(\underline{\overline{x}}, \cdot)$ is _linear_.

The **simplest linear model** is:
$$
y(\underline{x}, \underline{w}) = w_0 + \sum_{j=1}^D w_j x_j = \underline{w}^T \underline{x}_{\text{ext}}
$$
where $\underline{x}_\text{ext} = \begin{bmatrix} 1 & \underline{x}^T \end{bmatrix}^T$.

- In **linear regression** we apply a linear model to solve a regression problem.

Despite its simplicity, linear regression has many **advantages**:
- many real processes can be **approximated** with linear models;
- linear regression problems can be solved **analytically**;
- linear prediction provides an introduction to many of the **core concepts** of ML;
- as we will see, it can model _non-linear relations_ between $\underline{x}$ and $t$.

**Remember**: the first step in a supervised learning problem (like regression) is to define a metric to evaluate our model, i.e. we need to define a loss function $L$.

Furthermore, since we're dealing with random variables we need to take it into account through expectation. In particular, once we defined a loss function $L$, we can evaluate a given model $y$ through its expected loss:
$$
\mathbb{E}[L] = \int \int L(t, y(\underline{x})) p(\underline{x}, t) d\underline{x} dt \text{.}
$$
- A common choice for $L$ is the **squared loss function**:
$$
L(t, y(\underline{x})) = (t - y(\underline{x}))^2.
$$
Our aim is to find a model in our hypothesis space $\mathcal{H}$ (in this case the set of linear models with a fixed set of features [_see later_]) that minimizes $\mathbb{E}[L]$.

- **Theorem**: the model which minimizes the squared loss function is the _conditional average_ $y(\underline{x}) = \mathbb{E}[t|\underline{x}]$.

---

- **Proof**: (_remember that $\mathbb{E}[t|\underline{x}]$ is NOT a function of $t$_)

$$
\mathbb{E}[L] = \int \int (\tau - y(\underline{x}))^2 p(\underline{x}, \tau) d\underline{x} d\tau = \int \int (\tau - \mathbb{E}[t|\underline{x}] + \mathbb{E}[t|\underline{x}] - y(\underline{x}))^2 p(\underline{x}, \tau) d\underline{x} d\tau = 
$$

$$
= \int \int (\tau - \mathbb{E}[t|\underline{x}])^2 p(\underline{x}, \tau) d\underline{x} d\tau + \int \int (\mathbb{E}[t|\underline{x}] - y(\underline{x}))^2 p(\underline{x}, \tau) d\underline{x} +
$$

$$
+ 2 \int \int (\tau - \mathbb{E}[t|\underline{x}])(\mathbb{E}[t|\underline{x}] - y(\underline{x})) p(\underline{x}, \tau) d\underline{x} d\tau = \int \int (\tau - \mathbb{E}[t|\underline{x}])^2 p(\underline{x}, \tau) d\underline{x} d\tau + 
$$

$$
+ \int \int (\mathbb{E}[t|\underline{x}] - y(\underline{x}))^2 p(\underline{x}, \tau) d\underline{x} + 2 \int (\mathbb{E}[t|\underline{x}] - y(\underline{x})) \left( \int \tau p(\tau|\underline{x}) d\tau - \mathbb{E}[t|\underline{x}] \cdot 1 \right) p(\underline{x}) d\underline{x} =
$$

$$
= \int \int (\tau - \mathbb{E}[t|\underline{x}])^2 p(\underline{x}, \tau) d\underline{x} d\tau + \int \int (\mathbb{E}[t|\underline{x}] - y(\underline{x}))^2 p(\underline{x}, \tau) d\underline{x} + 0 \geq
$$

$$
\geq \int \int (\tau - \mathbb{E}[t|\underline{x}])^2 p(\underline{x}, \tau) d\underline{x} d\tau .
$$

- A simple generalization of the squared loss is the **Minkowski** loss:
$$
\mathbb{E}[L] = \int \int |t - y(\underline{x})|^q p(\underline{x}, t) d\underline{x} dt
$$
> where $q \in \mathbb{R}^+$.

- **Theorem**: the model which minimizes the Minkowski loss is:
> - the _conditional mean_ for $q = 2$ (what we just proved);
> - the _conditional median_ for $q = 1$;
> - the _conditional mode_ for $q \rightarrow 0^+$.

- **Proof**: maybe one day, I don't know calculus of variations YET! (: D)

**Important remark**: even though we want to minimize the expected loss $\mathbb{E}[L]$, we can't compute it. Indeed, in order to compute $\mathbb{E}[L]$, we need to know $p(\underline{x}, t)$. But, if we knew $p(\underline{x}, t)$ the problem would be solved: we know the analytic expression of the function that minimizes the expected loss for a given loss function (according to the previous theorems), and we can compute it from $p(\underline{x}, t)$. Indeed, in ML problems, $p(\underline{x}, t)$ is never known. The only thing that we can do is try to estimate the expected loss of a given model from the available training data-set. Usually we look for the model in the chosen hypothesis space that minimizes such estimate. Anyway, we've to always keep in mind that what we're minimizing is an empirical estimate, but what we want to minimize is the (_ideal_) expected loss. The two minimizations do not necessarily coincide (of course), and this mismatch is the core problem with which ML has to deal.

The last theorems and the remark allow us to characterize three **different approaches to regression**.

---

- In the **generative approach** we try to model the _joint density_ $p(\underline{x}, t)$ from the data, then we infer the _conditional density_ $p(t|\underline{x})$, and use it to compute the conditional mean $\mathbb{E}[t|\underline{x}]$.

- In the **discriminative approach** we try to model the _conditional density_ $p(t|\underline{x})$ and use it to compute the conditional mean $\mathbb{E}[t|\underline{x}]$.

- In the **direct approach** we find a regression function $y(\underline{x})$ directly from the training data.

We can easily generalize the simple linear model that we defined previously to account for non-linear relations between $\underline{x}$ and $t$. We just need to introduce a set of (scalar) **basis functions** (or features) $\phi_1(\underline{x}), \ldots, \phi_{M-1}(\underline{x})$. The general linear model is defined as:
$$
y(\underline{x}, \underline{w}) = w_0 + \sum_{j=1}^{M-1} w_j \phi_j(\underline{x}) = \underline{w}^T \underline{\phi}(\underline{x})
$$
where $\underline{\phi}(\underline{x}) = \begin{bmatrix} 1 & \phi_1(\underline{x}) & \ldots & \phi_{M-1}(\underline{x}) \end{bmatrix}^T$.
Indeed, the features can be non-linear without compromising the linearity of the model according to the given definition.

## Minimizing least squares

Once we have fixed an hypothesis space $\mathcal{H}$, which for linear models coincides with the choice of the basis functions, the most common approach to linear regression is to minimize the <u>empirical</u> squared loss:
$$
L(\underline{w}) = \frac{1}{2} \sum_{n=1}^N (y(\underline{x}_n, \underline{w}) - t_n)^2
$$
where $\mathcal{D} = \{ (\underline{x}_1, t_1), \ldots, (\underline{x}_n, t_n) \}$ is the given training set. (_The $\frac{1}{2}$ factor, as every other multiplicative positive constant, does not alter the set of minima of $L(\underline{w})$; it is there only for convenience in the expressions that we're going to derive_).

- We define **Residual Sum of Squares** the quantity:
$$
\text{RSS}(\underline{w}) = ||\underline{\varepsilon}||_2^2 = \sum_{n=1}^N \varepsilon_n^2,
$$
> with $\varepsilon_n = t_n - y(\underline{x}_n, \underline{w})$.

Hence: $L(\underline{w}) = \frac{1}{2} \text{RSS}(\underline{w})$.
_As remarked before_, we can compute the minimizer of $L$ explicitly. For doing so, it is convenient to rewrite $L$ in "matrix form".

---

Let:
- $\underline{t} = \begin{bmatrix} t_1 \\ \vdots  \\ t_N \end{bmatrix}$;

- $\Phi = \begin{bmatrix} \underline{\phi}^T(\underline{x_1}) \\ \cdots \\ \underline{\phi}^T(\underline{x}_N) \end{bmatrix}$;

then:
$$
\underline{\varepsilon} = \begin{bmatrix} t_1 - y(\underline{x}_1, \underline{w}) \\ \vdots \\ t_N - y(\underline{x}_N, \underline{w}) \end{bmatrix} = \begin{bmatrix} t_1 - \underline{\phi}^T(\underline{x}_1) \underline{w} \\ \vdots \\ t_N - \underline{\phi}^T(\underline{x}_N) \underline{w} \end{bmatrix} = \underline{t} - \Phi \underline{w},
$$
and so:
$$
L(\underline{w}) = \frac{1}{2}\text{RSS}(\underline{w}) = \frac{1}{2} ||\underline{\varepsilon}||_2^2 = \frac{1}{2} \underline{\varepsilon}^T \underline{\varepsilon} = \frac{1}{2} (\underline{t} - \Phi \underline{w})^T (\underline{t} - \Phi \underline{w}).
$$

Then the jacobian of $L$ is:
$$
\frac{\partial}{\partial \underline{w}} L(\underline{w}) = \frac{1}{2} \begin{bmatrix} (\underline{t} - \Phi \underline{w})^T & (\underline{t} - \Phi \underline{w})^T \end{bmatrix} \begin{bmatrix} -\Phi \\ -\Phi \end{bmatrix} = - (\underline{t} - \Phi \underline{w})^T \Phi.
$$
Hence:
$$
\nabla_{\underline{w}} L(\underline{w}) = -\Phi^T(\underline{t} - \Phi \underline{w}).
$$
Furthermore:
$$
\nabla^2_{\underline{w}\underline{w}} L(\underline{w}) = \frac{\partial}{\partial \underline{w}} \nabla_{\underline{w}} L(\underline{w}) = - \Phi^T (-\Phi) = \Phi^T \Phi \succcurlyeq O
$$
(_$A^T A$ is always positive semi-definite, see NAML summaries_).
Hence $L$ is convex, this implies that a NS condition for optimality is $\nabla_{\underline{w}} L(\underline{w}) = \underline{0}$.

We know that $r(\Phi^T \Phi) = r(\Phi)$ (_see NAML summaries_), hence $\Phi^T \Phi$ is full rank iff the columns of $\Phi$ are linearly independent, or, in other words (_take a look at the structure of $\Phi$_) the chosen features are linearly independent. Hence it is reasonable to require that $\Phi^T \Phi$ is full rank.

We're ready to determine the minimizer of $L(\underline{w})$: $\underline{\hat{w}}_{\text{OLS}}$ (_where OLS stands for Ordinary Least Squares_).

---

$$
\nabla_{\underline{w}} L(\underline{\hat{w}}_{\text{OLS}}) = \underline{0} \text{ iff } - \Phi^T(\underline{t} - \Phi \underline{\hat{w}}_{\text{OLS}}) = \underline{0} \text{ iff } \Phi^T \Phi \underline{\hat{w}}_{\text{OLS}} = \Phi^T \underline{t} \text{ iff}
$$

$$
\underline{\hat{w}}_{\text{OLS}} = (\Phi^T \Phi)^{-1} \Phi^T \underline{t}.
$$

### Sequential update

The matrix $(\Phi^T \Phi)^{-1} \Phi^T$ is known as **pseudo-inverse** (_see NAML summaries, remember that the columns of $\Phi$ are assumed to be linearly independent_), it can be computed efficiently in $O(N M^2)$ through QR factorization, then, the final product with $\underline{t}$ has a cost of $O(N M)$.
If $N$ or $M$ are too large, the _closed-form_ solution is not practical.
We can use **sequential** updates, in particular, we can apply **Stochastic Gradient Descent** (**SGD**). In particular, let:
$$
L_n(\underline{w}) = \frac{1}{2} (t_n - y(\underline{x}_n, \underline{w}))^2 = \frac{1}{2} (t_n - \underline{\phi}^T(\underline{x}_n) \underline{w})^2 \text{ for } n \in \{ 1, \ldots, N \}.
$$
Then: $L(\underline{w}) = \sum_{n=1}^N L_n(\underline{w})$. Now that we have decomposed $L(\underline{w})$ as a sum of losses, one per sample, we can apply the usual SGD update rule:
$$
\underline{w}^{(k+1)} = \underline{w}^{(k)} - \alpha^{(k)} \nabla L_n(\underline{w}^{(k)})
$$
where $n$ is sampled uniformly (with replacement) from $\{ 1, \ldots, N \}$ at each iteration.
In particular:
$$
\nabla L_n(\underline{w}) = (\underline{\phi}^T(\underline{x}_n) \underline{w} - t_n) \underline{\phi}(\underline{x_n}).
$$
To have a convergence guarantee, the sequence of learning rates has to satisfy:
$$
\sum_{k=0}^{+ \infty} \alpha^{(k)} = + \infty, \sum_{k=0}^{+ \infty} \left(\alpha^{(k)}\right)^2 < + \infty.
$$

### Geometric interpretation

[_Important: take a look at NAML summaries on least squares for an explanation of the geometric intuition_].
$\underline{\hat{t}} = \Phi (\Phi^T \Phi)^{-1} \Phi^T \underline{t}$ is the orthogonal projection of $\underline{t}$ onto $C(\Phi)$. The matrix $H = \Phi (\Phi^T \Phi)^{-1} \Phi^T$ is called the **hat matrix**.

### Maximum-Likelihood (ML) interpretation

It is possible to give a statistical meaning to the least squares approach. Suppose that:
$$
t = f(\underline{x}) + \epsilon
$$
where $\epsilon \sim \mathcal{N}(0, \sigma^2)$ and $f(\underline{x}) = \underline{\phi}(\underline{x})^T \underline{w}^\circ$ for some "_true_" parameters $\underline{w}^\circ$.
We're given $N$ **independent and identically distributed** (**iid**) samples with inputs $\mathbf{X} = \{ \underline{x}_1, \ldots, \underline{x}_n \}$ and outputs $\underline{t} = \begin{bmatrix} t_1 & \cdots & t_N \end{bmatrix}^T$.

---

Hence, for fixed parameters $\underline{w}$, the **likelihood** of the observed data is:
$$
p(\underline{t} | \mathbf{X}, \underline{w}, \sigma^2) = \prod_{n=1}^N \mathcal{N}(t_n | \underline{\phi}^T(\underline{x}_n) \underline{w}, \sigma^2).
$$

As in the usual _maximum likelihood_ approach, we can obtain an estimate of the "_true_" parameters $\underline{w}^\circ$ by finding the parameters $\underline{\hat{w}}_{\text{ML}}$ which maximizes the likelihood.
Equivalently, since the $\ln$ function is strictly increasing and the likelihood is positive, we can maximize the _log-likelihood_:
$$
l(\underline{w}) = \ln p(\underline{t} | \mathbf{X}, \underline{w}, \sigma^2) =  \sum_{n=1}^N \left[ \ln \frac{1}{\sqrt{2 \pi \sigma^2}} - \frac{(t_n - \underline{\phi}^T(\underline{x}_n) \underline{w})^2}{2 \sigma^2} \right] = - \frac{N}{2} \ln(2\pi \sigma^2) - \frac{1}{2 \sigma^2} \text{RSS}(\underline{w})^2.
$$
It follows that, since $\underline{\hat{w}}_{\text{OLS}}$ minimizes $\text{RSS}(\underline{w})$, it maximizes the _log-likelihood_ (and the _likelihood_). Hence:
$$
\underline{\hat{w}}_{\text{ML}} = \underline{\hat{w}}_{\text{OLS}} \text{.}
$$
In this setting we can also compute the variance of the least squares estimate (_for fixed input_):
$$
\mathbb{V}\text{ar}[\underline{\hat{w}}_{\text{OLS}} | \mathbf{X}] = \mathbb{V}\text{ar}[(\Phi^T \Phi)^{-1} \Phi^T \underline{t} | \mathbf{X}] = (\Phi^T \Phi)^{-1} \Phi^T \mathbb{V}\text{ar}[\underline{t} | \mathbf{X}] \Phi (\Phi^T \Phi)^{-1} =
$$
$$
= (\Phi^T \Phi)^{-1} \Phi^T \sigma^2 I_N \Phi (\Phi^T \Phi)^{-1} = \sigma^2 (\Phi^T \Phi)^{-1}.
$$

Observe that the "_true_" variance $\sigma^2$ is usually unknown. Anyways it is possible to build an unbiased estimate for it.

> Let $\underline{\varepsilon}_{\text{OLS}} = \underline{t} - \Phi \underline{\hat{w}}_{\text{OLS}} = \underline{t} - \Phi (\Phi^T \Phi)^{-1} \Phi^T \underline{t} = G \underline{t}$ with $G = I_N - \Phi (\Phi^T \Phi)^{-1} \Phi^T$. $\underline{\varepsilon}_{\text{OLS}}$ is a random vector obtained from $\underline{t}$.
Observe that: $G \Phi = O_N$. Remember that $\underline{t} = \Phi \underline{w}^\circ + \underline{\epsilon}$. It follows that: $\underline{\varepsilon}_{\text{OLS}} = G \underline{t} = G \Phi \underline{w}^\circ + G \underline{\epsilon} = \underline{0}_N + G \underline{\epsilon} = G \underline{\epsilon}$.
Hence:
$$
\mathbb{E}[\underline{\varepsilon}_{\text{OLS}}] = G \mathbb{E}[\underline{\epsilon}] = G \underline{0}_N = \underline{0}_N.
$$
> Then:
$$
\mathbb{V}\text{ar}[\underline{\varepsilon}_{\text{OLS}}] = \mathbb{E}[\underline{\varepsilon}_{\text{OLS}} \underline{\varepsilon}_{\text{OLS}}^T] = G \mathbb{E}[\underline{\epsilon} \underline{\epsilon}^T] G^T = G \mathbb{V}\text{ar}[\underline{\epsilon}] G^T = G \sigma^2 I_N G^T = \sigma^2 G G^T.
$$
> Let's work on the expression of $G G^T$:
$$
G G^T = (I - \Phi (\Phi^T \Phi)^{-1} \Phi^T) (I - \Phi (\Phi^T \Phi)^{-1} \Phi^T) = I - 2 \Phi (\Phi^T \Phi)^{-1} \Phi^T + \Phi (\Phi^T \Phi)^{-1} \Phi^T =
$$
$$
= I - \Phi (\Phi^T \Phi)^{-1} \Phi^T = G.
$$
> Hence:
$$
\mathbb{V}\text{ar}[\underline{\varepsilon}_{\text{OLS}}] = \sigma^2 G.
$$

---

> Now let
$$
\hat{\sigma}^2 = \frac{1}{N-M} \text{tr}[\underline{\varepsilon}_{\text{OLS}} \underline{\varepsilon}_{\text{OLS}}^T].
$$
> Then, remembering that the trace is cyclic:
$$
\mathbb{E}[\hat{\sigma}^2] = \frac{1}{N-M} \text{tr} \mathbb{E}[\underline{\varepsilon}_{\text{OLS}} \underline{\varepsilon}_{\text{OLS}}^T] = \frac{1}{N-M} \text{tr} \sigma^2 G = \frac{1}{N-M} \sigma^2 [\text{tr} I_N - \text{tr} (\Phi (\Phi^T \Phi)^{-1} \Phi^T) ] =
$$

$$
= \frac{1}{N-M} \sigma^2[\text{tr}I_N - \text{tr}((\Phi^T \Phi)^{-1} \Phi^T \Phi)] = \frac{1}{N-M} \sigma^2[\text{tr}I_N - \text{tr}I_M]= \frac{1}{N-M} \sigma^2 (N-M) = \sigma^2.
$$
> That is, $\hat{\sigma}^2$ is an **unbiased estimator** of $\sigma^2$.
Finally, observe that:
$$
\hat{\sigma}^2 = \frac{1}{N-M} \sum_{n=1}^N \varepsilon_{\text{OLS},n}^2 = \frac{1}{N-M} \sum_{n=1}^N (t_n - \underline{\phi}^T(\underline{x}_n) \underline{\hat{w}}_{\text{OLS}})^2.
$$

### Gauss-Markov theorem

The least squares estimate has other interesting properties.

- **Gauss-Markov theorem**: the least squares estimate of $\underline{w}$ has the **smallest variance** among all linear **unbiased** estimates.

This result implies that the least square estimator has the **lowest MSE** of all linear estimator with **no bias**. However, there may exist a **biased** estimator with **smaller MSE**. [_Remember that $\text{MSE } = \text{variance of the estimator} + \text{ bias of the estimator}^2$_].

### Multiple outputs

Let us now consider the case of **multiple outputs**. We could use a **different** set of basis functions for each output, thus having **independent** regression problems. Usually, a **single** set of basis functions is considered.
For each output $t_k$ we have:
$$
\underline{\hat{w}}_{\text{OLS},k} = (\Phi^T \Phi)^{-1} \Phi^T \underline{t}_k
$$
where $\underline{t}_k$ is an $N$-dimensional vector.
We can arrange the parameters for each output in a matrix:
$$
\hat{\mathbf{W}}_{\text{OLS}} = \begin{bmatrix} \underline{\hat{w}}_{\text{OLS},1} & \cdots & \underline{\hat{w}}_{\text{OLS},K} \end{bmatrix} = \begin{bmatrix} (\Phi^T \Phi)^{-1} \Phi^T \underline{t}_1 & \cdots & (\Phi^T \Phi)^{-1} \Phi^T \underline{t}_K \end{bmatrix} = (\Phi^T \Phi)^{-1} \Phi^T \mathbf{T}
$$
where $\mathbf{T} = \begin{bmatrix} \underline{t}_1 & \cdots & \underline{t}_K \end{bmatrix}$.

Observe that the pseudo-inverse has to be computed only once.

---

### Under-fitting vs Over-fitting

Imagine to apply linear regression to a synthetic dataset where $f$ is a sinusoidal function and $\epsilon$ is a Gaussian noise. We're in the perfect framework for applying least squares. Furthermore, suppose that we choose as basis functions $\phi_i(x) = x^{i-1}$ for all $i \in \{ 1, \ldots, M \}$. That is, we want to fit a polynomial of degree $M-1$ to the data.

What we would observe is that, for small values of $M$, we would have a large training error, which keeps decreasing until reaching 0 for $M = N$ if we assume that there are no two points with the same $x$ coordinate.

Now, if we were to test the OLS model obtained for every considered value of $M$ on a different dataset generated from the same distribution, we will observe that both the models with very small (close to 0) and very large (close to $N$) values of $M$ would perform poorly. These phenomena have a name.

- In the first case ($M$ close to 0) we have **under-fitting**: the model is "_too-simple_" to explain the data generating mechanism;
- in the second case ($M$ close to $N$) we have **over-fitting**: the model is too complex, we're learning the values of the noise together with $f$.

The best value of $M$ falls between these two extrema: finding it requires _model selection_ (which we will tackle later).

Observe that it is not weird that these phenomena happen: as we remarked at the beginning, we're minimizing an empirical loss while our aim is to minimize the ideal loss.

### Regularization

One way to improve the generalization capabilities of the learned model, other than decreasing the model family "_expressivity_", is to adopt regularization techniques.
Regularization techniques consist in modifying the loss function in order to account for the "_complexity_" of the model:
$$
L(\underline{w}) = L_D(\underline{w}) + \lambda L_W(\underline{w})
$$
where $L_D$ accounts for the error on the training set, and $L_W$ instead tries to measure the model complexity. $\lambda \geq 0$ is an hyperparameter which allows to tune the strength of the regularization.

#### Ridge regression

One of the most common regularization techniques is **Ridge regression** in which:
- $L_D(\underline{w}) = \frac{1}{2} \text{RSS}(\underline{w})$;
- $L_W(\underline{w}) = \frac{1}{2} ||\underline{w}||_2^2$.

---

Observe that it is still possible to compute the minimizer of $L(\underline{w})$ analytically.

$$
\nabla_{\underline{w}} L(\underline{w}) = \frac{1}{2} \nabla_{\underline{w}} \text{RSS}(\underline{w}) + \lambda \underline{w} = - \Phi^T (\underline{t} - \Phi \underline{w}) + \lambda \underline{w} = (\lambda I_M  + \Phi^T \Phi) \underline{w} - \Phi^T \underline{t}.
$$

Then:
$$
\nabla_{\underline{w}\underline{w}}^2 L(\underline{w}) = \lambda I_M + \Phi^T \Phi \succ O \text{ if } \lambda > 0.
$$

Hence, the problem is strictly convex and we can find the minimizer by imposing:
$$
\nabla_{\underline{w}} L(\underline{\hat{w}}_{\text{ridge}}) = (\lambda I_M + \Phi^T \Phi) \underline{\hat{w}}_{\text{ridge}} - \Phi^T \underline{t} = \underline{0}_M.
$$
That is:
$$
\underline{\hat{w}}_{\text{ridge}} = (\lambda I_M + \Phi^T \Phi)^{-1} \Phi^T \underline{t}.
$$

#### Least Absolute Shrinkage and Selection Operator (LASSO)

Another popular regularization method is **LASSO** in which:
- $L_D(\underline{w}) = \frac{1}{2} \text{RSS}(\underline{w})$;
- $L_W(\underline{w}) = \frac{1}{2}||\underline{w}||_1$.

The LASSO estimate has **no closed-form**, we need to rely on iterative optimization techniques.

Maybe the _most important property_ of LASSO regularization, is that it yields sparse models.
Let's try to understand why. It is possible to show that, for every continuously differentiable convex objective function $f$, there exist values of $\lambda$ and $t$ s.t. the two following optimization problems are equivalent:
$$
\min f(\underline{w}) + \frac{\lambda}{2}||\underline{w}||_1 \ (1)
$$
and:
$$
\min f(\underline{w}) \ (2)
$$
$$
\text{s.t.}
$$
$$
||\underline{w}||_1 \leq t \text{.}
$$

In particular it is easy to show that, for a fixed value of $\lambda$, it is possible to find a $t$ s.t. the optimal solution to $(1)$ is an optimal solution to $(2)$. The converse is more difficult, doing it formally requires KTT conditions in sub-gradient form + other properties of sub-gradients.
Fortunately to have a clue of why LASSO yields to sparsity it is sufficient the "first direction". So, let's prove the statement.

Let $\underline{w}_1^*$ be an optimal solution of $(1)$. Let $t = ||\underline{w}_1^*||_1$. Let $\underline{w}_2^*$ be an optimal solution of $(2)$ for the chosen $t$.

---

By the optimality of $\underline{w}_1^*$: $f(\underline{w}_1^*) + \frac{\lambda}{2}||\underline{w}_1^*||_1 \leq f(\underline{w}_2^*) + \frac{\lambda}{2}||\underline{w}_2^*||_1$.
By the optimality of $\underline{w}_2^*$, since $\underline{w}_1^*$ is feasible for $(2)$, then: $f(\underline{w}_2^*) \leq f(\underline{w}_1^*)$.
By the feasibility of $\underline{w}_2^*$: $||\underline{w}_2^*||_1 \leq t = ||\underline{w}_1^*||_1$.
Hence: $\frac{\lambda}{2}(||\underline{w}_2^*||_1 - ||\underline{w}_1^*||_1) \geq f(\underline{w}_1^*) - f(\underline{w}_2^*) \geq 0$ iff ($\lambda > 0$) $||\underline{w}_2^*||_1 \geq ||\underline{w}_1^*||_1$.
Then it must be: $||\underline{w}_2^*||_1 = ||\underline{w}_1^*||_1$.
Hence, since $f(\underline{w}_1^*) + \frac{\lambda}{2}||\underline{w}_1^*||_1 \leq f(\underline{w}_2^*) + \frac{\lambda}{2}||\underline{w}_2^*||_1$, $f(\underline{w}_2^*) \leq f(\underline{w}_1^*)$, and $||\underline{w}_2^*||_1 = ||\underline{w}_1^*||_1$, it must be $f(\underline{w}_1^*) = f(\underline{w}_2^*)$. That is, $\underline{w}_1^*$ is an optimal solution for $(2)$ as we wanted to prove.

Now, suppose that $f$ is a quadratic strictly convex function whose matrix has equal eigenvalues: its level curves are circles. The picture below plots the level curves of $f$ and the feasibility region of the equivalent constrained optimization problem $(2)$ in red.
By observing the picture, it is clear that, if the global minimum of $f$ is outside of the yellow region, then the optimum of $(2)$ is a vertex of the feasibility region. Indeed, in this setting the value of $f$ is proportional to the squared euclidean distance of the input point from the global minimum of $f$, and, if we're outside of the yellow area, to reach any point different from the vertex closest to the global minimum, we need to increase one of the legs of the highlighted right triangle, thus increasing the value of $f$ because of Pythagorean theorem. 
Finally, we need to observe that the vertices of the feasibility region of $(2)$ are sparse (one of the two coordinates is 0) and that, especially as the feasibility region of $(2)$ gets smaller, "it's more likely for the global minimum of $f$ to be outside of the yellow region than inside".

<p align="center">
    <img src="static/lasso-favors-sparsity.svg"
    width="300mm" />
</p>

In the lasso setting $f$ is quadratic and strictly convex (assuming linearly independent features), but the eigenvalues are not necessarily equal. The level curves of $f$ become some ellipses and thus also the shape of the yellow area changes accordingly.

---

Anyways it is possible to generalize the previous argument to elliptical level curves by showing that the "yellow area is still tiny", but it requires to do some math that unfortunately I have no time for (: ( ).

## Bayesian approach
### The Bayesian approach in general

Let's start by discussing the **Bayesian approach** in general.
In a Bayesian approach we formulate our knowledge about the world in a **probabilistic way**:
- we define the **model** that expresses our knowledge **qualitatively**;
- our model will have some **unknown parameters**;
- we capture our assumptions about unknown parameters by specifying the **prior distribution** over those parameters before seeing the data.

Every time we **observe some data**, we update the posterior probability distribution over the parameters, given the observed data. Finally, we can use the posterior distribution to:
- **make predictions**;
- **examine/account for uncertainty** in the parameter values;
- **make decisions** by minimizing expected posterior loss.

The **posterior distribution** for the model parameters can be **found** by combining the **prior with the likelihood** for the parameters given the data.
This is accomplished using **Bayes' rule**:
$$
p(\underline{w}|\mathcal{D}) = \frac{p(\mathcal{D}|\underline{w}) p(\underline{w})}{p(\mathcal{D})}
$$
where:
- $p(\underline{w}|\mathcal{D})$ is the **posterior** probability of parameters $\underline{w}$ given the training data $\mathcal{D}$;
- $p(\mathcal{D}|\underline{w})$ is the probability (**likelihood**) of observing $\mathcal{D}$ given $\underline{w}$;
- $p(\underline{w})$ is the **prior** probability over the parameters;
- $p(\mathcal{D})$ is the marginal likelihood, indeed, since $p(\underline{w}|\mathcal{D})$ is a probability distribution:
$$
1 = \int p(\underline{w}|\mathcal{D}) d\underline{w} = \int \frac{p(\mathcal{D}|\underline{w})p(\underline{w})}{p(\mathcal{D})} d\underline{w} \text{ iff } p(\mathcal{D}) = \int p(\mathcal{D}|\underline{w}) p(\underline{w}) d\underline{w}.
$$
> Hence we can compute it once we know the likelihood and the prior.

To make prediction we can adopt the **Maximum A Posteriori** (**MAP**) approach: we take the value of $\underline{w}$ most likely according to the posterior, i.e. the _mode_.

---

### Refresh on some properties of Gaussian vectors

Let's state some properties of Gaussian vectors which will be useful in a moment.

- **Theorem**: given a marginal Gaussian distribution for $\underline{x}$ and a conditional Gaussian distribution for $\underline{y}$ given $\underline{x}$ in the form:
> - $p(\underline{x}) = \mathcal{N}(\underline{x}|\underline{\mu}, \Lambda^{-1})$;
> - $p(\underline{y}|\underline{x}) = \mathcal{N}(\underline{y}|A \underline{x} + \underline{b}, L^{-1});$

> the marginal distribution of $\underline{y}$ and the conditional distribution of $\underline{x}$ given $\underline{y}$ are given by:

> - $(A) \ \ \ p(\underline{y}) = \mathcal{N}(\underline{y}|A \underline{\mu} + \underline{b}, L^{-1} + A \Lambda^{-1} A^T)$;
> - $(B) \ \ \ p(\underline{x}|\underline{y}) = \mathcal{N}(\underline{x}|\Sigma[A^T L (\underline{y} - \underline{b}) + \Lambda \underline{\mu}], \Sigma)$

> where $\Sigma = (\Lambda + A^T L A)^{-1}$.

### Bayesian approach to linear regression

**Bayesian approach** provides another way of dealing with the **over-fitting** problem in ML.
In particular, as discussed in the general setting, we assume that the parameters of our linear model are drawn by some distribution.
It is usual to choose the prior and likelihood distributions so that they are **conjugate priors**, that is, we want the posterior, obtained by multiplying the prior with the likelihood and then normalizing, to be of the same family of the prior, so that we can iterate this process by taking the posterior as the new prior.
A **Gaussian** prior and likelihood are conjugate priors, we will exploit this family.
Hence, we can set the **prior** as:
$$
p(\underline{w}) = \mathcal{N}(\underline{w}|\underline{w}_0, S_0).
$$
Given the data $\mathcal{D}$, the likelihood has the same expression that we used in the Maximum Likelihood setting:
$$
p(\mathcal{D}|\underline{w}) = \mathcal{N}(\underline{t}|\Phi \underline{w}, \sigma^2 I_N).
$$
We can compute the expression of the posterior, thanks to the properties of Gaussian vectors. In particular we will use property $(B)$. Let $\underline{x} = \underline{w}$, $\mu = \underline{w}_0$, $\Lambda^{-1} = S_0$, $\underline{y} = \underline{t}$, $A = \Phi$, $\underline{b} = \underline{0}$, $L^{-1} = \sigma^2 I_N$. Then:
$$
p(\underline{w}|\mathcal{D}) = \mathcal{N}(\underline{w}|\underline{w}_N, S_N)
$$
where:
- $S_N = \Sigma = (\Lambda + A^T L A)^{-1} = (S_0^{-1} + \frac{1}{\sigma^2} \Phi^T \Phi)^{-1}$;
- $\underline{w}_N = \Sigma [A^T L (\underline{y} - \underline{b}) + \Lambda \underline{\mu}] = S_N[\frac{1}{\sigma^2}\Phi^T\underline{t} + S_0^{-1} \underline{w}_0]$.

---

**Remark**: batch updates are equivalent to online updates. That is, if we were to do two updates with $N_1$ and $N_2$ data points respectively, we would get:
$$
S_{N_1+N_2}^{-1} = S_0^{-1} + \frac{1}{\sigma^2} \Phi_1^T \Phi + \frac{1}{\sigma^2} \Phi_2^T \Phi_2 = S_0^{-1} + \frac{1}{\sigma^2} \begin{bmatrix} \Phi_1^T & \Phi_2^T \end{bmatrix} \begin{bmatrix} \Phi_1 \\ \Phi_2 \end{bmatrix}, \text{ and}
$$
$$
\underline{w}_{N_1+N_2} = S^{-1}_{N_1 + N_2} [S_{N_1}^{-1}\{ S_{N_1} [S_0^{-1} \underline{w}_0 + \frac{1}{\sigma^2} \Phi_1^T \underline{t}_1] \} + \frac{1}{\sigma^2} \Phi^2 \underline{t}_2] = S_{N_1+N_2}^{-1}[S_0^{-1} \underline{w}_0 + \frac{1}{\sigma^2}\begin{bmatrix} \Phi_1^T & \Phi_2^T \end{bmatrix} \begin{bmatrix} \underline{t}_1 \\ \underline{t}_2 \end{bmatrix} ].
$$

Let's do some observations.

- In Gaussian distributions the **mode** coincides with the **mean**. It follows that $\underline{w}_N$ is the **MAP estimator**.

- If the priori has infinite variance, that is $S_0^{-1} = O_M$, then:
$$
S_N = \sigma^2 (\Phi^T \Phi)^{-1} \text{, and then } \underline{w}_N = S_N \frac{1}{\sigma^2} \Phi^T \underline{t} = (\Phi^T \Phi)^{-1} \Phi^T \underline{t} = \underline{\hat{w}}_{\text{OLS}},
$$
> that is, the Bayesian estimate coincides with the Maximum Likelihood estimate.

- **Important**: if $\underline{w}_0 = \underline{0}_M$ and $S_0 = \tau^2 I_M$, then:
$$
S_N = (\frac{1}{\tau^2} I_M + \frac{1}{\sigma^2} \Phi^T \Phi)^{-1} \text{, and then } \underline{w}_N = (\frac{\sigma^2}{\tau^2} I_M + \Phi^T \Phi)^{-1} \Phi^T \underline{t} = \underline{\hat{w}}_{\text{ridge}},
$$
> that is, the Bayesian estimate coincides with the Ridge regression estimate for $\lambda = \frac{\sigma^2}{\tau^2}$. This shows how Ridge regression arises naturally in a Bayesian setting.

Thanks to the properties of Gaussian vectors, we can also compute the **posterior predictive distribution**. In particular we will use property $(A)$ (observe that now $p(\underline{x}) = p(\underline{w}|\mathcal{D})$ and NOT $p(\underline{w})$, and $p(\underline{y}|\underline{x}) = p(t|\underline{w}, \mathcal{D}) = \mathcal{N}(t|\underline{\phi}^T(\underline{x})\underline{w}, \sigma^2)$):
$$
p(t|\mathcal{D}) = \mathcal{N}(\underline{t}|\Phi \underline{w}_N, \sigma^2_N(\underline{x}))
$$
where $\sigma_N^2(\underline{x}) = \sigma^2 + \underline{\phi}^T(\underline{x}) S_N \underline{\phi}(\underline{x})$. **Important**: the variance in the prediction depends on the input point.
Observe that, since $\lim_{N \rightarrow + \infty} S_N = O_M$, then: $\lim_{N \rightarrow +\infty} \sigma_N^2(\underline{x}) = \sigma^2$ for all $\underline{x}$.

#### Challenges

The Bayesian approach is powerful but requires to face many challenges.

##### Modelling challenges

The first challenge is in **specifying suitable model** and **suitable prior distributions**: a suitable model should admit all the possibilities that thought to be at all **likely**; a suitable prior should avoid giving zero or very small probabilities to possible events, but should also avoid spreading out the probability over all possibilities.

---

Furthermore, having fixed basis functions allows a tractable Bayesian treatment, with closed-form solution; but they are chosen independently from the dataset.

##### Computational challenges

The other big challenge is **computing the posterior distribution**. There are several approaches:
- **analytical integration**: if we use **conjugate priors**, the posterior distribution can be computed **analytically** (this works only for simple models);
- **Gaussian (Laplace) approximation**: we can approximate the posterior distribution with a Gaussian. It works well where there are a lot of data compared to the model complexity.
- **Monte Carlo integration**: once we have a sample from the posterior distribution, we can do many things. Currently, the most common approach is Markov Chain Monte Carlo (MCMC), that consists in simulating a Markov chain that converges to the posterior distribution.
- **Variational approximation**: a clever way of approximating the posterior. It is usually faster than MCMC, but it is less general.

