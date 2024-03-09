---
marp: true
theme: summary
math: mathjax
---
# Discrete time signals and systems

<div class="author">

Cristiano Migali

</div>

## Basic definitions

- We call **discrete time signal** a function $x : \mathbb{Z} \rightarrow \mathbb{R}^n$.

- We call **discrete time dynamical system** a system, whose **state**, **input**, and **output**, are represented respectively by the discrete time signals $x : \mathbb{Z} \rightarrow \mathbb{R}^n$, $u : \mathbb{Z} \rightarrow \mathbb{R}$, and $y : \mathbb{Z} \rightarrow \mathbb{R}$, which is governed by the following equations:
$$
\begin{cases}
    x(t+1) = \phi(x(t), u(t), t) \\
    y(t) = \gamma(x(t), u(t), t)
\end{cases} \text{.}
$$
> - $n$ is the **order** of the system.
> - The system is **strictly proper** if $\gamma$ does not depend on $u$.
> - The system is **time-invariant** if $\phi$, and $\gamma$ do not depend on $t$.
> - the system is **linear** if $\phi$, and $\gamma$ are linear functions w.r.t. $x$, and $u$.

- If (in a discrete time time-invariant system) in correspondence to a constant input $u(t) = \overline{u}$, there exists a constant state motion $x(t) = \overline{x}$, then it is called an **equilibrium state** (and the corresponding constant output is an **equilibrium output**).
To **calculate equilibrium states** we need to impose:
$$
\begin{cases}
\overline{x} = \phi(\overline{x}, \overline{u}) \\
\overline{y} = \gamma(\overline{x}, \overline{u})
\end{cases} \text{.}
$$

- A discrete time LTI system is said:
> - (**simply**) **stable** $\iff$ the **free motion is bounded** $\forall x(0)$;
> - **asymptotically stable** $\iff$ the **free motion tends to 0 for $t \rightarrow +\infty$** $\forall x(0)$;
> - **unstable** otherwise (i.e. if $\exists x(0)$ s.t. the free motion diverges for $t \rightarrow +\infty$). 

- We define **$\mathcal{Z}$-transform** for a discrete time real signal $f$ s.t. $f(t) = 0 \forall t < 0$ the function $F : \mathbb{C} \rightarrow \mathbb{C}$:
$$
F(z) = \sum_{t=0}^{+\infty} f(t)z^{-t} \text{.}
$$

- Given a **$\mathcal{Z}$-transform** $F(z)$, we define:
> - **zeroes** the values of $z$ s.t. $F(z) = 0$;
> - **poles** the values of $z$ s.t. $|F(z)| = +\infty$.

---

> If $F(z)$ is rational, then the zeroes are the roots of the numerator, while the poles are the roots of the denumerator.

- For a discrete time LTI system we define **transfer function $G(z)$** the ratio between the $\mathcal{Z}$-transform of the output and the input when the system has zero initial conditions. 

- For a discrete time dynamical system we define **static gain** the ratio of the output to the input at equilibrium: $\mu = \frac{\overline{y}}{\overline{u}}$.

---

## Basic properties

1. We can represent the **equations of a discrete time LTI** (Linear Time-Invariant) system as:
$$
\begin{cases}
x(t+1) = Fx(t) + gu(t) \\
y(t) = h^Tx(t) + lu(t)
\end{cases}
$$
> where $F \in \mathbb{R}^{n \times n}$, $g, h \in \mathbb{R}^n$, $l \in \mathbb{R}$.

2. Suppose that the initial state $x(0)$, and the input $u(t)$ of a discrete time LTI system are known. The system state at time $t$ is:
$$
x(t) = F^t x(0) + \sum_{j=0}^{t-1} F^{t-j-1} g u(j) \text{.}
$$

> **Proof**: by induction:
$$
x(t) = Fx(t-1) + gu(t-1) = F^tx(0) + \sum_{j=0}^{t-2}F^{t-j-2+1}gu(j) + gu(t-1) =
$$
$$
= F^tx(0) + \sum_{j=0}^{t-1}F^{t-j-1}gu(j) \text{.}
$$

> This is known as **Lagrange formulas** in discrete time.
> - $F^tx(0)$ is said **free motion**.
> - $\sum_{j=0}^{t-1}F^{t-j-1}gu(j)$ is said **forced motion**.

