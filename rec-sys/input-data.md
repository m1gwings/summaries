---
marp: true
theme: summary
math: mathjax
---
# Input data

<div class="author">

Cristiano Migali

</div>

In this set of notes we will describe in details which are the input data used by recommender algorithms and how they are usually organized.

## Item data

The first kind of data used by a recommender system are the **data regarding the items** it can recommend. A recommender system needs at least a list of recommendable items. Usually each item in the list is further characterized by a set of attributes which can be used to make recommendations.

### Item Content Matrix

Items data are usually organized in the so-called **Item-Content Matrix**, or **ICM**.
Rows in the ICM represent items, while columns represent attributes. In particular let $\mathcal{I}$ be the set of items and $\mathcal{A}$ the set of attributes. Then $\text{ICM} \in \mathbb{R}^{|\mathcal{I}| \times |\mathcal{A}|}$.
In their simplest form, the values in the ICM are in binary format: if an item contains a specific attribute, the corresponding value in the matrix will be set to 1 (0 otherwise).
In a more useful scenario, each number in the ICM represents how much important an attribute is in characterizing an item, and it can assume any positive value.

## User's interaction data

The second kind of data used by a recommender are the **past interactions between users and items**.

### User Rating Matrix

These data can be arranged in the so-called **User Rating Matrix**, or **URM**.
Rows in the user-rating matrix represent users, and columns represent items. In particular, let $\mathcal{U}$ be the set of users, then $R \in \mathbb{R}^{|\mathcal{U}| \times |\mathcal{I}|}$ (_we will denote the URM as $R = \{ r_{u,i} \}_{u \in \mathcal{U}, i \in \mathcal{I}}$_).
The numbers in the URM represent ratings, either **implicit** or **explicit**.
- If we have **no information** about the opinion of the user on an item, the corresponding value will be set to 0.
- If we know **only the past interactions between users and interactions** but we haven't asked directly to the users their opinions regarding some items, then we say that the ratings are implicit. In particular, we assume that users are interested in items with which they've interacted. For this reason implicit ratings usually take binary values: we mark the interaction with a user $u$ and an item $i$ as $r_{u,i} = 1$.

---

- Finally, if we have **asked directly to some users their opinion regarding some of the items**, we talk about explicit ratings. Users express how much they liked an item through a value in a rating scale which usually goes from 1 to 5. In this case the URM stores exactly such values.

The **goal** of any recommender algorithm is to predict missing values in the URM.

#### URM density

The URM density of an average recommender system, namely the percentage of non-zero elements, is usually below 0.01 percent.

#### How to build an URM matrix

The process required to build an URM depending on the kind of ratings (among implicit and explicit) and is strongly influenced by the context.

- If we're working with **implicit ratings** there are different ways to estimate the opinion of a user for an item, without asking for an opinion explicitly. It may be, for instance, the total viewing time of a movie, the number of times a user has listened to a song, or the fact that a user has made a purchase. In the case of movies, we can assume that, if a user has stopped watching a movie after 20 or 30 minutes, he, or she, did not like the movie. While, if the viewing time corresponds more or less to the length of the movie, probably the user has enjoyed it. Of course, this is NOT an absolute criterion, just an heuristic.

- If we're working with **explicit ratings** we need to design a suitable rating scale. We may want to use **large rating scales**, to have many possible grades that reflect the opinion of the user precisely. On the other hand, we have to be aware of the fact that it requires more effort for the user to choose the correct rating on a large rating scale, and therefore we have to expect fewer ratings. Another option is to opt for a simpler, **smaller ratings scale**. In this case, we will receive, on average, more ratings than before.
Another important decision is whether we prefer a scale with an **odd number of values** or an **even number of values**.
An **even rating scale** implies the absence of a neutral element, the one in the middle. You can receive only positive or negative ratings. The user is, in a way, forced to express an opinion and, again, it will eventually result in fewer ratings. Instead, if we opt for an odd rating scale, we have to be aware that the system will receive ratings that are neutral. The idea is that the possibility of giving a neutral rating will make users more comfortable, and therefore more ratings will be given. Unfortunately, it's a trend that users prefer giving the neutral rating. SO, in a way, the system receives more ratings, but lot of them are useless, because they do not express a real opinion.
Another issue is that users, in general, tend to publish their rating only if they had a positive experience. This evidently creates a bias, that affects the rating distribution.
