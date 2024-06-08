---
marp: true
theme: summary
math: mathjax
---
# Linear classification

<div class="author">

Cristiano Migali
(_adapted from the slides of Prof. Marcello Restelli_)

</div>

**Remember**: the **goal** of classification is to assign an input $\underline{x}$ into one of $K$ discrete classes $C_k$, where $k \in \{ 1, \ldots, K \}$. Typically, each input is assigned to **only one** class.

In **linear classification**, the input space is divided into **decision regions** whose boundaries are called **decision boundaries** or **decision surfaces**.

For classification problems, we wish to predict discrete class labels, or their posterior probabilities that lie in the range $(0, 1)$. To achieve this, we consider a _generalization_ of the linear model:
$$
y(\underline{x}) = f(\underline{w}^T \underline{x} + w_0)
$$
where $f$ is a non-linear, usually invertible, function known as _activation function_. $f$ maps $\underline{w}^T \underline{x} + w_0$ to $(y_\min, y_\max)$, usually $y_\min = 0$ and $y_\max = 1$. The class predicted by the model is determined by the fact that $f(\underline{w}^T \underline{x} + w_0) > \frac{y_\min + y_\max}{2}$ or $f(\underline{w}^T \underline{x} + w_0) < \frac{y_\min + y_\max}{2}$.
Hence, the decision boundary is given by:
$$
\underline{w}^T \underline{x} + w_0 \in f^{-1}\left( \left\{ \frac{y_\min + y_\max}{2} \right\} \right)
$$
which is an hyperplane in the input space (assuming that the inverse image is a singleton). That is the **decision surfaces** are linear, even though the activation function is not linear. As we did for regression, we can consider **fixed nonlinear basis functions**.

## Representing the targets

In two-class problems we have a binary target vale $t \in \{ 0, 1 \}$, such that $t = 1$ is the **positive class** and $t = 0$ is the **negative class**. We can interpret the value of $t$ as the **probability** of the positive class. The output of the model can be represented as the probability that the model assigns to the positive class.
If there are $K$ classes, we can use a 1-of-$K$ encoding scheme: $\underline{t}$ is a vector of length $K$ and contains a **single 1** for the correct class and 0 elsewhere. We can interpret $\underline{t}$ as a vector of class probabilities.

## Different approaches

Analogously to linear regression, we have three main **approaches** to classification:
- **discriminant approach**: build a function that **directly maps** each input to a specific class;

---

- **probabilistic approach**: model the conditional probability distribution $p(C_k | \underline{x})$ and use it to make optimal decisions. In particular, we distinguish among two alternatives:
> - **probabilistic discriminative approach**: model $p(C_k| \underline{x})$ directly, for instance using parametric models (e.g. logistic regression);
> - **probabilistic generative approach**: model class conditional densities $p(\underline{x}|C_k)$ together with prior probabilities $p(C_k)$ for the classes. Infer the posterior using **Bayes' rule**:
$$
p(C_k | \underline{x}) = \frac{p(\underline{x}|C_k) p(C_k)}{p(\underline{x})}.
$$

## Two-classes vs Multi-class classification

We can solve **two-classes** linear classification problems with the following generalized model:
$$
y(\underline{x}) = \text{sign}(\underline{x}^T \underline{w} + w_0).
$$
Observe that $y_\min = -1$, $y_\max = 1$, then we assign $\underline{x}$ to $C_1$ if $\underline{x}^T \underline{w} + w_0 > 0$, or we assign it to $C_2$ if $\underline{x}^T \underline{w} + w_0 < 0$. Since $\text{sign}^{-1}(\{ 0 \}) = \{ 0 \}$, the decision boundary is given by:
$$
\underline{x}^T \underline{w} + w_0 = 0.
$$
Because of the properties of hyperplanes, $\underline{w}$ is orthogonal to the hyperplane. Furthermore,
$$
\frac{\underline{x}^T \underline{w} + w_0}{||\underline{w}||_2}
$$
is the signed distance (positive if $\underline{x}$ is in the half-space $\underline{w}$ points towards, negative otherwise) of $\underline{x}$ from the decision boundary [_see NLO summaries regarding SVM_].
Hence, the signed distance of the decision boundary from the origin is: $\frac{w_0}{||\underline{w}||_2}$.

