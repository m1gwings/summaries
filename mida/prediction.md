---
marp: true
theme: summary
math: mathjax
---
# Prediction

<div class="author">

Cristiano Migali

</div>

Consider a process with rational spectrum:
$$
v(t) = W(z) \eta(t) = \frac{C(z)}{A(z)} \eta(t), \eta(\cdot) \sim WN(0, \lambda^2).
$$
**Prediction** addresses the problem of **estimating the future** value $v(t+r)$ (with $r > 0$) from the observation of the past of the process up to time $t$: $v(t)$, $v(t-1)$, $\ldots$ (<u>assuming that we know the system</u>, that is, we know $W(z)$).

- We will denote such **estimate** as $\hat{v}(t+r|t)$.

- We will call $r$ the **prediction horizon**.

In general, the predictor will have the following structure:
$$
\hat{v}(t+r|t) = f(v(t), v(t-1), \ldots).
$$

Our **objective** is to find the **_optimal_ predictor**, that perfectly blends the information coming from the model (data generation mechanism), and that associated with the available past observations.

- We define the **prediction error** (or **residual**):
$$
\varepsilon(t+r) = v(t+r) - \hat{v}(t+r|t).
$$

Notice that the **prediction error is** itself a **stochastic process**, as $\hat{v}(\cdot)$ depends on random variables.

- The optimal predictor is the one that **minimizes** the **mean square prediction error** (**MSPE**), i.e. the variance of the residual:
$$
\mathbb{E}[\varepsilon^2(t)] .
$$

Before dealing with actual optimal predictors, we need to (_it will be clear later why it is so_) build **fake predictors** which assume that we know the realization of the white noise up to time $t$: $\eta(t), \eta(t-1), \ldots$, to make predictions. This assumption is of course not satisfied in practice, since we can measure the values of $v$, but not the ones of $\eta$.

Remember that we can always expand $W(z)$ in negative powers of $z$ (_take a look at long division in "Discrete time signals and systems", property 7_):
$$
W(z) = w_0 + w_1 z^{-1} + w_2 z^{-2} + \ldots .
$$
Hence:
$$
v(t) = w_0 \eta(t) + w_1 \eta(t-1) + w_2 \eta(t-2) + \ldots .
$$

---

The last expression allows us to write:
$$
v(t+r) = \alpha(t) + \beta(t)
$$
with:
$$
\alpha(t) = w_0 \eta(t+r) + w_1 \eta(t+r-1) + \ldots + w_{r-1} \eta(t+1),
$$
$$
\beta(t) = w_r \eta(t) + w_{r+1} \eta(t-1) + \ldots .
$$

Now, $\alpha(t)$, and $\beta(t)$ are **uncorrelated random variables** (they are linear combinations of the same white noise process over non-overlapping time ranges).
- $\beta(t)$ can be computed once the past of $\eta(\cdot)$ (up to $t$) is known.
- $\alpha(t)$ depends on the _future_ of $\eta(\cdot)$ (from $t+1$ to $t+r$).
Therefore, $\alpha(t)$ is uncorrelated from the past up to time $t$. In other words, $\alpha(t)$ is unpredictable from the past, and we can only estimate its mean value, which is zero (_remember that $\eta \sim WN(0, \lambda^2)$_):
$$
\mathbb{E}[\alpha(t)] = w_0 \mathbb{E}[\eta(t+r)] + w_1 \mathbb{E}[\eta(t+r-1)] + \ldots + w_{r-1} \mathbb{E}[\eta(t+1)] = 0.
$$

Hence the **optimal fake predictor** is:
$$
\hat{v}(t+r|t) = \beta(t) = w_r \eta(t) + w_{r-1} \eta(t-1) + \ldots,
$$
and the **prediction error** equals:
$$
\varepsilon(t+r) = v(t+r) - \hat{v}(t+r|t) = \alpha(t) = w_0 \eta(t+r) + w_1 \eta(t+r-1) + \ldots + w_{r-1}(t+1).
$$

