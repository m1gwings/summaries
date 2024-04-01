---
marp: true
theme: summary
math: mathjax
---
# Miscellaneous

<div class="author">

Cristiano Migali

</div>

## Pre-filtering

An often adopted pre-computation step in model identification consists in pre-filtering both the input and output data with the _same_ discrete-time filter.
Let:
$$
\mathcal{M}(\theta): y(t) = G(z; \theta) u(t) + H(z; \theta) \eta(t)
$$
and assume that the data are filtered:
- $y^F(t) = F(z) y(t)$;
- $u^F(t) = F(z) u(t)$.

Observe that, fixed $\theta$, the expression of the (1-step) residual is:
$$
\varepsilon(t; \theta) = H^{-1}(z; \theta) \left[ y(t) - G(z; \theta) u(t) \right].
$$
Then, if we plug the filtered data instead of the original one, we get:
$$
\varepsilon^F(t; \theta) = H^{-1}(z; \theta)[y^F(t) - G(z; \theta) u^F(t)] = F(z) H^{-1}(z; \theta)[y(t) - G(z; \theta) u(t)] = F(z) \varepsilon(t; \theta).
$$
Remember that the variance of the residual can be computed from the spectrum:
$$
\mathbb{V}\text{ar}[\varepsilon(t; \theta)] = \int_{-\pi}^\pi \Gamma_{\varepsilon \varepsilon}(\omega; \theta) d\omega
$$
and coincides with the quantity that we want to minimize (by picking the right $\theta$) in the identification process.
Hence, for the pre-filtered data we are minimizing:
$$
\mathbb{V}\text{ar}[\varepsilon^F(t; \theta)] = \int_{-\pi}^\pi \Gamma_{\varepsilon^F\varepsilon^F}(\omega; \theta) d\omega = \int_{-\pi}^\pi |F(e^{j\omega})|^2 \Gamma_{\varepsilon \varepsilon}(\omega; \theta) d\omega.
$$
The frequency response $F(e^{j\omega})$ acts as a weight in the cost function and can be used to emphasize certain frequency bands, where we want the model to be more accurate.
Heep in mind that the system is always more complex than the model, so that a global approximation is not generally possible.

## Deterministic or stochastic models for non-stationarities

We can deal with systems which display a trend in the data in two different ways:
- We can fit a deterministic model, _e.g._ a polynomial trend, to the data:
$$
y^*(t) = \alpha_0 + \alpha_1 t + \ldots + \alpha_r t^r;
$$

---

$$
u^*(t) = \beta_0 + \beta_1 t + \ldots + \beta_s t^s
$$
> by linear regression. Notice that if $r=0$ and $s=0$ we are fitting a constant to the data which coincides with the arithmetic, while for $r>0$ or $s>0$ we can also model some drift. Then, we can compute the _de-trended_ data as follows:
$$
\tilde{y}(t) = y(t) - y^*(t), \tilde{u}(t) = u(t) - u^*(t).
$$
> Finally, we can apply an identification method to the data $\{ \tilde{u}(t), \tilde{y}(t) \}$.
Alternatively, we can include a specific term (_e.g._ a polynomial trend) in the model, and estimate the mean or trend together with the other parameters:
$$
y(t) = G(z; \theta) u(t) + H(z; \theta) \eta(t) + m(\theta).
$$

- We can use an ARIMA(X) model, or equivalently process the differenced data $\Delta u(\cdot)$ and $\Delta y(\cdot)$ with an ARMA(X) process.

## Presence of outliers in the data

It is often the case that the data contain isolated samples (or, which is worse, entire subsequences) with out-of-norm values, aka _outliers_. This can happen _e.g._ due to an occasional malfunctioning of a sensor. Outliers can greatly affect the estimation accuracy, as they are typically responsible for very large errors, which greatly impact the cost function.
Consider an ARMAX model:
$$
A(z) y(t) = z^{-k} B(z) u(t) + C(z) \eta(t)
$$
and assume that the measurement of $y(\cdot)$ is affected by noise:
$$
z(t) = y(t) + v(t)
$$
where $v(\cdot)$ is a particular white noise characterized as follows:
- $v(t)$ and $v(s)$ are independent if $t \neq s$;
- $v(t) = 0$ with high probability;
- $\mathbb{E}[v(t)] = 0$, $\mathbb{V}\text{ar}[v(t)] = \sigma^2 < +\infty$.

Then, the model can be reformulated as follows:
$$
A(z) z(t) = z^{-k} B(z) u(t) + C(z) \eta(t) + A(z) v(t).
$$
The two disturbance terms can be reduced to one by spectral factorization:
$$
A(z) z(t) = z^{-k} B(z) u(t) + \tilde{C}(z) w(t)
$$
where $\tilde{C}(z)$ and $v(t)$ are such that:
$$
\tilde{C}(z)\tilde{C}(z^{-1}) \lambda_w^2 = C(z) C(z^{-1}) \lambda^2 + A(z) A(z^{-1}) \sigma^2.
$$

---

If one should try to fit an ARMAX model on the data with outliers, the estimates of the noise model will tend to $\tilde{C}(z)$, as opposed to $C(z)$.
With an ARX model it is even worse, since the presence of outliers cannot be modeled inside the ARX family.

