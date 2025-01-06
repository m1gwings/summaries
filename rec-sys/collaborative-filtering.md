---
marp: true
theme: summary
math: mathjax
---
# Collaborative filtering

<div class="author">

Cristiano Migali

</div>

The **basic idea** of collaborative filtering methods is that the ratings a user has not given explicitly to the items, can be inferred, because the observed ratings are often highly correlated across various users and items.
Indeed, collaborative filtering techniques do NOT need item attributes to work, they rely on the opinions of a community of users.

The data required by collaborative filtering techniques is contained in the URM.

## User based collaborative filtering

The **idea** behind **user based collaborative filtering** is that we can compute the similarity between <u>two users</u> from their interactions in the URM, then use this similarity to infer unknown ratings.

### Implicit ratings

When implicit ratings are used, the entries of the URM take binary values, thus we can use the techniques we have seen in content-based filtering to compare items based on their binary attributes. In particular, let $\vec{r}_u = (r_{u,i})_{i \in \mathcal{I}}$ for all $u \in \mathcal{U}$ be the set of rows of the URM. We define the **cosine similarity** between two users $u, v \in \mathcal{U}$ as:
$$
s_{u,v} = \frac{\vec{r}_u \cdot \vec{r}_v}{||\vec{r}_u||_2 ||\vec{r}_v||_2 + t}
$$
where $t$ is a shrink term meant to add statistical significance.
We can store this information in a **similarity matrix** $S \in \mathbb{R}^{|\mathcal{U}| \times |\mathcal{U}|}$.

Once we have a similarity matrix, we can infer how user $u$ would rate item $i$ by taking a weighted average of the ratings of other users, weighted by their similarity. For the same reasons explained for content-based filtering, we consider only the $K$ most similar users ($u$ excluded):
$$
\tilde{r}_{u,i} = \frac{\sum_{v \in \text{KNN}(u)} r_{v,i} \cdot s_{v,u}}{\sum_{v \in \text{KNN}(u)} s_{v,u}}.
$$

#### In matrix notation

If we were to ignore the normalization factor $\frac{1}{\sum_{v \in \text{KNN}(u)} s_{v,u}}$, we could compute the predictions in matrix notation as:
$$
\tilde{R} = S R.
$$

---

### Explicit ratings

When the URM stores explicit ratings, cosine similarity does NOT work well. This is due to the fact that it doesn't take into account the **user bias**, i.e. the fact that some users give larger ratings than others, and the **item bias**, i.e. the fact that some items tend to attract larger ratings than others.

In particular, we defined the **user bias** of user $u$ as:
$$
\overline{r}_u = \frac{\sum_{i \in \mathcal{I}} r_{u,i}}{N_u + t}
$$
where $N_u$ is the number of non-zero ratings by user $u$ and $t$ is a shrink factor to add statistical significance.

Then, similarity can be computed through the **Pearson correlation coefficient**:
$$
s_{u,v} = \frac{(\vec{r}_u - \overline{r}_u) \cdot (\vec{r}_v - \overline{r}_v)}{|| \vec{r}_u - \overline{r}_u ||_2 || \vec{r}_v - \overline{r}_v ||_2 + t}
$$
where the subtractions like $\vec{r}_u - \overline{r}_u$ are to be intended with NumPy broadcasting notation.

Analogously, when we predict the ratings, we estimate a delta which represents how much the user likes an item more/less w.r.t. their average opinion by making a weighted average of the deltas of other users for that item. The weights are given by the similarity metric we just introduced. As always, we consider only the $K$ most similar users. The result is:
$$
\tilde{r}_{u,i} = \frac{\sum_{v \in \text{KNN}(u)}(r_{v,i} - \overline{r}_v) \cdot s_{v,u}}{\sum_{v \in \text{KNN}(u)} s_{v,u}}.
$$

## Item based collaborative filtering

The **idea** behind **item based collaborative filtering** is that we can compute the similarity between <u>two items</u> from their ratings inside the URM, then we can use this similarity metric to compute predictions as in content-based filtering.

### Implicit ratings

Analogously to what we did before, when the ratings in the URM are implicit, we can use cosine similarity. In particular, in this settings $\vec{i} = (r_{u,i})_{u \in \mathcal{U}}$ are the columns of the URM. Then, we can compute the similarity between two items as:
$$
s_{i,j} = \frac{\vec{i} \cdot \vec{j}}{||\vec{i}||_2 ||\vec{j}||_2 + t}.
$$

---

