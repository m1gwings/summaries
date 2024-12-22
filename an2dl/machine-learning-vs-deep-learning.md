---
marp: true
theme: summary
math: mathjax
---
# Machine Learning vs Deep Learning

<div class="author">

Cristiano Migali

</div>

The aim of this set of notes is to define what _Machine Learning_ and _Deep Learning_ are and highlight the differences between the two.

## Machine Learning

- **Machine Learning** is a research field focused on developing algorithms which find patterns in data and use those patterns to make predictions. It falls within the Artificial Intelligence (AI) umbrella.

Machine Learning is split in _three main subfields_:
- **supervised learning**;
- **unsupervised learning**;
- and **reinforcement learning**.

### Supervised learning

- In **supervised learning** we're given a _dataset_
$$
\mathcal{D} = \{ (x_1, t_1), \ldots, (x_N, t_N) \} \subseteq \mathcal{X} \times \mathcal{T}
$$
> where, by assumption, $t_i = f(x_i) + \varepsilon_i$ with $f$ being an _unknown function_ and $\varepsilon_1, \ldots, \varepsilon_N$ being an i.i.d. sequence of _0-centered additive noise_.
The values $x_1, \ldots, x_N$ are known as _inputs_, while the values $t_1, \ldots, t_N$ are known as _targets_. The goal is to _learn_ the IO relationship $f$ from the observations in $\mathcal{D}$, being thus able to make predictions for the target value $t$ corresponding to an input $x$ which is NOT present in the dataset.

Examples of classes of _supervised learning tasks_ are:
- **regression**: in which $\mathcal{T}$ is a metric space,
- and **classification**: in which $|\mathcal{T}| < + \infty$ and there is no clear notion of distance among the elements of $\mathcal{T}$ which are said _categorical_.

### Unsupervised learning

- In **unsupervised learning** we're given a _dataset_
$$
\mathcal{D} = \{ x_1, \ldots, x_N \} \subseteq \mathcal{X}
$$
> and we want to exploit its regularities to build a representation for the _input space_ $\mathcal{X}$ which can in turn be used for reasoning or prediction.

---

The most famous _task in unsupervised learning_ is **clustering**, whose aim is to build a partition of $\mathcal{D}$: $\mathcal{C}_1, \ldots, \mathcal{C}_k$ where different data points have been grouped in the same subset according to a certain definition of similarity.

### Reinforcement learning

- **Reinforcement learning** aims at solving sequential decision making problems, framed within a specific setting. In particular, the goal is to find an _optimal policy_ which defines the behavior of an agent inside an environment. At every time instant $t$ the agent interacts with the environment by executing an action $a_t \in \mathcal{A}$ and receives a scalar reward $r_t \in \mathbb{R}$. The quality of a policy is evaluated through an aggregating function of the received rewards (the higher the better). The optimal policy is the one which maximizes this quantity.

## Deep Learning

- **Deep Learning** is an approach to Machine Learning which aims at learning simultaneously a model to solve the given task and an optimized (w.r.t. the task) representation of the data. The name comes from the fact that we're moving the learning process _deeper_: we not only learn the model, but also the representation.

In order to understand why Deep Learning differs significantly from previous approaches, we need to describe the usual process to solve a problem in traditional Machine Learning.
Traditional Machine Learning algorithms work reasonably well under the assumption that the input space $\mathcal{X}$ is a vector space with "low dimensionality". Hence, instead of feeding the algorithm with raw data, like images of different classes of objects (which have a really high dimensionality), we compute a few _hand-crafted features_ (either directly from the physical objects, like measuring height and width, or by pre-processing the images). From the bias-variance tradeoff viewpoint, in this way we're introducing some bias in the model (since the features have been computed _a-priori_), but we're reducing its variance, since, in low-dimensional vector space, we need less samples to cover the relevant region of the space at a certain average density (this is known as the _curse of dimensionality_).
In Deep Learning we exploit the fact that we've a lot of samples at our disposal and use them to learn not only a model, but a also a representation, i.e. a set of features, which is specifically tailored for the task.
Deep Learning models are built hierarchically: the last layer in the hierarchy is the actual model to solve the task at hand (e.g. classification or regression), the other layers are feature extractors which take in input the features extracted by the previous layer (or the raw input) and process them again to make them more significant for the task.
