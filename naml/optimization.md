---
marp: true
theme: summary
---
# Optimization

<div class="author">

Cristiano Migali

</div>

## Introduction

Most of the times, when we apply a ML technique, we have to deal with a minimization problem. In particular we're interested in minimizing:
$$
J : \mathbb{R}^n \rightarrow \mathbb{R}
$$

$$
\underline{w} \mapsto J(\underline{w}) \text{,}
$$
or, more formally, we want to find
$$
\underline{w}^* = \arg \min_{\underline{w}} J(\underline{w}) \text{.}
$$

## First order methods

First order methods are optimization techniques which rely only on the gradient of the objective function $J$, computed in several points, in order to find a (local) optimum.

### Gradient descent

We will present an heuristic argument that motivates the iteration step of the **Gradient Descent** (**GD**) alogirthm, and then we will analyze its properties.
Assume that $J : A \rightarrow \mathbb{R}$ with $A \subseteq \mathbb{R}^n$ is differentiable.
Then, by the definition of differentiability
$$
\Delta J = J(\underline{w}^{(k+1)}) - J(\underline{w}^{(k)}) \approx \nabla J^T(\underline{w}^{(k)})(\underline{w}^{(k+1)} - \underline{w}^{(k)}) = \nabla J^T(\underline{w}^{(k)}) \Delta \underline{w} \text{.}
$$

Now let $\underline{w}^{(k+1)} = \underline{w}^{(k)} - \eta \nabla J(\underline{w}^{(k)})$ with $\eta > 0$.
Hence, $\Delta \underline{w} = -\eta \nabla J(\underline{w}^{(k)})$, and so
$$
\Delta J \approx - \eta \nabla J^T(\underline{w}^{(k)}) \nabla J(\underline{w}^{(k)}) = - \eta ||\nabla J(\underline{w}^{(k)})||^2 \leq 0 \text{.}
$$
That is, at every step we decrease the value of $J$ coherently with our objective of minimizing it.

- The **iteration step** of the gradient descent algorithm is:
$$
\underline{w}^{(k+1)} = \underline{w}^{(k)} - \eta^{(k)} \nabla J(\underline{w}^{(k)}) \tag{GD}\label{GD}
$$
> where $\eta^{(k)} > 0$ is known as step length or, more common in the ML community, **learning rate**, $J$ is the function which we want to minimize, and $\underline{w}^{(k)}$ is the result of the previous iteration.

---

> The initial value $\underline{w}^{(0)}$ is an input value of the algorithm.

**Notation**: $\underline{w}^* = \arg \min_{\underline{w}} J(\underline{w})$.

**Remark**: if we apply the GD algorithm with constant learning rate, its value has to be chosen carefully:
- if $\eta$ is too small, the convergence will be slow;
- if $\eta$ is too big, we could oscillate back and forth around the minimum.

Let's study the convergence of the GD algorithm.
Assume that we apply the GD algorithm to $J$ convex. Let $\underline{g}^{(k)} = \nabla J(\underline{w}^{(k)})$.
Then, by lemma (1) on convex functions:
$$
J(\underline{w}^*) \geq J(\underline{w}^{(k)}) + (\underline{g}^{(k)})^T(\underline{w}^* - \underline{w}^{(k)}) \text{ iff }
$$

$$
J(\underline{w}^{(k)}) - J(\underline{w}^*) \leq (\underline{g}^{(k)})^T (\underline{w}^{(k)} - \underline{w}^*) \text{.}
$$

By (GD):
$$
\underline{w}^{(k+1)} - \underline{w}^{(k)} = -\eta \underline{g}^{(k)} \text{, then}
$$

$$
\underline{g}^{(k)} = \frac{\underline{w}^{(k)} - \underline{w}^{(k+1)}}{\eta} \text{.}
$$

Hence
$$
J(\underline{w}^{(k)}) - J(\underline{w}^*) \leq \frac{1}{\eta} (\underline{w}^{(k)} - \underline{w}^{(k+1)})^T(\underline{w}^{(k)} - \underline{w}^*) \tag{A}\label{A}.
$$

It is easy to verify that:
$$
2 \underline{v}^T \underline{w} = ||\underline{v}||^2 + ||\underline{w}||^2 - ||\underline{v} - \underline{w}||^2 \text{.}
$$