As usual, the predictions are computed as:
$$
\tilde{r}_{u,i} = \frac{\sum_{j \in \text{KNN}(i)} r_{u,j} s_{j,i}}{\sum_{j \in \text{KNN}(i)} s_{j,i}}.
$$

### Explicit ratings

When the ratings in the URM are explicit, we encounter the same problems we had in the case of item based collaborative filtering. Again we need to remove the biases. In particular, let $\vec{\overline{r}} = (\overline{r}_u)_{u \in \mathcal{U}}$. We define the **adjusted cosine similarity** between two items as:
$$
s_{i,j} = \frac{(\vec{i} - \vec{\overline{r}})\cdot(\vec{j} - \vec{\overline{r}})}{||\vec{i} - \vec{\overline{r}}||_2 ||\vec{j} - \vec{\overline{r}}||_2 + t}.
$$
Observe that _adjusted cosine_ is **different** w.r.t. _Pearson correlation_.

### Other ways to compute similarity

#### Association rules

**Association rules** are a technique used in the data mining field to extract from a relational dataset of transaction the conditional probability $p(i|j)$ that item $i$ is in a transaction knowing that item $j$ is in the same transaction.
We can exploit this technique in the recommender systems world by estimating the probability that a user will like item $i$ knowing that it likes item $j$.
The technique prescribe to predict the probability as follows:
$$
p(i|j) \approx \frac{|\{ u \in \mathcal{U} \ | \ u \text{ likes items } i \text{ and } j \}|}{|\{ u \in \mathcal{U} \ | \ u \text{ likes item } j \}|}.
$$
We can interpret this estimated conditional probability as a similarity measure $s_{i,j}$ that we can exploit as usual to make predictions.
Observe that this similarity metric is NOT symmetric.

### ML for item-based collaborative filtering

The core idea which allows to cast _item-based collaborative filtering_ as a ML problem is that, instead of using an _heuristic_ to compute the similarity matrix, we can **learn it from the data**.

In particular, to define a ML problem, we need to specify the **parameters we want to learn** (in this case the matrix $S$), and the differentiable **loss functions** $E$ to minimize.
We have various options for our loss function.
Unfortunately, most of the metrics that we've seen so far are NOT differentiable and thus can't be optimized with standard iterative optimization algorithms.

---

#### Sparse Linear Method for Top-$N$ RS (SLIM)

In the **SLIM** method we use the **Mean Square Error** (**MSE**) as a loss function. In particular, we compute the MSE w.r.t. the ground truth.
This loss function is differentiable and intuitive, unfortunately, as we remarked when talking about RS evaluation, if suffers from the MAR assumption.

In formulas, the loss function is defined as:
$$
E(S, R) = \sum_{(u, i) \in \mathcal{U} \times \mathcal{I} \ | \ r_{u,i} > 0} (r_{u,i} - \tilde{r}_{u,i}(R, S))^2
$$
where
$$
\tilde{r}_{u,i}(R, S) = \sum_{j \in \mathcal{I}} r_{u,j} \cdot s_{j,i}.
$$

Observe that, if we allowed $s_{i,j} = \delta_{i,j}$ we would get a minimizer of the above loss which is however completely useless since, in production, we can't assume that we already know the rating of user $u$ for item $i$. For this reason we force $s_{i,i} = 0 \ \forall i \in \mathcal{I}$.
Furthermore, as in usual Ridge regression, we add a penalization term on the squared entries of similarity matrix.
The result is:
$$
E(S, R) = \sum_{(u, i) \in \mathcal{U} \times \mathcal{I} \ | \ r_{u,i} > 0} \left(r_{u,i} - \sum_{j \in \mathcal{I} \ \{ i \} } r_{u,j} \cdot s_{j,i} \right)^2 + \lambda \sum_{i, j \in \mathcal{I}, i \neq j} s_{i,j}^2
$$
where $\lambda$ is an hyper-parameter which tunes the amount of regularization.

Sometimes we also add a penalization term on the absolute value of the entries, as is done in Lasso regression. When we use both regularizations, we get the so-called elastic net.
$$
E(S, R) = \sum_{(u, i) \in \mathcal{U} \times \mathcal{I} \ | \ r_{u,i} > 0} \left(r_{u,i} - \sum_{j \in \mathcal{I} \ \{ i \} } r_{u,j} \cdot s_{j,i} \right)^2 + \lambda_2 \sum_{i, j \in \mathcal{I}, i \neq j} s_{i,j}^2 + \lambda_1 \sum_{i, j \in \mathcal{I}, i \neq j} |s_{i,j}|.
$$

