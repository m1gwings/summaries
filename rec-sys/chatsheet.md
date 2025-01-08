---
marp: true
theme: cheatsheet
paginate: true
math: mathjax
---
# RS Cheatsheet (A. Y. 2024/2025)
## SciPy

<div class="multiple-columns with-title">
<div class="column">

### The basics

The **SciPy** framework builds on top of the low-level NumPy framework for multidimensional arrays, and provides a large number of higher-level scientific algorithms.
The SciPy framework can be accessed through the `scipy` Python module.

### Sparse matrices

The SciPy utilities to deal with sparse matrices are contained in the `sparse` submodule, which can be imported as follows:
```
from scipy.sparse import *
```

Some methods common to sparse matrices are:
- **`todense`**: method which allows to convert a sparse matrix to a dense one.
- **`nnz`**: attribute with the number of non-zero entries.

The main ways to represent sparse matrices are:
- the **list of list form** (**LIL**);
- the **coordinate form** (**COO**);
- the **compressed-sparse column** (**CSC**), **and row** (**CSR**). 

#### LIL

The **LIL** form is often used to initialize a matrix before converting it to CSC or CSR form.
We can create a matrix in LIL form by specifying its shape:
```python
A = lil_matrix((2, 3))
```

</div>
<div class="column">

Then, we can populate it as we would do for a usual NumPy array:
```python
A[0, 0] = 1
A[0, 2] = 2
```
A matrix in LIL form is defined by two attributes:
- **`rows`**: it is an array (fixed length, equal to the number of rows) with a list in each entry which stores the sorted column indices of the non-zero elements in the corresponding row;
- **`data`**: it is an array of lists which contains the non-zero values in the matrix with a format analogous to `rows`.

In the example, `A.rows` is:
```python
array([list([0, 2]), list([])],
dtype=object)
```
while `A.data` is:
```python
array([list([1.0, 2.0]), list([])],
    dtype=object)
```

#### COO

We can create a matrix in **COO** form from a bi-dimensional array `B`:
```python
A = coo_matrix(B)
```

</div>
<div class="column">

A **COO matrix** is represented through three attributes:
- **`row`**: it is a list of row indices;
- **`col`**: it is a list of column indices;
- **`data`**: it is a list of all the non-zero values in the matrix, repeated according to their multiplicities.

`data[i]` is the entry of `A` at coordinates `(row[i], col[i])`.

#### CSR

We can create a matrix in **CSR** from from a bi-dimensional array `B`:
```python
A = csr_matrix(B)
```

A **CSR matrix** is represent through three attributes:
- **`indices`**: it refers to the column index, as `col` in the COO format;
- **`data`**: it contains the non-zero values, as `data` in the COO format;
- **`indptr`**: it is an array with one entry per row, given a row index `i`, the non-zero values of the row are in `data[indptr[i]], ..., data[indptr[i+1]-1]` and the corresponding column indices are `indices[indptr[i]], ..., indices[indptr[i+1]-1]`.

**Important remark**: `indptr[i+1] - indptr[i]` is the number of non-zero elements in the `i`-th row. We can compute the number of non-zero elements in each row with `np.ediff1d`.

#### CSC

It is analogous to CSR.

</div>
</div>

---

## Data preprocessing

<div class="multiple-columns">
<div class="column">

### Building a URM from a `DataFrame` of interactions

Interactions between users and items are usually stored in a relational form.
In particular we can assume they are in a `pandas.DataFrame` named `interactions_df` with `columns`: `["UserID", "ItemID", "Interaction", "Timestamp"]`.

We can retrieve the list of user and item IDs (without duplicates) with:
```
user_IDs = interactions_df['UserID'].unique()
item_IDs = interactions_df['ItemID'].unique()
```

The number of users and items is thus:
```
n_users = len(user_IDs)
n_items = len(item_IDs)
```

