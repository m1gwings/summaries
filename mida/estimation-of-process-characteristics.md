---
marp: true
theme: summary
math: mathjax
---
# Estimation of process characteristics

<div class="author">

Cristiano Migali

</div>

In this summary we will work in the following setting: there is a <u>stationary stochastic process</u> $v(t)$ with unknown probabilistic properties, of which we have a finite realization:
$$
\{ v(1), \ldots, v(N) \} \text{.}
$$
In other words, $v(1) = v(1; \overline{s})$, $v(2) = v(2; \overline{s})$, etc., where $\overline{s}$ is the outcome of the underlying random experiment.
We want to build some _functions of the available data_, known as **sample estimators**, to estimate the probabilistic properties of $v(t)$ ($\mu_v$, $\gamma_{vv}(\tau)$).

## Basic definitions

- An estimator is **correct** (or **unbiased**) if the expected value (taken w.r.t. all possible finite realizations of $v(t)$) of the estimator is equal to the probabilistic property to be estimated.

- An estimator is **consistent** it the _estimate error variance_ (i.e., the dispersion of the estimate around the true value [_for example $\mathbb{E}[(\hat{\mu}_N - \mu)^2]$_]) tends to zero as the number of data tends to infinity.

> **Remark**: an estimator is good if both correctness and consistency hold.

---

## The sample mean

A (_natural_) sample estimator of the mean would be:
$$
\hat{\mu}_N = \frac{1}{N} \sum_{t = 1}^N v(t) \text{.}
$$
It is a <u>correct estimator</u>:
$$
\mathbb{E}[\hat{\mu}_N] = \frac{1}{N} \sum_{t = 1}^N \mathbb{E}[v(t)] = \frac{1}{N} \mu_v \sum_{t=1}^N 1 = \mu_v \text{.}
$$
Observe that the correctness of an estimator does not suffice to conclude its goodness. For example, let $v(t, s) = v(s)$, $\forall t$, where $v(s)$ is a random variable. Then $\hat{\mu}_N = \frac{1}{N} v(\overline{s}) \sum_{t=1}^N = v(\overline{s})$ which can differ significantly from $\mu_v$. In this case, even though $\hat{\mu}_N$ is correct, it does not yield a good estimate of the expected value of $v(t)$, not even when there is an infinite amount of data. Indeed, if we try to verify the consistency of this estimator, we compute that:
$$
\mathbb{E}[(\hat{\mu}_N - \mu_v)^2] = \mathbb{E}[(v(s) - \mu)^2] = \mathbb{V}\text{ar}[v(s)]
$$
which can be different from 0 (depending on the distribution of $v(s)$).

Fortunately, if we **restrict our scope to ARMA processes**, we can prove a consistency result.
Observe that:
$$
\mathbb{E}[(\hat{\mu}_N - \mu_v)^2] = \mathbb{E}[(\frac{1}{N} \sum_{i=1}^N v(i) - \mu_v )( \frac{1}{N} \sum_{i=1}^N v(i) - \mu_v )] =
$$
$$
= \mathbb{E}[\frac{1}{N}(\sum_{i=1}^N v(i) - \sum_{i=1}^N \mu_v)\frac{1}{N}(\sum_{i=1}^N v(i) - \sum_{i=1}^N \mu_v)] = \frac{1}{N^2} \sum_{i=1}^N \sum_{j=1}^N \mathbb{E}[ (v(i) - \mu_v)(v(j) - \mu_v) ] =
$$
$$
= \frac{1}{N^2} \sum_{i=1}^N \sum_{j=1}^N \gamma_{vv}(i-j) \text{.}
$$

Because of the identity used in the proof ot property 11 in "_Stochastic processes_" summary:
$$
\mathbb{E}[(\hat{\mu}_N - \mu_v)^2] = \frac{1}{N^2} [ \sum_{i=1}^N \gamma_{vv}(0) + \sum_{\tau = 1}^{N-1} \sum_{i=1}^{N-\tau} \gamma_{vv}(-\tau) + \sum_{\tau = 1}^{N-1} \sum_{j=1}^{N-\tau} \gamma_{vv}(\tau) ] =
$$
$$
= \frac{1}{N^2}[\sum_{i=1}^N \gamma_{vv}(0) + 2 \sum_{\tau = 1}^{N-1} \sum_{i=1}^{N-\tau} \gamma_{vv}(-\tau)] = \frac{1}{N^2} [ N \gamma_{vv}(0) + 2 \sum_{\tau = 1}^{N-1}(N-\tau)\gamma_{vv}(\tau) ] =
$$

---

$$
= \frac{1}{N} \gamma_{vv}(0) + 2 \frac{1}{N} \sum_{\tau=1}^{N-1} (1-\frac{\tau}{N}) \gamma_{vv}(\tau) \text{.}
$$

