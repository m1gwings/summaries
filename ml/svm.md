---
marp: true
theme: summary
math: mathjax
---
# Support Vector Machines

<div class="author">

Cristiano Migali
(_adapted from the slides of Prof. Marcello Restelli_)

</div>

**Support Vector Machines** (**SVMs**) is one of the best methods for classification.
It is also one of the most mathematical and difficult topic in ML since combines learning theory, kernel theory, and constrained optimization.

We will not see all the details, but give a **basic understanding** of how SVMs works and what are the **important parameters**.

## Revisiting the Perceptron

We will introduce SVMs by revisiting the Perceptron.
As we know, the discriminative function used in the Perceptron to classify the samples has the shape:
$$
y(\underline{x}_q) = \text{sign}(\underline{\phi}^T(\underline{x}_q) \underline{w}^*)
$$
for a certain set of parameters $\underline{w}^*$. Furthermore, because of how the iteration rule to train a Perceptron is defined, if we start from $\underline{w}^{(0)} = \underline{0}$ (_which miss-classifies every point_):
$$
\underline{w}^* = \sum_{n=1}^N \alpha_n t_n \underline{\phi}(\underline{x}_n)
$$
(where $\alpha_n \in \mathbb{N}$).
Then, if we plug this back in the expression for $y$:
$$
y(\underline{x}_q) = \text{sign}\left(\sum_{n=1}^N \alpha_n t_n \underline{\phi}^T(\underline{x}_q) \underline{\phi}(\underline{x}_n)\right).
$$
We can replace the dot product between the feature maps with an arbitrary **similarity function**: a **kernel function**. This produces the shape of the classifier used in SVMs.

## Minimizing the margin

Now that we know the shape of the SVMs classifier, we need to define the optimization problem which has to be solved to compute the parameters.
For doing so we need a brief geometrical digression on computing the distance of a point from a plane.

Let $f(\underline{x}|\underline{w}, b) = \underline{w}^T \underline{x} + b$ with $\underline{w} \neq \underline{0}$. This function induces a plane: $\pi = \{ \underline{x} \ | \ f(\underline{x}|\underline{w},b) = 0 \}$.
Since $\underline{w} \neq \underline{0}$, $\underline{\tilde{x}} = -\frac{b \underline{w}}{||\underline{w}||_2^2}$ is well defined. Furthermore, $f(\underline{\tilde{x}}|\underline{w}, b) = 0$, hence $\underline{\tilde{x}} \in \pi$.

---

Fix an input $\underline{x}$. Let $\underline{d} = \underline{w}^T(\underline{x} - \underline{\tilde{x}}) \frac{\underline{w}}{||\underline{w}^2||_2^2} = f(\underline{x}|\underline{w}, b)\frac{\underline{w}}{||\underline{w}||_2^2}$.
Let $\underline{y} = \underline{x} - \underline{d}$; observe that $f(\underline{y}|\underline{w},b) = 0$, hence $\underline{y} \in \pi$.
Now pick $\underline{z} \in \pi$:
$$
||\underline{x} - \underline{z}||_2^2 = ||\underline{d} + \underline{y} - \underline{z}||_2^2 = ||\underline{d}||_2^2 + ||\underline{y} - \underline{z}||_2^2 + 2 \frac{f(\underline{x}|\underline{w},b)}{||\underline{w}||_2^2}(f(\underline{y}|\underline{w},b) - f(\underline{z}|\underline{w}, b)) =
$$
$$
= ||\underline{d}||_2^2 + ||\underline{y} - \underline{z}||_2^2 \geq ||\underline{d}||_2^2.
$$

Finally, since $\underline{y} = \underline{x} - \underline{d}$, then $\underline{d} = \underline{x} - \underline{y}$. Hence, because of the previous inequality, $\underline{y}$ is the point in $\pi$ which is closest to $\underline{x}$.
It follows that:
$$
\text{dist}(\underline{x}, \pi) = ||\underline{d}||_2 = |f(\underline{x}|\underline{w},b)| \frac{||\underline{w}||_2}{||\underline{w}||_2^2} = \frac{|f(\underline{x}|\underline{w},b)|}{||\underline{w}||_2}.
$$

