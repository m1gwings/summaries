---
marp: true
theme: summary
math: mathjax
---
# Text classification

<div class="author">

Cristiano Migali

</div>

<div class="centered-definition-expression">

(_adapted from Prof. Mark Carman's slides_)

</div>

**Text classification** is the process of _training a model_ to classify _textual_ documents into categories. Text classification is extensively used. Examples of applications are:
- **spam/phishing detection**;
- **authorship identification**;
- **sentiment analysis**;
- ... .

## Text features

When working with classical models, which assume their inputs to live in finite-dimensional vector space, it is necessary to extract **features** from documents which, in principle, can be arbitrarily long. The _features_ are **signals** in the documents that are useful for the classification.

A naive approach, which doesn't rely on meaningful features, would be to cut the documents at fixed lengths and treat them as categorical variables. This approach is of course un-effective due to the sparseness of the samples in the input space, given the average training data size.

The most common classes of features are:
- **syntax-based features**: e.g. the number of capitalized words;
- **part-of-speech based features**: e.g. the number of verbs versus proper nouns,
- **reading-difficulty** based features: e.g. average length of words/sentences;
- **bag-of-words**: represent documents as vectors of words counts.

### Bag-of-words model

The motivation behind the bag-of-words model is that much of the **useful information** for classifying documents is present in the **vocabulary** of the document.
This set of features _throws away all word order information_ but retains critical vocabulary information.

The usual BOW representation includes also the count of occurrences of each term. Anyway it is often possible to use the binary representation of the document with little information loss.

The BOW representation is very sparse. It is possible to generalize the representation to include **$n$-grams** (i.e., instead of counting the single words, we count the number of occurrences of each sequence of $n$ words, considering their order; $n$ is usually $2$ or $3$). 

---

This can increase the performance, but also greatly increases the number of dimensions, hence more data is needed.
An issue with BOW representation is that usually there are far fewer documents than vocabulary terms, i.e. far fewer samples than features. Thus **strong regularization** is needed to guide the learner and **prevent overfitting**.

## Word frequency
### Statistical laws for term frequencies

There are different _statistical law_ about the frequency of occurrence of terms in documents.

- **Heap's law**: vocabulary grows with approximately the square root of document/collection length:
$$
V(l) \propto l^\beta \text{ with } \beta \approx 0.5.
$$

- **Zip's law**: token's frequency is approximately proportional to the inverse of its rank:
$$
\text{ctf}_{t} \propto 1/\text{rank}(t)^s \text{ with } s \approx 1
$$
> where the **rank** is the position of the term in the ordered list from the most frequent to the least.

Both these laws can be explained with the **random typing model**.

## Linear Classification Algorithms

Due to the very **high number of dimensions** in a **bag-of-words** representation of documents, **linear models** are often used with text.
Linear models estimate one parameter per vocabulary word, making them **highly interpretable** and allowing to see which vocabulary terms influence prediction and by how much.
Linear classification algorithms find linear decision boundaries.

### Naive Bayes

**Naive Bayes** (NB) is one of the **oldest and simplest text classifiers**. It is called naive because it makes the simplifying assumption that word occurrences are **statistically independent** of each other given the **class label**. This means that words provide **independent information** about the class. This assumption makes calculating model parameters very simple. Anyway it doesn't hold in practice since words are highly correlated with each other.

Let's see how the method works with an example.

You want to estimate the probability of spam given text content of email:

---

$$
\mathbb{P}[\text{spam} \ | \ \text{"hi mark I am a student in your nlp course and ..."}]
$$
You can't estimate class probability directly, because you haven't seen any email **exactly** like it before, so use Bayes' rule to swap the order of the events:
$$
= \frac{\mathbb{P}[\text{"hi mark I am a student in your nlp course and ..."} \ | \ \text{spam}] \mathbb{P}[\text{spam}]}{\mathbb{P}[\text{"hi mark I am a student in your nlp course and ..."}]}
$$
We can ignore the denominator, since it's the same for both spam and not spam class, and we can normalize later:
$$
\propto \mathbb{P}[\text{"hi mark I am a student in your nlp course and ..."} \ | \ \text{spam}] \mathbb{P}[\text{spam}]
$$
Now we make the **simplifying** (and clearly wrong) **assumption** that words occurrences are not correlated within the classes:
$$
\propto \mathbb{P}[ \text{"hi"} \ | \ \text{spam}] \mathbb{P}[ \text{"mark"} \ | \ \text{spam}] \mathbb{P}[ \text{"I"} \ | \ \text{spam}] \mathbb{P}[ \text{"am"} \ | \ \text{spam}] \mathbb{P}[ \text{"a"} \ | \ \text{spam}] \dots \mathbb{P}[\text{spam}].
$$
Finally, we can **estimate the probabilities** from training data.
$$
\mathbb{P}[\text{"mark"} \ | \ \text{spam}] \approx \frac{\text{\# of spam emails containing the word "mark"}}{\text{\# of spam emails}};
$$
$$
\mathbb{P}[\text{spam}] \approx \frac{\text{\# of spam emails}}{\text{\# of emails}}.
$$
Usually the probability are smoothed to avoid problems when a word appears only in a class of emails (and thus its estimated probability in other classes would be $0$, leading to a final estimate of $0$).
$$
\mathbb{P}[\text{"inheritance"} \ | \ \text{not spam}] = \frac{\text{\# not-spam emails containing word "inheritance"} + \alpha}{\text{\# of not-spam emails} + 2 \alpha}.
$$

The **advantages** of NB is that it very **fast** to build the model. It provides a reliable predictor even if there is little data available (i.e., it is a stable classifier).

The **disadvantages** are that it doesn't perform quite well on large data as other classifiers, since redundant features are being counted twice (due to the independence assumption) and the predicted probabilities are not well calibrated: predictions are often **overconfident** (again, due to the independence assumption).

### Logistic Regression

In (binary) **logistic regression** we estimate the probability of belonging to the positive class by activating the signed distance from the decision boundary with the sigmoid.

The **advantages** of logistic regression are that it produces **well-calibrated probability estimates**, it can be trained efficiently and scales well to large numbers of features, it is explainable since each feature's contribution to final score is additive.

---

The **disadvantages** is that it assumes that feature values are **linearly related** to log odds, thus, if the assumption is "_strongly_ violated", the model will perform poorly.

### Support Vector Machines

**Support Vector Machines** use the _hinge loss_ to learn a decision boundary which maximizes the margin from the samples. The closest points to the decision boundary (those that determine the margin), are known as support vectors. In a $d$-dimensional space there are, at least, $d+1$ support vectors. A difference w.r.t. Logistic Regression is that moving internal (i.e. non support) points won't affect the boundary.

## Evaluating a Binary Text Classifier

An important tool to evaluate a binary text classifier is the confusion matrix:

| True class\\Predicted class | **Positive** | **Negative** |
|-----------------------------|--------------|--------------|
| **Positive**                | TP           | FN           |
| **Negative**                | FP           | TN           |

From it, we can compute metrics like:
- **accuracy**;
- **precision**;
- **recall**;
- **F1-score**;
- **Area under the Curve** (**AuC**).

If there are $n$ classes, the confusion matrix will be $n \times n$, again true class vs predicted class.
We can compute the precision and recall value for each class. Then we can either do the **macro-average** (i.e. average over classes weighting each class the same), or the **micro-average** (i.e. average over classes weighting each class by the number of data-points in it).
