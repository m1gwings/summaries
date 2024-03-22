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

#### Purely non-deterministic processes

An important family of purely non-deterministic processes is that of stationary processes obtained by **filtering white noise** through a **dynamical system** described by an **asymptotically stable** transfer function.

##### Moving average process

- Given $\eta(\cdot) \sim WN(0, \lambda^2)$, we denote as **moving average** (**MA**) **process** of order $n$ (briefly, $\text{MA}(n)$) the stochastic process defined by the expression:
$$
v(t) = c_0 \eta(t) + c_1 \eta(t-1) + \ldots + c_n \eta(t-n)
$$
> where $c_0, c_1, \ldots, c_n$ are real numbers.
In other words, $v(t)$ is given by a _linear combination_ (weighted average) of the current and past values of the white process,
over a _time window_ from $t$ to $t-n$.
As $t$ increases, the window on which the average is computed also shifts: this is why we refer to this process as _moving average_.

- For conceptual reasons it is important to introduce the **MA process of infinite order** ($\text{MA}(\infty)$):
$$
v(t) = \sum_{i=0}^{+\infty} c_i \eta(t-i) \text{.}
$$
> The expected value is $0$, but the variance may converge or diverge:
$$
\gamma_{vv}(0) = \sum_{i=0}^{+\infty} c_i^2 \lambda^2
$$
> (_see property 10.b_). The variance if finite iff $\sum_{i=0}^{+\infty} c_i^2 < + \infty$.
This condition also guarantees that all elements of $\gamma(\tau)$ are finite (since $|\gamma(\tau)| \leq \gamma(0)$), and therefore ensures that the process is stationary (_I haven't got why this implies stationarity_).

- We can define the **generalized MA** (briefly, GMA) **process**:
$$
v(t) = c_0 \eta(t) + c_1 \eta(t-1) + \ldots + c_n \eta(t-n) \text{,}
$$
> where $\eta$ is a stationary process, but <u>not white</u>.

##### The auto-regressive process

In MA processes (of finite order) $\gamma(\tau)$ has non-null elements only up to $|\tau| = n$. To have $\gamma(\tau) \neq 0$ for all values of $\tau$, one has to resort to the $\text{MA}(\infty)$ process, which however has infinite parameters. Auto-regressive models can achieve the same property with a finite number of coefficients.

---

- Given $\eta(\cdot) \sim WN(0, \lambda^2)$, we denote as **auto-regressive process** of order $n$ (briefly, $\text{AR}(n)$) the stochastic process defined by the expression:
$$
v(t) = a_1 v(t-1) + a_2 v(t-2) + \ldots + a_n v(t-n) + \eta(t)
$$
> where $a_1, \ldots, a_n$ are real numbers (**when the resulting process is stationary**).

##### ARMA process

- Given $\eta(\cdot) \sim WN(0, \lambda^2)$, we denote **ARMA** process the stochastic process defined by the expression:
$$
v(t) = a_1 v(t-1) + a_2 v(t-2) + \ldots + a_{n_a} v(t-n_a) + c_0 \eta(t) + c_1 \eta(t-1) + \ldots + c_{n_c} \eta(t-n_c)
$$
> where $a_1, a_2, \ldots, a_{n_a}, c_0, c_1, \ldots, c_{n_c}$ are real numbers (**when the resulting process is stationary**). We refer briefly to processes of this kind with $\text{ARMA}(n_a, n_c)$.

##### ARMAX process

The models that we've seen so far are suitable for describing time series, but they do not enable us to represent phenomena subject to the influence of other, external variables (_eXogenous variables_).

- The simplest extension that we can apply to the previous classes of models is the so called **ARMAX**, where we have renamed the process to $y(\cdot)$, in analogy to the notation of input-output systems:
$$
A(z) y(t) = B(z) u(t-k) + C(z) \eta(t)
$$
> where:
> - $u(\cdot)$ is the input variable;
> - $B(z) = b_0 + b_1 z^{-1} + \ldots + b_{n_b} z^{-n_b}$;
> - $k$ is the **input-output delay**.

> In the time domain, the expression becomes:
$$
y(t) = a_1 y(t-1) + a_2 y(t-2) + \ldots + a_{n_a} y(t-n_a) + b_0 u(t-k) + 
$$

$$
+ b_1 u(t-k-1) + \ldots + b_{n_b}(t-k-n_b) + c_0 \eta(t) + c_1 \eta(t - 1) + \\
$$

$$
+ \ldots + c_{n_c} \eta(t-n_c) \text{.}
$$

---

#### Frequency analysis

- The **spectrum** of a stationary stochastic process $v$ is the Fourier transform of the <u>correlation</u> function:
$$
\Gamma_{vv}(\omega) = \mathcal{F}[\tilde{\gamma}_{vv}(t)] = \sum_{\tau = - \infty}^{+ \infty} \tilde{\gamma}_{vv}(\tau) e^{-j \omega \tau}
$$
> where $\omega$ is the angular frequency (_measured in $\frac{\text{rad}}{\text{s}}$_).

- The **complex spectrum** of a stationary stochastic process $v$ is the bilateral $\mathcal{Z}$-transform of the correlation function:
$$
\Phi_{vv}(z) = \sum_{\tau = - \infty}^{+ \infty} \tilde{\gamma}_{vv}(\tau) z^{-\tau} \text{.}
$$

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
> which in operatorial notation becomes:
$$
P(z) v(t) = 0 \text{,}
$$

---

> $P(z) = z^n - a_1z^{n-1} - a_2z^{n-2} - \ldots - a_n$. This can only happen if $v(t)$ is of the type:
$$
v(t) = \alpha_1 \lambda_1^t + \alpha_2 \lambda_2^t + \ldots + \alpha_n \lambda_n^t
$$
> where $\lambda_1, \lambda_2, \ldots, \lambda_n$ are the zeros of $P(z)$. This is clearly a sufficient condition for the exponential response theorem [_see "fondamenti di controlli automatici", p. 256_], which states that, for a certain initial condition $v(0)$, the movement of a (discrete-time) dynamical system subject to the input $u(t) = U \lambda^t$ is:
$$
y(t) = W(\lambda) U \lambda^t
$$
> where $W(z)$ is the transfer function of the system. Hence, if the system is asymptotically stable, no matter the initial condition, we have that the movement of the system will tend asymptotically to $W(\lambda) U \lambda^t$.
The reason which make it also a necessary condition are unknown to me and are probably related to the theory of analytical functions.

8. **Wold decomposition**: any stationary process can be seen as the sum of two <u>uncorrelated</u> processes: a deterministic process, and $\sum_{i=0}^{+ \infty} w_i \eta(t-i)$ with $\eta(\cdot) \sim WN(\cdot, \cdot)$.

9. For the stochastic process $v(t) = \tilde{v}(t) + \hat{v}(t)$ where $\tilde{v}(t)$, and $\hat{v}(t)$ are two uncorrelated stationary processes with $0$ expected value, it holds that:
$$
\tilde{\gamma}_{vv}(\tau) = \tilde{\gamma}_{\tilde{v} \tilde{v}}(\tau) + \tilde{\gamma}_{\hat{v} \hat{v}}(\tau) \text{.}
$$

> **Proof**:
$$
\mathbb{E}[v(t)v(t-\tau)] = \mathbb{E}[\tilde{v}(t)\tilde{v}(t-\tau)] + \mathbb{E}[\tilde{v}(t)]\mathbb{E}[\hat{v}(t-\tau)] +
$$
$$
+ \mathbb{E}[\hat{v}(t)] \mathbb{E}[\tilde{v}(t - \tau)] + \mathbb{E}[\hat{v}(t)\hat{v}(t-\tau)] \text{.}
$$

#### Purely non-deterministic processes

##### Moving average process

10. Let's state some properties of a **$\text{MA}(n)$ process** $v$.
 a. Its expected value is:
 $$
 \mu_v = c_0 \mathbb{E}[\eta(t)] + c_1 \mathbb{E}[\eta(t-1)] + \ldots + c_n \mathbb{E}[\eta(t-n)] = 0 \text{.}
 $$
 > b. Its covariance function is:
 $$
 \gamma_{vv}(t) = \sum_{i=0}^{n - |\tau|} c_i c_{i+|\tau|} \lambda^2 \text{.}
 $$
 > Observe that $\gamma_{vv}(|\tau|) = 0$ if $|\tau| > n$.

---

 > **Proof**: Let $\tau \geq 0$.
 $$
 \gamma_{vv}(\tau) = \mathbb{E}\left[\sum_{i=0}^n c_i \eta(t-i) \sum_{j=0}^n c_j \eta(t-j-\tau) \right] \text{.}
 $$
 > Since white noise at different time step is uncorrelated, in the expression above:
 $$
 \mathbb{E}[\eta(t-i)\eta(t-j-i)] = \begin{cases}
 \lambda^2 \text{ if } t-i = t-j-\tau \text{ iff } j = i - \tau \\
 0 \text{ otherwise }
 \end{cases} \text{.}
 $$

 > Observe that $0 \leq j = i - \tau \leq n$ implies that $i \geq \tau$, $i \leq n + \tau$. Since $\tau \geq 0$, $n+\tau \geq n$, hence the only relevant constraint is that $i \geq \tau$.
 Hence:
 $$
 \gamma_{vv}(\tau) = \sum_{i=\tau}^n c_i c_{i-\tau} \lambda^2 = \sum_{i=0}^{n-\tau} c_ic_{i+\tau} \lambda^2 \text{.}
 $$
 > The result follows from the fact that, being even, if $\tau < 0$:
 $$
 \gamma_{vv}(\tau) = \gamma_{vv}(-\tau) = \gamma_{vv}(|\tau|) = \sum_{i=0}^{n-|\tau|}c_ic_{i+|\tau|} \lambda^2 \text{.}
 $$
 > c. The transfer function of the dynamical system which is fed with $\eta$ and produces $v$ is:
 $$
 W(z) = C(z) = c_0 + c_1 z^{-1} + \ldots + c_n z^{-n} = \frac{c_0 z^n + c_1 z^{n-1} + \ldots + c_n}{z^n} \text{.}
 $$
 > It tells us that the system is asymptotically stable (all poles are 0) (_see properties 4 and 8 of discrete-time LTI systems_), and that it is not proper (_the relative degree is 0_).
 **Proof**: just use operatorial notation.

 > d. The $\text{MA}(n)$ process is characterized by $n+2$ parameters: $c_0, c_1, \ldots, c_n, \lambda^2$. This representation is redundant, since the $\text{MA}(n)$ process with parameters $\tilde{c}_0 = \alpha c_0, \tilde{c}_1 = \alpha c_1, \ldots, \tilde{c}_n = \alpha c_n, \tilde{\lambda}^2 = \frac{\lambda^2}{\alpha^2}$ has identical probabilistic characteristics of the 1st and 2nd order (_it follows from properties 10.a, and 10.b_).
 To avoid this source of redundancy, parameter $c_0$ is normally set to 1 ($C(z)$ is a _monic_ polynomial).
 
 > e. What if $\eta(\cdot) \sim WN(\eta, \lambda^2)$ with $\mu \neq 0$. Then:
 $$
 \mu_v = c_0 \mathbb{E}[\eta(t)] + c_1 \mathbb{E}[\eta(t-1)] + \ldots + c_n \mathbb{E}[\eta(t-n)] = (c_0 + c_1 + \ldots + c_n) \mu \text{.}
 $$
 > But, since we can write
 $$
 v(t) = c_0 \tilde{\eta}(t) + c_1 \tilde{\eta}(t-1) + \ldots + c_n \tilde{\eta}(t-n) + (c_0 + c_1 + \ldots + c_n) \mu
 $$

---
 > where $\tilde{\eta}(\cdot) = \eta(\cdot) - \mu \sim WN(0, \lambda^2)$ (_since the variance is invariant to constant shifts_), then the expression of $\gamma_{vv}$ stays the same (_again because variance and covariance are invariant to constant shifts and $(c_0 + c_1 + \ldots + c_n) \mu$ is a constant_).


11. The variance of the GMA process $v$ fed by the stationary process $\eta$ is:
$$
\gamma_{vv}(0) = \sum_{i=0}^n c_i^2 \gamma_{\eta \eta}(0) + 2 \sum_{\tau = 1}^{n} \sum_{i=0}^{n-\tau} c_i c_{i+\tau} \gamma_{\eta \eta}(\tau) \text{.}
$$

> **Proof**: Let $A = \{ (i, j) \mid i, j \in \{ 0, \ldots, n \} \}$, $B_1 = \{ (i, i) \mid i \in \{ 0, \ldots, n \} \}$, $B_2 = \{ (i, i + \tau) \mid \tau \in \{ 1, \ldots, n \}, i \in \{ 0, \ldots, n-\tau \} \}$, $B_3 = \{ (j+\tau, j) \mid \tau \in \{ 1, \ldots, n \}, j \in \{ 0, \ldots, n-\tau \} ) \}$. It is easy to show that $A = B_1 \cup B_2 \cup B_3$, and that $B_1$, $B_2$, and $B_3$ are pairwise disjoint.
In virtue of this, we can write:
$$
\sum_{i=0}^n \sum_{j=0}^n a_{ij} = \sum_{i=0}^n a_{ii} + \sum_{\tau=1}^n \sum_{i=0}^{n-\tau} a_{i i+\tau} + \sum_{\tau=1}^n \sum_{j=0}^{n-\tau} a_{j+\tau j} \text{.}
$$
> If we apply it to
$$
\gamma_{vv}(0) = \sum_{i=0}^n \sum_{j=0}^n \mathbb{E}[c_i \eta(t-i) c_j \eta(t-j)] \text{,}
$$
> where $a_{ij} = \mathbb{E}[c_i \eta(t-i) c_j \eta(t-j)]$, we get:
$$
\gamma_{vv}(0) = \sum_{i=0}^n c_i^2 \mathbb{E}[\eta^2(t-i)] + \sum_{\tau=1}^n \sum_{i=0}^{n-\tau} c_i c_{i+\tau} \mathbb{E}[\eta(t-i) \eta(t-i-\tau)] + 
$$
$$
+ \sum_{\tau=1}^n \sum_{j=0}^{n-\tau} c_{j+\tau} c_j \mathbb{E}[\eta(t -j -\tau) \eta(t-j)] = \sum_{i=0}^n c_i^2 \gamma_{\eta \eta}(0) + \sum_{\tau=1}^n \sum_{i=0}^{n-\tau} c_i c_{i+\tau} \gamma_{\eta\eta}(\tau) +
$$
$$
+ \sum_{\tau=1}^n \sum_{j=0}^{n-\tau} c_{j+\tau} c_j \gamma_{\eta \eta}(-\tau) = \sum_{i=0}^n c_i^2 \gamma_{\eta \eta}(0) + 2 \sum_{\tau=1}^n \sum_{i=0}^{n-\tau} c_i c_{i+\tau} \gamma_{\eta\eta}(\tau) \text{,}
$$
> where the last equality comes from the fact that $\gamma_{\eta \eta}$ is even (_by property 5.c_).

