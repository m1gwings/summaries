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

**Logistic regression** is a probabilistic <u>discriminative</u> approach for linear classification. Before diving in the actual method, let's try to understand where does the shape of the conditional density $p(C_k | \underline{x})$ used in this method come from.
Let's start our analysis from the binary classification case $K = 2$.
Consider the following data generating mechanism:
$$
p(\underline{x} | C_i) = \mathcal{N}(\underline{x} | \underline{\mu}_i, \Sigma) \text{ for } i \in \{ 1, 2 \}.
$$

---

That is, the inputs for each class are generated according to a Gaussian distribution with mean $\underline{\mu}_i$. The variance **is the same for all classes** and corresponds to $\Sigma$.

Thanks to Bayes theorem and marginalization, we can write:
$$
p(C_i | \underline{x}) = \frac{p(\underline{x} | C_i) p(C_i)}{p(\underline{x})} = \frac{p(\underline{x}|C_i) p(C_i)}{p(\underline{x}|C_1)p(C_1)+p(\underline{x}|C_2)p(C_2)} \text{ for } i \in \{ 1, 2 \}.
$$
For reasons that will be come evident in a moment, we can rewrite:
$$
p(C_i | \underline{x}) = \sigma\left(\ln \frac{p(\underline{x}|C_i) p(C_i)}{p(\underline{x}|C_{j(i)})p(C_{j(i)})}\right)
$$
where:
$$
\sigma(x) = \frac{1}{1+e^{-x}} \text{, and } j(i) = \begin{cases} 2 \text{ if } i = 1 \\ 1 \text{ if } i = 2 \end{cases}.
$$
The function $\sigma(x)$ is known as **logistic sigmoid** function. It has many interesting properties:
- $\sigma(-x) = 1 - \sigma(x)$;
- $\sigma'(x) = \sigma(x)(1-\sigma(x))$;
- $\sigma(x) \in (0, 1)$ for all $x \in \mathbb{R}$.

Now observe that, because of our assumptions on the class-conditional densities (_remember that that the two Gaussian distribution are assumed to have the same variance, hence the multiplicative coefficients in front of the exponential simplify_):
$$
\ln \frac{p(\underline{x}|C_i) p(C_i)}{p(\underline{x}|C_{j(i)})p(C_{j(i)})} = \ln\frac{p(\underline{x}|C_i)}{p(\underline{x}|C_{j(i)})} + \ln\frac{p(C_i)}{p(C_{j(i)})} =
$$

$$
= - \frac{1}{2} (\underline{x} - \underline{\mu}_i)^T \Sigma^{-1} (\underline{x} - \underline{\mu}_i) + \frac{1}{2} (\underline{x} - \underline{\mu}_{j(i)}) \Sigma^{-1} (\underline{x} - \underline{\mu}_{j(i)}) + \ln\frac{p(C_i)}{p(C_{j(i)})} =
$$
$$
= (\underline{\mu}_i - \underline{\mu}_{j(i)})^T \Sigma^{-1} \underline{x} - \frac{1}{2} \underline{\mu}_i^T \Sigma^{-1} \underline{\mu}_i + \frac{1}{2} \underline{\mu}_2^T \Sigma^{-1} \underline{\mu}_2 + \ln\frac{p(C_i)}{p(C_{j(i)})} = \underline{w}_i^T \underline{x} + w_{i,0}
$$
where $\underline{w}_i = \Sigma^{-1} (\underline{\mu}_i - \underline{\mu}_{j(i)})$, and $w_{i,0} = - \frac{1}{2} \underline{\mu}_i^T \Sigma^{-1} \underline{\mu}_i + \frac{1}{2} \underline{\mu}_2^T \Sigma^{-1} \underline{\mu}_2 + \ln\frac{p(C_i)}{p(C_{j(i)})}$.
That is, we have written:
$$
p(C_i | \underline{x}) = \sigma(\underline{w}_i^T \underline{x} + w_{i,0}).
$$

