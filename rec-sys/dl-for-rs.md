---
marp: true
theme: summary
math: mathjax
---
# Deep Learning for Recommender Systems

<div class="author">

Cristiano Migali

</div>

## Autoencoders for recommendation

[_Check AN2DL summaries for a general introduction to autoencoders_].
The **input data** to the autoencoder is the full user profile $r_u$.
The **embedding** will be a <u>compressed representation of the user interests</u>, (hopefully) sufficient to reconstruct their interactions.
The **reconstructed input** contains the predictions of the model for <u>all items</u>, which we rank and use to decide what to recommend.
Thus, we have an **encoder** network $g_e$ which takes the user profile $r_u$ and produces the embedding $e_u = g_e(r_u)$. Then we apply a **decoder** network $\tilde{r}_u = g_d(e_u)$ to obtain the **predicted ratings**.
We can use **predicted ratings** to rank the items.

This is a form of collaborative filtering since the encoder architecture will be trained to create good embeddings for **any** user. Users with similar interactions will have similar embeddings.
Auto-encoders are **model-based**. If we have a new user or an existing user with additional interactions, we can provide their profile to the auto-encoder as-is.

Suppose that the autoencoder is implemented through shallow networks with no hidden layers both for encoding and decoding and the embedding has size $K$. Furthermore assume that the activations are linear and we have no biases. Then:
$$
e_u = f_i(r_u W_i + b_i) = r_u W_i
$$
and
$$
\tilde{r}_u = f_o(e_u W_o + b_o) = e_u W_o = r_u W_i W_o
$$
with $W_i \in \mathbb{R}^{|\mathcal{I}| \times K}$, $W_o \in \mathbb{R}^{K \times |\mathcal{I}|}$.
We can consider $W_i W_o$ as a **item-item similarity matrix**.
We can also force $W_o = W_i^T$, in this case we would get a **symmetric similarity matrix**. In particular, the first case corresponds to AsymmetricSVD, while the second corresponds to PureSVD.

### $\text{EASE}^R$

**$\text{EASE}^R$** stands for Embarrassingly Shallow Autoencoders for Sparse Data.
$\text{EASE}^R$ is an item-based similarity collaborative filtering model.

---

It is obtained by the following reasoning, we start with a constrained optimization problem to obtain the similarity matrix:
$$
\begin{matrix}
S^* = \arg \min_S \left[ || R - RS ||_F + \lambda || S ||_F \right] \\
\text{s.t. } \text{diag}(S) = 0
\end{matrix}.
$$

Then, we remove the constraint with **Lagrangian multipliers**:
$$
S^* = \arg \min_S \left[ || R - RS ||_F + \lambda || S ||_F + 2 \vec{\gamma} \odot \text{diag}(S) \right]
$$
where $\vec{\gamma} \in \mathbb{R}^{|\mathcal{I}|}$.

This new loss can be analytically optimized, be setting the gradient to 0.
Let's see how this is done step-by-step.
1. We set the derivative to zero to find the optimal $S$.
$$
S^*(\vec{\gamma}) = (R^T R + \lambda I_{|\mathcal{I}|})^{-1} (R^T R - \text{diagmat}(\vec{\gamma})).
$$
2. We find the multipliers that satisfy $\text{diag}(S(\vec{\gamma})) = 0$.
> In particular, let $P = (R^T R + \lambda I_{|\mathcal{I}|})^{-1}$, then:
$$
S^*(\vec{\gamma}) = P (P^{-1} - \lambda I_{|\mathcal{I}|} - \text{diagmat}(\vec{\gamma})) = I_{|\mathcal{I}|} - P (\lambda I_{\mathcal{I}} + \text{diagmat}(\vec{\gamma})).
$$
> Thus we can force $(\vec{\gamma} + \lambda \vec{1}) \odot \text{diag}(P) = \vec{1}$ iff $\vec{\gamma} = \vec{1} \oslash \text{diag}(P) - \lambda \vec{1}$.
3. The optimal $S$ is:
$$
S^* = ... .
$$

$\text{EASE}^R$ is fast and highly effective, but computing $R^T R$ and the inverse required for $P$ is <u>very memory intensive</u>.

Why does $\text{EASE}^R$ refer to autoencoders?
The loss function aims to minimize the Frobenious norm $R - RS$, hence a perfect solution would be an $S$ such that $R = RS$.
To quote the paper: "_This is done by reroducing the input as its output, as is typical for autoencoders_".

### Denoising autoencoders

One of the issues when training autoencoders is that the input space (the space of user profiles) is very sparse.

The **risks** are that:
- the encoder might create poor embeddings for new user profiles;
. the decoder may not know how to reconstruct correctly portions of the embedding space.

---

We can alleviate these problems through **denoising autoencoders**. The **idea** is to train the autoencoder to reconstruct the correct user profile from a noisy one.
For example we could use "salt & pepper noise" in which we randomly remove a certain portion of the positive interactions and randomly add a (very) small number of positive interactions.

### Variational autoencoders

**Variational autoencoders** encode the input as a <u>probability distribution</u> rather than a point (embedding).
In particular:
- the **encoder** encodes the input as mean and standard deviation of a Gaussian distribution;
- the **decoder** reconstructs the input from a sample of that probability distributions.

In formulas, the sampled embedding can be written as:
$$
\vec{e} = \vec{\mu} + \vec{\sigma} \odot \vec{\varepsilon}
$$
where $\vec{\varepsilon} \sim \mathcal{N}(0, 1)$.

This is called **reparametrization trick** and allows to move the sampling done by the decoder as part of the sampling in the SGD so that we can train the autoencoder.

## Two-Tower model

The idea of a **two-tower** architecture is to have two inputs:
- a _user_ input, and
- an _item_ input.

On each of these a "tower" of layers is applied up to a final embedding for the user and the item. The two are later combined to compute the prediction.

The user and item input can be of different types:
- one-hot encoding;
- full profiles;
- other non-structured data (like _text_, _images_, ...).

It is possible to combine multiple input types, e.g. the user input is the full profile, the input is a text document.

The two-tower model can use any loss function, because, as opposed to the autoencoder, its goal is NOT to reconstruct the input.

---

Consider a two-tower model with no hidden layers, embedding size $K$ and both user and item input one-hot encoded $x_u$, $x_i$. If $f = \text{id}$ and $b^\mathcal{U}, b^\mathcal{I} = 0$. Then:
$$
e_u = f^\mathcal{U}(x_u W^\mathcal{U} + b^\mathcal{U}) = x_u W^\mathcal{U} = W_u^\mathcal{U};
$$
$$
e_i = f^\mathcal{I}(x_i W^\mathcal{I} + b^\mathcal{I}) = x_i W^\mathcal{I} = W_i^\mathcal{I}.
$$
And thus the prediction is:
$$
\tilde{r}_{u,i} = e_u \cdot e_i = W_u^\mathcal{U} W_i^\mathcal{I}
$$
where $W_u^\mathcal{U}$ and $W_i^\mathcal{I}$ are user and item latent factors.

Observe that a **two tower model with one-hot encoded input is memory-based**. Thus, we cannot integrate new users or new interactions without retraining it.
**However**, the issue can be overcame if one uses other encodings, for example the entire user profile. In that case, the model becomes equivalent to AsymmetricSVD.