Notice that **$\varepsilon$ i s an MA process** (_see property 10.a,b of "Stochastic processes"_):
- its mean value is: $0$;
- its variance is:
$$
\mathbb[\varepsilon^2(t+r)] = (w_0^2 + w_1^2 + \ldots + w_{r-1}^2) \lambda^2.
$$

Notice that the variance is monotonically increasing with $r$: the prediction "gets worse" (its uncertainty increases) with the prediction horizon.

- For $r = 1$, the variance equals $w_0^2 \lambda^2$; if $w_0 = 1$, which occurs if e.g. $W(z)$ is canonical, then it coincides with the variance of the noise:
$$
\mathbb{V}\text{ar}[\varepsilon(t)] = \mathbb{V}\text{ar}[\eta(t)].
$$
- For $r \rightarrow + \infty$ the variance becomes $(w_0^2 + w_1^2 + \ldots) \lambda^2$, i.e. the variance of the whole process $v(t)$, expressed as a $\text{MA}(\infty)$:
$$
\mathbb{V}\text{ar}[\varepsilon(t)] = \mathbb{V}\text{ar}[v(t)].
$$

Indeed, prediction gets increasingly difficult with $r$, since the variable to be estimated refers to a time point at large distance ahead than the available data.

---

In the long run ($r \rightarrow + \infty$), the information brought by the past data is of no utility, so that the only reasonable estimate is the trivial one, i.e. the mean variable of the variable $\mathbb{E}[v(t+r)] = 0$.

The **optimal predictor** can be expressed in **operatorial notation**:
$$
\hat{v}(t+r|t) = (w_r + w_{r+1}z^{-1} + w_{r+2} z^{-2} + \ldots) \eta(t) = \hat{W}_r(z) \eta(t).
$$

## Computing $\hat{W}_r(z)$

To determine $\hat{W}_r(z)$ observe that the transfer function can be expressed as:
$$
W(z) = w_0 + w_1 z^{-1} + \ldots + w_{r-1} z^{-(r-1)} + w_r z^{-r} + w_{r+1} z^{-(r+1)} + \ldots =
$$
$$
= (w_0 + w_1 z^{-1} + \ldots + w_{r-1} z^{-(r-1)}) + z^{-r} (w_r + w_{r+1} z^{-1} + \ldots) = E(z) + z^{-r} \hat{W}_r(z).
$$
Observe that:
- $E(z)$ is a polynomial of degree $r-1$ in $z^{-1}$;
- $\hat{W}_r(z)$ is a power series in $z^{-1}$.

Hence we can determine $\hat{W}_r(z)$ by operating long division of $C(z)$ by $A(z)$.
In particular, after $r$ steps of long division of $C(z)$ by $A(z)$, we get:
$$
C(z) = E(z) A(z) + z^{-r} F_r(z)
$$
where:
- $E(z)$ is the quotient of the division, and is a polynomial of degree $r-1$;
- $z^{-r} F_r(z)$ is the remainder of the division.
Then:
$$
E(z) + z^{-r} \hat{W}_r(z) = W(z) = \frac{C(z)}{A(z)} = E(z) + z^{-r} \frac{F_r(z)}{A(z)} \text{ iff }
$$
$$
\hat{W}_r(z) = \frac{F_r(z)}{A(z)}.
$$

Observe that, by multiplying one of the equations above by $z^r$, we get:
$$
z^r C(z) = E(z) z^r A(z) + F_r(z) .
$$
Hence we can directly compute $F_r(z)$ as the remainder of the long division between $z^r C(z)$ by $z^r A(z)$.

---

### $\hat{W}_r(z)$ for a $\text{AR}(1)$ process

Consider the $\text{AR}(1)$ process:
$$
v(t) = a v(t-1) + \eta(t), \eta(\cdot) \sim WN(0, \lambda^2).
$$

Let's prove that $E(z) = \sum_{i=0}^{r-1} a^i z^{-i}$, $F_r(z) = a^r$.
Indeed:
$$
E(z) A(z) + z^{-r} F_r(z) = \sum_{i=0}^{r-1} a^i z^{-i} (1 - a z^{-1}) + z^{-r} a^r = \sum_{i=0}^{r-1} a^i z^{-i} - \sum_{i=0}^{r-1} a^{i+1}z^{-(i+1)} + z^{-r} a^r =
$$
$$
= \sum_{i=0}^r a^i z^{-i} - \sum_{i=1}^r a^i z^{-i} = a^0 z^0 = 1 = C(z).
$$

