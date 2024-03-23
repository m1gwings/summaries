---
marp: true
theme: summary
math: mathjax
---
# Identification

<div class="author">

Cristiano Migali

</div>

We have seen (_in the "Prediction" summary_) that given a model of a stationary process we can calculate the optimal predictors. But how do we get the model in the first place?

- **System identification** is the discipline that studies the methodologies to derive a model from the data.

What should we **expect of such models**?

- **Limited validity**: the identified model cannot reveal more on the system than what implicitly contained in the data used to determine it.

- **Difficult physical interpretation**: the model parameters do not have a direct physical interpretation. The model is conceived to explain the data, and is not derived from physical laws.

- **Simple derivation and usage**: this is probably one of the biggest advantages of identification.

The **fundamental elements of the identification problem** are:
- the **system** ($\mathcal{S}$);
- the **model family** ($\mathcal{M}$);
- the **identification method** ($\mathcal{I}$);
- the **identification experiment** ($\mathcal{E}$).

## Phases of the (parametric) system identification procedure

### Experiment design and data collection

First of all, one must design and perform an _identification experiment_ ($\mathcal{E}$) to obtain the data. For input-output systems, the system ($\mathcal{S}$) is subject to a suitable input signal and its input and outputs are observed over a period of time and collected.

### Choice of the model class ($\mathcal{M}$)

A _parametric model family_ $\mathcal{M}(\theta) = \{ M(\theta) | \theta \in \Theta \}$ is selected, that is (believed to be) sufficiently flexible to be able to explain the data. The set $\Theta$ defines the admissible parameterizations.
The identification problem consists in the determination of the appropriate $\theta$.

**Remark**: in _non-parametric_ system identification we can use models like curves, functions, tables, etc.

---

### Choice of identification criterion and parameter estimation

A suitable method (_identification algorithm_, $\mathcal{I}$) is employed to estimate the unknown model parameters. This generally entails the choice of an _identification criterion_ $J_N(\theta) \geq 0$ and its minimization w.r.t. $\theta$.

### Model validation

In the course of the identification procedure, we made some important assumption, _e.g._ that the system $\mathcal{S}$ belongs to the model family $\mathcal{M}(\theta)$, and we fixed the model orders ($n_a$, $n_b$, and $n_c$ for an ARMAX). What if they are wrong?
We must run a quality check on the obtained model, a.k.a. _validation_.
If found to be unsuccessful, we must reconsider the assumptions made and roll back the procedure to one of the previous steps.

## Static modeling

The general identification problem setting assumes that one has observed some input/output data from a system:
- _input data_: $\{ u(1), u(2), \ldots, u(N) \}$;
- _output data_: $\{ y(1), y(2), \ldots, y(N) \}$;

and looks for a model that can explain the relationship between input and output.
In the case where we are interested in the _static relationship_ between the two variables, the model takes the form:
$$
\hat{y}(u) = f(u; \hat{\theta})
$$
where the function $f(\cdot; \theta)$ specifies the model family $\mathcal{M}(\theta)$ and the "optimal" parameters $\hat{\theta} = g(u(1), u(2), \ldots, u(N), y(1), y(2), \ldots, y(N))$ are determined from the available data.

### Least squares

One of the most used _identification method_ when the model is linear in the parameters is the **least squares** method.
In this setting, a natural way to describe $f(u; \theta)$ is using a **functional expansion**:
$$
f(u; \theta) = \phi^T \theta = \sum_{i=1}^n\theta_i \phi_i(u)
$$
where the $\phi_i(u)$ are denoted _basis functions_. Sometimes the terms $\phi_i$ are known as **regressors**.

---

