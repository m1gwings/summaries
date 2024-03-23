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

## Dynamic modeling

The identification of dynamical models presents some additional difficulties and pitfalls, which we must be aware of:
- the identification algorithm $\mathcal{I}$ depends on the considered model class: for some classes we will still be able to apply a method as simple as least squares, but for some other classes we will need to develop new tools;
- the role of the noise model is crucial;
- model selection and validation are crucial to avoid under- or over-parameterization;
- the identifiability issue is more complicated.

### Model families

We can distinguish 2 different types of data-generating mechanisms, depending on the presence or absence of _exogenous_ variables:
- **time series** (no exogenous variables);
- **input-output systems** (with exogenous variables).

#### Time series

When dealing with time series, we are given a set of observations of a variable over a time range, and we are faced with the task of building a model that describes its evolution, and explains how the past history affects the current value of the variable.
We can represent time series through the following expression:
$$
v(t) = W(z) \eta(t), \eta(\cdot) \sim WN(0, \lambda^2).
$$

---

#### Input-output systems

When dealing with input-output systems, we are given a set of observations of both the input and the output of a given system over a time range, and we want to determine a dynamical model that describes how the input influences the output.
We can represent input-output systems through the following expression:
$$
y(t) = G(z) u(t-k) + W(z) \eta(t), \eta(\cdot) \sim WN(0, \lambda^2).
$$

Another classification is based on the disturbance model. We distinguish between:
- **output error models**;
- equation error models (**AR**/**ARX**);
- **ARMA**/**ARMAX** models;
- **ARXAR** models;
- **ARIMA**/**ARIMAX** models (a.k.a. **CARMA**/**CARMAX**);
- **FIR** models.

#### Output error models

We assume that the output is given by the sum of the variable that describes the direct influence of the input ($G(z) u(t-k)$) plus a white noise ($W(z) = 1$).
This amounts to attributing all the model error to the uncertainty in the measurement of the output.
We can describe output error models with the following expression:
$$
y(t) = G(z) u(t-k) + \eta(t), \eta(\cdot) \sim WN(0, \lambda^2).
$$

#### Equation error models (AR/ARX)

We can describe AR models with the following expression (_as usual_):
$$
A(z) y(t) = \eta(t),
$$
where:
$$
G(z) = 0, W(z) = \frac{1}{A(z)}.
$$

We can describe ARX models with the following expression:
$$
A(z)y(t) = B(z)u(t-k) + \eta(t),
$$
where:
$$
G(z) = \frac{B(z)}{A(z)}, W(z) = \frac{1}{A(z)}.
$$

---

**Recall** that $A(z)$ must be a Schur stable polynomial for process stationarity.
The noise $\eta(\cdot)$ is sometimes called **equation residual**.

#### ARMA/ARMAX models

Assuming that the equation residual is just a white noise may turn out to be a simplistic hypothesis; this is why we often introduce an MA process to account for this term.
We can describe ARMA models with the following expression (_as usual_):
$$
A(z)y(t) = C(z) \eta(t),
$$
where:
$$
G(z) = 0, W(z) = \frac{C(z)}{A(z)}.
$$
We can describe ARMAX models with the following expression:
$$
A(z) y(t) = B(z) u(t-k) + C(z) \eta(t),
$$
where:
$$
G(z) = \frac{B(z)}{A(z)}, W(z) = \frac{C(z)}{A(z)}.
$$
Again, $A(z)$ must be a Schur stable polynomial for the process stationarity.
Without loss of generality we can assume that the roots of $C(z)$ are all in the unit circle (_see spectral factorization in "Stochastic processes" summary_).

#### ARXAR models

Alternatively, the residual can be represented as an auto-regressive model.
In particular, we can describe ARXAR models with the following expression:
$$
A(z) y(t) = B(z) u(t-k) + \frac{1}{D(z)} \eta(t),
$$
where:
$$
G(z) = \frac{B(z)}{A(z)}, W(z) = \frac{1}{A(z) D(z)}.
$$
Observe that $D(z) = 1 + d_1 z^{-1} + \ldots + d_{n_d} z^{-n_d}$ must be a Schur polynomial in order for the noise term to be a stationary process.

---

#### ARIMA/ARIMAX models (a.k.a. CARMA/CARMAX)

It is sometimes of interest to model a non-stationary residual to describe a drift phenomenon:
$$
w(t) = w(t-1) + \eta(t), \eta(\cdot) \sim WN(0, \lambda^2).
$$
Observe that we can write the drift expression as:
$$
(1-z^{-1}) w(t) = \eta(t)
$$
where $1-z^{-1}$ is NOT a Schur stable polynomial. Indeed $\frac{1}{1-z^{-1}}$ is an **integral factor**.
Process $w(\cdot)$ takes the name of **random walk**. Observe that its variance is not constant, indeed, since $w(t-1)$ and $\eta(t)$ are uncorrelated:
$$
\mathbb{V}\text{ar}[w(t)] = \mathbb{V}\text{ar}[w(t-1)] + \mathbb{V}\text{ar}[\eta(t)] = \mathbb{V}\text{ar}[w(t-1)] + \lambda^2.
$$
Then, assuming that $\mathbb{V}\text{ar}[w(0)] = 0$, it is easy to see by induction that:
$$
\mathbb{V}\text{ar}[w(t)] = t\lambda^2.
$$

In the model equations, the noise term becomes:
$$
C(z) = \frac{C(z)}{1-z^{-1}} \eta(t)
$$
In particular, we can describe ARIMA models with the following expression:
$$
(1-z^{-1}) A(z) y(t) = C(z) \eta(t),
$$
where:
$$
G(z) = 0, W(z) = \frac{C(z)}{(1-z^{-1}) A(z)}.
$$

We can describe ARIMAX models with the following expression:
$$
(1-z^{-1}) A(z) y(t) = (1-z^{-1}) B(z) u(t-k) + C(z) \eta(t),
$$
where:
$$
G(z) = \frac{B(z)}{A(z)}, W(z) = \frac{C(z)}{(1-z^{-1}) A(z)}.
$$

#### FIR models

An ARX model with $n_a = 0$ is characterized by the following input-output equation:
$$
y(t) = B(z) u(t-1) + \eta(t).
$$

---

The output is a linear combination of a finite number of past input data (_plus noise_):
$$
G(z) = B(z) = b_0 + b_1 z^{-1} + \ldots + b_{n_b} z^{-n_b}.
$$
Since the transfer function can be interpreted as the $\mathcal{Z}$-transform of the deterministic part of the system's impulse response (_see "Discrete time signals and systems", property 11_), the $b_i$ coefficients are actually the values of the impulse response.
Only $n_b + 1$ coefficients are present, which amounts to assuming that the system's impulse response goes to 0 after a finite time, hence the name FIR (**Finite Impulse Response**).
