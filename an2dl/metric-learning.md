---
marp: true
theme: summary
math: mathjax
---
# Metric learning

<div class="author">

Cristiano Migali

</div>

- **Metric learning** is the task of training a network to learn a distance function defined over an input space $\mathcal{X}$ to capture a desired semantic in the comparison of objects.

A particular case is the one in which we have a dataset telling if two objects belong to the same class or NOT and we want to build a distance which is small between elements of the same class and big among elements of different classes.
This can be done by training a **siamese networks** model, in which we map the two objects to the latent space through two networks with the same topology and weights (siamese networks) and then compute the $L^2$ distance in the latent space.

We can use two possible loss functions to train the networks.

The **contrastive loss** function is defined as:
$$
\mathcal{L}_w(I_i, I_j, y_{i,j}) = \frac{1-y_{i,j}}{2} || f_w(I_i) - f_w(I_j) ||_2 + \frac{y_{i,j}}{2} \max\left(0, m-||f_w(I_i) - f_w(I_j)||_2 \right)
$$
where:
- $y_{i,j} \in \{ 0, 1 \}$ is the label associated to the input pair $(I_i, I_j)$ (0 when $(I_i, I_j)$ refer to the same class, 1 otherwise);
- $m$ is an hyper-parameter indicating the margin we want (like in hinge loss).

The **triplet loss** function is defined as:
$$
\mathcal{L}_w(I, P, N) = \max[0, m + (|| f_w(I) - f_w(P) ||_2 - || f_w(I) - f_w(N) ||_2)]
$$
where $I$ is a training sample which is compared against a positive input $P$, belonging to the same class, and a negative input $N$, belonging to a different class.
Again $m$ plays the role of the margin.
Triplet loss forces that a pair of samples from the same individual are smaller in distance than those with different ones.