From the input data ($u(1), u(2), \ldots, u(N)$) we can compute:
$$
\phi(t) = \begin{bmatrix}
\phi_1(u(1)) \\
\cdots \\
\phi_n(u(t))
\end{bmatrix}.
$$
Then we define (for given parameters):
$$
\hat{y}(t) = \phi^T(t) \theta,
$$
and the corresponding model error is:
$$
\varepsilon(t) = y(t) - \hat{y}(t)
$$
where $y(1), y(2), \ldots, y(N)$ are the output data.
In least squares, the identification algorithm consists in the minimization of the _average of the squared errors_ over the observation horizon:
$$
J(\theta) = \frac{1}{N} \sum_{t=1}^N \varepsilon^2(t; \theta).
$$
Minimizing $J(\theta)$ is relatively simple, since it turns out that $\varepsilon(t)$ is _linear_ in $\theta$, and consequently $J(\theta)$ is _quadratic_ in $\theta$.
Indeed:
$$
J(\theta) = \frac{1}{N} \sum_{t=1}^N (y(t) - \phi^T(t) \theta)^2;
$$
then:
$$
\frac{\partial J}{\partial \theta}(\theta) = - \frac{2}{N} \sum_{t=1}^N (y(t) - \phi^T(t) \theta) \phi^T(t),
$$
hence:
$$
\nabla_\theta J(\theta) = -\frac{2}{N} \sum_{t=1}^N (y(t) - \phi^T(t) \theta) \phi(t).
$$
Furthermore:
$$
\nabla^2_\theta J(\theta) = \frac{\partial}{\partial \theta} \nabla_\theta J(\theta) = - \frac{2}{N} \sum_{t=1}^N \phi(t) (-\phi^T(t)) = \frac{2}{N} \sum_{t=1}^N \phi(t) \phi^T(t) \succcurlyeq 0.
$$

If we assume that $\nabla_\theta^2 J(\theta)$ is invertible (_see NAML summaries for the case in which this doesn't hold_), then the objective function becomes strictly convex and hence admits a unique global minimizer. We can find it by setting $\nabla_\theta J(\theta) = 0$.

---

$$
- \frac{2}{N} \sum_{t=1}^N (y(t) - \phi^T(t) \theta) \phi(t) = 0 \text{ iff }
\sum_{t=1}^N \phi^T(t) \theta \phi(t) = \sum_{t=1}^N \phi(t) y(t) \text{ iff }
$$
$$
\text{(} \phi^T(t)\theta \text{ is a scalar) } \sum_{t=1}^N \phi(t) \phi^T(t) \theta = \sum_{t=1}^N \phi(t) y(t) \text{ iff}
$$
$$
\theta = \left(\sum_{t=1}^N \phi(t) \phi^T(t)\right)^{-1} \sum_{t=1}^N \phi(t) y(t).
$$
This is called **least squares estimate of $\theta$**.
We define:
$$
R(N) = \sum_{t=1}^N \phi(t) \phi^T(t);
$$
the condition $R(N) \succ 0$ (implied by the fact that $\nabla_\theta^2 J(\theta)$ is invertible) guarantees the _identifiability_ of the model, _i.e._ the possibility that _all its parameters can be unambiguously estimated_.

#### Properties of the least squares estimate

Let the mechanism generating the data be of the type:
$$
y(t) = \phi^T(t) \theta^\circ + v(t), v(\cdot) \sim WN(0, \lambda^2).
$$
Assume also that $R(N) \succ 0$.
Then the following properties hold:
- The least squares estimate
$$
\hat{\theta} = R^{-1}(N) \sum_{t=1}^N \phi(t) y(t)
$$
> is an **unbiased estimator** of $\theta^\circ$.

> **Proof**: observe that the input is not affected by the noise, hence $phi(t)$ are deterministic. It follows that:
$$
\mathbb{E}[\hat{\theta}] = R^{-1}(N) \sum_{t=1}^N \phi(t) \mathbb{E}[y(t)] = R^{-1}(N) R(N) \theta^\circ = \theta^\circ.
$$

- The uncertainty of the model parameters can be estimated as:
$$
\mathbb{V}\text{ar}[\hat{\theta}] = \lambda^2 R^{-1}(N).
$$

---

> **Proof**: it follows from the expression of the covariance matrix of a random vector obtained as a linear affine function of another random vector:
$$
\mathbb{V}\text{ar}[\hat{\theta}] = \mathbb{V}\text{ar}\left[ R^{-1}(N) \begin{bmatrix} 
    \phi(1) & \cdots & \phi(N)
\end{bmatrix} \begin{bmatrix}
y(1) \\
\cdots \\
y(N)
\end{bmatrix}\right] =
$$

$$
= R^{-1}(N) \begin{bmatrix} 
    \phi(1) & \cdots & \phi(N)
\end{bmatrix} \lambda^2 I \begin{bmatrix} 
    \phi^T(1) \\ \cdots \\ \phi^T(N)
\end{bmatrix} R^{-1}(N) = \lambda^2 R^{-1}(N) R(N) R^{-1}(N) = \lambda^2 R^{-1}(N).
$$

- An **unbiased estimated of the variance $\lambda^2$** of the noise is given by:
$$
\hat{\lambda}^2 = \frac{N J(\hat{\theta})}{N-n}.
$$

> **Proof**: _see ML summary on "Linear regression"_.
