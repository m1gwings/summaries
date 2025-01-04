---
marp: true
theme: summary
math: mathjax
---
# Quality of Recommender Systems

<div class="author">

Cristiano Migali

</div>

The purpose of this section is to analyze which aspects are relevant for the **quality** of a recommender system.

The quality of a recommender system depends on:
- the dataset;
- the algorithm;
- and, the user interface.

All the three of them contribute to increase the quality of the recommender system, and thinking that an aspect affects more the final result than another is wrong.

There are two kinds of evaluation than can be used to asses the quality of a RS:
- **on-line evaluation**: which allows to measure the quality of the dataset, of the algorithm, and the user interface;
- **off-line evaluation**: which allows to measure only the quality of the dataset and of the algorithm.

## Quality indicators

There are several **quality indicators** which allow to express the quality of a RS.

### Relevance

The first and most important quality indicator is **relevance**. It is the ability of the RS to recommend items that **vey likely** the user **will appreciate**.

### Diversity

**Diversity** is the ability to **diversify** the recommended items, this allows to make recommendations "less boring".

### Serendipity

**Serendipity** is the ability to **surprise the user**. Surprising means to recommend something unusual for the user, who can discover something unexpected. A recommender algorithm is serendipitous if it recommends something that the user would never be able to find by himself or that would never search for.

---

### Novelty

**Novelty** is the ability of **recommending items unknown to the user**.

### Coverage

**Coverage** is the ability of the system to **recommend most of the items in a catalogue**. In particular, it is the percentage of items that a recommender system is able to recommend.

### Consistency

**Consistency** refers to the **stability of the recommendations**. If recommendations change too often between sessions, the user might be disoriented.

### Confidence

**Confidence** is the ability of measuring how much the **system is sure about recommendations**. If a recommender system is not confident about a recommendation, it is probably better to avoid that recommendation. Unfortunately, not all recommender algorithms are able to provide confidence estimates.

### Scalability

**Scalability** refers to the time required for the **training of the recommender system**, and, in particular, the ability of the recommender system of handling increasingly large amount of input data.

### Serving time

**Serving time** refers to the **time** required by the system **to create a new recommendation list**.

### Fairness

**Fairness** is the ability of a recommender system of providing recommendations which are fair both for the users and the content providers.

## On-line evaluation

There are different ways to do on-line evaluation of a recommender system.

### Direct user feedback

The first online evaluation technique we consider is the **direct user feedback**. We can ask some real users to define their level of satisfaction about the recommender system, we can investigate satisfaction using questionnaires.

---

This technique is good, but there are some problem:
- the size of the sample should be meaningful;
- the opinions expressed by the users could NOT be reliable.

### A/B testing

Another possibility is to monitor online behavior of the users, and to apply the so-called **A/B testing**. The core idea is to compare the behavior of users who receive recommendations (the set A), with the behavior of the users who do NOT receive recommendations (the set B).
A/B testing is a powerful method of evaluation, but its results may be difficult to interpret. If users do NOT follow recommendations, what could be the problem? Is it because the lack of relevance of a lack of diversity?

### Controlled experiments

In a **controlled experiment**, a mockup application is made available to a group of potential users. Users are asked to use for a while the application, and then they are asked to give their opinion about the recommendations received.
However this method has some problems: the application is not a real application and the users are not real users, thus the results can be NOT reliable.

### Crowd-sourcing

The last on-line evaluation technique is **crowd-sourcing**. If consists in asking people, after an offer of some kind of compensation, to answer an online questionnaire, expressing their opinion about the mockup of an application.
This technique allows on one hand to reach a large crowd of volunteers, but their opinions could be NOT reliable since they may be interested just in the compensation and could provide random answers. We usually need strong statistical tests to asses the reliability of the answers.

## Off-line evaluation

In order to analyze the offline evaluation techniques, we have to mention some important aspects, namely:
- the **task** of a recommender system;
- the **evaluation dataset**;
- the **relevance metrics** we will use.

### Tasks

A recommender system can be evaluated on the two following tasks:
- **rating prediction**;
- **top-$N$ recommendation**.

---

#### Rating prediction

The **goal** of **rating prediction** is, given a pair $u \in \mathcal{U}$, $i \in \mathcal{I}$, to predict the rating which $u$ would give to $i$.

#### Top-$N$ recommendation

The **goal** of **top-$N$ recommendation** is to produce a list of $N$ items which are relevant for the user.
Ideally we should be able to rank the items from the most relevant to the least relevant and then select the first $N$ items.

### The evaluation dataset

