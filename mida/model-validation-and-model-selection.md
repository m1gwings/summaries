---
marp: true

theme: summary
math: mathjax
---
# Model validation and model selection

<div class="author">

Cristiano Migali

</div>

## Model validation

The identification procedure selects the "best" model belonging to a certain model family. However we need to ascertain if this model is sufficiently good.
In particular we say that a model is _good_ if it allows to solve satisfactorily the problem that motivated its construction.
To validate a model, we can operate in 2 directions:
- we can analyze the **model behavior** with **diagrams** and **simulation**;
- we can perform a **statistical test** on the residuals.

### Model analysis

Two possible ways to analyze the model behavior are the following.

- We can draw its Bode diagrams, possibly with confidence intervals, and we can use them to understand if the essential characteristics of the system dynamics have been captured.

- We can study the model's behavior in simulation:
$$
y_m(t) = G(z; \hat{\theta}) u(t).
$$
> In simulation, the output is made dependent on past values of the output model itself ($y_m(\cdot)$), as opposed to the output measurements ($y(\cdot)$).
If the model is any good, $y_m(\cdot)$ and $y(\cdot)$ should be close (although we cannot expect the two signals to be exactly equal, due to the effect of noise).

### Statistical tests on the residual

If the estimated model perfectly describes the data generation mechanism, the prediction error (residual) must be white and uncorrelated with the input signal.
A white noise is characterized by a null covariance function for all values of $\tau \neq 0$.
The **Anderson test** exploits this property by analyzing the sample covariance function obtained from data. Let $\varepsilon(\cdot)$ be the signal to be tested (assumed to be zero mean), and compute:
$$
\hat{\gamma}_N'(\tau) = \frac{1}{N} \sum_{t=1}^{N-\tau} \varepsilon(t)\varepsilon(t+\tau).
$$

---

Let:
$$
\hat{\rho}(\tau) = \frac{\hat{\gamma}_N'(\tau)}{\hat{\gamma}_N'(0)}
$$
be the corresponding _normalized sample covariance function_.
If $\varepsilon(\cdot)$ is white, then for $\tau > 0$, $\hat{\rho}(\tau)$ has a probability distribution that (for large $N$) tends to a gaussian with zero mean and variance $\frac{1}{N}$:
$$
\sqrt{N} \hat{\rho}(\tau) \sim \text{As}G(0, 1) \text{ if } \tau > 0.
$$
The Anderson test operates as follows.
Let the null hypothesis $\mathcal{H}_0$ be that the residual is white.
1. Fix the probability (confidence level $\alpha$) that $\mathcal{H}_0$ is rejected while true.
2. With reference to the standard gaussian with zero mean and unit variance ($G(0, 1)$), find the value $\beta$ for which the tails of the distribution outside the interval $(-\beta, \beta)$ cover an area equal to $\alpha$:
$$
\beta \text{ s.t. } \int_{-\beta}^\beta \frac{1}{\sqrt{2\pi}} e^{-\frac{y^2}{2}} dy = 1 - \alpha.
$$
3. Count the points of $\hat{\rho}(\tau)$ falling outside the interval $\left(-\frac{\beta}{\sqrt{N}}, \frac{\beta}{\sqrt{N}}\right)$.
4. If the fraction of points is more than $\alpha$, $\mathcal{H}_0$ is rejected.

In particular, let $n$ be the number of computed points of $\hat{\rho}(\tau)$ $(\tau \in \{ 1, \ldots, n \})$, and $n_{\text{out}}$ the number f points external to the interval $\left( -\frac{\beta}{\sqrt{N}}, \frac{\beta}{\sqrt{N}} \right)$.
If $\frac{n_{\text{out}}}{n} > \alpha$, then $\mathcal{H}_0$ is rejected (with probability $\alpha$ that it is instead true).

