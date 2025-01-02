---
marp: true
theme: summary
math: mathjax
---
# Generative models for images

<div class="author">

Cristiano Migali

</div>

- The **goal** of **generative models for images** is, given a training set of images $\mathcal{D} = \{ I_i \}$, to generate other images that are similar to those in $\mathcal{D}$.

Images live in a very "difficult to describe" manifold in a huge dimensional space.

## Why do we need generative models?

Generative models can be used for **data augmentation**, for simulation, for inverse problems like super-resolution, in-painting, and colorization.  Training generative models can also enable inference of latent representations that can be useful as **general features**.

Modeling the distribution of natural images is known as the "holy grail" of image processing. It can be avery useful regularization prior in other problems or to perform anomaly detection.

On top of specific applications of image generation, the first effective generative model (i.e. GANs) give rise to new training paradigm and practices.

On top of this, nowadays we all know how realistic generative models are and their use in everyday life.

## Generative Adversarial Networks

- **Generative Adversarial Networks** (**GANs**) are a family of generative models. They were born for image classification.

In the **GAN** approach, instead of trying to explicitly model the density $\phi_\underline{s}$ describing the manifold of natural images, we just find out a model able to generate samples that "look like" training samples $S$.

Instead of sampling from $\phi_\underline{s}$, we **sample a seed** from a known distribution $\phi_\underline{z}$ which is defined a-priori. The samples from this distribution are also referred to as **noise**. The seed is fed to a learned transformation that generates realistic samples, as if they were drawn from $\phi_\underline{s}$.

In particular this transformation is learned by a neural network. This neural network is going to be **trained in an unsupervised manner**: **no label is needed**.

The biggest challenge is to define a suitable loss for assessing whether the output is a realistic image or not.

---

The GAN solution is to resort to another neural network to define the loss.

In particular, we train a pair of neural networks addressing two different tasks that compete in a sort of **two players** (adversarial) **game**.
These models are:
- a **generator** $\mathcal{G}$ that produces realistic samples, e.g. taking as input some random noise;
- a **discriminator** $\mathcal{D}$ that takes as input an image and **assess whether it is real or generated by $\mathcal{G}$**.

We train the two and at the end, we keep only $\mathcal{G}$.

$\mathcal{G}$ is trained to generate images that can fool $\mathcal{D}$, namely can be classified as "real" by $\mathcal{D}$. The loss of $\mathcal{G}$ is therefore given by $\mathcal{D}$.

At the end of the training, we hope $\mathcal{G}$ to succeed in fooling $\mathcal{D}$ consistently. We discard $\mathcal{D}$ and keep $\mathcal{G}$ as generator.
$\mathcal{D}$ is expected to be effective in distinguishing real from fake images at the end of the training, thus, if $\mathcal{G}$ can fool $\mathcal{D}$, it mean that $\mathcal{G}$ is a generator.

Both $\mathcal{D}$ and $\mathcal{G}$ are conveniently chosen as FFNNs or CNNs.
In particular: $\mathcal{D}(\cdot, \theta_d) : \underline{s} \mapsto \mathcal{D}(\underline{s}, \theta_d)$ and $\mathcal{G}(\cdot, \theta_g) : \underline{z} \mapsto \mathcal{G}(\underline{z}, \theta_g)$ where $\theta_d$ and $\theta_d$ are network parameters, $\underline{s} \in \mathbb{R}^n$ is an input image (either real or generated by $\mathcal{G}$) and $\underline{z} \in \mathbb{R}^d$ is some random noise to be fed to the generator.

- $\mathcal{D}(\underline{s}, \theta_d) \in [ 0, 1 ]$ is the estimated probability that the input is a true image.
- $\mathcal{G}(\underline{z}, \theta_g) \in \mathbb{R}^n$ gives as output the generated image.

A good discriminator is such that:
- $\mathcal{D}(\underline{s}, \theta_d)$ is maximum when $\underline{s} \in S$ (i.e. $\underline{s}$ is a true image from the training set);
- $1-\mathcal{D}(\underline{s}, \theta_d)$ is maximum when $\underline{s}$ is generated from $\mathcal{G}$, and thus $1-\mathcal{D}(\mathcal{G}(\underline{z}, \theta_g), \theta_d)$ is maximum when $\underline{z} \sim \phi_\underline{z}$.

Training $\mathcal{D}$ consists in maximizing the **binary cross-entropy**:
$$
\max_{\theta_d} \left( \mathbb{E}_{\underline{s} \sim \phi_\underline{s}} [\log \mathcal{D}(\underline{s}, \theta_d) ] + \mathbb{E}_{\underline{z} \sim \phi_\underline{z}} [\log(1-\mathcal{D}(\mathcal{G}(\underline{z}, \theta_g), \theta_d))] \right).
$$

