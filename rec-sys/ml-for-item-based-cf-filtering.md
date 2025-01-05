---
marp: true
theme: summary
math: mathjax
---
# ML for item-based collaborative filtering

<div class="author">

Cristiano Migali

</div>

The core idea which allows to cast _item-based collaborative filtering_ as a ML problem is that, instead of using an _heuristic_ to compute the similarity matrix, we can **learn it from the data**.

In particular, to define a ML problem, we need to specify the **parameters we want to learn** (in this case the matrix $S$), and the differentiable **loss functions** $E$ to minimize.

## Loss functions

We have various options for our loss function.
Unfortunately, most of the metrics that we've seen so far are NOT differentiable and thus can't be optimized with standard iterative optimization algorithms.

### Sparse Linear Method for Top-$N$ RS (SLIM)

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

---

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
