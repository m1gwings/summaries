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

## Graph Convolutional Networks

The **idea** of Graph Convolutional Networks (GNN) is to learn user and item embeddings by leveraging the graph structure of the interaction data.

We could say that they merge latent factor models and graph-based ones.

We work with the usual bi-partite (or tri-partite) graph, but each user and item is associated with an embedding, denoted respectively with $e_u$ and $e_i$.

The **assumption** is that nodes that are close in the graph are similar, therefore they should have similar embeddings.

In particular, given a new item or user, we want to be able of computing its embedding by aggregating (for example with an average) the embeddings of the nodes attached to it.

Formally, the embedding of a node can be defined as:
$$
e_u^{(h)} = a\left( e_u^{(h-1)}; e_i^{(h-1)} \ | \ i \in \mathcal{I} \text{ is s.t. } (u, i) \in \mathcal{U} \times \mathcal{I}, r_{u,i} > 0 \right);
$$
$$
e_i^{(h)} = a\left( e_i^{(h-1)}; e_u^{(h-1)} \ | \ u \in \mathcal{U} \text{ is s.t. } (u, i) \in \mathcal{U} \times \mathcal{I}, r_{u,i} > 0 \right)
$$
where $a$ is called the **aggregation function**.

This aggregation process on a graph is called **graph convolution**.

The fact that embeddings depend on their value at the previous step is known as self-connection.

---

At an high level, the method works as follows:
0. initialize user and item embeddings $E^{(0)}$;
1. sample a data point;
2. apply $h$ hops of graph convolution on the nodes;
3. using $E^{(h)}$ compute the **prediction** and gradients;
4. go back to step 1.

This architecture where the embedding of each node is propagated in the graph and is used to compute other embeddings is called **message passing**.
The "message" is the node embedding.

We need to answer the following questions:
- How do we choose the **aggregation function**?
- How many hops do we perform?

### LightGCN: Light Graph Convolutional Network

**LightGCN** is a very simple GCN model for recommendation.
It uses a **weighted mean** as aggregation function.
The loss function is **BPR**.
It **does NOT** include self-connections.

In particular:
$$
E_u^{(h)} = \sum_{i \ | \ r_{u,i} > 0} \frac{1}{\sqrt{d_u d_i}} E_i^{(h-1)};
$$
$$
E_i^{(h)} = \sum_{i \ | \ r_{u,i} > 0} \frac{1}{\sqrt{d_u d_i}} E_u^{(h-1)}.
$$

We can represent this process with the formalism of random walks. Let $G \in \mathcal{R}^{|N| \times |N|}$ be the adjacency matrix. We define:
$$
\hat{G} = (\hat{g}_{x,y})_{x \in N, y \in N} = \left( \frac{g_{x,y}}{\sqrt{d_x d_y}} \right)_{x \in N, y \in N}
$$
as the **normalized adjacency matrix**.
Then:
$$
E^{(h)} = \hat{G} E^{(h-1)}.
$$
The prediction is computed as:
$$
\tilde{r}_{u,i} = E_u^{(h)} \cdot E_i^{(h)}.
$$

---

In matricial form, the process becomes:
0. initialize the embeddings $E^{(0)}$;
1. apply $h$ convolution steps $E^{(h)} = \hat{G}^h E^{(0)}$;
2. draw a BPR sample $u,i,j$ such that $r_{u,i} > 0$ and $r_{u,j} = 0$;
3. compute the prediction $\tilde{r}_{u,i} = E_u^{(h)} \cdot E_i^{(h)}$ and $\tilde{r}_{u,j} = E_u^{(h)} E_j^{(h)}$;
4. apply the gradient step of BPR.

### Advantages of GCN

Graph convolution methods have many advantages:
- they can work on **different types of graphs**;
- can accommodate different **aggregation** functions that may have parameters themselves;
- can accommodate different **loss** functions. 

The disadvantages of GCN method is that:
- they have **enormous computational cost**;
- they can exhibit **high popularity bias**.

Furthermore, in their basic form they are **not very effective** for collaborative filtering.

The computational cost of GCN comes from the fact that convolution requires matrix product of the whole adjacency matrix. Due to its high density, $\hat{G}^h$ is not computed, rather the product is iterated $h$ times.
Observe that each product requires $O(2 |\mathcal{U}| \mathcal{I} K)$ operations.

Let's understand where does the popularity bias come from.
From the spectral theorem:
$$
E^{(h)} = \hat{G}^h E^{(0)} = (V \Sigma V^T)^h E^{(0)} = V \Sigma^h V^T E^{(0)}.
$$
Thus we're raising the eigenvalues to the power of $h$. In this way small eigenvalues get dampened and we end up considering only frequent relationships, i.e. popularity bias.

We can alleviate this problem through a so-called **filter function** which modifies the eigenvalues before the convolution:
$$
E^{(h)} = V f(\Sigma)^h V^T E^{(0)}.
$$

---

**Graph-Filter Collaborative Filtering** (**GF-CF**) is an item-based collaborative filtering model that uses filter functions.

Since small singular values disappear during convolution, we compute analytically the item-item transition probability based on the truncated singular values.

In particular:
1. we normalize the URM
$$
\hat{r}_{u,i} = \frac{r_{u,i}}{\sqrt{d_u d_i}};
$$
2. we compute the truncated SVD decomposition:
$$
\hat{R} \approx U_k \Sigma_k V_k^T;
$$
3. we compute the item-item similarity:
$$
S = \hat{R}^T \hat{R} + \alpha D_\mathcal{I}^{-\frac{1}{2}} V_k V_k^T D_\mathcal{I}^{\frac{1}{2}}.
$$

Advantages:
- **fast computation** of the similarity and **very effective**;
- **flexible**, can extend it to change the exponent of the degree matrix.

Disadvantages:
- the similarity is **dense**;
- applying KNN is difficult, a large number of neighbors is required.

