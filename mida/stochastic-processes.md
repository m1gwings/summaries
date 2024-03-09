---
marp: true
theme: summary
math: mathjax
---
# Stochastic processes

<div class="author">

Cristiano Migali

</div>

## Definitions

- A (discrete-time) **stochastic process** is an (infinite) sequence of random variables, that depend on the outcome of a <u>single</u> random experiment:
$$
v(t) = \phi(s, t)
$$
> where $s$ is the **outcome** of the random experiment, and $t \in \mathbb{Z}$ is the **sequence index**. 

> **Remark**: given $s$, $\phi(s, \cdot)$ is a sequence of real numbers [that is, a (discrete-time) signal], which are the values assumed by the process at the outcome $s$ of the random experiment, aka a **realization** of the process.
Given $t$, $\phi(\cdot, t)$ is a **random variable**.

- Given a stochastic process $v(t)$, its **expected value** is a sequence of real numbers defined by:
$$
\mu_v(t) = \mathbb{E}[v(t)] \text{.}
$$
> $\mu_v(t)$ represents the mean of $v(t) = \phi(s, t)$ over all possible outcomes $s \in S$.

- Given a stochastic process $v$, we define its (**auto-**)**covariance** function as:
$$
\gamma_{vv}(t_1, t_2) = \mathbb{E}[(v(t_1) - \mu_v(t_1))(v(t_2) - \mu_v(t_2))] \text{.}
$$
> For two different stochastic processes $v_1$, and $v_2$, we can define the **cross-covariance** function as:
$$
\gamma_{v_1v_2}(t_1, t_2) = \mathbb{E}[(v_1(t_1) - \mu_{v_1}(t_1))(v_2(t_2) - \mu_{v_2}(t_2))] \text{.}
$$

> **Remark**: $\gamma_{vv}(t, t) = \text{Var}[v(t)]$.

- Given a stochastic process $v$, we define its (**auto-**)**correlation** function as:
$$
\tilde{\gamma}(t_1, t_2) = \mathbb{E}[v(t_1)v(t_2)] \text{.}
$$
> For two different stochastic processes $v_1$, and $v_2$, we can define the **cross-covariance** function as:
$$
\tilde{\gamma}_{v_1v_2}(t_1, t_2) = \mathbb{E}[v_1(t_1) v_2(t_2)] \text{.}
$$

- Given a stochastic process $v$, we define its **normalized covariance** function as:
$$
\rho_{vv}(t_1, t_2) = \frac{\gamma_{vv}(t_1, t_2)}{\sqrt{\gamma_{vv}(t_1, t_1)} \sqrt{\gamma_{vv}(t_2, t_2)}} \text{.}
$$

---

### Stationary processes

- A stochastic process $v$ is said to be **strongly stationary** if, for any positive integer $n$, given $n$ instants $t_1, t_2, \ldots, t_n \in \mathbb{Z}$ (however chosen), the joint probability distribution functions of $v(t_1 + T), v(t_2 + T), \ldots, v(t_n+T)$ coincide for every $T \in \mathbb{Z}$. That is:
$$
F_{t_1, t_2, \ldots, t_n}(q_1, q_2, \ldots, q_n) = F_{t_1+T, t_2+T, \ldots, t_n+T}(q_1, q_2, \ldots, q_n) \forall T, q_1, q_2, \ldots, q_n \text{.}
$$

> **Remark**: observe that we can have random variables with the same distribution which assign a different real value to the same outcome $s$ of a random experiment.
Hence, **the realization of a stationary process need not to be constant** (_by the definition above, $v(t)$ has the same probability distribution at every time instant_).

- A stochastic process $v$ is said to be **weakly stationary** if:
> - $\mu_v(t) = \mu_v(t+T)$, $\forall T, t$;
> - $\gamma_{vv}(t_1, t_2) = \gamma_{vv}(t_1 + T, t_2 + T)$, $\forall T, t_1, t_2$.