The **evaluation dataset** of a recommender system is built by partitioning the URM.
Usually, we know a very little percentage of all possible ratings. The part that we know is called "ground truth" and it is made of all the non-zero ratings.
They can be divided into two main categories:
- the **relevant part** contains all the positive opinions given by the users;
- on the other hand, the **non-relevant part** contains all the negative opinions.

Of course, the data in the URM that we use for evaluation should be consistent with the target scenario: it should have the <u>same domain</u>, similar distribution, and similar user behavior.

Let's understand how we can build an **evaluation dataset** by partitioning the URM.

#### URM partitioning

##### Hold-out of ratings

The most intuitive way to partition the URM is to select a portion $Z$ of the ground truth data which are hidden and used for testing. The resulting URM (with the hidden ratings) is the training set $X$. After having used $X$ to build our model, we check the performance of the recommender on the hidden predictions by comparing them with the predicted ratings.

This approach **has some problems**: there could be users which have part of their ratings in $X$ and part of their rating in $Z$. Even if it is fair to assume that the ratings by different users are independent, we can't treat different ratings of the same user to be independent, thus the training and test dataset would be somehow correlated and the evaluation would not be fair.

---

##### Hold-out of users

To solve the problem of overlapping users between test and training set, we can partition the URM by choosing a portion of the users $Y$ for testing. Again, the URM without the ratings of testing users is denoted as $X$.
Now the test and training datasets are independent.
However there is a new problem. For personalized recommendations, the model extracted by the URM is NOT enough, we need to feed the recommender with the user profile. Thus, when we evaluate the algorithm on testing users, we will have to choose a portion of the ratings of each testing user to be part of its user profile which we're going to feed to the recommender, while the other portion $Z$ is hidden and will be compared with the predicted rating.

Again, this introduces a **new problem**: it is NOT fair to use the information in future interactions of the user to predict past interactions since this can't happen when the recommender is in production.

##### Time based split

To account for the causality of predictions, we can split training and test data based on a **timestamp**.
Unfortunately, it is difficult to select a realistic timestamp:
- if the testing window is too short, the new interactions will cause frequent model retraining;
- if the testing window is too long, the model becomes stale.

Furthermore there are lost of **new** users with no previous interactions, and thus low test support.

### Relevance metrics

We can distinguish three kinds of relevance metrics:
- **error metrics**;
- **classification metrics**;
- **ranking metrics**.

#### Error metrics

The purpose of **error metrics** is to estimate the difference between ratings assigned by algorithms and ratings assigned by users.

---

We can compute the prediction error as:
$$
e_{u,i} = |r_{u,i} - \tilde{r}_{u,i}|
$$
where:
- $\tilde{r}_{u,i}$ is the rating estimated by the recommender system;
- $r_{u,i}$ is the true rating in the test set.

##### Mean absolute error

The **mean absolute error** is defined as:
$$
\text{MAE} = \frac{\sum_{u,i \in T} |r_{u,i} - \tilde{r}_{u,i}|}{N_T}
$$
where $T$ is the test set and $N_T$ is the number of non-zero interactions in $T$.

##### Mean squared error

The **mean squared error** is defined as:
$$
\text{MSE} = \frac{\sum_{u,i \in T} (r_{u,i} - \tilde{r}_{u,i})^2}{N_T}.
$$

##### Issue with error metrics

Error metrics rely on the so-called **Missing As Random** (**MAR**) assumption. In particular we are assuming that the portion of "relevant" and "non-relevant" ratings in the ground truth is on average the same of the corresponding portion for unknown ratings. Unfortunately, **this assumption is false**. Indeed, users are more likely to interact with relevant items, and thus, the portion of unknown ratings which are "non-relevant" is much higher than in the ground truth.

The result is that a recommendation model that optimizes error metrics is likely going to be **unsuitable** for ranking. The model has never been trained or evaluated on strongly non-relevant items that the user would not have interacted with.

#### Classification metrics

Fix a user $u \in \mathcal{U}$.
To use classification metrics we need to divide all the items in $\mathcal{I}$ in two groups: **relevant** and **non-relevant** according to the data in the row of the URM associated with $u$ (_we will see at the end how to deal with unknown data_).

We can regard the set of recommendations to user $u$ as a subset of $\mathcal{I}$. Ideally, the recommendations should include all and only the relevant items. Through classification metrics we will quantitatively asses these aspects.

---

We define:
- **true positives** (**TP**): the recommendations which are relevant; 
- **false positives** (**FP**): the recommendations which are NOT relevant;
- **false negatives** (**FN**): the items which are relevant but haven't been recommended;
- **true negatives** (**TN**): the items which are NOT relevant and haven't been recommended.