Now, we want to **extend** this approach to **multiple classes**: $K > 2$. Let's discuss several approaches.
- **One-versus-the-rest**: we build $K-1$ classifiers, each of which solves a two class problem which consists in distinguishing the points in $C_k$ from the points NOT in $C_k$. If all the $K-1$ classifiers predict that the point is not in "their class", then it belongs to the remaining $K$-th class. Anyways there can be regions where two or more classifiers predict that the point belongs to their class.

---

<p align="center">
    <img src="static/one-versus-the-rest-classifier.svg"
    width="300mm" />
</p>

- **One-versus-one**: we build $\frac{K(K-1)}{2}$ classifiers, each one distinguish if a point belongs class $i$ or to class $j$ for all $i, j \in \{ 1, \ldots, K \}$, $i < j$. Then to understand the final predicted class we do **majority voting** among the classifiers. Also in this case we have ambiguous region with no majority.

<p align="center">
    <img src="static/one-versus-one-classifier.svg"
    width="400mm" />
</p>

- **$K$-linear classifiers**: we can use $K$ linear discriminant functions of the form:
$$
y_k(\underline{x}) = \underline{x}^T \underline{w}_k + w_{k,0} \text{ where } k \in \{ 1, \ldots, K \}.
$$
> We assign $\underline{x}$ to class $C_k$ if $y_k(\underline{x}) > y_j(\underline{x})$ for all $j \neq k$. The resulting decision boundaries are **convex**. Let's see why. Let $y_k(\underline{x}_A) > y_j(\underline{x}_A)$ and $y_k(\underline{x}_B) > y_j(\underline{x}_B)$, that is: $\underline{w}_k^T \underline{x}_A + w_{k,0} > \underline{w}_j^T \underline{x}_A + w_{j,0}$ and $\underline{w}_k^T \underline{x}_B + w_{k,0} > \underline{w}_j^T \underline{x}_B + w_{j,0}$. Now fix $\alpha \in [ 0, 1 ]$:
$$
y_k(\alpha \underline{x}_A + (1-\alpha) \underline{x}_B) = \alpha (\underline{w}_k^T \underline{x}_A + w_{k,0}) + (1-\alpha)(\underline{w}_k^T \underline{x}_B + w_{k,0}) >
$$

$$
> \alpha (\underline{w}_j^T \underline{x}_A + w_{j,0}) + (1-\alpha) (\underline{w}_j^T \underline{x}_B + w_{j,0}) = y_j(\alpha \underline{x}_A + (1-\alpha) \underline{x}_B).
$$

---

## Least Squares for classification

Consider a general classification problem with $K$ classes using 1-of-$K$ encoding scheme for the target vector $\underline{t}$.
Recall: Least Squares approximates the **conditional expectation** (_which is the minimizer of the corresponding ideal loss_) $\mathbb{E}[\underline{t}|\underline{x}]$, which in this case corresponds to the vector of probabilities that $\underline{x}$ belongs to class $k$, for all $k \in \{ 1, \ldots, K \}$. This would suggest us to use a Least Squares approach to fit the 1-of-$K$ targets.

In particular we can predict the membership to each class (the target) by its own linear model:
$$
y_k(\underline{x}) = \underline{w}_k^T \underline{x} + w_{k,0} \text{ where } k \in \{ 1, \ldots, K \}.
$$
In vector notation:
$$
\underline{y}(\underline{x}) = \mathbf{W}^T \underline{x}_{\text{ext}}
$$
where $\mathbf{W} = \begin{bmatrix} w_{1,0} & \ldots & w_{K,0} \\ \underline{w}_1 & \ldots & \underline{w}_K \end{bmatrix}$.
We already seen that we can easily fit multiple output with the least squares approach:
$$
\hat{\mathbf{W}}_{\text{OLS}} = (X^T X)^{-1}X^T \mathbf{T}
$$
where $\mathbf{T} = \begin{bmatrix} \underline{t}_1 & \ldots & \underline{t}_N \end{bmatrix}$.