> We proved that the variance of the process does not depend upon $t$, the same can be shown to hold for $\gamma_{v v}(\tau)$ for any value of $\tau$ (_the proof should be analogous_). This implies that **passing a stationary process through an MA model produces a stationary process**.

##### The auto-regressive process

12. Let's state some properties of a **$\text{AR}(n)$ process** $v$.
 a. We can write the expression of the process in operatorial notation:

---

$$
(1 - a_1 z^{-1} - a_2 z^{-1} - \ldots - a_n z^{-n}) v(t) = \eta(t)
$$
> hence, the transfer function of the process is:
$$
W(z) = \frac{1}{A(z)} = \frac{1}{1 - a_1 z^{-1} - a_2 z^{-2} - \ldots - a_n z^{-n}} = \frac{z^n}{z^n - a_1 z^{n-1} - a_2 z^{n-2} - \ldots a_n} \text{.}
$$
> If the system is asymptotically stable, whatever the initial condition, $v(t)$ **converges to a stationary process** (**this is relevant for exercises**: we can show that the system is stationary by checking that the transfer function is the one of an asymptotically stable system; then it is easier to compute mean and covariance from the expression of the process) which is the only stationary process that solves the defining time domain equation.

13. The expression of a $\text{AR}(1)$ process is equivalent to:
$$
v(t) = \sum_{i = t_0}^{t-1} a^{t-1-i} \eta(i+1) + a^{t-t_0} v(t_0) \text{, for } t \geq t_0 \text{.}
$$

