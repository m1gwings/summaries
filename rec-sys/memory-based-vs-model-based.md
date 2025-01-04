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
On the contrary, **model-based techniques** do NOT rely on the whole dataset when recommendations are computed.

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

Memory based methods are easier to develop but they are NOT able to provide personalized recommendations for new users until we retrain them.

---

## Examples

Let's try to apply these concepts to collaborative filtering techniques. In this case, the model $\mathcal{M}$ is computed from the URM $R$.
In particular, for item based collaborative filtering, the model is the similarity matrix among items $S_{\mathcal{I},\mathcal{I}} = f(R)$. In the user based case instead, the model is the similarity matrix among users $S_{\mathcal{U}, \mathcal{U}} = f(R)$.