Hence, for a $\text{AR}(1)$ process, the optimal $r$-steps fake predictor is:
$$
\hat{W}_r(z) = \frac{F_r(z)}{A(z)} = \frac{a^r}{1-az^{-1}}.
$$

## From _fake_ to _actual_ predictor

As we have already remarked, the optimal fake predictor depends on **past values of the white noise** process which **are not available**.

Can we find a link between the past of $\eta(\cdot)$ and the past of $v(\cdot)$?

Assume that:
- $(W(z), \eta(t))$ is a **canonical representation** of $v(t)$ (that is, $\hat{W}(z) = W(z), \xi(t) = \eta(t)$);
- furthermore **$W(z)$ has no zeros on the unit circle boundary**.

Then we can **recover $\eta(t)$ using a _whitening filter_** (with transfer function $W^{-1}(z)$):
$$
\eta(t) = \check{W}(z) v(t) = W^{-1}(z) v(t) = \frac{A(z)}{C(z)} v(t).
$$

**Remark**: the whitening filter provides a well-defined representation of $\eta(t)$, since polynomials $A(z)$, and $C(z)$ have the same degree, and therefore $\check{W}(z) = W^{-1}(z)$ can rightfully be interpreted as a transfer function, and, besides, $C(z)$ is a Schur polynomial, which guarantees the stationarity of the process.

**Combining the whitening filter with the optimal fake predictor, we obtain the optimal predictor from the process data**. Its transfer function is calculated as follows:
$$
W_r(z) = \check{W}(z)\hat{W}_r(z) = \frac{A(z)}{C(z)}\frac{F_r(z)}{A(z)} = \frac{F_r(z)}{C(z)}.
$$

---

**Remark**:
$$
\varepsilon(t) = v(t) - \hat{v}(t|t-r) = E(z) \eta(t).
$$

**Proof**: Remember that:
$$
C(z) = E(z) A(z) + z^{-r} F_r(z).
$$
Then:
$$
\varepsilon(t) = v(t) - \hat{v}(t|t-r) = \frac{C(z)}{A(z)} \eta(t) - \frac{F_r(z)}{C(z)} v(t-r) = \frac{C(z)}{A(z)} \eta(t) - \frac{F_r(z)}{A(z)} \check{W}(z) v(t-r) =
$$

$$
= \frac{C(z)}{A(z)}\eta(t) - \frac{z^{-r} F_r(z)}{A(z)} \eta(t) = \frac{C(z) - z^{-r}F_r(z)}{A(z)} \eta(t) = \frac{E(z)A(z)}{A(z)} \eta(t) = E(z) \eta(t) \text{.}
$$

### $W_r(z)$ for a $\text{AR}(1)$ process

We already shown that, for an $\text{AR}(1)$, $F_r(z) = a^r$; furthermore, $C(z) = 1$. Hence, the optimal $r$-steps predictor from data is:
$$
\hat{y}(t|t-r) = \frac{F_r(z)}{C(z)} y(t-r) = a^r y(t-r).
$$

## Predictor initialization

Unless $C(z)$ is trivially $1$, the optimal predictor from data has the form of a _recursive equation_:
$$
\hat{v}(t|t-r) = -c_1 \hat{v}(t-1|t-r-1) - c_2 \hat{v}(t-2|t-r-2) - \ldots \ .
$$
The problem is that we have data only down to a certain instant (e.g. $t_0 = 1$).
We can employ the following solution: **we initialize $\hat{v}$ to $\mathbb{E}[v]$** (the _trivial predictor_), **when data are not available**, Thanks to the asymptotic stability of the filter $W_r(z)$, the effect of the initialization will vanish in the long run (_it will become negligible provided $t$ is large enough_).

## 1-step ahead predictor of ARMA processes

