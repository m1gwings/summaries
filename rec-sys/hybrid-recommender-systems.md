---
marp: true
theme: summary
math: mathjax
---
# Hybrid Recommender Systems

<div class="author">

Cristiano Migali

</div>

The **idea** behind hybrid RS is to combine different recommender systems into one. The result of such a combination is called Hybrid recommender system.

## Types of Hybrid RS

The are 5 **types of Hybrid Recommender Systems**:
1. **linear combination**;
2. **list combination**;
3. **pipelining**;
4. **merging models**;
5. **co-training**.

### Linear combination

In a hybrid recommender obtained by **linear combination**, we compute the predictions as a linear combination of the predictions of two different recommender systems:
$$
\tilde{r}_{u,i} = \alpha \tilde{r}_{u,i}^{(A)} + \beta \tilde{r}_{u,i}^{(B)}
$$
where $\tilde{r}_{u,i}^{(A)}$ is the prediction of the first recommender system, and $\tilde{r}_{u,i}^{(B)}$ is the prediction of the second. We usually choose $\beta = 1 - \alpha$.

The **advantage** of this method is that it is easy.

The **disadvantages** are that the optimal values of $\alpha$ and $\beta$ depend on the dataset and it works better when estimated ratings are on the same scale.

### List combination

**List combination** allows to combine two recommendations list produced by different systems into one.

One approach is to build the combined list through round robin.

The **advantage** of this method is that it is independent of the rating scale.

The **disadvantage** is that it is difficult to take into account which algorithm is better.

---

### Pipelining

In **pipelining** we combine two recommender systems in a sequential manner. In particular, we train the first recommender to produce the predicted ratings $\tilde{R}^{(A)}$ from the URM $R$. Then we train the second recommender on the ratings predicted by the first ($\tilde{R}^{(A)}$) to produce the actual recommendations $\tilde{R} = \tilde{R}^{(B)}$.

For example we can compute $\tilde{R}^{(A)}$ with a content based model, and then train a collaborative filtering algorithm on top of the results.
This allows to train the collaborative filtering algorithm on a denser URM.

The **advantages** are that:
- it increases the density of the URM;
- may add interactions for specific users and items;
- may leverage the prediction confidence.

The **disadvantages** are that:
- the training of the second system requires more time and more memory;
- there is an **high** risk of adding wrong predictions.

### Merging models

The **idea** behind merging models is, instead of combining the predictions of two models as it happens in _linear combination_ or _list combination_, we combine the models of the two algorithms, and use the _merged model_ to do predictions.
For example, if we use two algorithms that compute item-item similarity matrices, we could merge the two matrices into a new one. 
$$
S = \alpha S^{(A)} + (1-\alpha) S^{(B)}.
$$

The **advantages** are that:
- it is an easy method;
- there is no scalability loss.

The **disadvantage** is that only models using the same technique can be merged.

### Co-training

The **idea** behind **co-training** is to **train** two different models, sharing the same objective **simultaneously**.

---

#### Collaborative filtering with side information
##### SLIM with Side-information (S-SLIM)

In **S-SLIM** we learn an item-item similarity matrix to estimate the ICM. In particular, we want to solve:
$$
\arg \min_S || C - C S ||_F^2.
$$
At the same time, the item-item similarity matrix should be useful for predictions.
The final, optimization problem becomes:
$$
\arg \min_S \alpha || R - RS ||_F^2 + (1-\alpha) || C-CS ||_F^2.
$$
As usual, $\alpha$ is an hyper-parameter to be tuned.

We can optimize S-SLIM with any previous SLIM model we have developed, by stacking the two matrices:
$$
R' = \begin{bmatrix}
\alpha R \\
(1-\alpha) C^T
\end{bmatrix}.
$$
Stacking allows to obtain a new URM that you can use to train any other model based on item similarities.

**Important remark**: this method does NOT work for user-based similarity models.

## Hierarchical Hybrids

The **idea** behind **hierarchical hybrids** is to build a tree of hybrids, each using different methods.