Now, let's try to generalize this reasoning to $K$ classes:
$$
p(C_i | \underline{x}) = \frac{p(\underline{x} | C_i) p(C_i)}{\sum_{j=1}^K p(\underline{x}|C_j) p(C_j)} = \frac{ \exp\{-\frac{1}{2} (\underline{x} - \underline{\mu}_i)^T \Sigma^{-1} (\underline{x} - \underline{\mu}_i)\} p(C_i)}{\sum_{j=1}^K \exp\{-\frac{1}{2} (\underline{x} - \underline{\mu}_j)^T \Sigma^{-1} (\underline{x} - \underline{\mu}_j)\} p(C_j)} =
$$

---

$$
= \frac{\exp\{-\frac{1}{2} \underline{x}^T \Sigma^{-1} \underline{x}\} \exp\{ \underline{\mu}_i^T \Sigma^{-1} \underline{x} -\frac{1}{2} \underline{\mu}_i^T \Sigma^{-1} \underline{\mu}_i \} p(C_i)}{\sum_{j=1}^K \exp\{-\frac{1}{2} \underline{x}^T \Sigma^{-1} \underline{x}\} \exp\{ \underline{\mu}_j^T \Sigma^{-1} \underline{x} -\frac{1}{2} \underline{\mu}_j^T \Sigma^{-1} \underline{\mu}_j \} p(C_j)} =
$$
$$
= \frac{\exp\{ \underline{\mu}_i^T \Sigma^{-1} \underline{x} -\frac{1}{2} \underline{\mu}_i^T \Sigma^{-1} \underline{\mu}_i \} p(C_i)}{\sum_{j=1}^K \exp\{ \underline{\mu}_j^T \Sigma^{-1} \underline{x} -\frac{1}{2} \underline{\mu}_j^T \Sigma^{-1} \underline{\mu}_j \} p(C_j)} = \frac{e^{a_i}}{\sum_{j=1}^K e^{a_j}}
$$

where $a_k = \underline{w}_k^T \underline{x} + w_{k,0}$, $\underline{w}_k = \Sigma^{-1} \underline{\mu}_k$, and $w_{k,0} = -\frac{1}{2} \underline{\mu}_k^T \Sigma^{-1} \underline{\mu}_k + \ln p(C_k)$ for $k \in \{ 1, \ldots, K \}$.
The function:
$$
\underline{s}\left(\begin{bmatrix} x_1 \\ \vdots \\ x_n \end{bmatrix}\right) = \frac{1}{\sum_{i=1}^n e^{x_i}} \begin{bmatrix} e^{x_1} \\ \vdots \\ e^{x_n} \end{bmatrix}
$$
is known as **softmax function**. Indeed, if $x_i >> x_j$ for all $j \neq i$, then $\underline{s}(\underline{x}) \approx \underline{e}_i$.

Now we're ready to tackle logistic regression. Again let's start from the two class problem. We assume (_we just explained why_) that the posterior probability of class $C_1$ can be written as a **logistic sigmoid function**:
$$
p(C_1 | \underline{\phi}) = \sigma(\underline{w}^T \underline{\phi})
$$
(_the bias term is embedded in $\underline{\phi}$_). By the laws of probability: $p(C_2|\underline{\phi}) = 1 - p(C_1|\underline{\phi})$.
Let $\mathcal{D} = \{ (\underline{x}_1, t_1 ), \ldots, (\underline{x}_N, t_N) \}$ be our dataset of independent samples. Note that $t|\underline{x} \sim Be(p(C_1|\underline{\phi}))$. Then, the likelihood of the observed data, is:
$$
p(\underline{t}|\mathbf{X}, \underline{w}) = \prod_{n=1}^N p(C_1 | \underline{\phi}_n)^{t_n} (1-p(C_1 | \underline{\phi}_n))^{1-t_n}.
$$
Taking the negative log of the likelihood, we get the so-called **cross-entropy error function**:
$$
L(\underline{w}) = -\sum_{n=1}^{N}[ t_n \ln p(C_1 | \underline{\phi}_n) + (1-t_n) \ln (1-p(C_1 | \underline{\phi}_n ))].
$$
As in every Maximum Likelihood approach, we want to find the parameters which maximize the likelihood of the observed data, which is equivalent to minimize $L(\underline{w})$.
Let's add some notation to make it easier to differentiate $L(\underline{w})$:
$$
L(\underline{w}) = - \sum_{n=1}^N [t_n \ln y_n + (1-t_n)\ln(1-y_n)] = \sum_{n=1}^N L_n
$$