It is possible to derive the expression for the optimal 1-step ahead predictor for a generic ARMA process **without performing long division**.
Indeed, it is easy to see that:
$$
C(z) = 1 \cdot A(z) + (C(z) - A(z)).
$$
It follows that, **assuming that the representation is canonical**:
- $E(z) = 1$;
- $F_1(z) = z (C(z) - A(z))$.

---

Indeed, since $C(z)$ and $A(z)$ are both monic, $C(z) - A(z)$ has no "constant term" (the ones cancel out).

Then, the **optimal fake predictor** is:
$$
\hat{v}(t|t-1) = \frac{F_1(z)}{A(z)} \eta(t-1) = \frac{z(C(z) - A(z))}{A(z)} \eta(t-1) = \frac{C(z) - A(z)}{A(z)} \eta(t).
$$
And so, the **optimal predictor** is:
$$
\hat{v}(t|t-1) = \frac{C(z) - A(z)}{C(z)} \eta(t).
$$

**Remark**: the stability of the predictor only depends on the roots of $C(z)$.

**Important remark**: when we have to do prediction for an ARMA model **with expected value different from $0$** we have to **de-bias the process** first (_see property 18 of "Stochastic processes"_), then we can apply the usual techniques to the unbiased process and, at the end, retrieve a predictor for the biased process by adding the expected value.

## Prediction of an ARMAX process

Consider a generic ARMAX process:
$$
A(z) y(t) = B(z) u(t-k) + C(z) \xi(t).
$$
We want to derive the optimal $k$-steps predictor. We will do it in complete analogy with what we did previously. Through long division we can write:
$$
C(z) = E(z) A(z) + z^{-k} F_k(z)
$$
where $E(z) = e_0 + e_1 z^{-1} + \ldots + e_{k-1} z^{-(k-1)}$.
Let's plug this into the expression of the process:
$$
A(z) y(t) = B(z) u(t-k) + E(z) A(z) \xi(t) + z^{-k} F_k(z) \xi(t) \text{ iff}
$$
$$
y(t) = E(z) \xi(t) + \frac{B(z)}{A(z)} u(t-k) + \frac{F_k(z)}{A(z)} \xi(t-k).
$$
- Since $E(z) \xi(t) = e_0 \xi(t) + e_1 \xi(t-1) + \ldots + e_{k-1} \xi(t-(k-1))$ depends only on "the noise of the future", it is unpredictable.
- $\frac{B(z)}{A(z)}u(t-k)$ and $\frac{F_k(z)}{A(z)} \xi(t-k)$ both depend on information up to time $t-k$, which we have at disposal.

Hence the **optimal $k$-steps fake predictor** is:
$$
\hat{y}(t|t-k) = \frac{B(z)}{A(z)} u(t-k) + \frac{F_k(z)}{A(z)} \xi(t-k).
$$

---

Observe that, for ARMAX processes the expression of the whitening filter is different; by rearranging the expression of the process we get:
$$
\xi(t) = \frac{A(z)}{C(z)} y(t) - \frac{B(z)}{C(z)} u(t-k) = \frac{A(z)}{C(z)} y(t) - \frac{z^{-k} B(z)}{C(z)} u(t).
$$
Then:
$$
\hat{y}(t|t-k) = \frac{B(z)}{A(z)}u(t-k) + \frac{F_k(z)}{C(z)} y(t-k) - \frac{z^{-k} F_k(z) B(z)}{A(z) C(z)} u(t-k) =
$$
$$
= \frac{B(z)}{A(z)} \frac{C(z) - z^{-k} F_k(z)}{C(z)} u(t-k) + \frac{F_k(z)}{C(z)}y(t-k) =
$$
$$
= \frac{B(z)}{A(z)} \frac{E(z) A(z)}{C(z)}u(t-k) + \frac{F_k(z)}{C(z)} y(t-k) = \frac{B(z) E(z)}{C(z)} u(t-k) + \frac{F_k(z)}{C(z)} y(t-k).
$$

In particular, if $k = 1$, we already showed that $E(z) = 1$, $F_1(z) = C(z) - A(z)$.
Then, the expression of the predictor becomes:
$$
\hat{y}(t|t-1) = \frac{B(z)}{C(z)}u(t-1) + \frac{C(z) - A(z)}{C(z)}y(t-1).
$$