Now, in the optimization problem which defines SVMs we want to maximize the **margin** of the classifier, which is the minimum distance of a point from the decision boundary of the classifier, assuming that the classification is perfect.
- In particular, let $\underline{w}_\text{ext} = \begin{bmatrix} \underline{w}^T & b \end{bmatrix}^T$, assuming that the training set is linearly separable and that the parameters $\underline{w}_\text{ext}$ define an hyperplane which classifies correctly all points, the margin is defined as:
$$
\text{margin}(\underline{w}_\text{ext}) = \min_{n=1}^N \frac{|\underline{w}^T \underline{\phi}(\underline{x}_n) + b|}{||\underline{w}||_2} \stackrel{\text{classification is perfect}}{=} \min_{n=1}^N \frac{t_n(\underline{w}^T \underline{\phi}(\underline{x}_n) + b)}{||\underline{w}||_2}.
$$
Now, maximizing the margin directly isn't easy. Fortunately we can rewrite the expression in a simpler way through some observations.
First of all observe that, if $\alpha > 0$:
$$
\text{margin}(\alpha \underline{w}_\text{ext}) = \text{margin}(\underline{w}_\text{ext}).
$$
That is, the value of the objective function stays the same if we scale $\underline{w}_\text{ext}$ by a positive constant. This is intuitive, since the hyperplane is defined only by the direction of $\underline{w}_\text{ext}$, its magnitude is irrelevant.