**Important**: a statistical test is relevant only when we reject $\mathcal{H}_0$ (_this is by construction, since we bound the probability of rejecting $\mathcal{H}_0$ when it is actually true; the probability that we accept $\mathcal{H}_0$ while this is false has no constraint_). Hence using Anderson test to determine that a residual is actually white is wizardry. We can only use it to determine that our model is bad.

#### Cross-correlation test

If the model is correct, then the residual and the input should be independent.
Consider the cross-correlation between these two signals:
$$
\gamma_{\varepsilon u}(\tau) = \mathbb{E}\left[ \varepsilon(t+\tau) u(t) \right].
$$
If the model does not accurately represent the system, then $\gamma_{\varepsilon u}(\tau)$ will be significantly different from $0$ for $\tau \geq 0$. For $\tau < 0$, instead, $\gamma_{\varepsilon u}(\tau)$ can be null or not depending on the autocorrelation of $u(t)$ (since $\varepsilon(t-k)$ is correlated with $u(t-k)$, if $u(t)$ is correlated with $u(t-k)$, then $\gamma_{\varepsilon u}(-k)$ can be different from 0).

---

The sample cross-correlation is given by:
$$
\hat{\gamma}_{\varepsilon u}(\tau)' = \frac{1}{N} \sum_{t = 1}^{N-\tau} \varepsilon(t+\tau) u(t).
$$
Now, let
$$
\hat{\rho}_{\varepsilon u}(\tau) = \frac{\hat{\gamma}_{\varepsilon u}(\tau)}{\sqrt{\hat{\gamma}_\varepsilon(0) \hat{\gamma}_u(0)}}
$$
be the normalized cross-correlation function.
For $N \rightarrow +\infty$, the quantity tends to have a gaussian probability distribution:
$$
\sqrt{N} \hat{\rho}_{\varepsilon u}(\tau) \sim \text{As}G(0, 1).
$$
Then, we can set up a statistical test similar to the Anderson's test.

## Model selection

In the PEM identification process, we first have to pick a model family, and then we identify the best model in that category, _i.e._ the one that minimizes the cost function (the mean square prediction error).
In other words, $J_N(\hat{\theta})$ is an indicator of the adherence of the estimated model to the data.
However, the initial choice regarding the model family is somewhat arbitrary. What if we increase the model complexity? Since this increases the degrees of freedom over which we can optimize $J_N(\theta)$, we can only expect to get an even better $J_N(\hat{\theta})$.
Is this a sufficient indication that the more complex model is the best one? The answer is NO: $J_N(\hat{\theta})$ does not represent a reliable indicator of the adherence of the estimated model <u>to the underlying system</u>. This follows from the fact that it is calculated on the same data used for identification.

### Cross-validation

To have an _objective_ evaluation, we can use different data (w.r.t. those used for identification) to estimate the adherence of the model to the system. This approach is known as **cross-validation**. Data is split into two parts: the _identification_ (or _training_) _set_, and the _validation set_. The training set is used to estimate the model parameters, but the model quality is evaluated on the validation set, this indication being used for model structure selection.

The **drawback** of this approach is that not all data are used to estimate the model. While $J_N(\hat{\theta})$ evaluated on the identification data is a decreasing function of the model complexity, the same index evaluated on the validation data is not.
Indeed, a too-complex model will fit so well the identification data to generate _overfitting_: the excess degrees of freedom of the model are used to fit the noise in the data!

---

On the other hand, the adherence of the same model to the validation data will be worse compared to a more parsimonious one.

### FPE (Final Prediction Error) criterion

