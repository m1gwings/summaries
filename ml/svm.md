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

Know that we know the shape of the SVMs classifier, we need to define the optimization problem which has to be solved to compute the parameters.
For doing so we need a brief geometrical digression on computing the distance of a point from a plane.

Let $f(\underline{x}|\underline{w}, b) = \underline{w}^T \underline{x} + b$ with $\underline{w} \neq \underline{0}$. This function induces a plane: $\pi = \{ \underline{x} | f(\underline{x}|\underline{w},b) = 0 \}$.
Since $\underline{w} \neq \underline{0}$, $\underline{\tilde{x}} = \frac{b \underline{w}}{||\underline{w}||_2^2}$ is well defined. Furthermore, $f(\underline{\tilde{x}}|\underline{w}, b) = 0$, hence $\underline{\tilde{x}} \in \pi$.

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
\text{margin}(\underline{w}_\text{ext}) = \min_{n=1}^N \frac{|\underline{w}^T \underline{\phi}(\underline{x}_n) + b|}{||\underline{w}_\text{ext}||_2} \stackrel{\text{classification is perfect}}{=} \min_{n=1}^N \frac{t_n(\underline{w}^T \underline{\phi}(\underline{x}_n) + b)}{||\underline{w}_\text{ext}||_2}.
$$
Now, maximizing the margin directly isn't easy. Fortunately we can rewrite the expression in a simpler way through some observations.
First of all observe that, if $\alpha > 0$:
$$
\text{margin}(\alpha \underline{w}_\text{ext}) = \text{margin}(\underline{w}_\text{ext}).
$$
That is, the value of the objective function stays the same if we scale $\underline{w}_\text{ext}$ by a positive constant. This is intuitive, since the hyperplane is defined only by the direction of $\underline{w}_\text{ext}$, its magnitude is irrelevant.

Hence, for every optimal solution $\underline{w}^*_\text{ext}$ to the optimization problem, there is another optimal solution $\underline{w}_\text{ext}' = \frac{\underline{w}^*_\text{ext}}{\min_n (t_n ({\underline{w}^*}^T \underline{\phi}(\underline{x}_n + b^*)))}$ s.t.:
$$
\text{margin}(\underline{w}'_\text{ext}) = \text{margin}\left(\frac{\underline{w}^*_\text{ext}}{\min_n (t_n ({\underline{w}^*}^T \underline{\phi}(\underline{x}_n + b^*)))}\right) = \text{margin}(\underline{w}_\text{ext}^*).
$$
(_observe that $\min_n (t_n ({\underline{w}^*}^T \underline{\phi}(\underline{x}_n + b^*))) > 0$ since we assume that the training set is linearly separable_), and:

---

$$
\min_{n=1}^N (t_n ({\underline{w}'}^T \underline{\phi}(\underline{x}_n)) + b') = \text{margin}(\underline{w}_\text{ext}') ||\underline{w}_\text{ext}'||_2 = \text{margin}(\underline{w}^*_\text{ext}) \frac{||\underline{w}_\text{ext}^*||_2}{\min_n (t_n ({\underline{w}^*}^T \underline{\phi}(\underline{x}_n + b^*)))} =
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
\max \frac{1}{||\underline{w}_\text{ext}||_2}
$$
$$
\text{s.t.}
$$
$$
\underline{w}_\text{ext} \neq \underline{0}
$$
$$
t_n(\underline{w}^T \underline{\phi}(\underline{x}_n) + b) \geq 1 \text{ for all } n \in \{ 1, \ldots, N \}.
$$
Then, by what we proved, for every optimal solution $\underline{w}^*_\text{ext}$ to the original problem, there is another optimal solution $\underline{w}'_\text{ext}$ s.t.
$$
\frac{1}{||\underline{w}'_\text{ext}||_2} = \text{margin}(\underline{w}_\text{ext}') \geq \text{margin}(\underline{w}_\text{ext}) = \frac{\min_{n=1}^N (t_n(\underline{w}^T \underline{\phi}(\underline{x}_n) + b))}{||\underline{w}||_\text{ext}} \geq \frac{1}{||\underline{w}_\text{ext}||}
$$
for $\underline{w}_\text{ext}$ s.t. $t_n(\underline{w}^T \underline{\phi}(\underline{x}_n) + b) \geq 1 \text{ for all } n \in \{ 1, \ldots, N \}$.

Hence every optimal solution of the original problem has an equivalent optimal solution in the second problem. Now we need to show the converse: let $\epsilon > 0$ and suppose that $\underline{\tilde{w}}_\text{ext}$ is s.t.
$$
t_n (\underline{\tilde{w}}^T \underline{\phi}(\underline(x)) + \tilde{b}) \geq 1 + \epsilon \text{ for all } n \in \{ 1, \ldots, N \}.
$$
Then $\frac{\underline{\tilde{w}}_\text{ext}}{1+\epsilon}$ is feasible for the second problem and has a better objective function value than $\underline{\tilde{w}}_\text{ext}$. Hence [resume...]