---

where $y_n = p(C_1|\underline{\phi}_n)$, and $L_n = -[t_n \ln y_n + (1-t_n)\ln(1-y_n)]$.
Now:
$$
\frac{\partial L_n}{\partial y_n}(y_n) =  -\frac{t_n}{y_n} + \frac{1-t_n}{1-y_n} = \frac{y_n - t_n}{y_n(1-y_n)}.
$$
$$
\frac{\partial y_n}{\partial \underline{w}} = \frac{\partial}{\partial \underline{w}}\left[ \sigma(\underline{w}^T \underline{\phi}_n) \right] = \sigma'(\underline{w}^T \underline{\phi}_n) \underline{\phi}_n^T = \sigma(\underline{w}^T \underline{\phi}_n) (1 - \sigma(\underline{w}^T \underline{\phi}_n)) \underline{\phi}_n^T = y_n(1-y_n) \underline{\phi}_n^T.
$$
Then:
$$
\frac{\partial L_n}{\partial \underline{w}}(\underline{w}) = (y_n-t_n) \underline{\phi}_n^T.
$$
Hence:
$$
\nabla_{\underline{w}} L_n(\underline{w}) = (y_n - t_n) \underline{\phi}_n,
$$
and so:
$$
\nabla_{\underline{w}} L(\underline{w}) = \sum_{n=1}^N (y_n - t_n) \underline{\phi}_n.
$$
_Observe that this has the same form of the gradient of the **sum-of-squares error function** for linear regression, see Linear Regression, p. 5_.

Furthermore:
$$
\nabla_{\underline{w} \underline{w}}^2 L(\underline{w}) = \frac{\partial}{\partial \underline{w}} \nabla_{\underline{w}} L(\underline{w}) =  \sum_{n=1}^N \underline{\phi}_n \frac{\partial y_n}{\partial \underline{w}} = \sum_{n=1}^N y_n (1-y_n) \underline{\phi}_n \underline{\phi}_n^T
$$
is a conic combination of positive semi-definite matrices (remember that $y_n \in (0, 1)$) for every value of $\underline{w}$, hence, because of the second order sufficient condition (_see Non-Linear Optimization_), it is convex. Because of the nonlinearity in the expression of $y_n$, we can't solve $\nabla_{\underline{w}} L(\underline{w}) = \underline{0}_M$, anyway we can find the global minimum through gradient descent since the problem is convex (_see Non-Linear Optimization_).

Now let's tackle **multi-class logistic regression**. In this case we represent the class posteriors by a **softmax** transformation:
$$
p(C_k | \underline{\phi}) = \frac{\exp(\underline{w}_k^T \underline{\phi})}{\sum_{j=1}^K \exp(\underline{w}_j^T \underline{\phi})}.
$$

**Remark**: for the softmax function it holds that:
$$
\frac{\partial s_k}{\partial x_j}(\underline{x}) = s_k(\underline{x}) \delta_{kj} - s_k(\underline{x}) s_j(\underline{x}).
$$

---