> **Remark**: in a weakly stationary stochastic process $v$, the covariance and the correlation function depend only on the difference between the time instants. For let $t_1, t_2, t_1', t_2'$ s. t. $t_1 - t_2 = t_1' - t_2' = \tau$, then:
$$
\gamma_{vv}(t_1, t_2) = \gamma_{vv}(t_1, t_1-\tau) = \gamma_{vv}(t_1 + (t_1'-t_1), t_1 + (t_1' - t_1) - \tau) =
$$
$$
= \gamma_{vv}(t_1', t_1' - \tau) = \gamma_{vv}(t_1', t_2') \text{.}
$$

- A stochastic process $v$ is said to be **gaussian** if, for any positive integer $n$, given $n$ instants $t_1, t_2, \ldots, t_n$ (however chosen), the random variables $v(t_1), v(t_2), \ldots, v(t_n)$ are jointly gaussian.

- A stationary stochastic process is said to be **ergodic** if its statistical properties can be derived with probability 1 of performing a correct evaluation, from the analysis of only one realization of the process under consideration.
In other words, for an ergodic process the average sample value calculated on the data of a realization tends to the expected value (as the number of data goes to infinity):
$$
\lim_{N \rightarrow +\infty} \frac{1}{N} \sum_{i=1}^N \cdot = \mathbb{E}[\cdot] \text{.}
$$

- We define **white noise** a particular type of stationary stochastic process which consists in a sequence of i.i.d. random variables. A white noise whose random variables have mean $\mu$, and variance $\lambda^2$ is denoted as $\eta(\cdot) \sim WN(\mu, \lambda^2)$.

- We say that a stationary stochastic **process** is **deterministic** if, given a certain number of samples of a realization, it is possible to predict exactly its evolution.

---

## Properties

1. Given a stochastic process $v$, it holds for every couple of time instants $t_1$, $t_2$ that:
$$
|\gamma_{vv}(t_1, t_2)| \leq \sqrt{\gamma_{vv}(t_1, t_1)} \sqrt{\gamma_{vv}(t_2, t_2)} \text{.}
$$

> **Proof**: consider the random vector:
$$
\underline{v} = \begin{bmatrix}
v(t_1) - \mu_v(t_1) \\
v(t_2) - \mu_v(t_2)
\end{bmatrix}
$$
> for $t_1$, $t_2$ fixed. Observe that the matrix $\underline{v} \underline{v}^T$, being in _"Cholesky form"_, is positive semi-definite.
The positive semi-definiteness of $\underline{v} \underline{v}^T$ is preserved even when we take the expected value. For:
$$
\underline{x}^T \mathbb{E}[\underline{v} \underline{v}^T] \underline{x} = \mathbb{E}[ \underline{x}^T \underline{v} \underline{v}^T \underline{x}] \geq 0 \text{.}
$$
> (_Remember that the expected value is linear and preserves inequalities_).
Hence, the determinant of $\mathbb{E}[\underline{v} \underline{v}^T]$ (which is the product of its eigenvalues) must be non-negative (_see properties of positive semi-definite matrices in NAML summaries_). By writing down the expression of $\det \mathbb{E}[\underline{v} \underline{v}^T]$ and rearranging it we get:
$$
\gamma_{vv}(t_1, t_1) \gamma_{vv}(t_2, t_2) - (\gamma_{vv}(t_1, t_2))^2 \geq 0 \text{,}
$$
> which provides the result.

2. Given two stochastic processes $v_1$, $v_2$, it holds that:
$$
\gamma_{v_1v_2}(t_1, t_2) = \tilde{\gamma}_{v_1v_2}(t_1, t_2) - \mu_{v_1}(t_1) \mu_{v_2}(t_2)
$$
> for every couple of time instants $t_1$, $t_2$.

> **Proof**:
$$
\mathbb{E}[(v_1(t_1) - \mu_1(t_1))(v_2(t_2) - \mu_2(t_2))] =
$$