Clearly $\frac{1}{N} \gamma_{vv}(0) \rightarrow 0$, as $N \rightarrow + \infty$. We need to prove that the same holds for $\sum_{\tau=1}^{N-1} (1-\frac{\tau}{N}) \gamma_{vv}(\tau)$.
Let $\epsilon > 0$. Since, as we showed in property 18 of "_Stochastic processes_" for ARMA processes holds the vanishing covariance property, then there exists $T$ s.t. if $\tau \geq T$, then $|\gamma_{vv}(\tau)| < \frac{\epsilon}{2}$.
Once $T$ is fixed, we can choose $\hat{N}$ big enough that $\frac{T-1}{\hat{N}} \gamma_{vv}(0) < \frac{\epsilon}{2}$, and $\hat{N} > T$ (_so that, as we will see later, we can split the sum_). Then:
$$
|\frac{1}{\hat{N}} \sum_{\tau = 1}^{\hat{N}-1}(1-\frac{\tau}{\hat{N}}) \gamma_{vv}(\tau) | \leq \frac{1}{\hat{N}} \sum_{\tau = 1}^{\hat{N}-1} (1 - \frac{\tau}{\hat{N}}) |\gamma_{vv}(\tau)| < \frac{1}{\hat{N}} \sum_{\tau=1}^{\hat{N}-1} |\gamma_{vv}(\tau)| =
$$
$$
= \frac{1}{\hat{N}} \sum_{\tau = 1}^{T-1} |\gamma_{vv}(\tau)| + \frac{1}{\hat{N}} \sum_{\tau=T}^{\hat{N}-1} |\gamma_{vv}(\tau)| < \frac{T-1}{\hat{N}} \gamma_{vv}(0) + \frac{\hat{N} - T}{\hat{N}} \epsilon < \frac{\epsilon}{2} + \frac{\epsilon}{2} = \epsilon \text{.}
$$

---

## The sample covariance