A good generator $\mathcal{G}$ makes $\mathcal{D}$ to fail, thus minimizes the above:
$$
\min_{\theta_g} \max_{\theta_d} \left( \mathbb{E}_{\underline{s} \sim \phi_\underline{s}} [\log \mathcal{D}(\underline{s}, \theta_d) ] + \mathbb{E}_{\underline{z} \sim \phi_\underline{z}} [\log(1-\mathcal{D}(\mathcal{G}(\underline{z}, \theta_g), \theta_d))] \right).
$$

The optimization problem can be solved by an iterative numerical approach.
We **alternate**:
- $k$ steps of Stochastic Gradient Ascent w.r.t. $\theta_d$, keeping $\theta_g$ fixed;

---

- 1 step of SGD w.r.t. $\theta_g$, keeping $\theta_d$ fixed (observe that the first term in the loss does NOT depend on $\theta_g$).

During early learning stages, when $\mathcal{G}$ is poor, $\mathcal{D}$ can reject samples with high confidence because they are clearly different from the training data (thus $\mathcal{D}(\mathcal{G}(\underline{z}, \theta_g), \theta_d) \approx 0$). In this region, $\log(1-\mathcal{D}(\mathcal{G}(\underline{z}, \theta_g), \theta_d))$ is almost flat, thus has very low gradient. For this reason, when we optimize for $\theta_g$, instead of minimizing
$$
\log(1-\mathcal{D}(\mathcal{G}(\underline{z}, \theta_g), \theta_d)),
$$
we maximize
$$
\log(\mathcal{D}(\mathcal{G}(\underline{z}, \theta_g), \theta_d)).
$$
This is equivalent in terms of loss function, but provides a stronger gradient during the early learning stages.

### Vector arithmetic

The input space of the generator shows vector space properties w.r.t. the semantics of generated samples. For example,  let $\underline{z}_\text{sw}$ be a seed which generates a smiling woman, $\underline{z}_\text{nw}$ a seed which generates a neutral woman, and, finally, $\underline{z}_\text{nm}$ a seed which generates a neutral man.
Than
$$
\underline{z}_\text{sm} = \underline{z}_\text{nm} + (\underline{z}_\text{sw} - \underline{z}_\text{nw})
$$
is a seed which generates a smiling man. 

### Conditional GANs

Suppose each image in $S$ is connected with any auxiliary information $y$, such as class labels. We want to insert this information to steer image generation.
We can concatenate it (one-hot encoded) at the end of the input noise in the hope that the generator $\mathcal{G}$ will learn to generate an image of the same class.
To promote this process, we also **append the label information in a one-hot-encoded channel at the end of real images** and generated images as well. This will alow the discriminator to easily classify as "fake" generated images whose content is NOT consistent with the encoded class label. Indeed, such consistency is guaranteed on real images.

### Anomaly detection for GANs

GANs can successfully establish a mapping between random variables and the manifold of images. We might have a wonderful anomaly detection model if:
- we train a GAN generator $\mathcal{G}$ to generate normal images,
- we invert the GAN mapping and get $\mathcal{G}^{-1}$.

---

Indeed, even if we don't know the distribution of the manifold of images, we know the distribution of the seeds. Thus, by computing the likelihood of $\mathcal{G}^{-1}(\underline{s})$ according to $\phi_\underline{z}$ we get an estimate of the likelihood of $\underline{s}$ according to $\phi_\underline{s}$.
Unfortunately, it is not possible to invert $\mathcal{G}$, we need to train some neural network for this purpose.

This is done in the **BidirectionalGAN** (**BiGAN**) model. In particular, in a BiGAN we add an encoder $\mathcal{E}$ to the adversarial game which brings an image back to the space of "noise vectors". It can be used to reconstruct an input image $\underline{s}$ (as in auto-encoders) by computing $\mathcal{G}(\mathcal{E}(\underline{s}))$.
The discriminator $\mathcal{D}$ takes as input a tuple $(\underline{s}, \underline{z})$, which corresponds to $(\mathcal{G}(\underline{z}), \underline{z})$ for generated images, and to $(\underline{s}, \mathcal{E}(\underline{s}))$ for real images.
In principle, the encoder $\mathcal{E}(\cdot)$ can be used for anomaly detection by computing the likelihood of $\phi_\underline{z}(\mathcal{E}(\underline{s}))$ and consider as anomalous all the images $\underline{s}$ corresponding to a **low likelihood** (provided that $\phi_\underline{z}$ was not a uniform distribution).
Another option is to use the output of the discriminator as anomaly score: $\mathcal{D}(\underline{s}, \mathcal{E}(\underline{s}))$, since the discriminator will consider the anomalous samples as fake.
However, there are more effective anomaly scores, like:
$$
A(\underline{s}) = (1-\alpha) || \mathcal{G}(\mathcal{E}(\underline{s})) - \underline{s} ||_2 + \alpha || f(\mathcal{D}(\underline{s}, \mathcal{E}(\underline{s}))) - f(\mathcal{D}(\mathcal{G}(\mathcal{E}(\underline{s})), \mathcal{E}(\underline{s}))) ||_2.
$$