The minimization of the loss function happens through SGD.
1. We sample a data point $(u, i) \in \mathcal{U} \times \mathcal{I} \ | \ r_{u,i} > 0$.
2. We compute the gradient of the loss for the sampled data point.
In particular, let $s_i = (s_{j,i})_{j \in \mathcal{I}}$ be the $i$-th column of $S$, let $r_u = (r_{u,j})_{j \in \mathcal{I}}$ be the $u$-th row of the URM.
Then, the loss for the sampled data point is (we ignore the parameters not-used for the prediction even in the regularization):
$$
E_{u,i}(S, R) = (r_{u,i} - r_u \cdot s_i)^2 + \lambda_1 || s_i ||_1  + \lambda_2 || s_i ||_2^2.
$$

---

> Then:
$$
\frac{\partial E_{u,i}}{\partial s_i}(S, R) = -2(r_{u,i} - r_u \cdot s_i)r_u + \lambda_1 \text{sign}(s_i) + 2 \lambda_2 s_i.
$$

3. Finally we update the parameters by moving in the direction opposite to the gradient:
$$
s_i = s_i - l \cdot \frac{\partial E_{u,i}}{\partial s_i}(S, R)
$$
> where $l$ is known as learning rate.

This process has to be iterated.

---

## Matrix factorization

The **idea** behind matrix factorization methods is to estimate from the data a set of features $\mathcal{K}$, known as _latent features_, which are useful for recommendations. In particular, we can associate to each user $u$ a vector $\vec{x}_u = (x_{u,k})_{k \in \mathcal{K}}$ in which each entry represents how much user $u$ likes feature $k$. Analogously, we can associate to each item $i$ a vector $\vec{y}_i = (y_{i,k})_{k \in \mathcal{K}}$ in which each entry represents how much feature $k$ is important in item $i$.
Once we know these vectors, we can predict ratings simply as the scalar product between $\vec{x}_u$ and $\vec{y}_i$:
$$
\tilde{r}_{u,i} = \vec{x}_u \cdot \vec{y}_i.
$$

We can stack the vectors $\vec{x}_u$ in a matrix $X = (x_{u,k})_{u \in \mathcal{U}, k \in \mathcal{K}} \in \mathbb{R}^{|\mathcal{U}| \times |\mathcal{K}|}$, and the vectors $\vec{y}_i$ in a matrix $Y = (y_{i,k})_{k \in \mathcal{K}, i \in \mathcal{I}} \in \mathbb{R}^{|\mathcal{K}| \times |\mathcal{I}|}$. $X$ is known as **user-feature matrix**, while $Y$ is known as **feature-item matrix**.
Then:
$$
\tilde{R} = (\tilde{r}_{u,i})_{u \in \mathcal{U}, i \in \mathcal{I}} = X Y.
$$

The matrices $X, Y$ can be found using many different machine learning methods, by optimizing a loss function.
This matrix factorization model has $|\mathcal{K}| (|\mathcal{U}| + |\mathcal{I}|)$ parameters, typically much fewer than an item-based CF model. Furthermore, the number of parameters can be controlled by choosing $K = |\mathcal{K}|$, which is an hyper-parameter to be properly tuned.

If we choose $K$ big and we have few ratings there is a risk of overfitting.

Conversely, if $K$ is small the personalization capabilities are reduced. The system is biased towards popular items and, for $K = 1$, we get a behavior similar to the top-popular recommender.

As always, we usually add regularization terms to the loss function.

### Gradient descent for a MF model

As remarked before, we can find $X$ and $Y$ through the following optimization problem:
$$
X^*, Y^* = \arg \min_{X, Y} \left( || R - XY ||_2^2 + \lambda_x || X ||_2^2 + \lambda_y || Y ||_2^2 \right).
$$
$\lambda_x$ and $\lambda_y$ need to be tuned carefully, their value strongly impacts the effectiveness of the system. **Important**: the $|| \cdot ||_2$ is NOT the usual $2$-norm; it is the Frobenious norm in which we consider only relevant items.
If $\lambda_x$ and $\lambda_y$ are low, there is an high risk of overfitting. Conversely, if $\lambda_x$ and $\lambda_y$ are high, the matrices will be filled with zeroes.

Again, the minimization of the loss function happens through SGD.

1. We sample a data point $(u, i) \in \mathcal{U} \times \mathcal{I} \ | \ r_{u,i} > 0$.