More often than not data are not so abundant that we can spare some of them for cross-validation purposes. Does there exist a way to objectively evaluate the model quality using only the identification data?
Remember that data are realizations of stochastic processes:
$$
y(t) = y(t; s), \hat{y}(t) = \hat{y}(t; s, \theta).
$$
To obtain an _objective_ index of model accuracy, one must get rid of the particular sequence of data at hand and accounting for _all realizations_. This leads to consider the averaged index:
$$
\overline{J}(\theta) = \mathbb{E}\left[ (y(t; s) - \hat{y}(t; s, \theta))^2 \right].
$$
The averaging provided by the expectation operator $\mathbb{E}\left[ \cdot \right]$ enables to see $\overline{J}(\theta)$ as the accuracy of model $\mathcal{M}(\theta)$ over _all possible sequences of data_.
Now, we cannot forget that the estimate $\hat{\theta}_N$ depends on data too:
$$
\hat{\theta}_N = \hat{\theta}_N(s).
$$
By evaluating $\overline{J}$ at $\hat{\theta}_N$, we obtain the quantity $\overline{J}(\hat{\theta}_N(s))$, which represents the accuracy of model $\mathcal{M}(\hat{\theta}_N(s))$ over all possible sequences of data. On the other side, the model associated with parameter vector $\hat{\theta}_N(s)$ is just one of the possible models that can be estimated. To achieve a fully _objective_ index of accuracy, one can consider the average $\mathbb{E}[\overline{J}(\hat{\theta}_N(s))]$ over all possible $s$. The so-obtained quantity is denoted by the acronym **FPE** (**Final Prediction Error**):
$$
FPE = \mathbb{E}[\overline{J}(\hat{\theta}_N(s))].
$$
FPE represents the average accuracy of all possible estimates associated with all possible sequences of data. By minimizing the FPE, we obtain the optimal complexity.


#### FPE expression for $\text{AR}(n)$ systems

Assume that $\mathcal{S} = \mathcal{M}(\theta) = \text{AR}(n)$ (_this is a very ideal scenario_).
We know that:
$$
\mathcal{S}: y(t) = \phi^T(t) \theta^\circ + e(t) \text{, with } e(\cdot) \sim WN(0, \lambda^2),
$$
and:
$$
\hat{\mathcal{M}}(\theta): \hat{y}(t) = \phi^T(t) \theta = \phi^T(t; s) \theta.
$$

---

Then:
$$
\overline{J}(\theta) = \mathbb{E}[(y(t; s) - \hat{y}(t; s, \theta))^2] = \mathbb{E}[(\phi^T(t; s)(\theta^\circ - \theta) + e(t))^2] =
$$

$$
= (\theta^\circ - \theta)^T \mathbb{E}[\phi(t; s) \phi^T(t; s)] (\theta^\circ - \theta) + \lambda^2 = (\theta^\circ - \theta)^T \overline{R} (\theta^\circ - \theta) + \lambda^2
$$
(_where we used the fact that $e(t)$ and $\phi(t; s)$ are independent as already observed many times_).
Therefore:
$$
FPE = \mathbb{E}[(\theta^\circ - \hat{\theta}_N(s))^T \overline{R} (\theta^\circ - \hat{\theta}_N(s))] + \lambda^2.
$$
Remember that in _"Identification", p. 15_ we stated that:
$$
\mathbb{V}\text{ar}\left[ \theta^\circ - \hat{\theta}_N(s) \right] = \frac{\lambda^2}{N} \overline{R}^{-1},
$$
hence:
$$
\overline{R} = \frac{\lambda^2}{N}\left( \mathbb{V}\text{ar}\left[ \theta^\circ - \hat{\theta}_N(s) \right] \right)^{-1}.
$$
If we plug it into the FPE expression, we get:
$$
FPE = \mathbb{E}\left[(\theta^\circ - \hat{\theta}_N(s))^T \left( \mathbb{V}\text{ar}\left[ \theta^\circ - \hat{\theta}_N(s) \right] \right)^{-1} (\theta^\circ - \hat{\theta}_N(s))\right] \frac{\lambda^2}{N} + \lambda^2.
$$