There are various **ways to deal with outliers**:
- First, estimate a model according to the standard procedure. Then, test the residual $\varepsilon(t; \hat{\theta})$ for large values. Where $|\varepsilon(t; \hat{\theta})|$ is too large, change $y(t)$:
$$
y(t) \rightarrow 0.5( y(t-1) + y(t+1) ) \text{, or}
$$
$$
y(t) \rightarrow \hat{y}(t|t-1; \hat{\theta}).
$$
> Finally, re-estimate the model on the "corrected" data.

- Use a cost function that weights less the very large errors:
$$
J(\theta) = \frac{1}{N} \sum_{t=1}^N \frac{\varepsilon^2(t; \theta)}{\alpha^2 + \varepsilon^2(t; \theta)} \text{, or}
$$
$$
J(\theta) = \frac{1}{N} \sum_{t=1}^N l(\varepsilon(t; \theta)) \text{, with } l(\varepsilon) = \begin{cases} \varepsilon^2 \text{ if } \varepsilon^2 \leq \alpha^2 \\ \alpha^2 \text{ if } \varepsilon^2 > \alpha^2 \end{cases}.
$$

- Pre-process the data with a non-linear filter with the following behavior: substitute the $t$-th sample with the average of the data from $t-s$ to $t+s$, having previously removed the largest and smallest values (in $\{ y(t-s), \ldots, y(t+s) \}$).

## Durbin-Levinson's algorithm

Consider a generic $\text{AR}(n)$ model:
$$
v(t) = a_1 v(t-1) + \ldots + a_{n} v(t-n) + \eta(t), \eta(\cdot) \sim WN(0, \lambda^2).
$$
In the LS estimation, we need to compute the inverse of the $n \times n$ matrix $\sum_{t=1}^N \phi(t) \phi^T(t)$, which is an increasingly demanding calculation, as $n$ grows.
Especially if we need to estimate models with different orders, for structure selection purposes, this approach is computationally taxing.
The **Durbin-Levinson's algorithm** allows to estimate the parameters of an $\text{AR}(n)$ model iteratively, starting from those of the $\text{AR}(n-1)$ model, requiring only the inversion of a _scalar_ quantity.
Therefore, it is particularly convenient for model structure selection purposes.
The Durbin-Levinson's algorithm is based on the Yule-Walker equations.
Indeed we can use such equations in two different ways:
- given the model parameters one can calculate the function $\gamma(\cdot)$;
- given $\gamma(\cdot)$ one can determine the parameters $a_1$ and $\lambda^2$.

---

Durbin-Levinson's algorithm exploits the latter usage.
Consider the models:
- $\text{AR}(n)$ with coefficients $a_i^{(n)}$ for $i \in \{ 1, \ldots, n \}$, and corresponding noise variance $\lambda_(n)^2$.
- $\text{AR}(n+1)$ with coefficients $a_i^{(n+1)}$ for $i \in \{ 1, \ldots, n+1 \}$, and corresponding noise variance $\lambda_{(n+1)}^2$.

Then one can compute the parameters of the $\text{AR}(n+1)$ model from those of the $\text{AR}(n)$ model as follows:
$$
a_{n+1}^{(n+1)} = \frac{1}{\lambda_{(n)}^2} \left[ \gamma(n+1) - \sum_{i=1}^n a_i^{(n)} \gamma(n+1-i) \right];
$$
$$
a_i^{(n+1)} = a_i^{(n)} - a_{n+1}^{(n+1)} a_{n+1-i}^{(n)} \text{ for } i \in \{ 1, \ldots, n \};
$$
$$
\lambda^2_{(n+1)} = \left[ 1- \left( a_{n+1}^{(n+1)} \right)^2 \right] \lambda_{(n)}^2.
$$

We can initialize the algorithm with:
$$
a_1^{(1)} = \frac{\gamma(1)}{\gamma(0)} \text{ and } \lambda_{(1)}^2 = \gamma(0) - a_1^{(1)} \gamma(1).
$$

**Observe that**:
- For $N \rightarrow + \infty$ (NOT $n$) the parameters estimates provided by Durbin-Levinson's algorithm are the SAME as the one provided by LS.
- Notice that in an asymptotically stable auto-regressive model, the last parameter has an absolute value smaller than 1 (_it is the product of the poles of the system; it follows from polynomial factorization remembering that $A(z)$ is monic_), which guarantees the non-negativity of the noise variance according to the expression for $\lambda_{(n+1)}^2$. It also follows from the same expression that $\lambda_{(n+1)}^2 \leq \lambda_{(n)}^2$.

## The PARCOR function

Suppose we are estimating a stationary process with auto-regressive models of increasing order using the Durbin-Levinson's algorithm.

The function:
$$
\text{PARCOR}(\tau) = a_\tau^{(\tau)} \text{, for} \tau \in \{ 1, 2, \ldots \}
$$
is called **partial correlation function** (or **pcf**).
Assuming that the auto-regressive models are asymptotically stable (which should follow from the stationarity of the process), then it holds that $|\text{PARCOR}(\tau)| < 1$ (_we already observed this_).

---

If the process is an $\text{AR}(n)$ then $\text{PARCOR}(\tau) = 0$ for $\tau > n$ (assuming that $N$ is big enough to have a robust estimate).
Hence the pcf plays a role analogous to the auto-correlation function for MA processes.