> **Proof**: By induction (_the base case is trivially verified_):
$$
v(t) = a v(t-1) + \eta(t) = a \sum_{i=t_0}^{t-2}a^{t-2-i}\eta(i+1) + a^{t-t_0} v(t_0) + \eta(t) =
$$
$$
= \sum_{i=t_0}^{t-2}a^{t-1-i} \eta(i+1) + a^{t-1-(t-1)} \eta(t-1+1) + a^{t-t_0}v(t_0) \text{.}
$$

> If $|a| < 1$, the last term vanishes as $t_0 \rightarrow -\infty$, and the process becomes:
$$
v(t) = \sum_{j=0}^{+\infty} a^j \eta(t-j) \text{ (by putting } j = t-i-1 \text{).} 
$$
> That is $v$ is an $\text{MA}(\infty)$ process with coefficients $1, a, a^2, \ldots$ . Hence, $\mathbb{E}[v(t)] = 0$. Furthermore, thanks to property 10.b:
$$
\gamma_{vv}(\tau) = \sum_{j=0}^{+\infty} a^{j}a^{j+|\tau|} \lambda^2 = a^{|\tau|} \sum_{j=0}^{+\infty} a^{2j} \lambda^2 = a^{|\tau|} \frac{1}{1-a^2} \lambda^2 = \frac{\lambda^2 a^{|\tau|}}{1-a^2} \text{.}
$$
> (_Observe that the geometric series converges since $|a| < 1$_).

