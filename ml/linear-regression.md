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

**Important remark**: even though we want to minimize the expected loss $\mathbb{E}[L]$, we can't compute it. Indeed, in order to compute $\mathbb{E}[L]$, we need to know $p(\underline{x}, t)$. But, if we knew $p(\underline{x}, t)$ the problem would be solved: we know the analytic expression of the function that minimizes the expected loss for a given loss function (according to the previous theorems), and we can compute it from $p(\underline{x}, t)$. Indeed, in ML problems, $p(\underline{x}, t)$ is never known. The only thing that we can do is try to estimate the expected loss of a given model from the available training data-set. Usually we look for the model in the chosen hypothesis space that minimizes such estimate. Anyway, we've to always keep in mind that what we're minimizing is an empirical estimate, but what we want to minimize is the (_ideal_) expected loss. The two things does not necessarily coincide (of course), and this mismatch is the core problem with which ML has to deal.

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
where $\mathcal{D} = \{ (\underline{x}_1, t_1), \ldots, (\underline{x}_n, t_n) \}$ is the given training set. (_The \frac{1}{2} factor, as every other multiplicative positive constant, does not alter the set of minima of $L(\underline{w})$; it is there only for convenience in the expressions that we're going to derive_).

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

We're ready to determine the minimizer of $L(\underline{w})$: $\underline{w}_{\text{OLS}}$ (_where OLS stands for Ordinary Least Squares_).

---

$$
\nabla_{\underline{w}} L(\underline{w}_{\text{OLS}}) = \underline{0} \text{ iff } - \Phi^T(\underline{t} - \Phi \underline{w}_{\text{OLS}}) = \underline{0} \text{ iff } \Phi^T \Phi \underline{w}_{\text{OLS}} = \Phi^T \underline{t} \text{ iff}
$$

$$
\underline{w}_{\text{OLS}} = (\Phi^T \Phi)^{-1} \Phi^T \underline{t}.
$$

Resume from gradient optimization...
