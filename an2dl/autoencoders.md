---
marp: true
theme: summary
math: mathjax
---
# Autoencoders

<div class="author">

Cristiano Migali

</div>

**Autoencoders** (**AEs**) are a family of neural network models used in unsupervised learning.

An autoencoder is obtained by the composition of an _encoder_ $\mathcal{E}$, which compresses the $n$-dimensional input to a $d$-dimensional vector with $d \ll n$ and a _decoder_ $\mathcal{D}$ which takes as input the compressed vector and produces an $n$-dimensional reconstruction.

## Training autoencoders

Autoencoders can be trained to reconstruct all the data in a training set.
The reconstruction loss over a batch $S$ is
$$
l(S) = \sum_{\underline{s} \in S} || \underline{s} - \mathcal{D}(\mathcal{E}(\underline{s})) ||_2.
$$
The training of $\mathcal{D}(\mathcal{E}(\cdot))$ is performed through standard back-propagation algorithms.
The auto-encoder thus learns the identity mapping.

**Important remark**: there are **no external labels** involved in training the auto-encoder, as it performs the reconstruction of the input.

## Remarks on auto-encoders

The features $\underline{z} = \mathcal{E}(\underline{s})$ are typically referred to as **latent representation**.
AE typically do NOT provide exact reconstruction since $n \ll d$, by doing so we **expect the latent representation to be a meaningful and compact representation** of the input.
It is possible to add a **regularization term** $\lambda \mathcal{R}(\underline{s})$ to steer the latent representation $\mathcal{E}(\underline{s})$ to satisfy desired properties (e.g. sparsity, or to follow a Gaussian distribution), or the reconstruction $\mathcal{D}(\mathcal{E}(\underline{s}))$ (e.g. smoothness, sharp edges in case of images).

AEs can be used to **initialize classifiers** when the training set includes **few annotated data** and **many unlabeled ones**.

## Autoencoders' architectures

### Autoencoders using FFNNs

The typical structure of a FF autoencoder has 1 hidden layer with $d$ neurons, while the input and the output have both $n$ layers. The first FC layer plays the role of the encoder $\mathcal{E}$, while the second FC layer plays the role of the decoder $\mathcal{D}$.

We can learn a more powerful non-linear representation by stacking multiple hidden layers (obtaining deep auto-encoders).

---

### Convolutional autoencoders

Of course it is possible to use convolutional layers (in the encoder stage) and transpose convolution (in the up-sampling stage) to implement a deep convolutional autoencoder.

## Autoencoders as generative models

We could try to use the decoder $\mathcal{D}$ to generate new samples starting from new vectors in the latent space.

An intuitive approach is to draw random vectors $\underline{z} \sim \phi_\underline{z}$ to mimic "a new latent representation" and feed them to the decoder.
Unfortunately this approach does not work since **we do NOT know the distribution of proper latent representations** (or at least, it's very difficult to estimate).

An alternative when the latent space has low dimensionality (like 2 or 3) is to plot the latent representation of each sample in the dataset, annotated with its class (if it has one). Then we can build a grid in a populated region of the latent space and decode each point of the grid through $\mathcal{D}$.
As the latent space dimension grows, it is more likely to fall in a less populated area, thus to sample in regions which do NOT correspond to any class.

Another approach is to use **variational autoencoders** which force $\underline{z}$ to follow a Gaussian distribution (on top of enabling accurate reconstruction).