14. It is possible to prove that the generic $\text{AR}(n)$ process (_obtained from an asymptotically stable system_) is equivalent to a $\text{MA}(\infty)$ process. This also implies that its expected value is 0 (assuming that the same holds for $\eta$ as in the definition).

15. **Yule-Walker equations**: consider an $\text{AR}(n)$ process obtained from an asymptotically stable system. By property 12, we know that it must be stationary.
Yule-Walker equations allow to compute its covariance function easily.

---

> Observe that:
$$
v(t) = \sum_{i=1}^n a_i v(t-i) + \eta(t) \text{.}
$$
> Then, for $\tau \geq 0$:
$$
\gamma_{vv}(\tau) = \mathbb{E}[(\sum_{i=1}^n a_i v(t-i) + \eta(t))v(t-\tau)] = \sum_{i=1}^n a_i \mathbb{E}[v(t-i)v(t-\tau)] + \mathbb{E}[\eta(t)v(t-\tau)] \text{.}
$$
> Because of property 14, $v(t-\tau)$ depends on the values of $\eta$ up to time $t - \tau$. Hence:
$$
\mathbb{E}[\eta(t)v(t-\tau)] = \begin{cases}
\lambda^2 \text{ if } \tau = 0 \text{ (see the expression of } v(t) \text{)} \\
0 \text{ if } \tau > 0
\end{cases} \text{.}
$$
> If $\tau \in \{ 0, \ldots, n \}$, we can rewrite $\gamma_{vv}$ as:
$$
\gamma_{vv}(\tau) = \sum_{i=1}^{\tau} a_i \gamma_{vv}(\tau - i) + \sum_{i = \tau +1}^n a_i \gamma_{vv}(i-\tau) + \begin{cases}
\lambda^2 \text{ if } \tau = 0 \\
0 \text{ if } \tau > 0
\end{cases}
$$
> which produces $n+1$ equations with $n+1$ unknowns: $\gamma_{vv}(0), \ldots, \gamma_{vv}(n)$.
If $\tau > n$ instead:
$$
\gamma_{vv}(\tau) = \sum_{i=1}^n a_i \gamma_{vv}(\tau - i) \text{.}
$$
> Hence we can solve the system to obtain $\gamma_{vv}(0), \ldots, \gamma_{vv}(n)$, and then compute $\gamma_{vv}(n+1), \gamma_{vv}(n+2), \ldots$ iteratively through the expression above.
Finally, the values of $\gamma_{vv}(\tau)$ for $\tau < 0$ are easily determined since $\gamma_{vv}$ is even.

##### ARMA process

16. The expression which describes an ARMA process is the series of an auto-regressive and a moving average model.

> **Proof**: Let $x(t) = \sum_{i=1}^{n_a} a_i x(t-i) + \eta(t)$ be the output of the auto-regressive model. If $v$ is the moving average of $x$ then:
$$
v(t) = \sum_{j=0}^{n_c} c_j x(t-j) = \sum_{j=0}^{n_c} c_j (\sum_{i=1}^{n_a} a_i x(t-i-j) + \eta(t-j)) =
$$
$$
= \sum_{i=1}^{n_a} a_i \sum_{j=0}^{n_c} c_j x(t-i-j) + \sum_{j=0}^{n_c} c_j \eta(t-j) = \sum_{i=1}^{n_a} a_i v(t-i) + \sum_{j=0}^{n_c} c_j \eta(t-j) \text{.}
$$

---