Let $v(t)$ be a stationary stochastic process with zero mean.
Under this hypothesis $\gamma_{vv}(\tau) = \tilde{\gamma}_{vv}(\tau) = \mathbb{E}[v(t)v(t-\tau)] = \mathbb{E}[v(t)v(t+\tau)]$. Then, the sample estimator of $\gamma_{vv}(\tau)$ is given by:
$$
\hat{\gamma}_N(\tau) = \frac{1}{N-\tau} \sum_{t=1}^{N-\tau} v(t) v(t+\tau) \text{ for } 0 \leq \tau \leq N-1 \text{.}
$$
Observe that, given $\{ v(1), v(2), \ldots, v(N) \}$, then:
- $\hat{\gamma}_N(0)$ is constructed based on a sum of $N$ elements;
- $\hat{\gamma}_N(1)$ is constructed based on a sum of $N-1$ elements;
- $\ldots$ ;
- $\hat{\gamma}_N(N-1)$ is constructed based on just 1 element.
Hence, the accuracy of $\hat{\gamma}_N(\tau)$ decreases with $\tau$ (the approximation is good only for $\tau \ll N$).
Furthermore, we can estimate $\gamma(\tau)$ up to lag $N-1$.
Let's check the **correctness** of $\hat{\gamma}_N(\tau)$:
$$
\mathbb{E}[\hat{\gamma}_N] = \mathbb{E}[\frac{1}{N-\tau} \sum_{t=1}^{N-\tau} v(t)v(t+\tau)] = \frac{1}{N-\tau} \sum_{t=1}^{N-\tau} \mathbb{E}[v(t)v(t+\tau)] =
$$
$$
= \frac{1}{N-\tau} \gamma_{vv}(\tau) (N-\tau) = \gamma_{vv}(\tau) \text{.}
$$
It can be shown that $\hat{\gamma}_N(\tau)$ is also **consistent provided that $\gamma(\tau) \rightarrow 0$** for $\tau \rightarrow \infty$, which holds for stationary ARMA processes.
Notice that we can extend the estimation formula to negative lags, recalling that $\gamma(\tau)$ is an odd function ($\gamma(-\tau) = \gamma(\tau)$):
$$
\hat{\gamma}_N(\tau) = \frac{1}{N - |\tau|} \sum_{t=1}^{N - |\tau|} v(t)v(t + |\tau|) \text{ for } |\tau| \leq N-1 \text{.}
$$
An **alternative covariance estimator** is given by:
$$
\hat{\gamma}_N'(\tau) = \frac{1}{N} \sum_{t=1}^{N-|\tau|} v(t)v(t+|\tau|) \text{ for } |\tau| \leq N-1 \text{.}
$$
The estimator **is NOT correct** for finite $N$, as:
$$
\mathbb{E}[\hat{\gamma}_N'(\tau)] = \frac{N-|\tau|}{N} \gamma_{vv}(\tau) \text{,}
$$
but is still **asymptotically correct**.

---

Indeed, it holds that:
$$
\frac{N-|\tau|}{N} \gamma_{vv}(\tau) \rightarrow \gamma_{vv}(\tau) \text{ as } N \rightarrow + \infty \text{.}
$$
Moreover if $\tau \ll N$ and $N$ is big enough, then $\hat{\gamma}_N'(\tau) \approx \hat{\gamma}_N(\tau)$.
As for $\hat{\gamma}_N(\tau)$, also $\hat{\gamma}_N'(\tau)$ is consistent provided that $\gamma(\tau) \rightarrow 0$ as $\tau \rightarrow \infty$.
Of the two sample estimators, $\hat{\gamma}_N'(\tau)$ has smaller variance.
Furthermore only $\hat{\gamma}_N'(\tau)$ satisfies the positive semi-definiteness property of the covariance function.
Indeed:
$$
\begin{bmatrix}
\hat{\gamma}_N'(0) & \hat{\gamma}_N'(1) & \hat{\gamma}_N'(2) & \cdots & \hat{\gamma}_N'(N-1) \\
\hat{\gamma}_N'(1) & \hat{\gamma}_N'(0) & \hat{\gamma}_N'(1) & \cdots & \hat{\gamma}_N'(N-1) \\
\hat{\gamma}_N'(2) & \hat{\gamma}_N'(1) & \hat{\gamma}_N'(0) & \cdots & \hat{\gamma}_N'(N-3) \\
\vdots & \vdots & & \ddots & \vdots \\
\hat{\gamma}_N'(N-1) & \hat{\gamma}_N'(N-2) & \hat{\gamma}_N'(N-3) & \cdots & \hat{\gamma}_N'(0)
\end{bmatrix} = \frac{1}{N} T T^T \succcurlyeq 0
$$
where
$$
T = \begin{bmatrix}
0 & \cdots & 0 & 0 & x(1) & x(2) & \cdots & x(N) \\
0 & \cdots & 0 & x(1) & x(2) & \cdots & x(N) & 0 \\
\vdots & \kern3mu\raise1mu{.}\kern3mu\raise6mu{.}\kern3mu\raise12mu{.} & \kern3mu\raise1mu{.}\kern3mu\raise6mu{.}\kern3mu\raise12mu{.} & \kern3mu\raise1mu{.}\kern3mu\raise6mu{.}\kern3mu\raise12mu{.} & \kern3mu\raise1mu{.}\kern3mu\raise6mu{.}\kern3mu\raise12mu{.} & \kern3mu\raise1mu{.}\kern3mu\raise6mu{.}\kern3mu\raise12mu{.} & \kern3mu\raise1mu{.}\kern3mu\raise6mu{.}\kern3mu\raise12mu{.} & \vdots \\
0 & x(1) & x(2) & \cdots & x(N) & 0 & \cdots & 0
\end{bmatrix} \in \mathbb{R}^{N \times 2N} \text{ and } x(i) = v(i) - \hat{\mu}_N \text{.}
$$
Let's **prove this**: the element of $T$ at row $i \in \{ 1, \ldots, N \}$, and column $j \in \{ 1, \ldots, 2N \}$ is:
$$
\left[T\right]_{ij} = \begin{cases}
0 \text{ if } j \leq N+1-i \\
x(j-N-1+i) \text{ if } j > N+1-i \text{ and } j < 2N+2-i \\
0 \text{ if } j \geq 2N + 2 - i
\end{cases} \text{.}
$$
Then, the element of $TT^T$ at row $k$ and column $l$ is:
$$
\left[TT^T\right]_{kl} = \sum_{j=1}^{2N} T_{kj} T_{lj} = \sum_{j=\max(N+2-k, N+2-l)}^{\min(2N+1-k, 2N+1-l)} x(j-N-1+k)x(j-N-1+l) =
$$
$$
= \sum_{j = N+2-\min(k,l)}^{2N+1-\max(k,l)} x(j-N-1+k)x(j-N-1+l) \text{.}
$$
Clearly, since $TT^T$ is symmetric
$$
\left[ TT^T \right]_{kl} = \left[ TT^T \right]_{lk} \text{,}
$$
then, WLOG, we can assume that $k \geq l$.

---

Hence:
$$
\left[ TT^T \right]_{kl} = \sum_{j = N+2-l}^{2N+1-k} x(j-N-1+k)x(j-N-1+l) =
$$
$$
= \sum_{j=1}^{N-k+l} x(j+k-l)x(j) = N \hat{\gamma}_N'(k-l) \text{.}
$$

---

## Sample estimator of the spectrum

We want to estimate the spectrum $\Gamma(\omega)$ of a stationary process based on a set of samples $\{ v(1), v(2), \ldots, v(N) \}$.
Let's assume that the process has zero mean (_otherwise, we need to estimate the mean first through $\hat{\gamma}_N$, and then remove the bias_), which implies that $\tilde{\gamma}(\tau) = \gamma(\tau)$.
By definition, the spectrum is a sum of infinite terms:
$$
\Gamma(\omega) = \sum_{\tau = - \infty}^{+ \infty} \gamma(\tau) e^{-j \omega t} \text{.}
$$
In practice, we can estimate it using only a finite number of terms:
$$
\hat{\Gamma}_N(\omega) = \sum_{\tau = -(N-1)}^{N-1} \hat{\gamma}_N(\tau) e^{-j \omega \tau} \text{.}
$$
Notice that there are two sources of approximation in this definition:
- the sample estimator $\hat{\gamma}_N(\tau)$ is used instead of $\gamma(\tau)$;
- the sum is limited to the $\pm (N-1)$ terms. 

### The (extended) periodogram

We can also use the alternative covariance estimator $\hat{\gamma}_N'(\tau)$:
$$
\hat{\Gamma}_N'(\omega) = \sum_{\tau = -(N-1)}^{N-1} \hat{\gamma}_N'(\tau) e^{-j \omega \tau} \text{.}
$$

For this estimator, it holds that:
- $\hat{\Gamma}_N'(\omega) \geq 0$, $\forall \omega$ (the same does not hold for $\hat{\Gamma}_N'(\omega)$).
- $\hat{\Gamma}_N'(\omega) = \frac{1}{N} |\sum_{t=1}^N v(t) e^{-j \omega t}|^2$, i.e. it can be computed as the absolute value of the DFT (discrete Fourier transform) of the data sequence $\{ v(1), v(2), \ldots, v(N) \}$ (without having to resort to any of the two covariance estimators).

