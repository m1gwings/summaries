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

Finally, we can build the URM in COO form using the COO constructor which takes `data, (row, column)` as parameters:
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

</div>
<div class="column">

</div>
<div class="column">

</div>
</div>

---

## Non-personalized algorithms

<div class="multiple-columns">
<div class="column">

### Top popular recommender

</div>
<div class="column">

</div>
<div class="column">

</div>
</div>

---

## Pandas

<div class="multiple-columns">
<div class="column">

- `read_csv`

- `df.columns`

- `df.head`

- `df.unique()`

- `df.factorize`

- `Series`

- `map`

- `DataFrame['column'].values`

</div>
<div class="column">

</div>
<div class="column">

</div>
</div>

---

<div class="multiple-columns">
<div class="column">

</div>
<div class="column">

</div>
<div class="column">

</div>
</div>