If we use this identity in (A), we get:
$$
J(\underline{w}^{(k)}) - J(\underline{w}^*) \leq \frac{1}{2\eta}(||\underline{w}^{(k)} - \underline{w}^{(k+1)}||^2 + ||\underline{w}^{(k)} - \underline{w}^*||^2 - ||\underline{w}^* - \underline{w}^{(k+1)}||) =
$$

$$
= \frac{1}{2 \eta} \eta^2 ||\underline{g}^{(k)}||^2 + \frac{1}{2 \eta}(||\underline{w}^{(k)} - \underline{w}^*||^2 - ||\underline{w}^* - \underline{w}^{(k+1)}||^2) =
$$

$$
= \frac{\eta}{2} ||\underline{g}^{(k)}||^2 + \frac{1}{2 \eta}(||\underline{w}^{(k)} - \underline{w}^*||^2 - ||\underline{w}^{(k+1)} - \underline{w}^*||^2) \text{.}
$$

Now let's sum the inequalities above for every $k \in \{ 0, ..., N-1 \}$ where $N$ is the number of iterations of the algorithm. (_Observe that it is a telescopic sum_).

---

$$
\sum_{k=0}^{N-1} (J(\underline{w}^{(k)}) - J(\underline{w}^*)) \leq \frac{\eta}{2} \sum_{k=0}^{N-1} ||\underline{g}^{(k)}||^2 + \frac{1}{2 \eta} (||\underline{w}^{(0)} - \underline{w}^*||^2 - ||\underline{w}^{N} - \underline{w}^*||^2) \leq
$$

$$
\leq \frac{\eta}{2} \sum_{k=0}^{N-1} ||\underline{g}^{(k)}||^2 + \frac{1}{2 \eta} ||\underline{w}^{(0)} - \underline{w}^*||^2 \text{.} \tag{B}\label{B}
$$

**Remark**: From the last inequality, it is clear that the choice of $\underline{w}^{(0)}$ influences the convergence of the method. When dealing with NNs there are various techniques with which we can initialize weights and biases ($\underline{w}^{(0)}$) in order to make the algorithm more effective.

let's add a regularity constraint to $J$: assume that it is **Lipshitz convex**.

> **Theorem**: let $J : A \subseteq \mathbb{R}^d \rightarrow \mathbb{R}$ Lipshitz convex with parameter $L$, let $R$ s.t. $R \geq ||\underline{w}^{(0)} - \underline{w}^*||$. Then, if
$$
\eta = \frac{R}{L \sqrt{N}} \text{,}
$$

$$
\frac{1}{N} \sum_{k=0}^{N-1} (J(\underline{w}^{(k)}) - J(\underline{w}^*)) \leq \frac{R L}{\sqrt{N}} \text{.}
$$

> **Proof (*)**: by (B):
$$
\sum_{k=0}^{N-1} (J(\underline{w}^{(k)}) - J(\underline{w}^*)) \leq \frac{\eta}{2} \sum_{k=0}^{N-1} ||\underline{g}^{(k)}||^2 + \frac{1}{2 \eta} ||\underline{w}^{(0)} - \underline{w}^*||^2 \leq \frac{\eta}{2} \sum_{k=0}^{N-1} L^2 + \frac{1}{2 \eta} R^2 =
$$

$$
= \frac{\eta}{2}NL^2 + \frac{1}{2 \eta} R^2 = u(\eta) \text{.}
$$

> By studying the inequality $u'(\eta) > 0$, it is straightforward that $u(\eta)$ has a global minimum for $\eta = \frac{R}{L \sqrt{N}}$. (_This observetaion is not necessary for the proof, it is just to show that the value of $\eta$ in the theorem statement is the best one_).

> By subsituting $\eta = \frac{R}{L \sqrt{N}}$ into $u(\eta)$ we get the desired result.

> **Important remark**: the left hand of the inequality of the previous theorem is the average error:
$$
\frac{1}{N} \sum_{k=0}^{N-1} (J(\underline{w}^{(k)}) - J(\underline{w}^*)) \text{.}
$$
> If we want it to be less than or equal to $\epsilon > 0$, assuming $\eta = \frac{R}{L \sqrt{N}}$, we have to impose:

---

$$
\frac{RL}{\sqrt{N}} \leq \epsilon \text{ iff } N \geq \frac{R^2L^2}{\epsilon^2} \text{.}
$$

