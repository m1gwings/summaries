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