---

2. We compute the gradient of the loss for the sampled point. Observe that the loss for the sampled data point can be expressed as:
$$
E_{u,i}(X, Y, R) = (r_{u,i} - \vec{x}_u \cdot \vec{y}_i)^2 + \lambda_x || \vec{x}_u ||_2^2 + \lambda_y || \vec{y}_i ||.
$$
> Then:
$$
\frac{\partial E}{\partial \vec{x}_u}(X, Y, R) = -2(r_{u,i} - \vec{x}_u \cdot \vec{y}_i) \vec{y}_i + 2 \lambda_x \vec{x}_u;
$$
$$
\frac{\partial E}{\partial \vec{y}_i}(X, Y, R) = -2(r_{u,i} - \vec{x}_u \cdot \vec{y}_i)\vec{x}_u + 2 \lambda_y \vec{y}_i.
$$
3. Finally, we update the parameters by moving in the direction opposite to the gradient:
$$
\vec{x}_u = \vec{x}_u - l \frac{\partial E}{\partial \vec{x}_u}(X, Y, R);
$$
$$
\vec{y}_i = \vec{y}_i - l \frac{\partial E}{\partial \vec{y}_i}(X, Y, R).
$$

Observe that, again, we're **relying on the MAR assumption**.

### Funk SVD

Another way to solve the optimization function we introduced before, i.e.
$$
X^*, Y^* = \arg \min_{X, Y} \left( || R - XY ||_2^2 + \lambda_x || X ||_2^2 + \lambda_y || Y ||_2^2 \right)
$$
is to use the **alternating least squares** technique.
It works as follows:
1. we initialize $X$ and $Y$ randomly;
2. we fix the value of $X$ and optimize for $Y$ (this becomes a least squares problem which can be solved analytically);
3. we fix the value of $Y$ and optimize for $X$;
4. we go back to 2 until we get to a point where the improvements are very small.

Furthermore, in **Funk SVD**, the latent factors <u>are NOT computed all at once</u>.
In particular:
1. we start with $K = 1$ and find the first vector in $X$ and $Y$ through alternating least squares;
2. we increase $K$ and optimize for the new vectors in $X$ and $Y$ through alternating least squares;
3. we go back to 2 until we reach the desired value for $K$.

---

Learning one latent factor at a time is efficient and reduces overfitting.

The cons of Funk SVD are that:
- it relies on the MAR assumption;
- it works well for rating prediction but poorly for Top-$N$;
- there are no latent factors for new users or new items: we need to retrain the model.

### SVD++

SVD++ changes the way in which we compute predictions. In particular, in SVD++ we take into account the item and user bias as in global effects:
$$
\tilde{r}_{u,i} = \mu + b_u + b_i + \vec{x}_u \cdot \vec{y}_i.
$$
**Important remark**: the values for $\mu$, $b_u$, and $b_i$ are learned as parameters.
Indeed, SVD++ solves the following optimization problem:
$$
\mu^*, b_u^*, b_i^*, X^*, Y^* = \arg \min_{\mu, b_u, b_i, X, Y} \left( ||R-\tilde{R}||_2^2 + \lambda_x ||X||_2^2 + \lambda_y ||Y||_2^2 \right).
$$

The model has $K (|\mathcal{U}| + |\mathcal{I}|) + |\mathcal{U}| + \mathcal{I} + 1$ parameters.
The optimization is done through SGD.

Observe that also SVD++ relies on the MAR assumption, this makes it unsuitable for Top-$N$.
Furthermore, SVD++ is still memory-based, thus we need to recompute $X$ and $Y$ for each new user and item.

### Asymmetric SVD

As we already remarked, in SVD++ and FunkSVD we <u>do NOT have latent factors for new users</u>. **Asymmetric SVD** solves the problem by introducing new item latent factors $Z \in \mathbb{R}^{|\mathcal{I}| \times |\mathcal{K}|}$ which can be used to estimate the user latent factors from the ratings that we've at out disposal:
$$
x_{u,k} = \vec{r}_u \cdot \vec{z}_k
$$
where $\vec{z}_k = (z_{i,k})_{i \in \mathcal{I}}$.
Observe that, to compute $x_{u,k}$, we just need the user profile; thus this method is model-based.

The predicted ratings matrix becomes:
$$
\tilde{R} = X Y = R Z Y.
$$
This model has $2 K |\mathcal{I}|$ parameters.