$$
= \mathbb{E}[v_1(t_1)v_2(t_2)] - \mu_1(t_1) \mathbb{E}[v_2(t_2)] - \mathbb{E}[v_1(t_1)] \mu_2(t_2) + \mu_1(t_1) \mu_2(t_2) \text{.}
$$

### Stationary processes

3. If a process is strongly stationary, then it is weakly stationary.

> **Proof**: it is clear by how the expected value is defined (since distributions are the same).

4. If a process is both weakly stationary and gaussian, then it is also strongly stationary.

> **Proof**: a gaussian distribution is uniquely determined by its mean and variance.

---

5. Let's state some properties of $\gamma_{vv}$ for a weakly stationary stochastic process $v$:
 a. $\gamma_{vv}(0) = \mathbb{E}[(v(t) - \mu_v)^2] \geq 0$;
 b. $|\gamma_{vv}(\tau)| \leq \gamma_{vv}(0), \forall \tau$ (_it is a direct consequence of property 1 and stationarity_);
 c. $\gamma_{vv}(\tau) = \gamma_{vv}(-\tau), \forall \tau$, that is, $\gamma_{vv}$ is an even function (_it follows from the fact that $v(t)v(t-\tau) = v(t-\tau)v(t)$ and from stationarity_);
 d. $\gamma_{vv}(\tau) = \tilde{\gamma}_{vv}(\tau) - \mu_v^2$ (_it is a direct consequence of property 2 and stationarity_);
 e. For any positive integer $N$:
 $$
 \begin{bmatrix}
 \gamma_{vv}(0) & \gamma_{vv}(1) & \gamma_{vv}(2) & \cdots & \gamma_{vv}(N-1) \\
 \gamma_{vv}(1) & \gamma_{vv}(0) & \gamma_{vv}(1) & \cdots & \gamma_{vv}(N-2) \\
 \gamma_{vv}(2) & \gamma_{vv}(1) & \gamma_{vv}(0) & \cdots & \gamma_{vv}(N-3) \\
 \vdots & \vdots & & \ddots & \vdots \\
 \gamma_{vv}(N-1) & \gamma_{vv}(N-2) & \gamma_{vv}(N-3) & \cdots & \gamma_{vv}(0)
 \end{bmatrix} \succcurlyeq 0 \text{.}
 $$
 > **Proof**: we can write the matrix above (_which is a Toeplitz matrix_) as $\mathbb{E}[\underline{\gamma} \underline{\gamma}^T]$ where
 $$
 \underline{\gamma} = \begin{bmatrix} 
    v(0) - \mu_v \\
    v(1) - \mu_v \\
    \vdots \\
    v(N-1) - \mu_v
 \end{bmatrix} \text{.}
 $$
 > f. An even function $\gamma(t)$ can be interpreted as the covariance function of a stationary process $\iff$ the associated Toeplitz matrix is positive semi-definite for all values of $N$.

6. For a white noise $\eta$:
$$
\gamma_{\eta \eta}(\tau) = \begin{cases}
0 \text{ if } \tau \neq 0 \\
\lambda^2 \text{ if } \tau = 0
\end{cases} \text{.}
$$

> **Proof**: it is a direct consequence of independence. (_Remember that if $X$, and $Y$ are two independent random variables, then $\mathbb{E}[XY] = \mathbb{E}[X]\mathbb{E}[Y]$_).

7. Stochastic processes that satisfy the following equation:
$$
v(t) = a_1v(t-1) + a_2v(t-2) + \ldots + a_nv(t-n)
$$
> are deterministic. Indeed, since $v(t)$ is a linear combination of past values of the process, it is perfectly predictable based on the past.
We can rewrite the equation above as:
$$
v(t+n) = a_1v(t+n-1) + a_2v(t+n-2) + \ldots + a_nv(t) \text{,}
$$
> which in operatorial notation 

8. **Wold decomposition**: any stationary process can be seen as the sum of two <u>uncorrelated</u> processes: a deterministic process, and a $\text{MA}(\infty)$ process.