> Then $N$ grows with $\frac{1}{\epsilon^2}$ which is not good.
However $N$ doesn't depend directly on the dimension $d$ of the domain of $J$, which is nice (actually for analogous functions $J$ with different domains, $L$ could increase with $d$, but not in a dramatic way).

Let's try to improve the number of required iterations $N$ by changing the regularity properties of $J$.

- **Theorem**: let $J : \mathbb{R}^d \rightarrow \mathbb{R}$ differentiable and smooth with parameter $L$. Then, if $\eta = \frac{1}{L}$, GD satisfies the following inequality:
$$
J(\underline{w}^{(k+1)}) \leq J(\underline{w}^{(k)}) - \frac{1}{2L}||\nabla J(\underline{x}^{(k)})||^2
$$
> for every $k \in \{ 0, ..., N-1 \}$.

> **Proof**: By (GD), rememering that $\eta = \frac{1}{L}$:
$$
\underline{w}^{(k+1)} = \underline{w}^{(k)} - \frac{1}{L} \nabla J(\underline{w}^{(k)}) \text{.}
$$
> Then, by the smoothness of $J$:
$$
J(\underline{w}^{(k+1)}) \leq J(\underline{w}^{(k)}) + \nabla J^T (\underline{w}^{(k)})(\underline{w}^{(k+1)} - \underline{w}^{(k)}) + \frac{L}{2} ||\underline{w}^{(k+1)} - \underline{w}^{(k)}||^2 =
$$

$$
= J(\underline{w}^{(k)}) - \frac{1}{L} \nabla J^T(\underline{w}^{(k)}) \nabla J(\underline{w}^{(k)}) + \frac{L}{2} \frac{1}{L^2} ||\nabla J(\underline{w}^{(k)})||^2 =
$$


$$
= J(\underline{w})^{(k)} - \frac{1}{2L}||\nabla J(\underline{w}^{(k)})||^2 \text{.}
$$

We have found what is called a gurantee of reduction a.k.a. DC (Decreasing Condition) a.k.a. SDC (Sufficient Decreasing Condition) for $J$.

> **Theorem**: Let $J : \mathbb{R}^d \rightarrow \mathbb{R}$ differentiable, smooth with parameter $L$, and convex. Then, if $\eta = \frac{1}{L}$, GD satisfies
$$
J(\underline{w}^{(N)}) - J(\underline{w}^*) \leq \frac{2L}{N} ||\underline{w}^{(0)} - \underline{w}^*|| \text{.}
$$

> **Proof**: let
$$
\delta^{(k)} = J(\underline{w}^{(k)}) - J(\underline{w}^*) \text{.}
$$
> Then
$$
\delta^{(k+1)} = J(\underline{w}^{(k+1)}) - J(\underline{w}^*) \leq J(\underline{w}^{(k)}) - J(\underline{w}^*) - \frac{1}{2L} ||\nabla J(\underline{w}^{(k)})||^2 =
$$

---

$$
= \delta^{(k)} - \frac{1}{2L} ||\nabla J(\underline{w}^{(k)})||^2 \text{.} \tag{F}\label{F}
$$

Furthermore:
$$
\delta^{(k)} = J(\underline{w}^{(k)}) - J(\underline{w}^*) \leq
$$
$$
\leq \begin{matrix}
J(\underline{w}^{(k)}) - J(\underline{w}^{(k)}) - \nabla J^T(\underline{w}^{(k)}) (\underline{w}^* - \underline{w}^{(k)}) \\
\text{(convexity plus lemma (1))}
\end{matrix} = \nabla J^T(\underline{w}^{(k)}) (\underline{w}^{(k)} - \underline{w}^*) \leq
$$

$$
\leq ||\nabla J(\underline{w}^{(k)})|| ||\underline{w}^{(k)} - \underline{w}^*|| \text{.} \tag{G}\label{G}
$$

> Now let's prove that $||\underline{w}^{(k)} - \underline{w}^*||$ is decreasing in $k$:
$$
||\underline{w}^{(k+1)} - \underline{w}^*||^2 =^{\eta = \frac{1}{L}} ||\underline{w}^{(k)} - \frac{1}{L} \nabla J(\underline{w}^{(k)}) - \underline{w}^*||^2 =
$$