This method is called **asymmetric** because matrices $Z$ and $Y$ can be multiplied to obtain a similarity matrix that is likely NOT symmetric.

---

#### Asymmetric SVD with Global Effects

A variation of the method uses **learned global effects** in the predictions:
$$
\tilde{r}_{u,i} = \mu + b_u + b_i + \sum_{k \in \mathcal{K}} \sum_{j \in \mathcal{I}} r_{u,j} \cdot z_{j,k} \cdot y_{i,k}.
$$
This model has $2 K |\mathcal{I}| + |\mathcal{U}| + |\mathcal{I}| + 1$ parameters.

### PureSVD: Singular Value Decomposition

In **PureSVD** we apply the SVD decomposition to the URM, obtaining:
$$
R = U \Sigma V^T.
$$
The columns of $U$ correspond to latent features.
The rows of $V^T$ correspond to categories.

The SVD decomposition is truncated at rank $K$, in particular we select the $K$ highest singular values and the remaining ones are set to 0:
$$
R = U \Sigma V^T \approx U_K \Sigma_K V_K^T.
$$

In virtue of the **Eckart-Young-Mirsky theorem**, the approximation obtained through truncated SVD is the best rank $K$ approximation of the original matrix.

Using full-rank SVD doesn't allow to filter out the noise from the URM. This is instead done through truncated SVD.

Let $P = U \Sigma$, then, due to the orthonormality of $V$,
$$
R V = = U \Sigma V^T V = U \Sigma = P.
$$
Finally,
$$
R = U \Sigma V^T = P V^T = R V V^T = R S
$$
with $S = V V^T$. Thus PureSVD is equivalent to an item-based CF model where $S = V V^T$.

By using truncated SVD, PureSVD optimizes the Frobenious norm. The Frobenious norm accounts for all values of $R$, including the missing ratings which are treated as zeroes. Thus, **PureSVD relies on the Missing-as-Negative assumption**.

---

## Bayesian Personalized Ranking (BPR)

In this section, we will see **Bayesian Personalized Ranking**, which is another technique used to optimize the quality metrics of a recommender.

So far, we have focused our attention on optimizing the mean square error. But, from now on, we will focus on optimizing the so-called pairwise ranking.
In particular, our goal is to estimate the rating of user $u$ for items $i$ and $j$, where $i$ is relevant for user $u$ and $j$ is NOT, in such a way that the estimated rating for item $i$ is greater than the estimated rating for item $j$. In this way, the estimated pairwise ranking will be identical to the true pairwise ranking.
We can cast this into an optimization problem where we maximize the probability
$$
p(\tilde{r}_{u,i} > \tilde{r}_{u,j} | u) \text{ where } i \text{ is relevant, and } j \text{ is NOT.}
$$
Furthermore, we will <u>assume</u> that such probability takes the following functional form:
$$
p(\tilde{r}_{u,i} > \tilde{r}_{u,j} | u) = \sigma(x_{u,i,j})
$$
where $\sigma(x) = \frac{1}{1+\exp(-x)}$ is the sigmoid function, and $x_{u,i,j}$ is defined as $x_{u,i,j} = \tilde{r}_{u,i} - \tilde{r}_{u,j}$. Thus, we wish to maximize the difference.

The predicted ratings $\tilde{r}_{u,i}, \tilde{r}_{u,j}$ depend on the parameters of our model; we highlight this dependence as $\tilde{r}_{u,i}(\theta), \tilde{r}_{u,j}(\theta)$. Thus, the same holds for $x_{u,i,j}$ which becomes $x_{u,i,j}(\theta)$.

