---
marp: true
theme: summary
math: mathjax
---
# Model based methods vs Memory based methods

<div class="author">

Cristiano Migali

</div>

In this section, we will make a comparison between two types of techniques that are commonly used in collaborative filtering: **model-based methods** and **memory-based methods**.

In **memory-based techniques**, ratings are predicted on the basis of user neighborhoods.
On the contrary, **model-based techniques** do NOT rely on the dataset when recommendations are computed.

Consider the notation we introduced when highlighting the difference between algorithm and model.
A usual recommender system can be represented at an high level as a two steps process.
- In the first step we build a model $\mathcal{M}$ by applying an algorithm $f$ to the required dataset:
$$
\mathcal{M} = \begin{cases}
f(R) \text{ if we're doing collaborative filtering} \\
f(C) \text{ if we're doing content-based filtering instead}
\end{cases}.
$$

- In the second step, we use a recommendation routine $g$ to produce the recommendations for user $u$ from its profile $r_u$ and the model $\mathcal{M}$:
$$
\tilde{r}_u = g(\mathcal{M}, r_u).
$$

It is **in this second step** that we can appreciate the difference between content based and memory based methods.
Memory based methods require the user profile $r_u$ to be part of the dataset (the URM) from which they extracted the model. While model based method can handle user profiles that they haven't seen in the dataset.

Memory based methods are easier to develop but what happens if we have a new user in the system? In case of memory-based techniques, we need to add the new user to the URM, and recompute the similarity between the new user and all the other users. This operation is computational heavy. Therefore, we can make recommendations only to users present in the model.
In case of model-based techniques, we don't need to add the user to the URM, and, therefore, we can make recommendations even to users that are NOT in the model without having to recompute the similarity matrix.

---

## Examples

Let's try to apply these concepts to collaborative filtering techniques. In this case, the model $\mathcal{M}$ is computed from the URM $R$.
In particular, for item based collaborative filtering, the model is the similarity matrix among items $S_{\mathcal{I},\mathcal{I}} = f(R)$.
Then, given a user profile $\vec{r}_u$, we can make predictions:
$$
\tilde{r}_{u,i} = \frac{\sum_{j \in \text{KNN}(i)} r_{u,j} \cdot s_{j,i}}{\sum_{j \in \text{KNN}(i)} s_{j,i}}.
$$
Observe that the profile $\vec{r}_u$ doesn't need to be in the URM used to compute $S_{\mathcal{I}, \mathcal{I}}$, therefore **item-based collaborative filtering** is a **model-based technique**.

In the user based case instead, the model is the similarity matrix among users $S_{\mathcal{U}, \mathcal{U}} = f(R)$. Then, given a user profile, we can make predictions:
$$
\tilde{r}_{u,i} = \frac{\sum_{v \in \text{KNN}(u)} r_{v,i} \cdot s_{v,u}}{\sum_{v \in \text{KNN}(u)} s_{v,u}}.
$$
In this case, the similarity $s_{v,u}$ is defined only for $u, v$ in the URM, thus, **user-based collaborative filtering** is a **memory-based technique**.