The user and item IDs are NOT contiguous in general. Let's see how to build a bijection from `user_IDs` to `list(range(n_users))` and an analogous bijection for the items.
```
cont_user_IDs, user_IDs = pd.factorize(
    interactions_df['UserID'].unique())
user_indices = pd.Series(cont_user_IDs,
    index = user_IDs)

cont_item_IDs, item_IDs = pd.factorize(
    interactions_df['ItemID'].unique())
item_indices = pd.Series(cont_item_IDs,
    index = item_IDs)
```

Then we can replace the IDs in the `DataFrame` with the contiguous ones:
```
interactions_df['UserID'] = interactions_df['UserID']\
    .map(user_indices)
interactions_df['ItemID'] = interactions_df['ItemID']\
    .map(item_indices)
```

</div>
<div class="column">

Now, we can build the URM in COO form using the COO constructor which takes `data, (row, column)` as parameters:
```
URM = coo_matrix(interactions_df['Interaction'].values,
    (interactions_df['UserID'].values,
    interactions_df['ItemID'].values))
```
Finally, we convert the URM into CSR form:
```
URM.tocsr()
```

### Splitting train and test data

We can define a `tran_mask` as:
```
train_test_split = 0.8
n_interactions = URM.nnz
train_mask = np.random.choice([True, False], n_interactions,
    p=[train_test_split, 1-train_test_split])
```
The corresponding `test_mask` is:
```
test_mask = np.logical_not(train_mask)
```
Then we create `URM_train` as a COC by masking some interactions:
```
URM.tocoo() # Make sure that the URM is in COO form
URM_train = coc_matrix(URM.data[train_mask],
    (URM.row[train_mask], URM.col[train_mask])).tocsr()
```
Analogously, we define `URM_test`.

</div>
</div>

---

## Evaluation

<div class="multiple-columns">
<div class="column">

Fix a user index:
```
u = 42
```
Under the MAN assumption, the indices of the relevant items for user `u` are the ones with which they have interacted:
```
relevant_items = URM_test.indices[URM_test.indptr[u]:\
    URM_test.indptr[u+1]]
```
**Remark**: `np.in1d(a, b)` where `a` and `b` are two 1D arrays, returns a 1D array with the same dimension of `a` which stores the boolean results of `a[i] in b`.

### Precision

```
def precision(recommended_items, relevant_items):
    is_relevant = np.in1d(recommended_items, relevant_items,
        assume_unique=True)
    
    return np.sum(is_relevant, dtype=np.float32) / len(is_relevant)
```

### Recall

```
def recall(recommended_items, relevant_items):
    is_relevant = np.in1d(recommended_items, relevant_items,
        assume_unique=True)
    
    return np.sum(is_relevant, dtype=np.float32) /\
        relevant_items.shape[0]
```

</div>
<div class="column">

### Average precision

```
def average_precision(recommended_items, relevant_items):
    is_relevant = np.in1d(recommended_items, relevant_items,
        assume_unique=True)
    
    precisions = np.cumsum(is_relevant) /\
        (1 + np.arange(is_relevant.size))

    return np.sum(is_relevant * precisions) /\
        relevant_items.size
```

### Utility to evaluate a recommender system

```
# We pass as paramether the recommender class

def evaluate_algorithm(URM_test, recommender_object, at=5):
    
    cumulative_precision = 0.0
    cumulative_recall = 0.0
    cumulative_AP = 0.0
    
    num_eval = 0


    for user_id in range(URM_test.shape[0]):

        relevant_items = URM_test.indices[URM_test.indptr[user_id]\
            :URM_test.indptr[user_id+1]]
        
        if len(relevant_items)>0:
            
            recommended_items = recommender_object\
                .recommend(user_id, at=at)
            num_eval+=1
```

</div>
</div>

---

<div class="multiple-columns without-title">
<div class="column">

```
            cumulative_precision += \
                precision(recommended_items, relevant_items)
            cumulative_recall += \
                recall(recommended_items, relevant_items)
            cumulative_AP += \
                AP(recommended_items, relevant_items)
            
    cumulative_precision /= num_eval
    cumulative_recall /= num_eval
    MAP = cumulative_AP / num_eval
    
    print("Recommender results are: Precision = {:.4f}," + \
        " Recall = {:.4f}, MAP = {:.4f}".format(
        cumulative_precision, cumulative_recall, MAP))
```