But, **there are serious problems when using LS for linear classification**.
First of all observe that the values of $y_k(\underline{x})$ grows in magnitude as $\underline{x}$ gets further from the decision boundary, hence, even for points that are on the right side of the decision boundary, if they are very distant from it they will introduce high loss, **penalizing the correct model**. Indeed LS applied to linear classification is sensitive to outliers and can produce wrong models even when the training set could be classified perfectly.
Another consideration that will make us understand immediately why LS is a bad choice for linear classification is that we derived it in the Maximum Likelihood setting, assuming that the conditional distribution of the target given the input was Gaussian. This is clearly false for binary vectors like the ones that we want to fit.

## Fixed basis functions

So far we've considered classification models that work directly in the **input space**. All considered algorithms are equally applicable if we first make a **fixed nonlinear transformation** of the input space using vector of basis functions $\underline{\phi}(\underline{x})$. Decision boundaries will be **linear** in the **feature space**, but would correspond to **nonlinear** boundaries in the original **input space**. Classes that are linearly separable in the feature space **need not** be linearly separable in the original input space.

---

## Perceptron

The **perceptron** (Rosenblatt, 1958) is another example of **linear discriminant models**. It is an **online** linear classification algorithm. It correspond to a two-class model:
$$
y(\underline{x}) = \text{sign}(\underline{\phi}^T(\underline{x}) \underline{w}).
$$
The **target values** are +1 for class $C_1$ and -1 for class $C_2$. The algorithm finds the **separating hyperplane** by minimizing the _distance_ of **misclassified points** to the **decision boundary**. Indeed, using the number of misclassified points as a loss function is NOT effective, since it is a _piecewise constant function_.

We look for a vector $\underline{w}$ such that $\underline{\phi}^T(\underline{x}_n) \underline{w} > 0$ when $\underline{x}_n \in C_1$ and $\underline{\phi}^T(\underline{x}_n) \underline{w} < 0$ when $\underline{x}_n \in C_2$.

The **perceptron criterion** assign:
- _zero error_ to correct classification;
- $-t_n \underline{\phi}^T(\underline{x}_n) \underline{w}$ to misclassified pattern $\underline{x}_n$ (observe that, because of how $t_n$ is defined, by the properties of the decision boundary we discussed before, $-t_n \underline{\phi}^T(\underline{x}_n) \underline{w} = ||\underline{w}||_2 d$ where $d$ is the distance of $\underline{x}_n$ from the boundary).

The corresponding loss function is:
$$
L_P(\underline{w}) = - \sum_{n \in \mathcal{M}(\underline{w})} t_n \underline{\phi}^T(\underline{x}_n) \underline{w}
$$
where $\mathcal{M}(\underline{w})$ is the set of points miss-classified by model $\underline{w}$. Observe that, the fact that $\mathcal{M}$ depends on $\underline{w}$ makes the loss function piece-wise linear instead of being linear. For this reason the optimization of $L_P$ is done iteratively. The update rule can be derived heuristically imagining $\mathcal{M}$ fixed and applying SGD. The learning rate can be set to 1 since it only affects the magnitude of $\underline{w}$, which is immaterial w.r.t. to the decision boundary.
$$
\underline{w}^{(k+1)} = \underline{w}^{(k)} + t_{n^{(k)}} \underline{\phi}(\underline{x}_{n^{(k)}}) \text{ where } n_k \text{ is s.t. } \underline{x}_{n^{(k)}} \text{ is miss-classified.}
$$
We can easily translate this in an algorithm: we scan all the samples from $n=1$ to $n=N$ and we apply the update rule every time we encounter a miss-classified sample. After $n = N$, we restart with $n=1$ and we stop after a full scan with no miss-classified points.

Every step reduces the error due to the miss-classified pattern:
$$
- t_{n^{(k)}} \underline{\phi}^T(\underline{x}_{n^{(k)}}) \underline{w}^{(k+1)} = - t_{n^{(k)}} \underline{\phi}^T(\underline{x}_{n^{(k)}}) \underline{w}^{(k)} - ||t_{n^{(k)}} \underline{\phi}(\underline{x}_{n^{(k)}})||_2^2 \leq - t_{n^{(k)}} \underline{\phi}^T(\underline{x}_{n^{(k)}}) \underline{w}^{(k)}.
$$
**Remark**: this DOES not imply that the loss is reduced at each stage, we could increase the miss-classification error on another sample.

