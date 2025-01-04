---
marp: true
theme: summary
math: mathjax
---
# Algorithm vs Model

<div class="author">

Cristiano Migali

</div>

- The **algorithm** is the process or set of rules to be followed in calculations or other problem-solving operations.

- The **model** is the final product resulting from the application of an algorithm to a dataset.

The relationship between the two is the following: the **algorithm** provides the steps needed to train a model; the **model** contains a compressed representation of the dataset and can be used to make predictions.

Let:
- $\mathcal{D}$ be the input dataset;
- $f$ be an algorithm for model training;
- $\mathcal{M}$ be the resulting model;
- $r_u$ be the user profile of a user $u \in \mathcal{U}$;
- $g$ be the routine encharged of serving recommendations;
- $\tilde{r}_u$ the predicted user profile (which is equivalent to providing recommendations).

The relationships between these components are the following:
$$
\mathcal{M} = f(\mathcal{D});
$$
$$
\tilde{r}_u = g(\mathcal{M}, r_u).
$$

For **example**, in the _global effects_ algorithm:
- $\mathcal{D} = R$;
- $f$ is **how to compute** $\mu, b_i, b_u$;
- $\mathcal{M} = (\mu, b_i, b_u)$;
- $g$ is $\tilde{r}_{u,i} = \mu + b_i + b_u$ ($r_u$ is NOT needed).
