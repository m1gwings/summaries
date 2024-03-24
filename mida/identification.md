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

### Uniqueness

Assume that the true system falls exactly in the considered model class:
$$
\mathcal{S} : y(t) = G^\circ u(t-k)+ W^\circ (z) \eta^\circ(t), \eta^\circ(\cdot) \sim WN(0, {\lambda^\circ}^2); \mathcal{S} \in \mathcal{M}(\theta).
$$
Even so, it is not granted that the identification is successful.
Let
$$
\mathcal{D}(\mathcal{S}, \mathcal{M}) = \{ \theta | G^\circ(z) = G(z, \theta), W^\circ(z) = W(z, \theta), {\lambda^\circ}^2 = \lambda^2(\theta) \}
$$
be the set of parameterizations for which $\mathcal{M}(\theta)$ provides a perfect description of $\mathcal{S}$.
Three things can occur:
- $\mathcal{D}(\mathcal{S}, \mathcal{M}) = \emptyset$ (_under-parameterized model_);
- $\mathcal{D}(\mathcal{S}, \mathcal{M}) = \{ \theta^\circ \}$ where $\theta^\circ$ is the "true" parameter vector (_ideal case_);
- $\mathcal{D}(\mathcal{S}, \mathcal{M}) = \{ \theta', \theta'', \ldots \}$ (_over-parameterized model, there are multiple models in $\mathcal{M}(\theta)$ that provide a perfect description of $\mathcal{S}$_).

**For example**: for an ARMAX model we are in the 3rd case if $A(z) = A^\circ(z)D(z)$, $B(z) = B^\circ(z)D(z)$, $C(z) = C^\circ(z)D(z)$, for any Schur stable polynomial $D(z)$.

### Prediction Error Minimization (PEM)

In the _predictive approach_, a model is "good" if it provides accurate (1-step ahead) predictions. Given a model family $\mathcal{M}(\theta)$, we represent the family of predictors a.k.a. **prediction form model** as:
$$
\hat{\mathcal{M}}(\theta): \begin{cases}
    \hat{y}(t+1|t) = f(y(t), y(t-1), \ldots; \theta) \text{ for time series} \\
    \hat{y}(t+1|t) = f(u(t), u(t-1), \ldots, y(t), y(t-1), \ldots; \theta) \text{ for I/O systems}
\end{cases}.
$$
Fixed the parameters $\theta$, we can compute the prediction error at any time:
$$
\varepsilon(t; \theta) = y(t) - \hat{y}(t|t-1; \theta).
$$

---

Given the sequence $\varepsilon(\cdot)$ we can evaluate the average size of the error, _e.g._ with the quadratic criterion:
$$
J_N(\theta) = \frac{1}{N} \sum_{t=\tau}^N \varepsilon^2(t; \theta),
$$
where $\tau > 1$ is the smallest integer for which $\varepsilon(t)$ can be computed.
The **optimal** mode in the considered model family has parameters $\theta$ that minimize $J_N(\theta)$ over the set $\Theta$ of admissible parameterizations.
**Important remark**: notice that this quadratic cost is a very partial indicator of the quality of the model; it does not emphasize the dynamic characteristics of $\varepsilon(\cdot)$. Therefore, besides the value of $J_N(\theta)$, one must also check the whiteness of $\varepsilon(\cdot)$, so that it does not contain any predictable dynamics. Only in that case we can be sure all the dynamics contained in the data are explained by the model.

#### General expression of the 1-step predictor from $G(z)$, $W(z)$

All the model families that we listed can be expressed as:
$$
\mathcal{M}(\theta): y(t) = G(z)u(t-k) + W(z)\eta(t), \eta(\cdot) \sim WN(0, \lambda^2).
$$
Suppose that **$W(z)$ is a canonical factor, with no zeros on the unit circle**.
Then it is the ratio between two monic polynomials and so it must be: $W(z) = 1 + w_1 z^{-1} + \ldots$ (it easy to see this with a proof by contradiction; it it were $W(z) = w_0 + w_1 z^{-1} + \ldots$ with $w_0 \neq 1$ then, calling $N(z)$ the numerator and $D(z)$ the denominator of $W(z)$, since $D(z)$ is monic, $N(z) = W(z)D(z) = w_0 + n_1 z^{-1} + \ldots$ which is not monic).
Hence we can decompose $W(z) = 1 + (W(z) - 1)$. Let's plug this in the expression of the model:
$$
y(t) = G(z)u(t-k) + \eta(t) + (W(z)-1)\eta(t).
$$
Because of what we remarked, $(W(z)-1)\eta(t)$ depends only on the "past" noise, hence we can write the expression of the optimal one-step fake predictor:
$$
\hat{y}(t|t-1) = G(z)u(t-k) + (W(z)-1)\eta(t).
$$
Because of our assumption, $W(z)$ is invertible, hence we can derive the _whitening filter_:
$$
\eta(t) = \frac{1}{W(z)}\left[ y(t) - G(z)u(t-k) \right].
$$
Then, the expression of the optimal predictor from data is:
$$
\hat{y}(t|t-1) = G(z)u(t-k) + \left( 1-\frac{1}{W(z)} \right) y(t) - \left( 1-\frac{1}{W(z)} \right) G(z)u(t-k) =
$$
$$
= \frac{G(z)}{W(z)} u(t-k) + \left( 1 - \frac{1}{W(z)} \right)y(t).
$$

---

Let's see **some examples**.

- ARX
$$
G(z) = \frac{B(z)}{A(z)}, W(z) = \frac{1}{A(z)}.
$$
> Then:
$$
\hat{y}(t|t-1) = B(z) u(t-k) + (1-A(z))y(t).
$$
> The prediction is a linear combination of past values of $u(\cdot)$ and $y(\cdot)$ and does not depends from past predictions: the predictor is always stable!

- ARMAX
$$
G(z) = \frac{B(z)}{A(z)}, W(z) = \frac{C(z)}{A(z)}
$$
> Then:
$$
\hat{y}(t|t-1) = \frac{B(z)}{C(z)}u(t-k) + \left(1-\frac{A(z)}{C(z)}\right)y(t).
$$
> In this case the stability depends on $C(z)$.

- ARXAR
$$
G(z) = \frac{B(z)}{A(z)}, W(z) = \frac{1}{A(z)D(z)}.
$$
> Then:
$$
\hat{y}(t|t-1) = B(z)D(z)u(t-k) + \left(1-A(z)D(z)\right)y(t).
$$
> As with ARX models, the stability of the prediction is guaranteed.

There is an important difference in the _prediction form model_ for ARX, ARXAR, and ARMAX models, which impacts on the complexity of the algorithms that we have to use to solve the identification task:
- In ARX models:
$$
\hat{y}(t|t-1) = a_1 y(t-1) + \ldots + a_{n_a} y(t-n_a) + b_0 u(t-k) +
$$
$$
+ b_1 u(t-k-1) + \ldots + b_{n_b} u(t-k-n_b).
$$
> $\hat{y}(t|t-1)$ depends _linearly_ on the parameters $a_i$, and $b_i$, so that the predictor equation is actually a _linear regression_:
$$
\hat{y}(t|t-1) = \phi^T(t) \theta
$$

---

> where
$$
\phi(t) = \begin{bmatrix} y(t-1) & \ldots & y(t-n_a) & u(t-k) & u(t-k-1) & \ldots & u(t-k-n_b) \end{bmatrix}^T,
$$
$$
\theta = \begin{bmatrix} a_1 & \ldots & a_{n_a} & b_0 & b_1 & \ldots & b_{n_b} \end{bmatrix}^T.
$$
> Hence, **we can use least squares**.

- In ARXAR models the predictor contains the products $A(z)B(z)$, and $B(z)D(z)$ which are **bilinear in the parameters**. Thus, if one fixes $D(z)$, then $\hat{y}(t|t-1)$ depends _linearly_ on the $a_i$, and $b_i$ parameters. Conversely, if $A(z)$, and $B(z)$ are fixed, $\hat{y}(t|t-1)$ depends _linearly_ on the $d_i$ parameters.
One can still employ least squares, alternating between the $a_i$, $b_i$ parameters, and the $d_i$ parameters (it is possible to show that, under certain hypotheses, this converges).

- In ARMAX models $\hat{y}(t|t-1)$ depends on the parameters in a _nonlinear_ fashion.
Consider _e.g._ an $\text{ARMAX}(1, 0, 1)$, with polynomials $A(z) = 1 - az^{-1}$, $B(z) = b$, $C(z) = 1+cz^{-1}$.
It can be proven that:
$$
\frac{1}{C(z)} = 1-cz^{-1}+c^2z^{-2}-c^{3}z^{-3} + \ldots.
$$
> For, let $N^{(k)}$, and $Q^{(k)}$ be respectively the numerator and the quotient at the $k$-th step of long division between $1$, and $C(z)$.
We want to prove by induction that $Q^{(k)} = (-c)^kz^{-k}$.
Base case: $N^{(0)} = 1$, $Q^{(0)} = 1$ (_trivial_).
Inductive step: suppose that $N^{(k)}(z) = (-c)^k z^{-k}$, $Q^{(k)} = (-c)^kz^{-k}$.
Then:
$$
N^{(k+1)}(z) = N^{(k)}(z) - Q^{(k)}(1+cz^{-1}) = (-c)^{k+1}z^{-(k+1)}.
$$
> Hence, if we want to divide $N^{(k+1)}(z)$ by $C(z)$, $Q^{(k+1)}(z)$ must be:
$$
Q^{(k+1)}(z) = (-c)^{k+1}z^{-(k+1)}.
$$

> Another way to see that
$$
\frac{1}{C(z)} = 1-cz^{-1}+c^2z^{-2}-c^3z^{-3} + \ldots
$$
> is to observe that $1-cz^{-1}+c^2z^{-2}-c^{3}z^{-3} + \ldots$ is the geometric series of $-cz^{-1}$.

> Then:
$$
\frac{C(z) - A(z)}{C(z)} = \frac{1}{C(z)}(C(z) - A(z)) = (1-cz^{-1}+c^2z^{-2}-c^3z^{-3})(1+cz^{-1}-1+az^{-1}) =
$$

---

$$
= (a+c)z^{-1} - c(a+c)z^{-2} + c^2(a+c)z^{-3} - c^3(a+c)z^{-4} + \ldots \ .
$$

> Analogously:
$$
\frac{B(z)}{C(z)} = b -cbz^{-1} + c^2bz^{-2} - c^3bz^{-3} + \ldots \ .
$$

> **We cannot use a simple algorithm as least squares anymore**.

#### Asymptotic analysis of PEM methods

Let $\hat{\theta}_N$ be the minimum point of the cost function $J_N(\theta)$.
Now, since $\varepsilon(t)$ depends on the data, which are described as stochastic processes, then $\hat{\theta}_N$ is also a random variable, for each value of $N$.
We want to ask ourselves:
- what are the characteristics of the sequence $\hat{\theta}_N$ for increasing $N$?
- what happens _asymptotically_, _i.e._ for $N \rightarrow + \infty$?
- how good is the system estimate in those ideal conditions?

Assuming that the predictor is stable and that $u(\cdot)$ and $y(\cdot)$ are stationary processes (_remember that, if we are in control of the identification experiment $\mathcal{E}$, we can choose $u$ to be stationary_), then $\hat{y}(\cdot)$ will also be a stationary process.
Consequently, the residual $\varepsilon(t) = y(t) - \hat{y}(t)$ will be a stationary process as well, and the same applies to the sequence $\varepsilon^2(\cdot)$ (_I think that it can be proven, under certain additional hypotheses, that if $v(\cdot)$ is stationary, then $v^2(\cdot)$ is also stationary_).

Therefore, $J_N$ is the sample mean value of a stationary process.
If the process is ergodic (_things that holds for stationary processes, under mild assumptions_), then the sample mean will tend to the expected value:
$$
J_N(\theta) = \frac{1}{N} \sum_{t=\tau}^N \varepsilon^2(t; \theta) \stackrel{N \rightarrow + \infty}{\rightarrow} \overline{J}(\theta) = \mathbb{E}[\varepsilon^2(t; \theta)].
$$
If the convergence of $J_N$ is sufficiently regular (_I think that uniform convergence should be enough_), then the minimum of $J_N$ will converge to the minimum of $\overline{J}$ as well.
Accordingly, if we denote as $\Delta = \{ \overline{\theta} | \overline{J}(\overline{\theta}) \leq \overline{J}(\theta), \forall \theta \in \Theta \}$ the _set of minima_ of $\overline{J}$, we expect $\hat{\theta}_N$ to tend to $\Delta$.

Suppose that we are in the very fortunate case where $\mathcal{S} = M(\theta^\circ)$ for some $\theta^\circ$ (_that is, $\mathcal{S} \in \mathcal{M}(\theta)$_).
Does the fact that $\hat{\theta}_N \rightarrow \Delta$ for $N \rightarrow +\infty$ also imply that $\hat{\theta}_N \rightarrow \theta^\circ$, at least asymptotically?

To answer this question we need to decompose the expression of the residual:
$$
\varepsilon(t; \theta) = y(t) - \hat{y}(t; \theta) = \left[ y(t) - \hat{y}(t; \theta^\circ) \right] + \left[ \hat{y}(t; \theta^\circ) - \hat{y}(t; \theta) \right].
$$

---

- The first term in the RHS: $e(t) = y(t) - \hat{y}(t; \theta^\circ)$ is called **innovation**. It represents the error committed by the optimal predictor that we could calculate if we knew the true system ($e(t) = \varepsilon(t; \theta^\circ)$).

- The second term in the RHS: $\hat{y}(t; \theta^\circ) - \hat{y}(t; \theta)$ is the combination of two variables that both depend on the past of $u(\cdot)$, and $y(\cdot)$.

By what we have seen in "Prediction", for the optimal predictor, $\varepsilon(t; \theta^\circ)$ is uncorrelated with the past (_the optimal predictor exploits all the available information_). Hence the two terms in the RHS are uncorrelated.
In view of this, it holds that:
$$
\overline{J}(\theta) = \mathbb{V}\text{ar}[\varepsilon(t; \theta)] = \mathbb{V}\text{ar}[\varepsilon(t; \theta^\circ)] + \mathbb{V}\text{ar}[\hat{y}(t; \theta^\circ) - \hat{y}(t; \theta)] \geq \mathbb{V}\text{ar}[\varepsilon(t; \theta^\circ)] = \overline{J}(\theta^\circ).
$$
This means that **$\theta^\circ$ is certainly a minimum of $\overline{J}$**, _i.e._ it belongs to $\Delta$.
Then, if $\Delta$ is a singleton ($\overline{J}$ has a unique minimum), we can conclude that a PEM method will lead to a model that asymptotically tends to the true system.
However, in practice, it is very rarely the case that $\mathcal{S} \in \mathcal{M}(\theta)$. If this doesn't holds, then the models in the set $\Delta$ are the _best approximants_ of $\mathcal{S}$ within $\mathcal{M}(\theta)$.

In particular, we can distinguish between $4$ cases:
- $\mathcal{S} \in \mathcal{M}(\theta)$, and $\Delta$ is a singleton
In this case the only element of $\Delta$ is $\theta^\circ$, then $\hat{\theta}_N \rightarrow \theta^\circ$.

- $\mathcal{S} \in \mathcal{M}(\theta)$, and $\Delta$ is NOT a singleton
Now $\Delta$ contains other points besides $\theta^\circ$. These correspond to models which are equivalent to $\theta^\circ$ in terms of predictive performance.
The estimate $\hat{\theta}_N$ tends to a point in $\Delta$ (_not necessarily $\theta^\circ$_), **or enters in $\Delta$ without converging to a point**.

- $\mathcal{S} \not \in \mathcal{M}(\theta)$, and $\Delta$ is a singleton
There is only one optimal models in $\mathcal{M}(\theta)$, say $\overline{\theta}$, but it does not coincide with the true system: $\overline{\theta}$ is the best approximant of the true system in $\mathcal{M}(\theta)$.

- $\mathcal{S} \not \in \mathcal{M}(\theta)$, and $\Delta$ is NOT a singleton
$\Delta$ contains the best approximants of the true system in $\mathcal{M}(\theta)$. Then, $\hat{\theta}_N$ tends to a point in $\Delta$ (not necessarily $\theta^\circ$), **or asymptotically wands in $\Delta$**.

#### Experimental vs Structural identifiability

- If it is possible to _unambiguously estimate all the parameters_ (_i.e._ $\Delta$ is a singleton), we say that the system is _identifiable_.

Identifiability depends on:
- the _identification experiment_ $\mathcal{E}$ (since $\hat{y}$ depends onto $u$, the choice of $u$ affects the expression of $\overline{J}$);

---

- the _model family_ $\mathcal{M}(\theta)$.

The input should be sufficiently "_rich_" of information content to allow the unambiguous estimation of all parameters.
If the experiment cannot be designed ad hoc, we should employ a model family with few parameters (_i.e. such that the unambiguous estimation of all parameters is indeed possible_).

- **Experimental identifiability** refers to the uniqueness of the parameter values compatibly with the information contained in the data.

- **Structural identifiability** refers to the property that the best approximant of $\mathcal{S}$ in $\mathcal{M}(\theta)$ is unique.

> If, for example, $\mathcal{S}$ is an $\text{ARMAX}(1, 1, 1)$, and $\mathcal{M}$ is the family of $\text{ARMAX}(2, 2, 2)$, however we design $\mathcal{E}$, the set $\Delta$ will be infinite (_as we already saw in the "Uniqueness" paragraph, if the $\text{ARMAX}(1, 1, 1)$ has polynomials $A_1(z)$, $B_1(z)$, $C_1(z)$, we can build an  $\text{ARMAX}(2, 2, 2)$ with polynomials $A_2(z) = A_1(z)D(z)$, $B_2(z) = B_1(z)D(z)$, $C_2(z) = C_1(z)D(z)$ for every Schur stable polynomial $D(z) = 1 + d_1 z^{-1}$, condition satisfied if $|d_1| < 1$_).
In this case, we say the **the model is _over-parameterized_**.

> In the opposite case (we swap the families of $\mathcal{S}$, and $\mathcal{M}(\theta)$) we say the **the model is _under-parameterized_**. Anyway, unless $\mathcal{E}$ is badly designed, the set $\Delta$ will be a singleton, albeit not corresponding to the true system.

#### Uncertainty of the estimated parameters

Assume that $\Delta = \{ \overline{\theta} \}$, with $\overline{\theta}$ not on the boundary of $\Theta$ (_we need to take derivatives wrt $\overline{\theta}$_).
Let also $\mathcal{S} \in \mathcal{M}(\theta)$, so that $\overline{\theta} = \theta^\circ$.
Define the (column) vector with the same size as $\theta$:
$$
\psi(t; \theta) = -\left(\frac{\partial \epsilon(t; \theta)}{\partial \theta}\right)^T.
$$
Notice that, if all the involved processes are stationary, then the same is true for $\psi(\cdot)$.
Then, we can define:
$$
\overline{R} = \mathbb{E}[\psi(t; \theta^\circ) \psi^T(t; \theta^\circ)].
$$
It can be shown that for large $N$, the variance of the PEM estimator $\hat{\theta}_N$ is given by $\frac{\overline{P}}{N}$, where:
$$
\overline{P} = \mathbb{V}\text{ar}[\varepsilon(t; \theta^\circ)] \overline{R}^{-1} \text{, or, more precisely, } \sqrt{N}(\hat{\theta}_N - \theta^\circ) \sim \text{As}G(0, \overline{P}).
$$
(_$\text{As}G$ stands for asymptotically gaussian_).

---

In other words, matrix $\overline{P}$ provides the variance of the vector of estimated parameters. To estimate $\overline{P}$ in practice we will approximate $\overline{R}$ with its sampled version:
$$
\frac{1}{N} \sum_{t=1}^N \psi(t; \hat{\theta}_N) \psi^T(t; \hat{\theta}_N).
$$
Similarly, we can estimate $\mathbb{V}\text{ar}[\varepsilon(t; \theta^\circ)]$ using:
$$
\frac{1}{N} \sum_{t=1}^N \varepsilon^2(t; \hat{\theta}_N).
$$