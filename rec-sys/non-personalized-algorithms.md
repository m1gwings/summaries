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

We will now study a technique called the **global effects**, that can be used to make simple but effective recommendations when we have explicit ratings.
Global effect can also be sued to normalize the URM before using more advanced algorithms.

---

The basic idea behind global effects is that some items have larger ratings than other items, and some users give more generous ratings than other users.
These _differences from the average behavior_ are called the **biases of items and users**.
The global effects method use these biases to make predictions.
The method is described with a _six steps procedure_.

- Step 1: **compute the global bias**
$$
\mu = \frac{\sum_{u \in \mathcal{U}, i \in \mathcal{I}} r_{u,i}}{N}
$$
> where $N = |\{ (u, i) \in \mathcal{U} \times \mathcal{I} \ | \ r_{u,i} > 0 \}|$.
In this step we compute the so-called _global bias_, which is the average of all the non-zero ratings.

- Step 2: **remove the global bias**
$$
r_{u,i}' = r_{u,i} - \mu \ \forall (u, i) \in \mathcal{U} \times \mathcal{I} \ | \ r_{u,i} > 0.
$$
> In this step we de-bias the URM by removing the global bias from all the non-zero ratings.

- Step 3: **compute item biases**
$$
b_i = \frac{\sum_{u \in \mathcal{U}} r_{u,i}'}{N_i + C} \ \forall i \in \mathcal{I}
$$
> where $N_i = |\{ u \in \mathcal{U} \ | \ r_{u,i} > 0 \}|$.
In this step we compute the so-called _item bias_, which is the average of all the non-zero ratings of a given item.
As we explained for the _best rated_ algorithm, we add a shrink term $C$ in the average to account for statistical significance of the average rating.

- Step 4: **remove item biases**
$$
r_{u,i}'' = r_{u,i}' - b_i \ \forall i \in \mathcal{I}, \forall u \in \mathcal{U} \ | \ r_{u,i} > 0
$$
> In this step we remove the corresponding item bias to all the non-zero ratings of an item.

- Step 5: **compute user biases**
$$
b_u = \frac{\sum_{i \in \mathcal{I}} r_{u,i}''}{N_u + C} \ \forall u \in \mathcal{U}
$$
> where $N_u = |\{ i \in \mathcal{I} \ | \ r_{u,i} > 0 \}|$.
In this step we compute the so-called _user bias_, which is the average of all the non-zero ratings given by a certain user and accounts for the fact that some users are more generous than others in their ratings.
Again we have a shrink term $C$.

---

- Step 6: **compute the "personalized ratings"**
$$
\tilde{r}_{u,i} = \mu + b_i + b_u \ \forall (u, i) \in \mathcal{U} \times \mathcal{I} \ | \ r_{u,i} > 0.
$$
> In this step we apply the final formula to compute the personalized ratings. Observe that the ratings are personalized in the sense that they can potentially differ for different users due to the presence of the term $b_u$. **Important**: this is NOT enough to consider global effects a personalized algorithm, indeed the items ranking is the same for all users since, after fixing a user $u \in \mathcal{U}$, $b_u$ becomes a fixed additive term which doesn't affect the ordering among items.
