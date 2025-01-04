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

- **`todense`**: allows to convert a sparse matrix to a dense one.

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
array([list([0, 2]), list([])], dtype=object)
```
while `A.data` is:
```python
array([list([1.0, 2.0]), list([])], dtype=object)
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

<div class="multiple-columns with-title">
<div class="column">

</div>
<div class="column">

</div>
<div class="column">

</div>
</div>