Now, for a random vector $v$ of length $n$ with <u>null expected value</u> it holds that:
$$
\mathbb{E}[v^T \mathbb{V}\text{ar}[v]^{-1} v] = n.
$$
Indeed, $v^T \mathbb{V}\text{ar}[v]^{-1} v$ is a scalar, and a scalar equals its trace:
$$
v^T \mathbb{V}\text{ar}[v]^{-1}v = \text{tr}(v^T \mathbb{V}\text{ar}[v]^{-1} v) = \text{tr}(v v^T \mathbb{V}\text{ar}[v]^{-1}).
$$
Furthermore, both the trace and the expected value are linear operators, hence we can exchange them:
$$
\mathbb{E}[v^T \mathbb{V}\text{ar}[v]^{-1}v] = \text{tr}[\mathbb{E}[v v^T] \mathbb{V}\text{ar}[v]^{-1}] = \text{tr}(I_n) = n.
$$
In conclusion we get:
$$
FPE = \frac{n}{N} \lambda^2 + \lambda^2 = \frac{N+n}{N} \lambda^2.
$$
In the previous formula $\lambda^2$ is not known, but it can be estimated as we already know:
$$
\hat{\lambda}^2 = \frac{N}{N-n} J(\hat{\theta}_N)
$$
(_see ML summaries_).

---

Hence, an estimate of FPE is given by:
$$
\hat{FPE} = \frac{N+n}{N-n} J(\hat{\theta}_N).
$$
The FPE includes 3 elements:
- $J(\hat{\theta}_N)$: the variance of the residual of the estimated model;
- $n$: the model complexity;
- $N$: the number of employed data.

As $n$ increases, $J(\hat{\theta}_N)$ decreases, whereas for $n$ sufficiently large the FPE will tend to increase (indeed $\lim_{n \rightarrow N} \hat{FPE} = \infty$).

### Akaike's information criterion (AIC)

Another criterion for the selection of the optimal model complexity is Akaike's information criterion (AIC), which derives from statistical analysis.
In this case, we minimize the distance between the true probability density of the data and the one that would be generated by a given model. We obtain:
$$
AIC = \ln(J(\hat{\theta}_N)) + 2 \frac{n}{N}.
$$
For large $N$, AIC and FPE yield similar results:
$$
\ln(\hat{FPE}) = \ln(\frac{N+n}{N-n} J(\hat{\theta}_N)) = \ln(1+\frac{n}{N}) - \ln({1-\frac{n}{N}}) + \ln(J(\hat{\theta}_N)) \approx
$$
$$
\frac{n}{N} - (-\frac{n}{N}) + \ln(J(\hat{\theta}_N)) = \ln(J(\hat{\theta}_N)) + 2 \frac{n}{N} = AIC,
$$
_where we used the fact that $\ln(1+x) \approx x$ for small $x$_.

### Rissanen's criterion or Minimum Description Length (MDL)

The **Minimum Description Length** (**MDL**) criterion is based on arguments from code theory. The idea is that the optimal complexity of the model should be such that the complete description of the data by means of the model _and_ the prediction error requires the minimum number of information bits.
Indeed, as complexity increases, the size of the parameter vector grows, and so does the number of bits necessary for its digital encoding.
Conversely, the error amplitude decreases on average, since the fitting improves, so that fewer bits are required for its digital encoding.
The expression for the criterion is:
$$
MDL = \ln(J(\hat{\theta}_N)) + \ln(N)\frac{n}{N}.
$$
It is similar to AIC, but the linear component with $n$ has a higher slope (since $\ln(N) > 2$ unless we use an incredible small dataset).

---

### Asymptotic properties of the criteria

Let $\mathcal{S} \in \mathcal{M}(\theta)$, $N \rightarrow +\infty$, and let $n^\circ$ be the true order model. Do the three criteria allow to estimate correctly the model complexity at least in these ideal conditions?
We have that:
- for large $N$, FPE is in accordance with AIC (as already seen);
- FPE and AIC have a non-zero probability of _over-estimating_ $n^\circ$, and thus of suggesting an over-parameterized model ($P(\hat{n} > n^\circ) \approx 0.3$);
- MDL consistently estimates $n^\circ$ with probability $1$ ($P(\hat{n} = n^\circ) = 1$).

In view of these observations, FPE and AIC are preferred over MDL only for small values of $N$, to avoid the risk of under-parameterization.
