---
marp: true
theme: summary
math: mathjax
---
# Generalization

<div class="author">

Cristiano Migali

</div>

In this set of notes we will briefly tackle the core objective of supervised learning: **generalization**. For a richer treatment check ML notes.

## Introduction

- We refer to **generalization** as the ability of a _supervised learning model_ to make good predictions of target values over input regions which are outside of the training set.

In order to achieve generalization, supervised learning relies on the **inductive hypothesis**: a solution approximating the target function over a sufficiently large set of training examples will also approximate it over _unobserved examples_.

## Model complexity

The first step in a supervised learning problem is the choice of a model class (a.k.a. hypothesis space), which is a set of models from which we will select the one which better describes the observations. Indeed, what is referred as training  is usually just an optimization process in which we look for the model in the model class which minimizes a given loss function that rewards models whose predictions are close to the ground truth in the training set.
_The choice of the model class is fundamental w.r.t. the ability of the selected model to generalize._
- If the _model class is too inexpressive_ (too simple) there won't be any model capable of representing the target function and thus, a-fortiori, we won't be able of learning it from data. This phenomenon is called **under-fitting**.
- If instead the _model class is too expressive_ (too complex) there will be models not only capable of representing the target function, but also the specific realizations of the noise in the training set which, ideally, should be filtered out. Such models will minimize the considered loss function, fitting the training set almost perfectly, but won't be able to generalize since, as remarked before, they are not learning the target function; they are learning the target function with the addition of noise realizations which are meaningless outside of the given trainign set. This phenomenon is called **over-fitting**.

## Measuring generalization

Because of what we just explained, _training error_ is not a good indicator of the performance of the model. Indeed it is an optimistic estimate.
In this section we'll describe some techniques to measure the generalization capability of our models.

---

### Independent test set

The simplest technique to evaluate a model is to compute the average prediction error on a set of data which we never used during training: an **independent test set**. This will guarantee that the evaluation is unbiased. To be more precise, a detailed evaluation of the model would require to compute a confidence interval.

### Cross-validation

The _independent test set_ approach is great if we have to carry out the final evaluation of the model. The issue is that we can use it only once: if we take decisions depending on the performance obtained on the test set, the model and the test set would no longer be independent. But many times we need to take decisions upon the estimated generalization capability: the usual scenario in which we need to do so is **model selection**. In model selection we compare different model classes in order to choose the one which generalizes the most. To this end we take apart a third portion of the dataset: the **validation set**. In particular: we use the training set to select the model which fits the data the best inside a given model class; then we compare different model classes through different validations set. Indeed, using the training error to compare different classes would not work: the more complex classes will always fit better the data but we're interested in generalization.
Since by selecting a model class we're taking a decision, the evaluation on the validation set is also optimistically biased. For this reason to have a final unbiased estimate, we still need a test set.
The fact that the evaluation on the validation set is optimistically biased could become a problem when we have to compare a lot of model classes, since we could end up choosing the model class which is the best for the given validation set and not the one which is the best for the true distribution.
To prevent the problem we use a technique known as **cross-validation**. It works as follows: instead of splitting the "non-test" data in training and validation, we split it in $k$ folds. Then we iterate for each fold: in each iteration we train a model on all the folds except the current one and use the current fold for evaluation. At the end we average the results of the evaluations. This approach is more robust w.r.t. a fixed validation set, but also more computationally expensive.
In particular robustness is proportional with $k$, but the same holds for computational requirements.
When $k = N$ we talk about **Leave One Out** (**LOO**) **cross-validation**, otherwise we refer to it as **$k$-fold cross-validation**.