Again, we can express the likelihood of the observed data (_assuming that we used one-hot encoding for the targets_):
$$
p(\mathbf{T}|\mathbf{X}, \underline{w}_1, \ldots, \underline{w}_K) = \prod_{n=1}^N \left( \prod_{k=1}^K p(C_k | \underline{\phi}_n)^{t_{n,k}} \right) = \prod_{n=1}^N \left( \prod_{k=1}^K y_{n,k}^{t_{n,k}} \right)
$$
where $y_{n,k} = p(C_k | \underline{\phi}_n)$.
Taking the negative logarithm of the likelihood gives the **cross-entropy function** for multi-class classification problems:
$$
L(\underline{w}_1, \ldots, \underline{w}_K) = - \ln p(\mathbf{T}|\mathbf{X},\underline{w}_1, \ldots, \underline{w}_K) = - \sum_{n=1}^N \left(\sum_{k=1}^K t_{n,k} \ln y_{n,k} \right).
$$

Observe that:
$$
\frac{\partial y_{n,k}}{\partial \underline{w}_j}(\underline{w}_1, \ldots, \underline{w}_k) = \frac{\partial}{\partial \underline{w}_j} s_k(W^T \underline{\phi}_n) = \begin{bmatrix} \frac{\partial s_k}{\partial x_1}(W^T \underline{\phi}_n) & \cdots & \frac{\partial s_k}{\partial x_K}(W^T \underline{\phi}_n) \end{bmatrix} \begin{bmatrix} \frac{\partial}{\partial \underline{w}_j}\underline{w}_1^T \underline{\phi}_n \\ \vdots \\ \frac{\partial}{\partial \underline{w}_j}\underline{w}_K^T \underline{\phi}_n \end{bmatrix} =
$$
$$
= \underline{0}_M^T + \ldots + \underline{0}_M^T + [s_k(W^T \underline{\phi}_n) \delta_{kj} - s_k(W^T \underline{\phi}_n) s_j(W^T \underline{\phi}_n)] \underline{\phi}^T_n + \underline{0}_M^T + \ldots + \underline{0}_M^T =
$$
$$
= y_{n,k}(\delta_{kj} - y_{n,j}) \underline{\phi}_n^T.
$$

Hence:
$$
\frac{\partial L}{\partial \underline{w}_j}(\underline{w}_1, \ldots, \underline{w}_K) = - \sum_{n=1}^N \left( \sum_{k=1}^K \frac{t_{n,k}}{y_{n,k}} y_{n,k} (\delta_{kj} - y_{n,j}) \underline{\phi}_n^T \right) = - \sum_{n=1}^N \left( \sum_{k=1}^K t_{n,k} (\delta_{kj} - y_{n,j}) \underline{\phi}_n^T \right) =
$$
$$
= -\sum_{n=1}^N \left[ \sum_{k=1}^K t_{n,k} \delta_{kj} - y_{n,j} \sum_{k=1}^K t_{n,k} \right] \underline{\phi}_n^T = - \sum_{n=1}^N \left[ t_{n,j} - y_{n,j} \cdot 1 \right] \underline{\phi}_n^T = \sum_{n=1}^N (y_{n,j} - t_{n,j}) \underline{\phi}_n^T.
$$

That is:
$$
\nabla_{\underline{w}_j} L(\underline{w}_1, \ldots, \underline{w}_K) = \sum_{n=1}^N (y_{n,j} - t_{n,j}) \underline{\phi}_n.
$$

### Connection between Logistic Regression and Perceptron

Observe that, if we were to optimize the Logistic Regression loss function with a SGD approach, then the update rule would be analogous to that of the perceptron:
$$
\underline{w}^{(k+1)} = \underline{w}^{(k)} - \alpha (y(\underline{x}_n, \underline{w}) - t_n) \underline{\phi}_n.
$$

In particular, for the perceptron $t_n \in \{ -1, 1 \}$, $y(\underline{x}_n, \underline{w}) = \text{sign}(\underline{w}^T \underline{\phi}_n)$, $\alpha = 1$.