- The **recall** is the portion of relevant items which have been recommended:
$$
\text{recall} = \frac{\text{TP}}{\text{TP} + \text{FN}}.
$$

- The **precision** is the portion of recommended items which is relevant:
$$
\text{precision} = \frac{\text{TP}}{\text{TP} + \text{FP}}.
$$

Classification metrics rely on the **Missing As Negative** (**MAN**) assumption, i.e. we assume that unknown ratings correspond to non-relevant items. This assumption is also false in general, but works better than MAR (which is used in error metrics).

#### Ranking metrics

**Ranking metrics** evaluate the ability of the recommender system to provide a **list of recommendations**: the recommendations are not merely treated as a set of items, we also consider the order among them.

Again fix a user $u \in \mathcal{U}$ and let $\mathcal{R}(u) \subseteq \mathcal{I}$ the set of items recommended to $u$. We denote with $\mathcal{R}(u, n)$ the best $n$ items in $\mathcal{R}(u)$ according to the order relation defined by the recommender system, where $n \in \{ 0, \ldots, |\mathcal{R}(u)| \}$.

We can compute the number of true positives, false positives, true negatives, and false negatives and thus the **precision** and **recall** of $\mathcal{R}(u, n)$ for each value of $n \in \{ 1, \ldots, |\mathcal{R}(u)| \}$.
Observe that the recall is non-decreasing with respect to $n$.

We can plot the $|\mathcal{R}(u)|$ points $(\text{recall}{n}, \text{precision}(n))$ on the Precision (on the $y$ axis) vs Recall (on the $x$ axis) plane.

We can use highlight 3 behaviors on this curve.

- In a **perfect recommender model**: the relevant items come in the order before all the non-relevant ones, thus, at the beginning, as $n$ increases the precision stays at $1$ while the recall increases, when $n$ is the number of relevant items we have precision $1$ and recall $1$, then, as $n$ increases, the recall stays at $1$ and the precisions starts dropping to the fraction of relevant items $p$.

---

- In a **random recommender model**: the precision is on average equal to $p$ for any value of $n$ (since we pick the items at random and thus the probability that they are relevant is $p$) while the recall increases (not steadily) as $n$ increases.

- In an **anti-perfect recommender model**: the relevant items are at the end of the list. Both the precision and recall start from 0 and stay still while $n$ increases to the number of non-relevant items, then precision and recall start to increase together steadily. At the end the precision becomes $p$ while the recall becomes $1$.

We can use this curve also to define an important metric.

- The **average precision** is the area under the curve on the precision vs recall plane. It can be compute by an approximations with rectangle. Remember that recall is non-decreasing; each rectangle has area: $(\text{recall}(n) - \text{recall}(n-1)) \cdot \text{precision}(n)$ where we set $\text{recall}(0) = 0$. Observe that the perfect recommender has average precision $1$, the random recommender has average precision $p$. Hence:
$$
\text{AP}(n) = \sum_{i=1}^n (\text{recall}(i) - \text{recall}(i-1)) \cdot \text{precision}(i).
$$

We can compute the average precision through an equivalent expression. Let $\text{rel}(i) = \mathbb{1}[\text{the } i\text{-th item in the list is relevant}]$.
Then:
$$
\text{AP}(n) = \sum_{i=1}^n (\text{recall}(i) - \text{recall}(i-1)) \cdot \text{precision}(i)
$$
$$
= \sum_{i=1}^n \frac{\sum_{j=1}^i \text{rel}(j)  - \sum_{j=1}^{i-1}\text{rel}(j)}{|\{ i \in \mathcal{I} \ | \ i \text{ is relevant for } u \}|} \cdot \text{precision}(i)
$$
$$
= \frac{1}{|\{ i \in \mathcal{I} \ | \ i \text{ is relevant for } u \}|} \sum_{i=1}^n \text{precision}(i) \cdot \text{rel}(i).
$$

##### Mean Average Precision

- We define the **mean average precision** as the average precision computed on the whole set of users:
$$
\text{MAP}(n) = \frac{\sum_{u \in \mathcal{U}} \text{AP}_u(n)}{|\mathcal{U}|}
$$
> where $\text{AP}_u(\cdot)$ is the average precision computed for the user $u$.

---

##### Average Reciprocal Hit-Rate

- We define the **average reciprocal hit-rate** as:
$$
\text{ARHR}(n) = \frac{\frac{\sum{i=1}^n \text{rel}(i)}{i}}{|\{ i \in \mathcal{I} \ | \ i \text{ is relevant for } u \}|}.
$$