Hence, for every optimal solution $\underline{w}^*_\text{ext}$ to the optimization problem, there is another optimal solution $\underline{w}_\text{ext}' = \frac{\underline{w}^*_\text{ext}}{\min_n (t_n ({\underline{w}^*}^T \underline{\phi}(\underline{x}_n) + b^*))}$ s.t.:
$$
\text{margin}(\underline{w}'_\text{ext}) = \text{margin}\left(\frac{\underline{w}^*_\text{ext}}{\min_n (t_n ({\underline{w}^*}^T \underline{\phi}(\underline{x}_n) + b^*))}\right) = \text{margin}(\underline{w}_\text{ext}^*).
$$
(_observe that $\min_n (t_n ({\underline{w}^*}^T \underline{\phi}(\underline{x}_n) + b^*)) > 0$ since we assume that the training set is linearly separable_), and:

---

$$
\min_{n=1}^N (t_n ({\underline{w}'}^T \underline{\phi}(\underline{x}_n) + b')) = \text{margin}(\underline{w}_\text{ext}') ||\underline{w}'||_2 = \text{margin}(\underline{w}^*_\text{ext}) \frac{||\underline{w}^*||_2}{\min_n (t_n ({\underline{w}^*}^T \underline{\phi}(\underline{x}_n + b^*)))} =
$$
$$
= \frac{\text{margin}(\underline{w}^*_\text{ext})}{\text{margin}(\underline{w}^*_\text{ext})} = 1.
$$

This implies that:
$$
t_n({\underline{w}'}^T \underline{x}_n + b') \geq 1 \text{ for all } n \in \{ 1, \ldots, N \}.
$$

Now consider the following optimization problem:
$$
\max \frac{1}{||\underline{w}||_2}
$$
$$
\text{s.t.}
$$
$$
\underline{w} \neq \underline{0}
$$
$$
t_n(\underline{w}^T \underline{\phi}(\underline{x}_n) + b) \geq 1 \text{ for all } n \in \{ 1, \ldots, N \}.
$$
Then, by what we proved, for every optimal solution $\underline{w}^*_\text{ext}$ to the original problem, there is another optimal solution $\underline{w}'_\text{ext}$ s.t.
$$
\frac{1}{||\underline{w}'||_2} = \text{margin}(\underline{w}_\text{ext}') \geq \text{margin}(\underline{w}_\text{ext}) = \frac{\min_{n=1}^N (t_n(\underline{w}^T \underline{\phi}(\underline{x}_n) + b))}{||\underline{w}||_2} \geq \frac{1}{||\underline{w}||_2}
$$
for $\underline{w}_\text{ext}$ s.t. $t_n(\underline{w}^T \underline{\phi}(\underline{x}_n) + b) \geq 1 \text{ for all } n \in \{ 1, \ldots, N \}$.

Hence every optimal solution of the original problem has an equivalent optimal solution in the second problem. Now we need to show the converse: let $\epsilon > 0$ and suppose that $\underline{\tilde{w}}_\text{ext}$ is s.t.
$$
t_n (\underline{\tilde{w}}^T \underline{\phi}(\underline(x)) + \tilde{b}) \geq 1 + \epsilon \text{ for all } n \in \{ 1, \ldots, N \}.
$$
Then $\frac{\underline{\tilde{w}}_\text{ext}}{1+\epsilon}$ is feasible for the second problem and has a better objective function value than $\underline{\tilde{w}}_\text{ext}$. Hence every optimal solution of the second problem $\underline{w}^{**}_\text{ext}$ must be s.t. there exists $\hat{n} \in \{ 1, \ldots, N \}$ with $t_\hat{n}({\underline{w}^{**}}^T \underline{\phi}(\underline{x}_\hat{n}) + b^{**}) = 1$ (_easy proof by contradiction_).
Then, for every optimal solution to the second problem:
$$
\min_{n=1}^N t_n({\underline{w}^{**}}^T \underline{\phi}(\underline{x}_n) + b^{**}) = 1.
$$
This is implies that:
$$
\text{margin}(\underline{w}^{**}_\text{ext}) = \frac{1}{||\underline{w}^{**}||_2} \stackrel{\underline{w}^{**}_\text{ext} \text{ is optimal}}{\geq} \frac{1}{||\underline{w}'||_2} = \text{margin}(\underline{w}'_\text{ext}).
$$

---

But, since $\underline{w}'_\text{ext}$ is optimal for the first problem, we also have:
$$
\text{margin}(\underline{w}'_\text{ext}) \geq \text{margin}(\underline{w}^{**}_\text{ext}).
$$
Hence it must be $\text{margin}(\underline{w}'_\text{ext}) = \text{margin}(\underline{w}^{**}_\text{ext})$.

This proves that every optimal solution to the second problem is an optimal solution of the first problem.

In conclusion we know that if the original problem admits an optimal solution, we have another equivalent optimal solution to the original problem which is also an optimal solution of the second problem, which then is also feasible. Furthermore, every optimal solution to the second problem is an optimal solution for the original problem. In other words the <u>two problems are equivalent</u>.
Finally observe that the constraint $\underline{w} \neq \underline{0}$ is implied by $t_n(\underline{w}^T \underline{\phi}(\underline{x}_n) + b) \geq 1$ for all $n \in \{ 1, \ldots, N \}$ if there are $t_{n_1} = 1$ and $t_{n_2} = -1$ (_a reasonable assumption_), since it can be both $b \geq 1$ and $b \leq 1$. Hence we can remove such constraint. Furthermore, maximizing $\frac{1}{||\underline{w}||_2}$ is equivalent to minimizing $\frac{1}{2}||\underline{w}||_2^2$.

This leads to the final form of the optimization problem, which is convex!

$$
\min \frac{1}{2}||\underline{w}||_2^2
$$
$$
\text{s.t.}
$$
$$
t_n(\underline{w}^T \underline{\phi}(\underline{x}_n) + b) \geq 1 \text{ for all } n \in \{ 1, \ldots, N \}.
$$

As usual, let's construct the dual problem in order to summon kernels. This will also allow us to define what a support vector is.
The lagrangian for the problem is:
$$
\mathcal{L}(\underline{w}, b, \underline{\alpha}) = \frac{1}{2}||\underline{w}||_2^2 - \sum_{n=1}^N \alpha_n[t_n(\underline{w}^T \underline{\phi}(\underline{x}_n) + b) - 1].
$$
Let's look for the minimizers of the lagrangian for fixed $\underline{\alpha}$.
First of all observe that:
$$
\frac{\partial}{\partial b} \mathcal{L}(\underline{w}, b, \underline{\alpha}) = - \sum_{n=1}^N \alpha_n t_n,
$$
hence, if $\sum_{n=1}^N \alpha_n t_n \neq 0$, the lagrangian is unbounded below for fixed $\underline{\alpha}$, and so the dual objective function has value $\tilde{L}(\underline{\alpha}) = -\infty$.
If otherwise $\sum_{n=1}^N \alpha_n t_n = 0$, the lagrangian does not depend on $b$ and, most important, is <u>strictly convex</u> in $\underline{w}$. We can compute the minimizer:
$$
\nabla_{\underline{w}} \mathcal{L}(\underline{w}, b, \underline{\alpha}) = \underline{w} - \sum_{n=1}^N \alpha_n t_n \underline{\phi}(\underline{x}_n) = \underline{0}
$$

---

This happens if and only if:
$$
\underline{w} = \sum_{n=1}^N \alpha_n t_n \underline{\phi}(\underline{x}_n).
$$
hence, if $\sum_{n=1}^N \alpha_n t_n \neq 0$:
$$
\tilde{L}(\underline{\alpha}) = \frac{1}{2} \sum_{n=1}^N \alpha_n t_n \underline{\phi}^T(\underline{x}_n) \sum_{m=1}^N \alpha_m \alpha_m t_m \underline{\phi}(\underline{x}_m) - \sum_{n=1}^N \alpha_n t_n \underline{\phi}(\underline{x}_n) \sum_{m=1}^N \alpha_m t_m \underline{\phi}(\underline{x}_m) - b \sum_{n=1}^N \alpha_n t_n + \sum_{n=1}^N \alpha_n =
$$
$$
= - \frac{1}{2} \sum_{n=1}^N \sum_{m=1}^M  \alpha_n \alpha_m t_n t_m \underline{\phi}^T(\underline{x}_n) \underline{\phi}(\underline{x}_m) - b \cdot 0 + \sum_{n=1}^n \alpha_n = \sum_{n=1}^N \alpha_n - \frac{1}{2} \sum_{n=1}^N \sum_{n=1}^M \alpha_n \alpha_m t_n t_m \underline{\phi}^T(\underline{x}_n) \underline{\phi}(\underline{x}_m).
$$

In conclusion:
$$
\tilde{L}(\underline{\alpha}) = \begin{cases}
\sum_{n=1}^N \alpha_n - \frac{1}{2} \sum_{n=1}^N \sum_{n=1}^M \alpha_n \alpha_m t_n t_m \underline{\phi}^T(\underline{x}_n) \underline{\phi}(\underline{x}_m)  \text{ if } \sum_{n=1}^N \alpha_n t_n = 0 \\
- \infty \text{ otherwise}
\end{cases}.
$$
The dual problem is:
$$
\max_{\underline{\alpha}} \tilde{L}(\underline{\alpha}) 
$$
$$
\text{s.t.}
$$
$$
\underline{\alpha} \geq \underline{0}.
$$
Clearly, an <u>equivalent</u> (same optimal solutions) problem is:
$$
\max_{\underline{\alpha}} \tilde{L}(\underline{\alpha}) = \sum_{n=1}^N \alpha_n - \frac{1}{2} \sum_{n=1}^N \sum_{n=1}^M \alpha_n \alpha_m t_n t_m \underline{\phi}^T(\underline{x}_n) \underline{\phi}(\underline{x}_m)
$$
$$
\text{s.t.}
$$
$$
\sum_{n=1}^N \alpha_n t_n = 0
$$
$$
\underline{\alpha} \geq \underline{0}.
$$

The primal problem satisfies Slater's conditions, hence we have strong duality. Then, by p. 242, 248 _Convex Optimization by Boyd, Vandenberghe: complementary slackness, solving the primal problem via the dual_, we know that every optimal solution to the primal is a minimizer of the lagrangian fixed the optimal multipliers.
Once we fix the optimal multipliers (which must satisfy $\sum_{n=1}^N \alpha_n t_n = 0$ because of what we remarked before), the minimizer w.r.t $\underline{w}$ of the lagrangian is unique, hence, since the primal admits an optimal solution (_it is convex_), it must correspond to the primal optimal weights $\underline{w}^*$.

---

Hence, once we solve the dual problem, finding the optimal multipliers $\underline{\alpha}^*$, the optimal weights are:
$$
\underline{w}^* = \sum_{n=1}^N \alpha_n^* t_n \underline{\phi}(\underline{x}_n).
$$

Again, by p. 242 _Convex Optimization by Boyd, Vandenberghe: complementary slackness_, we know that optimality the complementary slackness conditions hold:
$$
\alpha_n^* [t_n({\underline{w}^*}^T \underline{\phi}(\underline{x}_n) + b^*) - 1] = 0.
$$

We call the points $S = \{ n \in \{ 1, \ldots, N \} \ | \ \alpha_n^* > 0 \}$ support vectors. Let $N_S = |S|$. The complementary slackness conditions imply that:
$$
t_s({\underline{w}^*}^T \underline{\phi}(\underline{x}_s) + b^*) = 1 \text{ for all } s \in S.
$$
Now that we know $\underline{w}^*$, we can solve once of the equations above to determine $b^*$. In practice a more numerically stable solution is used: let's understand it.
First of all note that $\alpha_m^* \neq 0$ iff $m \in S$. Hence:
$$
\underline{w}^* = \sum_{m \in S} \alpha_m^* t_m \underline{\phi}(\underline{x}_m).
$$
Then:
$$
t_s \left( \sum_{m \in S} \alpha^*_m t_m \underline{\phi}^T(\underline{x}_m) \underline{\phi}(\underline{x}_s) + b^* \right) = 1.
$$
Let's multiply both sides by $t_s$, observing that $t_s^2 = 1$ for all $s \in N$:
$$
\sum_{m \in S} \alpha^*_m t_m \underline{\phi}^T(\underline{x}_m) \underline{\phi}(\underline{x}_s) + b^* = t_s.
$$
Let's sum over all $s \in S$:
$$
\sum_{s \in S} \sum_{m \in S} \alpha^*_m t_m \underline{\phi}^T(\underline{x}_m) \underline{\phi}(\underline{x}_s) + N_S b^* = \sum_{s \in S} t_s.
$$
Finally:
$$
b^* = \frac{1}{N_S} \sum_{s \in S} \left( t_s - \sum_{m \in S} \alpha^*_m t_m \underline{\phi}^T(\underline{x}_m) \underline{\phi}(\underline{x}_s) \right) = \frac{1}{N_S} \sum_{s \in S} \left( t_s - \sum_{m \in S} \alpha^*_m t_m k(\underline{x}_m,\underline{x}_s) \right).
$$

We're ready to classify new points with the usual shape of the classifier we revised before:
$$
y(\underline{x}) = \text{sign}\left( {\underline{w}^*}^T \underline{\phi}(\underline{x}) + b^* \right) = \text{sign}\left( \sum_{m \in S} \alpha^*_m t_m k(\underline{x}_m, \underline{x}) + b^* \right).
$$

---

**Remarks**:
- there are very efficient methods specially tailored to solve the dual problem of SVMs (Sequential Quadratic Programming);
- all the support vectors, in the linearly separable case, are on the margin because of the complementary slackness conditions;
- usually $N_S \ll N$:
- in high dimensional problems the percentage of support vectors can become significant, scalability becomes an issue, and it can affect generalization guarantees.

As we mentioned at the beginning, SVMs have important learning theory guarantees.
The bound on VS dimension **decreases** with the margin. The larger the margin, the less the capacity to over-fit, the less the VS dimension. But, margin bound is quite loose.

We have also another bound that can be estimated through **LOO cross validation**:
$$
L_\text{true}(\hat{h}_{\mathcal{D}_\text{train}}) \leq \frac{\mathbb{E}[\text{\# of support vectors}]}{N}.
$$
It can be easily computed and we do not need to run SVM multiple times (I think that this is due to the fact that, if we remove a point which is not a support vector from $\mathcal{D}_\text{train}$ we do not need to retrain: the old solution satisfies the KKT conditions of the new problem).

## Handling noisy data

Often we have to deal with non-separable data (even in high dimensional feature spaces). We can do so with **soft margin SVMs**. In particular we need to introduce **slack variables** $\xi_n$ which allow to violate the constraint by paying a penalty.
The new problem becomes:
$$
\min ||\underline{w}||_2^2 + C \sum_{n=1}^N \xi_n
$$
$$
\text{s.t.}
$$
$$
t_n(\underline{w}^T \underline{\phi}(\underline{x}_n) + b) \geq 1 - \xi_n \text{ for all } n \in N
$$
$$
\xi_n \geq 0 \text{ for all } n \in N.
$$
$C$ is a coefficient that allows to **tradeoff bias-variance**. If $C = +\infty$ it must be $\xi_n = 0$ for all $n \in N$: we are in the original problem with "low bias and high variance", as $C \rightarrow 0$ violating the margin costs less and less, we don't need to over-fit: "high bias and low variance".
$C$ is chosen by cross validation.

Let's derive again the dual representation:
$$
\mathcal{L}(\underline{w}, b, \underline{\xi}, \underline{\alpha}, \underline{\beta}) = ||\underline{w}||_2^2 + C \sum_{n=1}^N \xi_n - \sum_{n=1}^N \alpha_n (t_n (\underline{w}^T \underline{\phi}(\underline{x}_n) + b) + \xi_n - 1) - \sum_{n=1}^N \beta_n \xi_n.
$$

---

Again if we don't set the coefficients of $b$ and $\xi_n$ to $0$, then the value of the dual objective function $\tilde{L}$ is $-\infty$.
In particular:
$$
\frac{\partial}{\partial b} \mathcal{L}(\underline{w}, b, \underline{\xi}, \underline{\alpha}, \underline{\beta}) = - \sum_{n=1}^N \alpha_n t_n = 0.
$$
$$
\frac{\partial}{\partial \xi_n} \mathcal{L}(\underline{w}, b, \underline{\xi}, \underline{\alpha}, b) = C - \alpha_n - \beta_n = 0 \text{ iff } \beta_n = C - \alpha_n \text{ for all } n \in \{ 1, \ldots, N \}.
$$
Once these conditions are satisfied, the lagrangian for fixed multipliers depends only on $\underline{w}$ and is strictly convex. The unique minimizer satisfies:
$$
\nabla_{\underline{w}} \mathcal{L}(\underline{w}, b, \underline{\xi}, \underline{\alpha}, \underline{\beta}) = 2 \underline{w} - \sum_{n=1}^N \alpha_n t_n \underline{\phi}(\underline{x}_n) = \underline{0} \text{ iff}
$$
$$
\underline{w} = \frac{1}{2} \sum_{n=1}^N \alpha_n t_n \underline{\phi}(\underline{x}_n).
$$

By plugging these results into the lagrangian we get:
$$
\tilde{L}(\underline{\alpha}) = \frac{1}{4} \sum_{n=1}^N \sum_{m=1}^N \alpha_n \alpha_m t_n t_m k(\underline{x}_n, \underline{x}_m) + C \sum_{n=1}^N \xi_n -
$$
$$
- \frac{1}{2} \sum_{n=1}^n \sum_{m=1}^N \alpha_n t_n \alpha_m t_m k(\underline{x}_n, \underline{x}_m) - b \sum_{n=1}^N \alpha_n t_n - \sum_{n=1}^N \alpha_n \xi_n + \sum_{n=1}^N \alpha_n - \sum_{n=1}^N C \xi_n + \sum_{n=1}^N \alpha_n \xi_n =
$$
$$
= \sum_{n=1}^N \alpha_n - \frac{1}{4} \sum_{n=1}^N \sum_{m=1}^N \alpha_n \alpha_m t_n t_m k(\underline{x}_n, \underline{x}_m) - b \cdot 0 = \sum_{n=1}^N \alpha_n - \frac{1}{4} \sum_{n=1}^N \sum_{m=1}^N \alpha_n \alpha_m t_n t_m k(\underline{x}_n, \underline{x}_m).
$$

Furthermore, in the dual we need to impose, $\alpha_n \geq 0$, $\beta_n = C - \alpha_n \geq 0$ iff $\alpha_n \leq C$.
Hence, the dual problem is equivalent to:
$$
\max_{\underline{\alpha}} \tilde{L}(\underline{\alpha}) = \sum_{n=1}^N \alpha_n - \frac{1}{4} \sum_{n=1}^N \sum_{m=1}^N \alpha_n \alpha_m t_n t_m k(\underline{x}_n, \underline{x}_m)
$$
$$
\text{s.t.}
$$
$$
\sum_{n=1}^N \alpha_n t_n = 0
$$
$$
0 \leq \alpha_n \leq C \text{ for all } n \in \{ 1, \ldots, N \}.
$$

Again the **support vectors** are the point associated with $\alpha_n > 0$. If $\alpha_n < C$, then $\xi_n = 0$ and the point lies on the margin, otherwise, if $\alpha_n = C$ the point can lie in the margin and be either correctly ($\xi_n \leq 1$) or incorrectly ($\xi_n > 1$) classified.
