---
marp: true
theme: summary
math: mathjax
---
# Introduction to ML

<div class="author">

Cristiano Migali
(_adapted from the slides of Prof. Marcello Restelli_)

</div>

In order to _define_ what Machine Learning is we need to understand what is learning from a _computer program_ viewpoint.
- _According to Mitchell (1977)_ a **computer program** is said to **learn** from **experience $E$** with respect to some class of **tasks $T$** and **performance measure $P$**, if $P$ improves with $E$.

- **Machine Learning** (**ML**) is a sub-field of AI which aims at building **knowledge** from **experience**, through **induction**.

**Remark**: ML is NOT magic! It can extract information from data, but it can't create it.

In _traditional programming_ a program is executed on a computer to process input data and produce a desired output. In ML instead a computer, running specifically tailored algorithms, extracts a program from the input data and the corresponding desired output.

ML allows computers to make informed decisions on new, unseen data. Often it is too difficult to design a set of rules by hand, ML allows to automatically extract relevant information from data.

We can distinguish 3 main subfields of ML:
- **Supervised learning**: which has the aim of learning a model of the mechanism that generated the observed data;
- **Unsupervised learning**: which has the aim of learning the best representation for the observed data;
- **Reinforcement learning**: which has the aim of learning how to take optimal decisions from the observed past outcomes.

Supervised learning problems are grouped in 3 main categories:
- **classification**;
- **regression**;
- **probability estimation**.

The main problems in unsupervised learning are:
- **compression**, and
- **clustering**.

The main problems in reinforcement learning can be formalized as:
- **Markov Decision Processes** (**MDPs**);

---

- **Partially Observable MDPs** (**POMDPs**);
- **Stochastic games**.

## Overview of supervised learning

Supervised learning is the largest, most mature, and most widely used sub-field of machine learning. Given a training data set $\mathcal{D} = \{ (x_1, t_1), \ldots, (x_N, t_N) \}$ generated by a mechanism (_a function_) $f$ ($t = f(x) + \varepsilon$ where $\varepsilon$ is a random variable with $\mathbb{E}[\varepsilon] = 0$), we want to find a **good approximation of $f$** that _generalizes_ well on test data.

The **input variables $x$** are also called **features**, **predictors**, **attributes**. The **output variables $t$** are also called **targets**, **responses**, **labels**.
If $t$ is a _categorical variable_ (i.e. it can assume a fixed discrete set of values and there is no clear definition of distance among them), then the problem is said to be a _classification_. If $t$ assumes infinitely many values or if it belongs to a metric space, then the problem is said to be a _regression_. If $t$ is the probability of observing $x$, then we're dealing with _probability estimation_.

It is appropriate to use supervised learning when either of these conditions holds:
- there is no human expert in the problem;
- humans can perform the task but cannot explain how;
- the desired function changes frequently;
- each user needs a customized function $f$.

All supervised learning techniques are composed of 3 steps:
1. definition of a **loss function** $L$;
2. choice of an **hypothesis space** $\mathcal{H}$;
3. optimization to find the best model in $\mathcal{H}$ according to $L$ (i.e. the one which minimizes the value of $L$).

## Dichotomies in ML

We can classify ML methods in many ways.

- **Parametric** vs **Non-parametric**

> In parametric methods the number of parameters of the model is fixed and finite; conversely, in non-parametric methods, the number of parameters depends on the training set.

- **Frequentist** vs **Bayesian**

> Frequentist methods use probabilities to model the **sampling** process; bayesian methods use probability to model the uncertainty of the estimate.

---

- **Generative** vs **Discriminative**

> Generative methods try to learn the **joint** probability distribution $p(x, t)$; discriminative methods try to learn the **conditional** probability distribution $p(t|x)$.

- **Empirical Risk Minimization** vs **Structural Risk Minimization**

> Empirical risk minimization methods try to reduce the error over the training set as much as possible. Conversely, structural risk minimization methods try to find a balance between training error and model complexity.
