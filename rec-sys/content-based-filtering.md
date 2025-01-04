---
marp: true
theme: summary
math: mathjax
---
# Content based filtering

<div class="author">

Cristiano Migali

</div>

The **idea** behind **content based filtering** is to compare items based on their attributes; then we can recommend to a user $u$ the items which are similar to those with which they have already positively interacted.
The rationale is that a user that expressed a preference for an item is likely to enjoy similar items.

Content based filtering relies on the **data in the ICM**.
In articular, we represent the entries of the ICM as:
$$
C_{i,a} = \begin{cases}
1 \text{ if item } i \text{ has attribute } a \\
0 \text{ otherwise}
\end{cases}.
$$

## Measuring similarity

In this section we will list the possible options to asses similarity between two items.

### Dot product

The most intuitive way to measure the similarity of two items is to count the number of attributes that they have in common. In particular, given two items $i, j \in \mathcal{I}$ represented as rows of the ICM: $\vec{i} = (C_{i,a})_{a \in \mathcal{A}}$, $\vec(j) = (C_{j,a})_{a \in \mathcal{A}}$, this is equivalent to taking their **dot product**:
$$
s_{i,j} = \vec{i} \cdot \vec{j} = \sum_{a \in \mathcal{A}} C_{i,a} C_{j,a}.
$$

### Cosine similarity

The dot product is unbounded. By normalizing it between -1 and +1, we get **cosine similarity**:
$$
s_{i,j} = \frac{\sum_{a \in \mathcal{A}} C_{i,a} C_{j,a}}{\sqrt{\left(\sum_{a \in \mathcal{A}} C_{i,a}^2\right)\left(\sum_{a \in \mathcal{A}} C_{j,a}^2\right)}} = \cos(\theta)
$$
where $\theta$ is the angle between the two vectors.

#### Similarity support

The statistical significance of the cosine similarity depends on the number of attributes of the items we're comparing. If they have few attributes, they could have a large portion of attributes in common by chance.

---

For this reason we add a **shrink term** $t$ to the cosine similarity expression:
$$
s_{i,j} = \frac{\vec{i} \cdot \vec{j}}{||\vec{i}||_2 ||\vec{j}||_2 + t}.
$$

## Similarity matrix

The similarity between all items is stored in a similarity matrix $S \in \mathbb{R}^{|\mathcal{I}| \times |\mathcal{I}|}$.
The diagonal of this matrix should be ignored since the similarity of an item with itself is NOT informative.

## Predicting ratings

We can use similarity between items to **predict the rating** that a user $u$ would give to an item $i$ by making a **weighted average** of known ratings $r_{u,j}$ scaled by the similarity between $i$ and $j$:
$$
\tilde{r}_{u,i} = \frac{\sum_{j \in \mathcal{I}} r_{u,j} \cdot s_{j,i}}{\sum_{j \in \mathcal{I}} s_{j,i}}.
$$

If we just need top-$N$ recommendations, we can simply sort the items from the one with the highest predicted rating to that we the lowest predicted rating. In this setting we usually do NOT normalize the prediction:
$$
\tilde{r}_{u,i} = \sum_{j \in \mathcal{I}} r_{u,j} \cdot s_{j,i}.
$$

### In matrix notation

Content based filtering can be expressed in matrix notation.
Let $\vec{n} = (\sqrt{\sum_{a \in \mathcal{A}} C_{i,a}^2})_{i \in \mathcal{I}}$. Let $C = (C_{i,a})_{i \in \mathcal{I}, a \in \mathcal{A}}$ be the ICM. Then:
$$
S = \frac{C C^T}{\vec{n} \otimes \vec{n} + t}
$$
where we use NumPy broadcasting in the sum $\vec{n} \otimes \vec{n} + t$ and the division is element-wise.

Then, letting $\tilde{R} = (\tilde{r}_{u,i})_{u \in \mathcal{U}, i \in \mathcal{I}}$, if $\tilde{r}_{u,i} = \sum_{j \in \mathcal{I}} r_{u,j} \cdot s_{j,i}$, we have:
$$
\tilde{R} = R S
$$

### $K$-nearest neighbors

Using the whole similarity matrix to compute predictions as we just described has two problems:

---

- first of all the matrix is **dense**, and thus computing the products is computationally heavy;
- furthermore **small similarity values are often very noisy**, thus reducing the quality of the recommendations.

The solution is to use only the $K$ most similar items to do predictions. In particular, let $\text{KNN}(i) \subset \mathcal{I}$ be the set of the $K$ items most similar to $i$ ($i$ excluded).
Then the predictions are computed as:
$$
\tilde{r}_{u,i} = \frac{\sum_{j \in \text{KNN}(i)} r_{u,j} \cdot s_{j,i} }{\sum_{j \in \text{KNN}(i)} s_{j,i}}.
$$

The hyper-parameter $K$ influences the quality of the recommendations. If it is too small, there is not enough data for estimation; if it is too big, then there could be too much noise in the data.

## Improving the ICM

Up to now we've considered always an ICM with binary attributes.
In this setting all the attributes have the same importance to determine the similarity, but this assumption is NOT true in general. We can improve the ICM by putting entries different from 0 and 1, according to the importance of the corresponding attribute.

### Term Frequency - Inverse Document Frequency (TF-IDF)

- **TF-IDF** is a technique to automatically adjust the weight of each attribute depending on its frequency.

The rationale is that the presence of a very frequent attribute is less informative than the presence of a more rare one.

- We define **term frequency**:
$$
\text{TF}_{a,i} = \frac{N_{a,i}}{N_i}
$$
> where $N_{a,i}$ is the number of appearances of attribute $a$ in $i$ (this is often 1), while $N_i$ is the number of attributes of item $i$.

- We define **inverse document frequency**:
$$
\text{IDF}_a = \log \left( \frac{N_\text{items}}{N_a} \right)
$$
> where $N_\text{items}$ is the total number of items and $N_a$ is the number of items with attribute $a$.

Finally, we set $C_{i,a} = \text{TF}_{a,i} \cdot \text{IDF}_a$.

---

The consequence of this choice is that:
- if an item has many attributes, the weight of the single attribute is small;
- if an attribute is present in most of the items, the informative value of that attribute is close to 0.