> Furthermore, by writing the expression of $v(t)$ in operatorial notation, we get the transfer function:
$$
v(t) = W(z) \eta(t) = \frac{C(z)}{A(z)} \eta(t) = \frac{c_0 +c_1z^{-1} + \ldots + c_{n_c} z^{-n_c}}{1-a_1 z^{-1} - \ldots - a_{n_a} z^{-n_a}} \eta(t) \text{.}
$$
> **If the transfer function is the one of an asymptotically stable system, then the process generated by the equation is stationary**. Again, under this hypothesis, the ARMA process is equivalent to an $\text{MA}(\infty)$ process. **We can compute the coefficient of the moving average through long division of $W(z)$** (_see property 7 of "Discrete time signals and systems" summary_).

17. If an ARMA process is stationary, we can exploit stationarity to compute its expected value from the expression which defines the process. Furthermore, to compute the covariance function it is possible to generalize the Yule-Walker equations to ARMA processes (_see property 15_).

##### Vanishing covariance property

18. The previous classes of processes share the property that $\lim_{\tau \rightarrow + \infty} \gamma(\tau) = 0$.
 a. For $\text{MA}(n)$ processes, $\gamma(\tau) = 0$ for $\tau > n$ (_see proeprty 10.b_).

 > b. For an $\text{AR}(1)$ process it holds that $\gamma(\tau) = a^{|\tau|} \gamma(0)$ (_see property 13_), which implies the vanishing property, since $|a| < 1$.

 > c. For an $\text{AR}(n)$ process, if $\tau > n$, it holds that:
 $$
 \gamma(\tau) = a_1 \gamma(\tau - 1) + a_2 \gamma(\tau - 2) + \ldots + a_{n_a} \gamma(\tau - n_a)
 $$
 > (_see property 15_), which in operatorial notation becomes $A(z) \gamma(\tau) = 0$, and is equivalent to $\gamma(\tau) = \frac{1}{A(z)} 0$. We know that the system described by $\frac{1}{A(z)}$ is asymptotically stable (remember that this is the condition that implies the stationarity of the process, _see property 12_). Hence, if we subject the system to null input, the output will be null asymptotically. Since the output is $\gamma(\tau)$, it must go to $0$.
 
 > d. For $\text{ARMA}(n_a, n_c)$ processes, the Yule-Walker equation is still valid for sufficiently large values of $\tau$ ($\tau > n_c$), and so the same consequence follows.

#### Frequency analysis

19. The sum of the Fourier series exists only for stationary processes whose correlation function $\tilde{\gamma}_{vv}(\tau)$ tends to $0$ sufficiently rapidly when $\tau$ tends to infinity. A sufficient condition for the existence of the Fourier transform is the absolute convergence of $\tilde{\gamma}_{vv}(\tau)$.

20. Let $\Gamma_{vv}(\omega)$ be the spectrum of a stationary stochastic process $v$. The anti-transformation formula allows to retrieve the correlation function of the process and to establish a one-to-one correspondence between it and the spectrum:


---

$$
\tilde{\gamma}_{vv}(\tau) = \mathcal{F}^{-1}[\Gamma(\omega)] = \frac{1}{2 \pi} \int_{-\pi}^{\pi} \Gamma_{vv}(\omega) e^{j \omega \tau} d \omega \text{.}
$$

21. From the definition of spectrum, remembering that $\tilde{\gamma}$ is even, it follows that:
$$
\Gamma(\omega) = \ldots + \tilde{\gamma}(-2) e^{j2\omega} + \tilde{\gamma}(-1) e^{j\omega} + \tilde{\gamma}(0) + \tilde{\gamma}(1)e^{-j\omega} + \tilde{\gamma}(2)e^{j2\omega} + \ldots =
$$

$$
= \tilde{\gamma}(0) + \tilde{\gamma}(1)(e^{j\omega} + e^{-j\omega}) + \tilde{\gamma}(2)(e^{j2\omega} + e^{-j2\omega}) + \ldots =
$$

$$
= \tilde{\gamma}(0) + 2 \tilde{\gamma}(1) \cos(\omega) + 2 \tilde{\gamma}(2) \cos(2 \omega) + \ldots \text{.}
$$
> Therefore, the spectrum $\Gamma(\omega)$ is:
 a. a **real** function;
 
 > b. an **even** function;
 
 > c. a **periodic** function of period $2 \pi$.

 > Furthermore, it can be proven that it is also:
 d. **non-negative**.

22. For a stationary stochastic processes with zero expected value, the variance of the process is proportional to the are below the spectrum curve.

> **Proof**: by the anti-transformation formula:
$$
\gamma(0) = \tilde{\gamma}(0) = \frac{1}{2\pi} \int_{-\pi}^{\pi} \Gamma(\omega) d\omega \text{.}
$$

23. For a stationary stochastic process $v$ it holds that:
$$
\Phi_{vv}(e^{j \omega}) = \Gamma_{vv}(\omega), \forall \omega \text{.}
$$

> **Proof**: straightforward by comparing both definitions.


24. The spectrum of $\eta(\cdot) \sim WN(0, \lambda^2)$ is:
$$
\Gamma_{\eta \eta}(\omega) = \lambda^2, \forall \omega \text{.}
$$


> **Proof**: follows from the definition of spectrum and from property 6.

25. **Fundamental theorem of spectral analysis**: consider the process $y(\cdot)$ obtained by filtering a <u>stationary</u> input process $u(\cdot)$ through an <u>asymptotically stable</u> dynamical system described by the transfer function $W(z)$:
$$
y(t) = W(z) u(t) \text{,}
$$
> then it holds the following relationship among the spectrum of the two processes:
$$
\Gamma_{yy}(\omega) = |W(e^{j \omega})|^2 \Gamma_{uu}(\omega) \text{.}
$$