We assume the probabilities for each pair of items are independent (this assumption clearly doesn't hold in reality). Let $\mathcal{I}^+ = \{ i \in \mathcal{I} \ | \ r_{u,i} > 0 \}$, $\mathcal{I}^- = \mathcal{I} \setminus \mathcal{I}^+$. Then, the objective function becomes:
$$
\prod_{u \in \mathcal{U}, i \in \mathcal{I}^+, j \in \mathcal{I}^-} \sigma(x_{u,i,j}(\theta)).
$$
The optimization problem is:
$$
\theta^* = \arg \max_\theta \left[ \prod_{u \in \mathcal{U}, i \in \mathcal{I}^+, j \in \mathcal{I}^-} \sigma(x_{u,i,j}(\theta)) \right]
$$
$$
= \arg \max_\theta \left[ \sum_{u \in \mathcal{U}, i \in \mathcal{I}^+, j \in \mathcal{I}^-} \log \sigma(x_{u,i,j}(\theta)) \right]
$$
$$
= \arg \min_\theta \left[ - \sum_{u \in \mathcal{U}, i \in \mathcal{I}^+, j \in \mathcal{I}^-} \log \sigma(x_{u,i,j}(\theta)) \right].
$$

As usual, the final loss may include regularization terms:
$$
E(\theta) = - \sum_{u \in \mathcal{U}, i \in \mathcal{I}^+, j \in \mathcal{I}^-} \log \sigma(x_{u,i,j}(\theta)) + \lambda || \theta ||_2^2 + \ldots .
$$

---

As usual, we can optimize this loss through gradient descent.
In particular, remembering that $\sigma'(x) = \sigma(x)(1-\sigma(x))$:
$$
\frac{d E}{d \theta}(\theta) = - \sum_{u \in \mathcal{U}, i \in \mathcal{I}^+, j \in \mathcal{I}^-} \frac{1}{\sigma(x_{u,i,j}(\theta))} \frac{d}{d \theta}\left[ \sigma(x_{u,i,j}(\theta)) \right]
$$
$$
= - \sum_{u \in \mathcal{U}, i \in \mathcal{I}^+, j \in \mathcal{I}^-} \frac{1}{\sigma(x_{u,i,j}(\theta))} \sigma(x_{u,i,j}(\theta)) (1-\sigma(x_{u,i,j}(\theta)))\frac{d x_{u,i,j}}{d\theta}(\theta)
$$
$$
= - \sum_{u \in \mathcal{U}, i \in \mathcal{I}^+, j \in \mathcal{I}^-} (1-\sigma(x_{u,i,j}(\theta))) \frac{d x_{u,i,j}}{d\theta}(\theta).
$$

Of course, we still need to compute the gradient $\frac{d x_{u,i,j}}{d\theta}(\theta)$ based on the model we're training.

### BPR optimizes ranking

We define, analogously to what we did for precision and recall,
$$
\text{fallout}(n) = \frac{\text{FP}(n)}{\text{FP}(n) + \text{TN}(n)}.
$$
Then, analogously to what we did for the average precision, we can define the **Area Under the Curve** (**AUC**) as the area under the **ROC** which is the curve we obtain on the plain recall (on the $y$-axis) vs fallout (on the $x$-axis).

**It is possible to show that BPR minimizes the AUC**.

### BPR for SLIM

In **SLIM**,
$$
x_{u,i,j}(S) = \vec{r}_u \cdot \vec{s}_i - \vec{r}_u \cdot \vec{s}_j = \vec{r}_u \cdot (\vec{s}_i - \vec{s}_j).
$$
Then:
$$
\frac{\partial x_{u,i,j}}{\vec{s}_i}(S) = \vec{r}_u;
$$
$$
\frac{\partial x_{u,i,j}}{\vec{s}_j}(S) = -\vec{r}_u.
$$

**Important remark**: to be precise we use Stochastic Gradient Descent instead of plain Gradient Descent.

---

### BPR for Matrix Factorization

In **Matrix factorization** approaches:
$$
x_{u,i,j}(X, Y) = \vec{x}_u \cdot \vec{y}_i - \vec{x}_u \cdot \vec{y}_j = \vec{x}_u \cdot (\vec{y}_i - \vec{y}_j).
$$
Then:
$$
\frac{\partial x_{u,i,j}}{\partial \vec{x}_u}(X, Y) = \vec{y}_i - \vec{y}_j;
$$
$$
\frac{\partial x_{u,i,j}}{\partial \vec{y}_i}(X, Y) = \vec{x}_u;
$$
$$
\frac{\partial x_{u,i,j}}{\partial \vec{y}_j}(X, Y) = - \vec{x}_u.
$$

### BPR variants

Several variants and evolutions of BPR exist, for example **WARP** (Weighted Approximate-Rank Pairwise) loss.
The **idea behind WARP** is that, when sampling $u, i, j$, we check if the mode predictions would already produce the right ranking, if so, we draw another $j$. In particular, we look for training samples that <u>violate</u> the correct ranking.

### BPR popularity bias

**BPR exhibits a <u>very strong</u> popularity bias**:
- popular items will be sampled a lot, their predictions will tend to be high;
- unpopular items will be sampled rarely, their predictions will tend to be low.

Offline evaluation often uses test data splits that exhibit popularity bias (the same of the training data). BPR may look good offline but perform poorly online.
