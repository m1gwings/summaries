---
marp: true
theme: summary
math: mathjax
---
# Non-personalized algorithms

<div class="author">

Cristiano Migali

</div>

In this section, we are going to talk about non-personalized recommenders. As we said before, non-personalized techniques recommend the same list of items to all the users.

## Top popular

An intuitive type of this category of recommender systems are **top popular recommendations**.
We can compute top popular recommendations starting from the URM matrix. In particular we count the number of non-zero ratings for each item. This corresponds to producing a 1D vector with the number of non-zero entries in each column of the URM. In this way we can see which items have been rated the greatest number of times, i.e. the most popular.
The popularity of an item is computed by using its ratings, without taking into account the opinion of the users, but just the number of users by which the item has been judged.

## Best rated

Another non-personalized technique is based on the **best rated** items.
In this case, instead of simply counting the number of non-zero entries in each column of the URM, we compute the average rating per item.
Then we recommend the items with the highest average ratings.
Observe that we only consider the non-zero entries when computing the average of each column. Mathematically, let $N_i$ be the number of ratings associated to the item $i \in \mathcal{I}$, then it's average rating is:
$$
b_i = \frac{\sum_{u \in \mathcal{U}} r_{u,i}}{N_i}.
$$
This approach has a big issue: it doesn't take into account the fact that the average rating is more robust when we have many ratings, while it can be very noisy if the ratings are few. To account for this problem, as it's usually done, we add a **shrink term** $C > 0$:
$$
b_i = \frac{\sum_{u \in \mathcal{U}} r_{u,i}}{N_i + C}
$$

## Global effects