3. To calculate the equilibrium states of a discrete time LTI system, one has to solve:
$$
\overline{x} = F \overline{x} + g \overline{u} \text{ iff}
$$
$$
(I-F) \overline{x} = g \overline{u} \text{.}
$$
> If $I-F$ is invertible, we have one unique solution (for every input $\overline{u}$): $\overline{x} = (I-F)^{-1} g \overline{u}$. Then, the corresponding equilibrium output is: $\overline{x} = [h^T(I-F)^{-1} g + l] \overline{u}$.
Otherwise we could have $\infty$ or $0$ solutions.

4. A discrete time LTI system is:
> - **asymptotically stable** $\iff$ $|\lambda_i(F)| < 1$, $\forall i$;
> - $\exists i \mid |\lambda_i(F)| > 1$ $\implies$ **unstable**;
> - if $|\lambda_i(F)| \leq 1$, $\forall i$, and $\exists \hat{i} \mid |\lambda_{\hat{i}}(F)| = 1$, then:
>> - **simply stable** $\iff$ $m_a(\lambda_i(F)) = m_g(\lambda_i(F))$, $\forall i \mid |\lambda_i(F)| = 1$;

---

>> - **unstable** $\iff$ $\exists \hat{i} \mid |\lambda_i(F)| = 1$, and $m_a(\lambda_i(F)) > m_g(\lambda_i(F))$.

5. Let's **compute some $\mathcal{Z}$ transforms**.
> 5.1 Let:
$$
\text{sca}^*(t) = \begin{cases}
0 \text{ if } t < 0 \\
1 \text{ if } t \geq 0
\end{cases} \text{ ;}
$$
> then:
$$
\mathcal{Z}[\text{sca}^*(t)] = \sum_{t=0}^{+\infty} z^{-t} = \frac{1}{1-z^{-1}} = \frac{z}{z-1} \text{,}
$$
> which converges for $|z^{-1}| < 1 \iff |z| > 1$.

> 5.2 Let:
$$
\text{imp}^*(t) = \begin{cases}
1 \text{ if } t = 0 \\
0 \text{ otherwise}
\end{cases} \text{ ;}
$$
> then:
$$
\mathcal{Z}[\text{imp}^*(t)] = z^{-0} = 1 \text{.}
$$

> 5.3
$$
\mathcal{Z}[\lambda^t] = \sum_{t=0}^{+\infty} \lambda^t z^{-t} = \frac{1}{1-\lambda z^{-1}} = \frac{z}{z-\lambda} \text{,}
$$
> which converges for $|\lambda z^{-1}| < 1 \iff |z| > |\lambda|$.

6. Let's state some **properties of the $\mathcal{Z}$-trainsform**.
> - **Linearity**: $\mathcal{Z}[\alpha_1 f_1(t) + \alpha_2 f_2(t)] = \alpha_1 \mathcal{Z}[f_1(t)] + \alpha_2 \mathcal{Z}[f_2(t)]$.

> - **Forward shift**: $\mathcal{Z}[f(t+1)] = z(\mathcal{Z}[f(t)] - f(0))$.

> - **Backward shift**: $\mathcal{Z}[f(t-1)] = z^{-1} \mathcal{Z}[f(t)]$.
> **Proof**:
$$
\mathcal{Z}[f(t-1)] = \sum_{t=0}^{+\infty} f(t-1) z^{-t} = z^{-1} \sum_{t=0}^{+\infty} f(t-1)z^{-(t-1)} = z^{-1}f(-1) + 
$$
$$
+ z^{-1} \sum_{t=1}^{+\infty} f(t-1) z^{-(t-1)} = 0 + z^{-1} \sum_{t=0}^{+\infty} f(t)z^{-t} = z^{-1} \mathcal{Z}[f(t)] \text{.}
$$

---

> - **Initial value theorem**: $f(0) = \lim_{z \rightarrow +\infty} \mathcal{Z}[f(t)]$.

> - **Final value theorem**: if $\lim_{t \rightarrow +\infty}$ f(t) exists, then:
$$
\lim_{t \rightarrow +\infty} f(t) = \lim_{z \rightarrow 1} (z-1)\mathcal{Z}[f(t)] \text{.}
$$