</div>
<div class="column">

</div>
</div>

---

## Recommender template
<div class="multiple-columns">
<div class="column">

We can implement a recommender system by defining a class like the following:
```
class Recommender(object):
    def fit(self, URM_train):
        ...
    
    def recommend(self, user_id, at=5):
        ...
```
For example, a random recommender would be:
```
class RandomRecommender(object):
    def fit(self, URM_train):
        self.n_items = URM_train.shape[1]
    
    def recommend(self, user_id, at=5):
        recommended_items = np.random.choice(self.n_items, at)
        return recommended_items
```

### Utility to remove "seen" items from recommendations

```
def remove_seen(user_id, best_items):
    seen_items = self.URM_train.indices[self.URM_train\
        .indptr[user_id]:self.URM_train.indptr[user_id+1]]
    to_remove = np.in1d(seen_items, best_items,
        assume_unique=True)
    return best_items[np.logical_not(to_remove)]
```

</div>
<div class="column">

</div>
</div>

---

## Non-personalized algorithms

<div class="multiple-columns">
<div class="column">

### Top popular recommender

```
class TopPopRecommender(object):
    def fit(self, URM_train):
        items_popularity = np.ediff1d(URM_train.tocsc().indptr)
        self.popular_items = np.argsort(items_popularity)
        self.popular_items = np.flip(self.popular_items)
    
    def recommend(self, user_id, at=5):
        recommended_items = self.popular_items[:at]
        return recommended_items
```

### Global effects recommender

```
class GlobalEffectsRecommender(object):
    def fit(self, URM_train):
        self.mu = URM_train.sum() / URM_train.nnz
        unbiased_URM_train = URM_train - self.mu
        col_nnz = np.ediff1d(URM_train.tocsc().indptr)
        self.item_bias = unbiased_URM_train.sum(axis=0) / col_nnz
        unbiased_URM_train -= self.item_bias[np.newaxis, :]
        row_nnz = np.ediff1d(URM_train.tocsr().indptr)
        self.user_bias = unbiased_URM_train.sum(axis=1) / row_nnz
    
    def recommend(self, user_id, at=5):
        # This implementation is inefficient!
        predicted_ratings = self.item_bias + mu + \
            self.user_bias[user_id]
        best_items = np.argsort(predicted_ratings)
        best_items = np.flip(best_items)
        return best_items[:at]

```

</div>
<div class="column">

</div>
</div>

---

## Content-based filtering

<div class="multiple-columns">
<div class="column">

### Building an ICM from a `DataFrame` of items

We can build an ICM starting from a `pandas.DataFrame` named `items_df` with `columns`: `["ItemID", "FeatureID"]` analogously to what we did for the URM.
In particular, we take the IDs from the items both from the `interactions_df` and the `items_df`.
```
cont_item_IDs, item_IDs = pd.factorize(
    pd.concat(interactions_df['ItemID'], items_df['ItemID'],
    ignore_index=True).unique())
item_indices = pd.Series(cont_item_IDs, index = item_IDs)
```
We can do the same for features:
```
cont_feature_IDs, feature_IDs = pd.factorize(
    items_df['FeatureID'].unique())
feature_indices = pd.Series(cont_feature_IDs, index = feature_IDs)
```
Finally, we apply the usual map in the `DataFrame`s:
```
interactions_df['ItemID'] = interactions_df['ItemID'] \
    .map(item_indices)
items_df['ItemID'] = items_df['ItemID'].map(item_indices)
items_df['FeatureID'] = items_df['FeatureID'].map(feature_indices)
```
We're ready to build the `ICM`:
```
ICM = coo_matrix(np.ones(len(items_df['ItemID'].unique())),
        (items_df['ItemID'].values, items_df['FeatureID'].values)) \
        .tocsr()
```

</div>
<div class="column">

### Computing KNN cosine similarity