---

> **Proof**: to compute the input-output cross-correlation function, we can exploit property 11 in _"Discrete time signals and systems"_ (_assuming that we're at steady state_):
$$
y(t) = \sum_{i=0}^{+ \infty} w(i) u(t-i) \text{,}
$$
> where $w(i)$ is the impulse response of the system (with zero initial condition).
If we multiply both sides by $u(t-\tau)$, we get:
$$
y(t)u(t-\tau) = \sum_{i=0}^{+ \infty} w(i) u(t-i) u(t-\tau) \text{.}
$$
> If we do the same, multiplying this time by $y(t-\tau)$, we get:
$$
y(t)y(t - \tau) = \sum_{i=0}^{+ \infty} w(i) u(t-i) y(t - \tau) \text{.}
$$
> By taking expectation of both expressions, we obtain (_remember that $u(\cdot)$ is stationary by assumption, and $y(\cdot)$ is stationary since the dynamical system is asymptotically stable [we never proved nor stated this result]_):
$$
\tilde{\gamma}_{yu}(\tau) = \sum_{i=0}^{+ \infty} w(i) \tilde{\gamma}_{uu}(\tau-i) \text{,}
$$
$$
\tilde{\gamma}_{yy}(\tau) = \sum_{i=0}^{+ \infty} w(i) \tilde{\gamma}_{uy}(\tau-i) \text{.}
$$
> [_Remember that $\mathbb{E}[v_1(t_1)v_2(t_2)] = \tilde{\gamma}_{v_1v_2}(t_1-t_2)$ assuming that the two processes are stationary_].
> Let's compute the complex spectrum of these correlation functions, remembering that the $\mathcal{Z}$-transform of the convolution is the product of the $\mathcal{Z}$-transforms (see property 12 of "Discrete time signals and systems" which can be generalized to the bilateral $\mathcal{Z}$-transform):
$$
\Phi_{yu}(z) = \mathcal{Z}[w(i)] \Phi_{uu}(z) = W(z) \Phi_{uu}(z) \text{,}
$$
$$
\Phi_{yy}(z) = W(z) \Phi_{uy}(z) \text{,}
$$
> where we used the fact that $\mathcal{Z}[w(i)] = W(z)$ (see property 8 of "Discrete time signals and systems").
Observe that:
$$
\tilde{\gamma}_{uy}(\tau) = \mathbb{E}[u(t)y(t-\tau)] = \mathbb{E}[y(t-\tau)u(t)] = \tilde{\gamma}_{yu}(-\tau) \text{,}
$$
> then, by property 13 of "Discrete time signals and systems":
$$
\Phi_{uy}(z) = \Phi_{yu}(-z) \text{.}
$$

---

> By combining the equalities we get:
$$
\Phi_{yy}(z) = W(z) W(z^{-1}) \Phi_{uu}(z^{-1}) = W(z) W(z^{-1}) \Phi_{uu}(z)
$$
> again, by property 13 of "Discrete time signals and systems", since $\tilde{\gamma}_{uu}$ is even.
The result is now proved by making the following remarks:
> - $\Gamma_{yy}(\omega) = \Phi_{yy}(e^{j\omega})$ (_just substitute in the definition of complex spectrum_);
> - $(e^{j \omega})^{-1}$ is the complex conjugate of $e^{j \omega}$, and, said $z^*$ the complex conjugate of $z$, by the properties of the conjugate, it holds that for every rational function $W(z)$: $W(z^*) = W(z)^*$;
> - $z z^* = |z|^2$.

> **Important remark**: the "_Fundamental theorem of spectral analysis_" relates the spectrum of a process with the frequency response $W(e^{j \omega})$ of the dynamical system which generates it. Hence, if the value of the spectrum at a given frequency is small, it means that signals at that frequency are attenuated by the system.

26. Let's list the expressions of the spectrum for some deterministic processes.
> - The **constant process**: $v(t) = v$, $\forall t$ where $v$ is a random variable.
>> $\tilde{\gamma}_{vv}(\tau) = \mathbb{E}[v^2]$, then $\Gamma_{vv}(\omega) = \mathbb{E}[v^2] \delta(\omega)$ (where $\delta(\omega)$ is _Dirac's delta_). Indeed:
$$
\mathcal{F}^{-1}[\Gamma_{vv}(\omega)] = \frac{1}{2 \pi} \int_{-\pi}^\pi \mathbb{E}[v^2] \delta(\omega) e^{j\omega} d\omega = \mathbb{E}[v^2] e^{j0} = \mathbb{E}[v^2] \text{.}
$$
>> _Remember that: $\frac{1}{2 \pi} \int_{-\pi}^{\pi} \delta(\omega - \omega_0) e^{j \omega} d\omega = e^{j \omega 0}$_.

> - The **alternated process**: $v(t) = (-1)^t v$, where $v$ is a random variable.
>> $\tilde{\gamma}_{vv}(\tau) = \mathbb{E}[(-1)^t v (-1)^{t-\tau} v] = (-1)^{- \tau} \mathbb{E}[v^2] = (-1)^\tau \mathbb{E}[v^2]$.
Then $\Gamma_{vv}(\omega) = \frac{\delta(\omega + \pi) + \delta(\omega - \pi)}{2}$ (_it can be verified through the anti-transform formula_). [_I've modified the formula which was originally on the slides, since the spectrum wasn't even_].

##### Spectral factorization

We have addressed the problem of calculating the spectrum of a process given the transfer function, but in practice the opposite is typically more useful: we are often given a set of data with certain spectral characteristics and we are faced with the problem of describing the generator process (i.e. of finding the pair $(W(z), \eta(\cdot))$).

**Observe that**:
- Given a spectrum, there is NOT always a corresponding (_rational_) transfer function (which would allow to interpret it as the spectrum of an ARMA process). 

---

> Indeed, the spectrum of an ARMA process has NOT a completely arbitrary shape: for example it cannot be 0 on an entire interval $[\omega_1, \omega_2]$ (_rational functions have a finite number of zeros, if they are different from zero [at least I think that this should hold :D]_). $\Gamma(\omega)$ must be a _rational function_ in $e^{j \omega}$.

- There are different pairs $(W(z), \eta(\cdot))$ which produce the same spectrum.

27. Let's list some **equivalent pairs $(W(z), \eta(\cdot))$**.
 a. **Multiplication by a constant**: let $\alpha \in \mathbb{R} \setminus \{ 0 \}$, $\tilde{W}(z) = \frac{1}{\alpha} W(z)$, $\tilde{\eta}(\cdot) = \alpha \eta(\cdot) \sim WN(0, \alpha^2 \lambda^2)$. Then:
$$
\tilde{\Phi}(z) = \frac{1}{\alpha} W(z) \frac{1}{\alpha} W(z^{-1}) \alpha^2 \lambda^2 = \Phi(z) \text{.}
$$
> Indeed, $\frac{1}{\alpha} W(z) \alpha \eta(t) = W(z) \eta(t) = v(t)$.

> b. **Multiplication by $z^n$**: let $\tilde{W}(z) = z^n W(z)$, $\tilde{\eta}(t) = z^{-n} \eta(t) = \eta(t-n)$, with $n \in \mathbb{N}$. Then:
$$
\tilde{\Phi}(z) = z^n W(z) z^{-n} W(z^{-1}) \lambda^2 = \Phi(z) \text{.}
$$
> Furthermore: $z^n W(z) z^{-n} \eta(t) = W(z) \eta(t) = v(t)$. That is, a **time shift** of the process **does NOT alter its process characteristics**.

> c. **Multiplication of both the numerator and the denominator by the same factor**: $\tilde{W}(z) = W(z) \frac{z-p}{z-p}$ with $p \in \mathbb{C}$, $|p| < 1$, $\tilde{\eta}(t) = \eta(t)$. Then:
$$
\tilde{\Phi}(z) = \Phi(z) \text{ since } W(z) = \tilde{W}(z) \text{ after the simplification.}
$$
> Indeed, $W(z) \frac{z-p}{z-p} \tilde{\eta}(t) = W(z) \eta(t) = v(t)$.

> d. **Multiplication by an all-pass filter**: let $\tilde{W}(z) = W(z)T(z)$ where
$$
T(z) = \frac{1}{q} \frac{z-q}{z-\frac{1}{q}} \text{,}
$$
> and $\tilde{\eta}(t) = \eta(t)$. The fact that $\tilde{\Phi}(z) = \Phi(z)$ follows from:
$$
T(z)T(z^{-1}) = \frac{1}{q} \frac{z-q}{z-\frac{1}{q}} \frac{1}{q} \frac{z^{-1} - q}{z^{-1} - \frac{1}{q}} = \frac{z-q}{qz-1}\frac{1-z q}{q - z} = 1 \text{.}
$$

> **Important remark**: if $q$ is a pole of $W(z)$, this operation essentially substitutes the pole in $q$ with one in $\frac{1}{q}$ (a similar reasoning applies to zeroes). Stated otherwise, **if we substitute a singularity of $W(z)$ with its reciprocal, the spectrum changes only by a constant factor**.

---

28. If we filter a stationary stochastic process through an "_un-normalized_" asymptotically stable all-pass filter $\hat{T}$, we get a stationary stochastic process with expected value, and covariance function multiplied by a factor $\hat{T}(1)$, and $\hat{T}^2(1)$ respectively, w.r.t. the original one. (Also the correlation function gets multiplies by $\hat{T}^2(1)$).

> **Proof**: let
$$
\hat{T}(z) = \frac{z-q}{z-\frac{1}{q}} \text{,}
$$
> $v_2(t) = \hat{T}(z) v_1(t)$. $v_2(\cdot)$ is stationary since $\hat{T}$ is the transfer function of an asymptotically stable system by assumption. Furthermore:
$$
v_2(t+1) - \frac{1}{q} v_2(t+1) = v_1(t+1) - q v_1(t+1) \text{.}
$$
> Hence:
$$
(1 - \frac{1}{q}) \mu_{v_2} = (1 - q) \mu_{v_1} \text{ iff } \mu_{v_2} = \hat{T}(1) \mu_{v_1} \text{.}
$$
> Observe that:
$$
\hat{T}(1) = \frac{1-q}{1-\frac{1}{q}} = q \frac{\frac{1}{q}-1}{1-\frac{1}{q}} = -q
$$
> Furthermore:
$$
\hat{T}(z) \hat{T}(z^{-1}) = \frac{1}{q^2} \frac{z-q}{z-\frac{1}{q}} \frac{z^{-1} - q}{z^{-1} - \frac{1}{q}} q^2 = 1 \cdot q^2 = \hat{T}^2(1) \text{.}
$$
> Then:
$$
\Gamma_{v_2 v_2}(\omega) = \left[ \hat{T}(z) \hat{T}(z^{-1}) \right]_{\vert_{z = e^{j \omega}}} \Gamma_{v_1 v_1}(\omega) = \hat{T}^2(1) \Gamma_{v_1 v_1}(\omega) \text{.}
$$
> Hence:
$$
\tilde{\gamma}_{v_2 v_2}(\tau) = \mathcal{F}^{-1}[\Gamma_{v_2 v_2}(\omega)] = \mathcal{F}^{-1}[\hat{T}^2(1) \Gamma_{v_1 v_1}(\omega)] = \hat{T}^2(1) \tilde{\gamma}_{v_1 v_1}(\tau) \text{.}
$$
> Finally:
$$
\gamma_{v_2 v_2}(\tau) = \tilde{\gamma}_{v_2 v_2}(\tau) - \mu_{v_2 v_2}^2 = \hat{T}^2(1) \tilde{\gamma}_{v_1 v_1}(\tau) - \hat{T}^2(1) \mu_{v_1}^2 = \hat{T}^2(1) \gamma_{v_1 v_1}(\tau) \text{.}
$$

Now we ask ourselves the following question: is there one representation that is more suitable than the others for solving the prediction problem?
The following result allows to select the so called _canonical representation_, which gets rid of all the possible sources of redundancy that we listed.

---

29. **Spectral factorization theorem**: let $v(\cdot)$ be a stationary stochastic process with rational spectrum.
There exist a unique pair $\left( \hat{W}(z) = \frac{C(z)}{A(z)}, \xi(t) \right)$ such that:
> 1. **$C(z)$** and **$A(z)$** are **monic**;

> 2. **$C(z)$** and **$A(z)$** have the **same degree**;

> 3. **$C(z)$** and **$A(z)$** are **co-prime** (_no common roots_);

> 4. **$C(z)$** and **$A(z)$** have all their **roots in the closed and open unit circle, respectively** ($|z| \leq 1$, $\forall z$ s.t. $C(z) = 0$, $|z| < 1$, $\forall z$ s.t. $A(z) = 0$).

> $\hat{W}(z)$ takes the name of _canonical spectral factor_.

> **Example**: consider the process
$$
v(t) = \eta_1(t-1) + \eta_2(t) - \eta_2(t-1)
$$
> where $\eta_1(\cdot) \sim WN(0, \lambda_1^2)$, and $\eta_2(\cdot) \sim WN(0, \lambda_2^2)$ are <u>independent</u> white noise processes.
The process is constructed as the sum of two stationary processes, and therefore it is also stationary.
It is easy to see that $\gamma_{vv}(\tau) = 0$ for $|\tau| > 1$. Then, the process can be reformulated as an $\text{MA}(1)$:
$$
v(t) = \xi(t) + c \xi(t-1) \text{,} \xi(t) \sim WN(0, \lambda^2)
$$
> provided it has the same spectral characteristics, or, which is equivalent, the same auto-covariance function.
By property 10.b:
$$
\gamma_{vv}(0) = (1 + c^2) \lambda^2 \text{,}
$$
$$
\gamma_{vv}(1) = c \lambda^2 \text{.}
$$
> If we compute the auto-covariance starting from the original expression:
$$
\gamma_{vv}(0) = \lambda_1^2 + 2 \lambda_2^2 \text{,}
$$
$$
\gamma_{vv}(1) = \mathbb{E}[(\eta_1(t-1) + \eta_2(t) - \eta_2(t-1))(\eta_1(t-2) + \eta_2(t-1) - \eta_2(t-2))] = - \lambda_2^2 \text{.}
$$
> If we equate the expressions and solve the system, we get two possible solutions: $(c = -\frac{1}{2}, \lambda^2 = 1)$, and $(c = -2, \lambda^2 = \frac{1}{4})$, but only the **first one is canonical** ($-c$ is a zero of the system).

> **Important remark**: suppose that
$$
v(t) = \frac{(1- c z^{-1}) C'(z)}{A(z)} \eta(t) \text{ with } |c|>1, \eta(\cdot) \sim WN(0, \lambda^2).
$$

---

> Hence, $\left(W(z) = \frac{(1- c z^{-1}) C'(z)}{A(z)}, \eta(t)\right)$ **is NOT a canonical representation of the process**. We can bring it in canonical form as follows:
$$
v(t) = \frac{(1- c z^{-1}) C'(z)}{A(z)} \frac{1-\frac{1}{c}z^{-1}}{1-\frac{1}{c}z^{-1}} \eta(t) = \frac{(1- \frac{1}{c} z^{-1}) C'(z)}{A(z)} T(z) \eta(t),
$$
> where
$$
T(z) = \frac{1-cz^{-1}}{1-\frac{1}{c}z^{-1}} \text{ is an all-pass filter}.
$$
> Observe that, since $|c|>1$, then $|\frac{1}{c}| = \frac{1}{|c|} < 1$. This implies that $T(z)$ is an "asymptotically stable all-pass filter". Then, by property 28,
$$
\eta'(t) = T(z) \eta(t) \sim WN(0, T^2(1) \lambda^2) = WN(0, c^2 \lambda^2),
$$
> and
$$
W'(z) = \frac{(1- \frac{1}{c} z^{-1}) C'(z)}{A(z)}
$$
> has one less zero outside of the unit circle. We can iterate the process until we remove all the zeros outside of the unit circle from $W(z)$. At the end we will reach $\left( \hat{W}(z), \xi(t) \right)$ with $\hat{W}(z)$ with no zeros or poles outside of the unit circle.