7. If $\mathcal{Z}[f(t)] = \frac{N(z)}{D(z)}$ ($\mathcal{Z}[f(t)]$ is rational) we can retrieve $f$ by long dividing $N(z)$ by $D(z)$.
In particular: let $D(z) = d_n z^n + \cdots + d_1 z + d_0$, $N^{(0)}(z) = N(z)$, $N^{(k)} = n_n^{(k)}z^{n-k} + \cdots + n_1^{(k)} z^{1-k} + n_0^{(k)} z^{-k}$ for every $k$.
Furthermore $Q^{(k)}(z) = \frac{n_n^{(k)}}{d_n}z^{-k}$, and $N^{(k+1)}(z) = N^{(k)}(z) - D(z) Q^{(k)}(z)$ for every $k$. Then:
$$
f(t) = \frac{n_n^{(t)}}{d_n} \text{.}
$$

8. By applying the $\mathcal{Z}$-transform to the equations of a discrete time LTI system we get:
$$
\begin{cases}
z X(z) - zx(0) = FX(z) + g U(z) \\
Y(z) = h^T X(z) + l U(z)
\end{cases} \text{.}
$$
> If $zI - F$ is invertible:
$$
\begin{cases}
X(z) = (zI-F)^{-1}zx(0) + (zI-F)^{-1}gU(z) \\
Y(z) = h^T(zI-F)^{-1}zx(0) + [h^T(zI-F)^{-1}g + l]U(z)
\end{cases} \text{.}
$$
> Then, the transfer function of the system is:
$$
G(z) = \frac{Y(z)_{\vert_{x(0)=0}}}{U(z)} = h^T(zI - F)^{-1}g \text{.}
$$
> If $u(t) = \text{imp}^*(t)$, then $U(z) = 1$, hence $G(z) = Y(z)_{\vert_{x(0) = 0}}$.
Let's list some structural properties of $G(z)$:
> - $G(z) = \frac{N(z)}{D(z)}$ where $N(z)$, and $D(z)$ are polynomials in $z$ (that is, **$G$ is a rational function**);
> - **$D(z)$** coincides with the **characteristic polynomial of $F$**;
> - the degree of polynomial $D(z)$ is equal to the system's order $n$;
> - the degree of polynomial $N(z)$ is smaller or equal to that of $D(z)$ (it is equal _iff_ the system is **not** strictly proper).

9. For a discrete time LTI system, if $I - F$ is invertible (_iff_ $1$ is not a root of the denominator of the transfer function), then:
$$
\mu = G(1) \text{.}
$$

---

> If the transfer function has singularities in $z = 1$, we can also define the generalized gain:
> - if $G(z)$ has $q$ poles in $z=1$ ($I-F$ is not invertible), $\mu = [(z-1)^q G(z)]_{\vert_{z=1}}$;
> - if $G(z)$ has $q$ zeroes in $z=1$ ($G(1) = 0$), $\mu = [\frac{G(z)}{(z-1)^q}]_{\vert_{z=1}}$.

10. We can retrieve the **input-output** relationship in the time-domain of a discrete time LTI system from its transfer function (assuming that the initial conditions are zero):
$$
\frac{Y(z)}{U(z)} = G(z) = \frac{N(z)}{D(z)} = \frac{b_0 z^m + \cdots + b_{m-1}z + b_m}{a_0 z^n + \cdots + a_{n-1} z + a_n} = \frac{b_0 z^{m-n} + \cdots + b_{m-1}z^{1-n} + b_mz^{-n}}{a_0+ \cdots + a_{n-1} z^{1-n} + a_n z^{-n}} \text{ iff}
$$
$$
(a_0+ \cdots + a_{n-1} z^{1-n} + a_n z^{-n}) Y(z) = (b_0 z^{m-n} + \cdots + b_{m-1}z^{1-n} + b_mz^{-n})U(z) \text{ iff}
$$
$$
a_0 y(t) + \cdots + a_{n-1} y(t-n+1)+a_ny(t-n) = b_0 u(t-n+m) + \cdots + b_{m-1}u(t-n+1) + b_mu(t-n) \text{.}
$$