$$
= ||\underline{w}^{(k)} - \underline{w}^*||^2 -\frac{2}{L} \nabla J^T(\underline{w}^{(k)})(\underline{w}^{(k)} - \underline{w}^*) + \frac{1}{L^2}||\nabla J(\underline{w}^{(k)})||^2 =
$$

$$
= ||\underline{w}^{(k)} - \underline{w}^*||^2 -\frac{2}{L} (\nabla J(\underline{w}^{(k)}) - \nabla J(\underline{w}^*))^T(\underline{w}^{(k)} - \underline{w}^*) + \frac{1}{L^2}||\nabla J(\underline{w}^{(k)})||^2 \leq
$$

$$
\leq^{\text{lemma (5) of convex functions}} ||\underline{w}^{(k)} - \underline{w}^*||^2 - \frac{2}{L} \cdot \frac{1}{L} ||\nabla J(\underline{w}^{(k)}) - \nabla J(\underline{w}^*)||^2 + \frac{1}{L} ||\nabla J(\underline{w}^{(k)})||^2 =
$$

$$
= ||\underline{w}^{(k)} - \underline{w}^*||^2 - \frac{1}{L^2} ||\nabla J(\underline{w}^{(k)}||^2 \leq ||\underline{w}^{(k)} - \underline{w}^*|| \text{.} \tag{H}\label{H}
$$

> Observe that

> Then
$$
\delta^{(k+1)} \leq^{\text{(F)}} \delta^{(k)} - \frac{1}{2L}||\nabla J(\underline{w}^{k})||^2 \leq^{\text{(G) + } \delta^{(k)} \geq 0} \delta^{(k)} - \frac{1}{2L} \frac{(\delta^{(k)})^2}{||\underline{w}^{(k)} - \underline{w}^*||^2} \leq
$$

$$
\leq^{\text{(H)}} \delta^{(k)} - \frac{1}{2L} \frac{(\delta^{(k)})^2}{||\underline{w}^{(0)} - \underline{w}^*||^2} \text{.}
$$

> Let $w = \frac{1}{2L ||\underline{w}^{(0)} - \underline{w}^*||}$. We jsut proved that
$$
\delta^{(k+1)} \leq \delta^{(k)} - w (\delta^{(k)})^2 \text{ iff } w (\delta^{(k)})^2 + \delta^{(k+1)} \leq \delta^{(k)} \text{ iff }
$$

$$
w \frac{\delta^{(k)}}{\delta^{(k+1)}} + \frac{1}{\delta^{(k)}} \leq \frac{1}{\delta^{(k+1)}} \text{ iff } \frac{1}{\delta^{(k+1)}} - \frac{1}{\delta^{(k)}} \geq w \frac{\delta^{(k)}}{\delta^{(k+1)}} \geq^{\text{(F)}} w \text{.}
$$

> Then
$$
\frac{1}{\delta^{(N)}} - \frac{1}{\delta^{(0)}} = \sum_{k=0}^{N-1}(\frac{1}{\delta^{(k+1)}} - \frac{1}{\delta^{(k)}}) \geq \sum_{k=0}^{N-1} w = N w \text{, then}
$$

---

$$
\frac{1}{\delta^{(N)}} \geq^{\delta^{0} \geq 0} \frac{1}{\delta^{(N)}} - \frac{1}{\delta^{(0)}} \geq Nw \text{ iff }
$$

$$
\delta^{(N)} \leq \frac{1}{Nw} \text{.}
$$

> If we subsitute the definitions for $\delta^{(N)}$, and $w$ in the expression above we get the result we wished to prove.

> **Important remark**: let $||\underline{w}^{(0)} - \underline{w}^*|| \leq R$. Then, if we desired $J(\underline{w}^{(N)}) - J(\underline{w}^*) < \epsilon$, by the previous theorem, we need:
$$
N > \frac{2LR}{\epsilon} \text{.}
$$

Let's increase again the regularity of $J$. For stronglu convex functions, it holds the following convergence result for GD:
> **Theorem**: let $J : \mathbb{R}^d \rightarrow \mathbb{R}$ convex and differentiable. Suppose that $J$ is smooth with parameter $L$, and strongly convex with parameter $\mu > 0$. Choosing GD with arbitrary $\underline{w}^{(0)}$ satisfies:
>> i. $||\underline{w}^{(k+1)} - \underline{w}^*||^2 \leq (1 - \frac{\mu}{L}) ||\underline{w}^{(k)} - \underline{w}^*||^2$ for every $k \in \mathbb{N}$;
>> ii. $J(\underline{x}^{(N)}) - J(\underline{x}^*) \leq \frac{L}{2}(1 - \frac{\mu}{L})^N ||\underline{w}^{(0)} - \underline{w}^*||$
> for every $N \in \mathbb{N}^+$.

> **Remark**: according to this result, assume that we desire
$$
J(\underline{w}^{(N)}) - J(\underline{w}^*) < \epsilon \text{,}
$$
> let $R \geq ||\underline{w}^{(0)} - \underline{w}^*||^2$, then we need to impose
$$
N > \frac{L}{\mu} \log(\frac{L R^2}{2 \epsilon}) \text{.}
$$

> **Remarks**:
>> i. In practical applications, at least locally, we can assume strong convexity;
>> ii. When we minimize the loss function of a NN we don't need to reach its global minimum since it would cause overfitting: the model would become too "specialized" at "sovling the problem" for the training data, and would lose the ability to generalize.

> **Proof of (i)**: observe that
$$
J(\underline{w}^*) \leq^{\underline{w}^* \text{ is optimal }} J(\underline{w}^{(k)} - \frac{1}{L} \nabla J(\underline{w}^{(k)})) \leq 
$$

---

$$
\leq J(\underline{w}^{(k)}) + \nabla J^T(\underline{w}^{(k)}) (-\frac{1}{L} \nabla J(\underline{w}^{(k)})) + \frac{L}{2}\frac{1}{L^2} ||\nabla J(\underline{w}^{(k)})||^2 =
$$

$$
= J(\underline{w}^{(k)}) - \frac{1}{2L}||\nabla J(\underline{w}^{(k)})||^2 \text{ iff }
$$

$$
||\nabla J(\underline{w}^{(k)})||^2 \leq 2 L (J(\underline{w}^{(k)}) - J(\underline{w}^*)) \text{.} \tag{I}\label{I}
$$

> By strong convexity, we have
$$
J(\underline{w}^*) \geq J(\underline{w}^{(k)}) + \nabla J^T(\underline{w}^{(k)})(\underline{w}^* - \underline{w}^{(k)}) + \frac{\mu}{2}||\underline{w}^{(k)} - \underline{w}^*|| \text{ iff }
$$

$$
\nabla J^T(\underline{w}^{(k)}) (\underline{w}^{(k)} - \underline{w}^*) \geq J(\underline{w}^{(k)}) - J(\underline{w}^*) + \frac{\mu}{2}||\underline{w}^{(k)} - \underline{w}^*||^2 \text{.} \tag{J}\label{J}
$$

> Then:
$$
||\underline{w}^{(k+1)} - \underline{w}^*||^2 = ||\underline{w}^{(k)} - \frac{1}{L} \nabla J(\underline{w}^{(k)}) - \underline{w}^*||^2 =
$$

$$
= ||\underline{w}^{(k)} - \underline{w}^*||^2 - \frac{2}{L} \nabla J^T(\underline{w}^{(k)}) (\underline{w}^{(k)} - \underline{w}^*) + \frac{1}{L^2}||\nabla J(\underline{w}^{(k)})||^2 \leq^{\text{(J)}}
$$

$$
\leq^{\text{(J)}} ||\underline{w}^{(k)} - \underline{w}^*||^2 - \frac{2}{L}(J(\underline{w}^{(k)}) - J(\underline{w}^*) + \frac{\mu}{2} ||\underline{w}^{(k)} - \underline{w}^*||^2) + \frac{1}{L^2} ||\nabla J(\underline{w}^{(k)})||^2 \leq^{\text{(I)}}
$$

$$
\leq^{\text{(I)}} ||\underline{w}^{(k)} - \underline{w}^*||^2 - \frac{2}{L}(J(\underline{w}^{(k)}) - J(\underline{w}^*)) - \frac{\mu}{L} ||\underline{w}^{(k)} - \underline{w}^*|| + \frac{2}{L}(J(\underline{w}^{(k)} - J(\underline{w}^*))) =
$$

$$
= (1 - \frac{\mu}{L})||\underline{x}^{(k)} - \underline{x}^*||^2 \text{.}
$$

---

### Accelerated GD

There are some thoeretical results which provide a lower-bound to the number of iterations required in order to achieve error $\epsilon$ for every first order method.

> **Theorem (Nemirovski & Yudin, 1979)**: every first order method needs in the worst case $\Omega(\frac{1}{\sqrt{\epsilon}})$ steps (_assuming that the objective function is $L$-smooth and convex_).

It has been found a first order method which achieves the theoretical best possible performance: the **Accelereted Gradient Descent** (**AGD**) (Nesterov, 1983). We will put its pseudocode below. Let $J : \mathbb{R}^d \rightarrow \mathbb{R}$ convex, differentiable, and smooth with parameter $L$, $\underline{w}^{(0)} \in \mathbb{R}^d$, $N \in \mathbb{N}^+$.

<div class="algorithm">

1. $\text{AGD}(J, \underline{w}^{(0)}, N):$
1. &emsp; $\underline{z}^{(0)} \gets \underline{w}^{(0)}$
1. &emsp; $\underline{y}^{(0)} \gets \underline{w}^{(0)}$
1. &emsp; **while** $k < N$:
1. &emsp; &emsp; $\underline{y}^{(k+1)} \gets \underline{w}^{(k)} - \frac{1}{L} \nabla J (\underline{w}^{(k)})$
1. &emsp; &emsp; $\underline{z}^{(k+1)} \gets \underline{z}^{(k)} - \frac{k+1}{2L} \nabla J(\underline{w}^{(k)})$
1. &emsp; &emsp; $\underline{w}^{(k+1)} \gets \frac{k+1}{k+3} \underline{y}^{(k+1)} + \frac{2}{k+3} \underline{z}^{(k+1)}$
1. &emsp; &emsp; $k \gets k + 1$

</div>

We can formally state the convergence result for AGD:
> **Theorem**: let $J : \mathbb{R}^d \rightarrow \mathbb{R}$ convex, differentiable, with a global minimum $\underline{w}^*$; suppose that $J$ is smooth with parameter $L$. AGD yields:
$$
J(\underline{y}^{(N)}) - J(\underline{x}^*) \leq \frac{2L||\underline{z}^{(0)} - \underline{w}^*||^2}{N(N+1)}
$$

> for every $N \in \mathbb{N}^+$.

---

### Stochastic GD

In ML we're usually interested in minimizing functions with a peculiar shape, that is:
$$
J(\underline{w}) = \frac{1}{N} \sum_{i=1}^N J_i(\underline{w})
$$
where $N$ is the number of samples and $J_i(\underline{w})$ is the error in the prediction of the model for the $i$-th sample.

For example, in LS we wanted to minimize:
$$
J(\underline{w}) = \frac{1}{N}||\underline{y} - X \underline{w}||^2 = \frac{1}{N} \sum_{i=1}^N (y_i - \underline{x}_i^T \underline{w})^2 \text{.}
$$

There exists a variation of GD which has been specifically designed to achieve great performance when minimizing functions with the shape of $J(\underline{w})$: the **Stochastic Gradient Descent** (**SGD**).

It works as follows: at iteration $k$, we select (for example through uniform sampling), $i_k \in \{ 1, .., N \}$, and compute
$$
\underline{w}^{(k+1)} = \underline{w}^{(k)} - \eta \nabla J_{i_k}(\underline{w}^{(k)}) \text{.}
$$

Observe that
$$
\nabla J(\underline{w}) = \frac{1}{N} \sum_{i=1}^N \nabla J_i (\underline{w}) \text{,}
$$
hence, computing only $\nabla J_i (\underline{w})$ is $N$ times faster than computing the whole $\nabla J(\underline{w})$.

> **Remark**: in ML we can describe our training data as $\{ (\underline{x}_1, \underline{y}_1), ..., (\underline{x}_N, \underline{y}_N) \}$ where $\underline{x}_j \in \mathbb{R}^d$ ($\underline{y}_i \in \mathbb{R}^1$ _usually_), and both $N$ and $d$ are large.

When we observe empirically the behavior of SGD, what we usually see is the following:
> i. at the beginning the trahectory of $\underline{w}^{(k)}$ is quite regular and approaches the minimum point $\underline{w}^*$;
> ii. when we get close to $\underline{w}^*$, the behavior becoms cahotic: $\underline{w}^{(k)}$ oscillates back and forth around the minimizer.

We will rpvoide an explanation of the observed behavior through an example in 1D.
Let
$$
J(w) = \frac{1}{N} \sum_{i=1}^N (x_i w - b_i)^2 \text{.}
$$

---

Each $J_i(w) = (x_i w - b_i)^2$ is a quadratic function which attains minimum at $w_i^*$ s.t. $\frac{\partial J_i(w^*)}{\partial w} = 0 \text{ iff } 2 (x_i w_i^* - b_i) x_i = 0 \text{ iff } w_i^* = \frac{b_i}{x_i}$ (we assume $x_i \neq 0$).

Let's study $J(w)$:
$$
\frac{d J(w)}{d w} = \frac{1}{N} \sum_{i=1}^N 2(x_i w - b_i)x_i \geq 0 \text{ iff }
$$

$$
w \sum_{i=1}^N x_i^2 \geq \sum_{i=1}^N b_i x_i \text{ iff } w \geq \frac{\sum_{i=1}^N b_i x_i}{\sum_{i=1}^N x_i^2} \geq \frac{\sum_{i=1}^N \frac{b_i}{x_i}x_i^2}{\sum_{i=1}^N x_i^2} = \frac{\sum_{i=1}^N x_i^2 w_i^*}{\sum_{i=1}^N x_i^2} \text{.}
$$

Then $J(w)$ attains its minimum at:
$$
w^* = \frac{\sum_{i=1}^N x_i^2 w_i^*}{\sum_{i=1}^N x_i^2} \text{,}
$$
which is a weighted average of $w_i^*$ (with $x_i^2$ as weights).
Hence
$$
w^* \in [\min_{i \in \{ 1, ..., N \}} w_i^*, \max_{i \in \{ 1, ..., N \}} w_i^*] \text{.}
$$

By the results that we proved for GD, at the $k$-th step of SGD, $w^{(k)}$ gets closer to $w_{i_k}^*$. Then, if $w^{(k)} < \min_{i \in \{ 1, ..., N \}} w_i^*$, no matter which $i_k$ we pick, $w^{(k)}$ will "move" towards right and, since $w^* \in [\min_{i \in \{ 1, ..., N \}} w_i^*, \max_{i \in \{ 1, ..., N \}} w_i^*]$, it will get closer not only to $w_{i_k}^*$, but also to $w^*$. Analogous behavior if $w^{(k)} > \max_{i \in \{ 1, ..., N \}} w_i^*$.
When $w^{(k)} \in [\min_{i \in \{ 1, ..., N \}} w_i^*, \max_{i \in \{ 1, ..., N \}} w_i^*]$, it will start "bouncing around", moving towards $w_{i_k}^*$ at each step.
For this reason we call:
- $R = [\min_{i \in \{ 1, ..., N \}} w_i^*, \max_{i \in \{ 1, ..., N \}} w_i^*]$ the **region of confusion**;
- $\mathbb{R} \setminus R$ the **far out zone** (**FOZ**).

At each iteration SGD uses an **unbiased estimator** $g$ of $\nabla J$, that is:
$$
\mathbb{E}[g] = \nabla J \text{.}
$$
$\text{var}(g)$ controls the speed of convergence (we can get an intuition on why it is so by what has been explained in the 1D example).

**Reamrk**: There are two main ways of choosing $i_k$:
> i. Randomly pick $i_k$ with replacement (_that is we can pick the same $i_k$ twice without having to pick any other $\{ 1, ..., N \} \setminus \{ i_k \}$ before the "re-pick of $i_k$"; basically we sample from $\{ 1, ..., N \}$ at every step_) (_this approach is good for proving theoretical results_);

---

> ii. Randomly pick $i_k$ without replacement (_the converse of (i)_) (_this approach is good in practice since we can pre-shuffle the samples and stream through them_).

In order to shrink $\text{var}(g)$ we can apply the so-called **minibatch** technique:
$$
\underline{w}^{(k+1)} = \underline{w}^{(k)} - \frac{\eta}{|I_k|} \sum_{i \in I_k} \nabla J_i(\underline{w}^{(k)}) \text{.}
$$


**Remarks**:
> i. Very large mini-batch shrinks the confusion region (reduces noise) and can create overfitting;
> ii. We can parallelize the computation of $\nabla J(\underline{w}^{(k)})$ for every $i \in I_k$. 