Observe that the reason why the update rule is heuristic is that, since $\mathcal{M}$ depends on $\underline{w}$, we are NOT in the right setting to apply SGD. Anyways we have convergence guarantees.

---

- **Perceptron COnvergence Theorem**: if the training data set is **linearly separable** in the feature space $\mathbf{\Phi}$, then the perceptron learning algorithm is guaranteed to find an **exact solution** in a **finite number of steps**.

> **Proof**: assuming that the dataset is linearly separable is equivalent to assuming that there exist $\underline{w}^* \in \mathbb{R}^M$, $\gamma > 0$ s.t. $t_n \underline{\phi}^T(\underline{x}_n) \underline{w}^* > \gamma$ for all $n \in \{ 1, \ldots, N \}$.
Furthermore, since the samples are limited in number, we can assume that there exists $R > 0$ s.t. $||\underline{\phi}(\underline{x}_n)||_2 \leq R$ for all $n \in \{ 1, \ldots, N \}$.
Now we're going to prove that, under this assumption, the number of times that we can apply the update rule is finite, hence, the algorithm will terminate.
$$
{\underline{w}^{(k+1)}}^T \underline{w}^* = {\underline{w}^{(k)}}^T \underline{w}^* + t_{n^{(k)}} \underline{\phi}^T(\underline{x}_{n^{(k)}}) \underline{w}^* > {\underline{w}^{(k)}}^T \underline{w}^* + \gamma.
$$
> Hence, by induction:
$$
\underline{w}^{(k)} > {\underline{w}^{(0)}}^T \underline{w}^* + k \gamma.
$$
> Furthermore: $||\underline{w}^{(k)}||_2 || \underline{w}^* ||_2 \geq {\underline{w}^{(k)}}^T \underline{w}^* > {\underline{w}^{(0)}}^T \underline{w}^* + k \gamma$ iff $|| \underline{w}^{(k)} ||_2 > \frac{{\underline{w}^{(0)}}^T \underline{w}^*}{|| \underline{w}^* ||_2} + k \frac{\gamma}{|| \underline{w}^* ||_2}$ (observe that it must be $||\underline{w}^*||_2 > 0$ by how we defined $\underline{w}^*$).

> To obtain an upper bound, we argue that:
$$
||\underline{w}^{(k+1)}||_2^2 = ||\underline{w}^{(k)}||_2^2 + 2 t_{n^{(k)}} \underline{\phi}^T(\underline{x}_{n^{(k)}}) \underline{w}^{(k)} + t_n^2 ||\underline{\phi}(\underline{x}_{n^{(k)}})||_2^2 \leq
$$
$$
\leq ||\underline{w}^{(k)}||_2^2 + t_n^2 ||\underline{\phi}(\underline{x}_{n^{(k)}})||_2^2 = ||\underline{w}^{(k)}||_2^2 + ||\underline{\phi}(\underline{x}_{n^{(k)}})||_2^2 \leq ||\underline{w}^{(k)}||_2^2 + R^2.
$$
> Hence, by induction: $||\underline{w}^{(k)}||_2^2 \leq ||\underline{w}^{(0)}||_2^2 + k R^2$.
> Finally:
$$
\frac{({\underline{w}^{(0)}}^T \underline{w}^*)^2}{|| \underline{w}^* ||_2^2} + k^2 \frac{\gamma^2}{|| \underline{w}^* ||_2^2} + 2 k \frac{{\underline{w}^{(0)}}^T \underline{w}^* \gamma}{|| \underline{w}^* ||_2^2}  \leq ||\underline{w}^{(k)}||_2^2 \leq ||\underline{w}^{(0)}||_2^2 + k R^2;
$$
> since $\frac{\gamma^2}{||\underline{w}^*||_2^2} > 0$, this puts an upper bound on the value of $k$ (the quadratic function eventually grows faster than the linear one).

## Logistic regression