> **Proof**: we will use the identity shown in the proof of property 11 in "Stochastic processes".
$$
\hat{\Gamma}_N'(\omega) = \sum_{\tau = -(N-1)}^{N-1} \hat{\gamma}_N'(\tau) e^{-j \omega \tau} = \sum_{\tau = -(N-1)}^{N-1} \frac{1}{N} \sum_{t = 1}^{N - |\tau|} v(t) v(t + |\tau|) e^{-j \omega \tau} =
$$

$$
= \frac{1}{N}\left[\sum_{t=1}^N v(t)v(t+0)e^{-j\omega0} + \sum_{\tau = 1}^{N-1} \sum_{t=1}^{N-\tau} v(t)v(t+\tau)e^{-j \omega \tau} + \sum_{\tau = -(N-1)}^{-1} \sum_{t=1}^{N+\tau} v(t)v(t-\tau)e^{-j \omega \tau} \right] =
$$

---

$$
= \frac{1}{N}\left[\sum_{t=1}^N v(t)v(t+0)e^{-j\omega0} + \sum_{\tau = 1}^{N-1} \sum_{t=1}^{N-\tau} v(t)v(t+\tau)e^{-j \omega \tau} + \sum_{\tau = 1}^{N-1} \sum_{t=1}^{N-\tau} v(t+\tau)v(t)e^{j \omega \tau} \right] =
$$

$$
\stackrel{a_{ik} = v(i)v(k)e^{-j\omega (k-j)}}{=} \frac{1}{N} \sum_{t=1}^N \sum_{s=1}^N v(t)v(s)e^{-j \omega (s-t)} = \frac{1}{N}\left( \sum_{t=1}^N v(t)e^{j \omega t} \right)\left( \sum_{s=1}^N v(s)e^{-j \omega s} \right) =
$$

$$
= \frac{1}{N}\left( \sum_{t=1}^N v(t)e^{-j \omega t} \right)^* \left( \sum_{s=1}^N v(s)e^{-j \omega s} \right) = \frac{1}{N} \left| \sum_{t=1}^N v(t) e^{-j \omega t} \right|^2 \text{.}
$$

- $\mathbb{E}[\hat{\Gamma}_N'(\omega)] \rightarrow \Gamma(\omega)$ as $N \rightarrow + \infty$ (it is an **asymptotically correct estimator**);
- $\mathbb{E}[(\hat{\Gamma}_N'(\omega) - \Gamma(\omega))^2] \rightarrow \Gamma^2(\omega)$ as $N \rightarrow + \infty$ (it is **NOT a consistent estimator**);
- $\mathbb{E}[(\hat{\Gamma}_N'(\omega_1) - \Gamma(\omega_1))(\hat{\Gamma}_N'(\omega_2) - \Gamma(\omega_2))] \rightarrow 0$, for $\omega_1 \neq \omega_2$ (two **points** of the periodogram are **uncorrelated regardless of how close the respective frequencies are**).

From these last two properties, it follows that the spectral estimate can fluctuate significantly around $\Gamma(\omega)$, ultimately resulting in very irregular functions.