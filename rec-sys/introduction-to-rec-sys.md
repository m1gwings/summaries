---
marp: true
theme: summary
math: mathjax
---
# Introduction to Recommender Systems

<div class="author">

Cristiano Migali

</div>

## What is a recommender system?

In this section, we will introduce what a **recommender system** is, its goals and its data inputs.

- A **recommender system** is a system which filters and analyzes input data with the goal of providing users with hints and suggestions about _items that can meet their interest_.

Some of the most common applications of recommender systems are _e-commerce_ and _streaming services_.

### Input data

Let's describe the main classes of data which a recommender system takes as input.

#### Items data

A **list of available items** is the first, main input to any recommender algorithm. The description of each item can be enriched by a set of attributes.

For instance, if we recommend movies, genre, director, and actors could be a meaningful set of attributes.

#### Users data

A recommender system also needs to know something about the users, in order to provide them with recommendations. As a consequence, a second source of information for a recommender are **user attributes**.
Demographics, such as gender and age, are examples of user attributes.

#### Interaction between users & items

A third important source of information are **interactions between users and items**. Interactions reveal the opinions of users on some of the items. For instance, a user, may have rated some movies. In this case, we explicitly know the opinion of the user on these movies. Alternatively, we may know which books a user has bought in the past, or which movies a user has watched. In this case, we can implicitly assume that if a user watched a movie, or bought a book, probably the user likes that movie or that book. Knowing these interactions, may be useful to recommend other users what to read, or what to watch next, based on what they have already read or watched.

---

For example, if people who buy running shoes usually buy headbands as well, a recommender system will encourage you to buy both of the items.

Interactions have attributes as well. These attributes are called the **context**. Examples of contextual attributes are geographical location, day of the week, hour of the day, mood of the user, and so on ... .
The same user may have different opinions on the same item, based on the context. For instance, a restaurant could be perfect for a business lunch, but not for a romantic dinner. Business lunch and romantic dinner are examples of context when recommending restaurants. Similarly, if the weather is sunny, the user might prefer a restaurant with an outdoor garden, while if the weather is rainy, the user might prefer a restaurant with a fireplace. Sun and rain are two other examples of context. 

## Taxonomy of recommender systems

### Personalized vs Non-personalized

Recommender algorithms can be first classified into two categories: **personalized** and **non-personalized** algorithms.

- We say that a recommendation algorithm is **non-personalized** when _all users receive the same recommendations_.

Examples of non-personalized recommendations are the most popular movies, recent music hits, ... .

- Conversely, with **personalized** algorithms, different users receive different recommendations.

The goal of a personalized recommender is to make better recommendations than non-personalized techniques.

### Content-based filtering vs Collaborative filtering

Personalized recommendation techniques can be further categorized into a number of different categories. The most important are **content-based filtering** and **collaborative filtering**.

#### Content-based filtering

The _basic idea_ with **content-based recommendations** is to recommend items, similar to the items a user liked in the past. Content-based filtering has been one of the first approaches used to build recommender systems.
One important pre-requisite for content-based filtering is to have, for each product, a list of good quality attributes.

---

#### Collaborative filtering

**Collaborative filtering** techniques, on the contrary, do NOT require any item attribute to work, but rely on the opinions of a community of users.

The _first type_ of collaborative recommender invented was based on **user-uer similarities**. The basic idea is to search for users with similar taste, that is, users sharing the same opinion on a number of items. This idea seems reasonable, but we will see later in the course that the user-user approach does not work always well.

The _second type_ of collaborative recommenders are based on **item-item algorithms**. The basic idea is to calculate the similarity between each pair of items, according to how many users have the same opinions on the two items.
Nowadays, many commercial recommenders rely on item-item algorithms.

The _third type_ of collaborative recommenders has been invented during a competition on recommender systems held by Netflix. It is based on a technique called **matrix factorization**, which is part of a more general family of algorithms, called dimensionality reduction. Contrary to user-user and item-item algorithms, it is not easy to provide an intuitive explanation of how algorithms based on matrix factorization work.

Finally, there are others techniques used to build collaborative recommenders, like **factorization machines** and **deep learning**.

### Other kinds of personalized algorithms

**Context-aware Recommender Systems** (**CARS**) extend collaborative filtering in order to be able to use the context, and to improve the quality of recommendations.

Modern algorithms are able to simultaneously use multiple, heterogeneous sources of information, in order to build **hybrid recommender systems** that merge and improve the capabilities of content, collaborative and context-based techniques. These hybrid algorithms can be roughly considered as collaborative filtering techniques in which users, items, and interactions are enriched with side information.