Fix an item ID, a shrink term, and a value for `k`:
```
item_id = 42
shrink = 10
k = 100
```
The computation is:
```
numerator_vector = ICM[item_id] @ ICM.T
norms = (ICM ** 2).sum(axis=0).sqrt()
denominator = norms[item_id] * norms + shrink

cosine_similarity = numerator_vector / denominator
cosine_similarity[item_id] = 0.

not_KNN = np.argsort(-cosine_similarity)[k:]
cosine_similarity[not_KNN] = 0.
```
We can compute teh similarity for all the items by vectorizing the code in blocks.

### CBF recommender
```
class CBFRecommender(object):
    def fit(self, URM_train, ICM):
        self.S = cosine_similarity(ICM)
        self.URM_train = URM_train

    def recommend(self, user_id, at=5):
        user_profile = self.URM_train[user_id]
        predicted_ratings = user_profile @ self.S
        best_items = np.argsort(-predicted_ratings)
        return best_items[:at]
```

</div>
</div>

---

<div class="multiple-columns without-title">
<div class="column">

### TF-IDF

Let's see how we can compute an ICM with **TF-IDF** values.

```
n_items = ICM.shape[0]
items_per_feature = np.ediff1d(ICM.tocsc().indptr)
IDF = np.log(n_items/items_per_feature)
TF = ICM / np.ediff1d(ICM.tocsr().indptr)[np.newaxis, :]
TF_IDF_ICM = TF * IDF[:, np.newaxis]
```

</div>
<div class="column">

</div>
</div>

---

## Collaborative filtering
<div class="multiple-columns">
<div class="column">

### Item-based collaborative filtering

We can compute the similarity matrix, as we explained for content-based filtering.
```
class ItemBasedCollRecommender(object):
    def fit(self, URM_train):
        self.S = cosine_similarity(URM)
        self.URM_train = URM_train

    def recommend(self, user_id, at=5):
        user_profile = self.URM_train[user_id]
        predicted_ratings = user_profile @ self.S
        best_items = np.argsort(-predicted_ratings)
        return best_items[:at]
```

### User-based collaborative filtering
```
class ItemBasedCollRecommender(object):
    def fit(self, URM_train):
        self.S = cosine_similarity(URM.T)
        self.URM_train = URM_train

    def recommend(self, user_id, at=5):
        user_profile = self.URM_train[user_id]
        predicted_ratings = user_profile @ self.S
        best_items = np.argsort(-predicted_ratings)
        return best_items[:at]
```

</div>
<div class="column">

### SLIM
We'll provide an implementation of the routine which learns the SLIM similarity matrix.
```
def SLIM_similarity(URM_train, learning_rate=1e-6, epochs=100000,
                    reg_1=1e-3, reg_2=1e-3):
    n_items = URM_train.shape[1]
    S = np.zeros((n_items, n_items), dtype=np.float32)
    for e in range(epochs):
        sample_index = np.random.randint(URM_train.nnz)

        URM_train_coo = URM_train.tocoo()
        user_id = URM_train_coo.row[sample_index]
        item_id = URM_train_coo.col[sample_index]
        true_rating = URM_train_coo.data[sample_index]

        predicted_rating = URM_train[user_id] @ S[:, item_id]
        prediction_error = true_rating - predicted_rating

        items_in_user_profile = \
            URM_train.indices[URM_train.indptr[user_id]:\
            URM_train.indptr[user_id+1]]
        ratings_in_user_profile = URM_train[user_id,
            items_in_user_profile]
        gradient = - 2*prediction_error*ratings_in_user_profile + \
            reg_1*np.sign(S[:, items_in_user_profile].flatten()) + \
            2*reg_2*S[:, items_in_user_profile].flatten()
        S[:, items_in_user_profile] -= learning_rate * gradient

        S[item_id, item_id] = 0.

        return S
```

</div>
</div>

---

<div class="multiple-columns without-title">
<div class="column">

### Matrix factorization



</div>
<div class="column">

</div>
</div>

---

<div class="multiple-columns without-title">
<div class="column">

</div>
<div class="column">

</div>
</div>
