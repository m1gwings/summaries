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

- **$K$-linear classifiers**: we can ise $K$ linear discriminant functions of the form:
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
