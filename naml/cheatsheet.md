---
marp: true
theme: cheatsheet
paginate: true
---
<style>
img {
    filter: none;
}
</style>
# NAML Cheatsheet (A. Y. 2023/2024)

## NumPy

<div class="multiple-columns with-title">
<div class="column">

### The basics

NumPy’s main object is the **homogeneous multidimensional array**. It is a table of elements, all of the same type, indexed by a tuple of non-negative integers. In NumPy dimensions are called **axes**. NumPy's array class is called **`ndarray`**, it is also known by the alias `array`.

The more important attributes of an `ndarray` are:
- **`ndim`**: the number of axes of the array;
- **`shape`**: a tuple of integers indicating the size of the array in each dimension (the length of `shape` is `ndim`);
- **`size`**: the total number of elements of the array (`size` is the product of the elements of `shape`);
- **`dtype`**: an object describing the type of the elements in the array (one can use standard Python types or the ones provided by NumPy: `numpy.int32`, `numpy.int16`, `numpy.float64`, ... ).

### Array creation

- **`array`**: creates arrays **from a regular Python list or tuple**:
```
a = np.array([1, 2, 3, 4])
```
> The value of `a` is:
```
array([1, 2, 3, 4])
```
> **Sequences of sequences become two-dimensional arrays**, sequences of sequences of sequences become three-dimensional arrays, and so on ... :
```
b = np.array([(1.5, 2, 3), (4, 5, 6)])
```

</div>
<div class="column">

> The value of `b` is:

```
array([[1.5, 2. , 3. ],
       [4. , 5. , 6. ]])
```
> **The type of the array** can also be explictly specified at creation time:
```
c = np.array([[1, 2], [3, 4]],
    dtype=complex)
```
> The value of `c` is:
```
array([[1.+0.j, 2.+0.j],
       [3.+0.j, 4.+0.j]])
```

#### Array with initial placeholder content

- **`zeros`**: creates an **array full of zeros** given its shape (and optionally type):
```
a = np.zeros((3, 4), dtype = np.float64)
```
> The value of `a` is:
```
array([[0., 0., 0., 0.],
       [0., 0., 0., 0.],
       [0., 0., 0., 0.]])
```
- **`ones`**: creates an **array full of ones** given its shape (and optionally type):
```
a = np.ones((2, 3), dtype = np.complex64)
```

</div>
<div class="column">

> The value of `a` is
```
array([[1.+0.j, 1.+0.j, 1.+0.j],
       [1.+0.j, 1.+0.j, 1.+0.j]],
       dtype=complex64)
```
- **`empty`**: creates an **array** whose **initial content** is random and **depends on the state of the memory**: 
```
a = np.empty((2, 2), dtype = np.int64)
```
> The value of `a` is:
```
array([[1, 2],
       [3, 4]])
```
> **Remark**: the **default type** for all these array creation functions is **`np.float64`**.

#### Array with sequence of numbers

- **`arange`**: it is **analogous** to the Python built-in `range`, but returns an array:
```
a = np.arange(0, 10, 2)
```
> The value of `a` is:
```
array([0, 2, 4, 6, 8])
```

- **`linspace`**: returns an array of `n` numbers evenly distributed in a segment $[a, b]$ where `n` is specified by us. In particular the first element of the returned array is $a$ and the last is $b$:

</div>
</div>

---

<div class="multiple-columns without-title">
<div class="column">

```
a = np.linspace(0, 2, 9)
```
> The value of `a` is:
```
array([0.  , 0.25, 0.5 , 0.75,
    1.  , 1.25, 1.5 , 1.75, 2.  ])
```

#### More advanced array creation

- **`meshgrid`**: makes N-D coordinate arrays for vectorized evaluations of N-D scalar/vector fields over N-D grids, given one-dimensional coordinate arrays `x1`, `x2`, ..., `xn`. This function supports both indexing convetions through the `indexing` keyword argument: giving the string `"ij"` returns a meshgrid with matrix indexing, while `"xy"` returns a meshgrid with Cartesian indexing. For example:
```
x = np.array([0, 1])
y = np.array([0, 2, 4])
xv, yv = np.meshgrid(x, y, indexing = "ij")
for i in range(x.size):
    for j in range(y.size):
        print(f'({xv[i, j]}, {yv[i, j]})')
```
> The result is:
```
(0, 0)
(0, 2)
(0, 4)
(1, 0)
(1, 2)
(1, 4)
```
> While, with _cartesian_ indexing, the value on the `y` axis is determined by the first index and the value on the `x` axis is determined by the second index:

</div>
<div class="column">

```
x = np.array([0, 1])
y = np.array([0, 2, 4])
xv, yv = np.meshgrid(x, y, indexing = "xy")
for i in range(x.size):
    for j in range(y.size):
        print(f'({xv[j, i]}, {yv[j, i]})')
```
(_The result is the same as before_).

### Printing arrays

When you print an array, NumPy displays it in a similar way to nested lists, but with the following layout:
- the **last axis** is printed from **left to right**,
- the **second-to-last axis** is printed from **top to bottom**,
- the **rest** are also printed from **top to bottom**, with each slice separated from the next by an **empty line**.

One-dimensional arrays are then printed as rows, bidimensional as matrices, and tridimensional as lists of matrices:
```
a = np.array([[[1, 2], [3, 4]],
              [[5, 6], [7, 8]]])
```
`a` is printed as:
```
array([[[1, 2],
        [3, 4]],

       [[5, 6],
        [7, 8]]])
```


### Basic operations on arrays

Most of NumPy operators on arrays **apply _elementwise_**.
For example:

</div>
<div class="column">

```
a = np.array([20, 30, 40, 50])
b = np.arange(4)
c = a + b
```
The value of `c` is:
```
array([20, 31, 42, 53])
```
The value of `b**2` is:
```
array([0, 1, 4, 9])
```

#### Broadcasting

**Broadcasting** allows NumPy's binary operations to deal in a meaningful way with inputs that do not have exactly the same shape.
- The **first rule** of broadcasting is that if all input arrays do not have the same number of dimensions, a "1" will be repeatedly prepended to the shapes of the smaller arrays until all the arrays have the same number of dimensions.
- The **second rule** of broadcasting ensures that arrays with a size of 1 along a particular dimension act as if they had the size of the array with the lalrgest shape along that dimension. The value of the array element is assumed to be the same along that dimension for the "broadcast" array.

That is:
```
a = np.zeros((2, 3))
b = np.arange(3)
```
The value of `a + b` is:

</div>
</div>

---

<div class="multiple-columns without-title">
<div class="column">

```
array([[0., 1., 2.],
       [0., 1., 2.]])
```

> **Remark**: if, after applying the first rule, the two arrays differ in the size of an axis and neither of the two is 1, then the **broadcasting fails**:
```
a = np.zeros((2, 3))
b = np.arange(2)
```
> Then `a + b` produces a **`ValueError`**.

#### Arithmetic operations

NumPy supports all the usual Python arithmetic operators, we will list some:
- **`a + b`**: returns the **elementwise sum** between `a` and `b`;
- **`a * b`**: returns the **elementwise product** between `a` and `b`;
- **`a - b`**: returns the **elementwise difference** between `a` and `b`;
- **`a / b`**: returns the **elementwise division** between `a` and `b`;
- **`a**n`** (where `n` is a number): **raises every element** of `a` to the power `n`.

#### Mathematical functions

NumPy supports all the usual mathematical functions, we will list some: `exp`, `sin`, `cos`, `sqrt`, ... .
They are all **applied _elementwise_**:
```
a = np.array([[0, 1],
              [2, 3]])
```
The value of `np.exp(a)` is:
</div>
<div class="column">

```
array([[ 1.        ,  2.71828183],
       [ 7.3890561 , 20.08553692]])
```

> **Important remark**: all the operations that we've listed so far **return new arrays**. **Some operators**, instead, **act in place to modify an existing array**, for example:
> - **`a += b`**;
> - **`a *= b`**;
> - ... .

### Arrays indexing

**One-dimensional** arrays can be indexed, sliced, and iterated over, much like `list`s and other Python sequences:
```
a = np.arange(12)
```
Then the value of `a[2]` is:
```
2
```
The value of `a[:6:2]` is:
```
array([0, 2, 4])
```

**Multidimensional** arrays can have one index (**or slice**) per axis. These **indices** are **given in a tuple spearated by commas**:
```
a = np.array([[[1, 2, 3], [4, 5, 6]],
              [[6, 5, 4], [3, 2, 1]]])
```
The value of `a[0, 1, 2]` is:

</div>
<div class="column">

```
6
```
**`a[0, :, 2]`** is a one-dimensional array with all the values of `a` in the second axis, after having fixed the value for the first and second axis to 0 and 2 respectively:
```
array([3, 6])
```
The value of `a[0, 1, :2]` is:
```
array([4, 5])
```
(_Of course we can use slicing on more than one axis_).

When **fewer indices are provided** than the number of axes, the **missing indices are considered complete slices**:
```
a = np.array([[1, 2],
              [3, 4]])
```
Then `a[-1]` is equal to `a[-1, :]`:
```
array([3, 4])
```

> **Important remark**: you can also use **indexing on arrays as a taget to assign to**:
```
a = np.array([[1, 2],
              [3, 4]])
a[:, 0] = 0
a[:, 1] = [ 11, 12 ]
```
> Then, the value of `a` is:

</div>
</div>

---

<div class="multiple-columns without-title">
<div class="column">

```
array([[ 0, 11],
       [ 0, 12]])
```

#### Advanced indexing

NumPy offers more indexing facilities than regular Python sequences. In addition to indexing by integers and slices, arrays can be indexed by arrays of integers and arrays of booleans.

##### Indexing with arrays of integers

Let's start with a **one-dimensional** array first:
```
a = np.arange(12) ** 2
b = np.array([0, 3, 7])
```

Then the value of `a[b]` is:
```
array([ 0,  9, 49])
```

If `a` is **multidimensional** instead, we can give indexes for more than one dimension. The **arrays of indices for each dimension must have the same shape**.
For example:
```
a = np.array([[0, 1, 2, 3],
              [4, 5, 6, 7],
              [8, 9, 10, 11]])
i = np.array([[0, 1],
              [1, 2]])
j = np.array([[2, 1],
              [3, 3]])
```
Then `a[i, j]` is equal to:
```
array([[ 2,  5],
       [ 7, 11]])
```

</div>
<div class="column">

We can also use arrays of indices in conjuction with slices or normal indexing:
```
a = np.array([[0, 1, 2, 3],
              [4, 5, 6, 7],
              [8, 9, 10, 11]])
b = np.array([0, 2])
```
Then, the value of `a[b, :]` is:
```
array([[ 0,  1,  2,  3],
       [ 8,  9, 10, 11]])
```

##### Indexing with arrays of booleans

To understand indexing with arrays of booleans we have to introduce the `nonzero` function:
- **`nonzero`**: returns a tuple of arrays, one for each dimension of a, containing the indices of the non-zero elements in that dimension (for boolean arrays, non-zero means `True`).
For example:
```
a = np.array([False, True, False, True])
```
> Then, the value of `a.nonzero()` is:
```
(array([1, 3]),)
```
Indexing `a` with an array of booleans `b` (which is achieved through the syntax `a[b]`), is equivalent to: `a[b.nonzero()]` which we can interpret with the "indexing with arrays of integers semantics".
For example:
```
a = np.array([[1, 2],
              [3, 4]])
```

</div>
<div class="column">

```
b = np.array([[True, False],
              [False, True]])
```
Then the value of `a[b]` is:
```
array([1, 4])
```
Indeed `b.nonzero()` is:
```
(array([0, 1]), array([0, 1]))
```
(_Of course, since indexing with arrays of booleans boils down to indexing with arrays of integers, we can use indexing with arrays of boolean together with normal indexing or slicing_).

### Aggregations on arrays

NumPy allows easily to compute the sum, minimum, maximum, ... of **all** the elements in an array through the corresponding methods: **`sum`**, **`min`**, **`max`**, ... .
For example:
```
a = np.array([[3, 4],
              [5, 8]])
```
Then, the value of `a.max()` is:
```
8
```

By specifying the **`axis` parameter** we can apply an aggregation along the specified axis of an array:
```
b = np.array([[ 0,  1,  2,  3],
              [ 4,  5,  6,  7],
              [ 8,  9, 10, 11]])
```

</div>
</div>

---

<div class="multiple-columns without-title">
<div class="column">

The value of `b.sum(axis = 0)` is the **sum of each column** of `b`:
```
array([12, 15, 18, 21])
```
while `b.sum(axis = 1)` is the **sum of each row**:
```
array([0, 4, 8])
```

More **advanced aggregation operators** are:
- **`cumsum`**: which is the cumulated sum of the array (if we don't specify an axis, multidimensional arrays are "unwinded" in one-dimensional arrays, see `ravel` in the "Shape manipulation" paragraph);
- **`mean`**: _it has straightforward semantics_.

### Shape manipulation

The **shape** of an **array can be changed** with various commands.

- **`ravel`**: returns the array, **flattened**:
```
a = np.array([[1, 2, 3],
              [4, 5, 6]])
```
> The value of `a` is:
```
array([1, 2, 3, 4, 5, 6])
```
> The order of the elements in the array resulting from `ravel` is normally "C-style", that is, the rightmost index "changes the fastest", so the element after `a[0, 0]` is `a[0, 1]`.

- **`reshape`**: returns the array **with a modifies shape**.
For example, let:
</div>
<div class="column">

```
a = np.arange(12)
```
> Then, the value of `a.reshape(3, 4)` is:
```
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11]])
```
> The new shape must have the same `size` as the old one: the array is flattened and then rebuilt with the new shape.
If a dimension is given as `-1` in a reshaping operation, it is automatically calculated:
```
a = np.arange(15)
```
> Then, the value of `a.reshape(3, -1)` is:
```
array([[ 0,  1,  2,  3,  4],
       [ 5,  6,  7,  8,  9],
       [10, 11, 12, 13, 14]])
```
> **Important remark**: both `ravel` and `reshape` **don't modify the original array**, they return a new one.

- **`newaxis`**: **increases the dimension** of an array:
```
a = np.arange(5)
```
> Then, the value of `a[:, np.newaxis]` is:
```
array([[0],
       [1],
       [2],
       [3],
       [4]])
```

</div>
<div class="column">

> (_That is, a column vector_). While, the value of `a[np.newaxis, :]` is:
```
array([[0, 1, 2, 3, 4]])
```
> (_That is, a row vector_).

### Copies

- **`copy`**: makes a **complete** (deep) copy of the array and its data:
```
a = np.arange(4).reshape(2, -1)
d = a.copy()
a[0, 0] = 42
```
> But, the value of `d` remains:
```
array([[0, 1],
       [2, 3]])
```

### Predicates on arrays

#### Atomic predicates

**Atomic predicates** on arrays, defined for example through the usual comparison operators, are **evaluated _elementwise_** and return **arrays of booleans**, _which can be used for indexing_:
```
a = np.array([[7, 11, 2],
              [3, 8, 4]])
```
The value of `a <= 5` is:
```
array([[False, False,  True],
       [ True, False,  True]])
```

</div>
</div>

---

<div class="multiple-columns without-title">
<div class="column">

All the usual comparison operators are supported: `<=`, `>=`, `==`, `!=`, `<`, `>`.

#### Compound predicates

We can compose atomic predicates into **compound predicates** through the usual **logical connectors**.
- **`logical_or`**: computes the truth value of `x1 OR x2` elementwise.
For example, let:
```
a = np.array([[7, 9, 9],
              [1, 3, 2]])
```
> Then, the value of `np.logical_or(a <= 2, a >= 9)` is:
```
array([[False,  True,  True],
       [ True, False,  True]])
```
- **`logical_and`**: computes the truth value of `x1 AND x2` elementwise.
- **`logical_not`**: computes the truth value of `NOT x` elementwise.
- **`logical_xor`**: computes the truth value of `x1 XOR x2` elementwise.

### Randomness

- **`random.seed`**: sets the seed of the NumPy random number generator. For example:
```
np.random.seed(0)
```
- **`random.uniform`**: samples an array of shape specified by the parameter `size` from a uniform distribution with lower boundary specified by the parameter `low` and upper boundary specified by the parameter `high`.

</div>
<div class="column">

> For example:
```
np.random.seed(0)
a = np.random.uniform(low = 0, high = 5,
    size = (3, 2))
```
> The value of `a` is:
```
array([[2.74406752, 3.57594683],
       [3.01381688, 2.72441591],
       [2.118274  , 3.22947057]])
```
> (_The default values for the parameters are: `size = None` (it returns just one number), `low = 0.0`, `high = 1.0`_).

- **`random.normal`**: samples an array of shape specified by the parameter `size` from a normal (gaussian) distribution with mean specified by the paramter `loc` and standard deviation specified by the paramter `scale`.
(_The default values for the parameters are: `size = None`, `loc = 0.0`, `scale = 1.0`_).

### Linear algebra

In this paragraph we will deal with bidimensional arrays which represent matrices and vectors. (_Yes, also vectors are represented by bidimensional arrays, take a look at the "Shape manipulation" paragraph, and, in particular, at the `newaxis` operator_).

#### Create matrices with a certain structure

- **`zeros`**: we've already encountered this function in the "Array creation" paragraph, it can be used to create the matrix $0_{m \times n}$.
- **`ones`**: we've already encountered this funciton in the "Array creation" paragraph, it can be used to create the matrix $1_{m \times n}$.

</div>
<div class="column">

- **`identity`**: returns the identity matrix $I_n$:
```
I_5 = np.identity(5)
```
> Then, the value of `I_5` is:
```
array([[1., 0., 0., 0., 0.],
       [0., 1., 0., 0., 0.],
       [0., 0., 1., 0., 0.],
       [0., 0., 0., 1., 0.],
       [0., 0., 0., 0., 1.]])
```
- **`diag`**: returns a diagonal matrix with the specified elements on the diagonal:
```
d = np.arange(5)
D = np.diag(d)
```
> Then, the value of `D` is:
```
array([[0, 0, 0, 0, 0],
       [0, 1, 0, 0, 0],
       [0, 0, 2, 0, 0],
       [0, 0, 0, 3, 0],
       [0, 0, 0, 0, 4]])
```

#### Linear algebra operations

- **`A @ B`**: returns the matrix product between `A` and `B`:
```
A = np.arange(16).reshape(4, 4)
B = np.ones((4, 5))
```
> Then, the value of `A @ B` is:

</div>
</div>

---

<div class="multiple-columns without-title">
<div class="column">

```
array([[ 6.,  6.,  6.,  6.,  6.],
       [22., 22., 22., 22., 22.],
       [38., 38., 38., 38., 38.],
       [54., 54., 54., 54., 54.]])
```
> (_`A @ B` is equivalent to `np.dot(A, B)`_).

- **`outer`**: computes the outer product between two vectors:
```
v = np.arange(5)[:, np.newaxis]
u = np.arange(6)[np.newaxis, :]
```
> Then, the value of `np.outer(v, u)` is:
```
array([[ 0,  0,  0,  0,  0,  0],
       [ 0,  1,  2,  3,  4,  5],
       [ 0,  2,  4,  6,  8, 10],
       [ 0,  3,  6,  9, 12, 15],
       [ 0,  4,  8, 12, 16, 20]])
```

- **`A.T`**: returns the tranpose of `A`:
```
A = np.arange(12).reshape(3, 4)
```
> Then, the value of `A.T` is:
```
array([[ 0,  4,  8],
       [ 1,  5,  9],
       [ 2,  6, 10],
       [ 3,  7, 11]])
```

#### Decompositions

- **`linalg.svd`**: returns the SVD of the matrix `A`. The boolean parameter `full_matrices` allow to choose between the full SVD and the reduced one.

</div>
<div class="column">

> In particular, it only returns 
> For example, let:
```
A = np.arange(12).reshape(4, 3)
```
> Note that `2*A[:, 1] - A[:, 0]` is:
```
array([ 2,  5,  8, 11])
```
> which corresponds to `A[:, 2]`, hence `A` is singular.
Now, let:
```
U, s, V_T = np.linalg.svd(A)
```
> Then `U.shape` is `(4, 4)`, `V_T.shape` is `(3, 3)` and `s` is:
```
array([2.24467488e+01, 1.46405850e+00,
       1.54736923e-15])
```
> (_The default value of `full_matrices` is `True`_).
To reconstruct `A` we can do the following:
```
S = np.zeros((U.shape[0], V_T.shape[0]))
for i in range(s.size):
    S[i, i] = s[i]

A_rec = U @ S @ V_T
```
> Indeed, the value of `np.round(A_rec)` is:
```
array([[ 0.,  1.,  2.],
       [ 3.,  4.,  5.],
       [ 6.,  7.,  8.],
       [ 9., 10., 11.]])
```

</div>
<div class="column">

> If we were instead to put `full_matrices` to `False`:
```
U_r, s_r, V_T_r = np.linalg.svd(A,
       full_matrices = False)
```
> then `U_r.shape` would be `(4, 3)`.

- **`linalg.qr`**: computes the QR factorization of the given matrix. The parameter `mode` allows to specify if we want the reduced form (with the value `"reduced"`), or the complete one (with the value `"complete"`).
For example:
```
A = np.arange(12).reshape(4, 3)
Q, R = np.linalg.qr(A)
```

</div>
</div>

---

## Matplotlib

<div class="multiple-columns">
<div class="column">

Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations.

### Importing

We can import Matplotlib with:
```
import matplotlib.pyplot as plt
```

### The basics

The **fundamental classes** in Matplotlib are:
- **`Artist`**: basically, everything which is visible on a Matplotlib plot is an `Artist`;
- **`Figure`**: represents the **whole** plotted figure. It keeps track of all the child `Axes`, a group of 'special' `Artist`s (titles, figure legends, colorbars, etc. ), and even nested subfigures;
- **`Axes`**: it is an `Artist` attached to a `Figure` that contains a region for plotting data, and usually includes two (or three in the case of 3D) `Axis` objects (**be aware of the difference between `Axes` and `Axis`**). Each `Axes` also has a title, an x-label, an y-label (and, in the 3D case, a z-label);
- **`Axis`**: they provide ticks and tick labels to set scales for the data in the `Axes`.

### Create a `Figure` with some `Axes`

- **`subplots`**: allows to create a `Figure` with a certain number of `Axes`. In particular:

```
fig, axes = plt.subplots()
```

<p align="center">
    <img src="http://localhost:8080/naml/static/axes.png" width="250mm" />
</p>

</div>
<div class="column">

> creates a `Figure` with a single `Axes`.
We can also create a figure with several `Axes` arranged in a "matrix-like" fashion with the `nrows` and `ncols` parameters:

```
fig, axes = plt.subplots(nrows = 2, ncols = 2)
```

<p align="center">
    <img src="http://localhost:8080/naml/static/multiple-axes.png" width="300mm" />
</p>

> in this case, `axes` is a bidimensional NumPy array, which allows us to access the `Axes` object in a certain position.
Finally we can specify the size of the figure through the `figsize` parameter which takes the width and height of the figure (in this order) in a pair (the units are inches):

```
fig, axes = plt.subplots(nrows = 2, ncols = 3, figsize = (8, 4))
```

<p align="center">
    <img src="http://localhost:8080/naml/static/figsize.png" width="350mm" />
</p>

</div>
</div>

---

<div class="multiple-columns without-title">
<div class="column">

### Plotting on a `Axes`

Plotting functions expect NumPy arrays as input, or objects that can be passed to `np.asarray`.
- **`plot`**: plots y versus x as lines and/or markers.
In particular:

```
fig, axes = plt.subplots()

y = np.arange(12) ** 2
axes.plot(y)
```

<p align="center">
    <img src="http://localhost:8080/naml/static/plot.png" width="450mm" />
</p>

> plots `y` using the index array `[0, ..., y.size - 1]` as `x`; while

```
fig, axes = plt.subplots()

x = np.linspace(0, 1, 10)
y = x ** 2
axes.plot(x, y)
```

</div>
<div class="column">

<p align="center">
    <img src="http://localhost:8080/naml/static/plot-y-vs-x.png" width="270mm" />
</p>


> plots y versus x with the given `x`.
`plot` provides several parameters to change the default plotting style:
> - `linestyle`: with values `"-"`, `"--"`, '"-."', ":", ... allows to specify the style of the line;
> - `linewidth`: allows to specify the width (in points) of the line;
> - `markersize`: allows to specify the size (in points) of marker.

> Additionally, we can use several "format strings" to specify the plotting style, for example:

```
fig, axes = plt.subplots()
x = np.linspace(0, 2 * np.pi, 20)
y = np.sin(x)

axes.plot(x, y, 'v-.')
```

<p align="center">
    <img src="http://localhost:8080/naml/static/format-strings.png" width="300mm" />
</p>

</div>
</div>

---

<div class="multiple-columns without-title">
<div class="column">

> You can find all the available format strings here: [https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html) .

- **`scatter`**: makes a scatter plot y versus x, with varying marker size and/or color:

```
fig, axes = plt.subplots()

np.random.seed(0)
n = 10
x = np.random.uniform(0, 5, n)
y = np.random.uniform(-1, 3, n)
axes.scatter(x, y)
```

<p align="center">
    <img src="http://localhost:8080/naml/static/scatter.png" width="330mm" />
</p>

> Through the `s` parameter we can change the size of the markers, `c` allows to change their color (with `cmap` we can set the color map to use):

```
fig, axes = plt.subplots()

np.random.seed(0)
n = 10
x = np.random.uniform(0, 5, n)
y = np.random.uniform(-1, 3, n)
s = (np.arange(n) + 1) * 5
c = x * y
axes.scatter(x, y, s = s, c = c)
```

</div>
<div class="column">

<p align="center">
    <img src="http://localhost:8080/naml/static/scatter-with-size-and-color.png" width="330mm" />
</p>

> Finally, the `marker` parameter allows to change the style of the marker using the same syntax of `plot`'s format strings (with only the character relative to the marker) and the `c` parameter can be used also to set a color for all the markers:

```
fig, axes = plt.subplots()

np.random.seed(0)
n = 10
x = np.random.uniform(0, 1, n)
y = np.random.uniform(0, 1, n)

axes.scatter(x, y, marker = 'v', c = 'r')
```

<p align="center">
    <img src="http://localhost:8080/naml/static/scatter-with-marker-and-color.png" width="330mm" />
</p>

</div>
</div>

---

<div class="multiple-columns without-title">
<div class="column">

- **`semilogy`**: analogous to plot, but the y axis is logarithmic. For example:

```
fig, axes = plt.subplots()

x = np.linspace(0, 1, 10)
y = np.exp(x)
axes.semilogy(x, y)
```

<p align="center">
    <img src="http://localhost:8080/naml/static/semilogy.png" width="290mm" />
</p>

- **`loglog`**: analogous to plot, but both the x and y axis are logarithmic. For example:

```
fig, axes = plt.subplots()

x = np.linspace(0, 10, 100)
y = x ** 2
axes.loglog(x, y)
```

<p align="center">
    <img src="http://localhost:8080/naml/static/loglog.png" width="290mm" />
</p>

</div>
<div class="column">

### Style `Axes`

#### Set `Axes`' title

- **`set_title`**: allows to set the title of an `Axes`:

```
fig, axes = plt.subplots()

axes.set_title("My title")
```

<p align="center">
    <img src="http://localhost:8080/naml/static/title.png" width="260mm" />
</p>

#### Add `Axes` labels

- **`set_xlabel`**: sets the label of the `Axes`. **`set_ylabel`** has analogous behavior:

```
fig, axes = plt.subplots()

axes.set_xlabel("My x label")
axes.set_ylabel("My y label")
```

<p align="center">
    <img src="http://localhost:8080/naml/static/axis-label.png" width="260mm" />
</p>

</div>
</div>

---

<div class="multiple-columns without-title">
<div class="column">

#### Add `Axes` legend

Often we want to identify lines or markers onto an `Axes`. For doing so, we can use the **`label`** parameter inside the plotting functions that we discussed earlier. Finally, we need to invoke the **`legend`** method:

```
fig, axes = plt.subplots(ncols = 2)

x = np.linspace(0, 1, 100)
y1 = x
y2 = np.exp(x)

np.random.seed(0)
u = np.random.normal(loc = 0.5, scale = 0.5, size = (20, 2))

axes[0].semilogy(x, y2, 'b-', label = '$e^x$')
axes[1].plot(x, y1, 'b-', label = '$x$')
axes[1].scatter(u[:, 0], u[:, 1], marker = '^', c = 'r',
    label = '$y_1$ vs $y_2$')

for a in axes:
    a.legend()
```

<p align="center">
    <img src="http://localhost:8080/naml/static/legend.png" width="500mm" />
</p>

</div>
<div class="column">

#### Hide `Axes`'s ticks

- **`axis`**: can be used to hide the ticks of an `Axes`:

```
fig, axes = plt.subplots()

axes.plot(np.sqrt(np.arange(100)))
axes.axis('off')
```

<p align="center">
    <img src="http://localhost:8080/naml/static/hidden-axis.png" width="400mm" />
</p>

#### Set `Axes` aspect ratio

- **`axis`**: can be used to set the aspect ratio of an `Axes` to 1:1 :

```
fig, axes = plt.subplots()

theta = np.linspace(0, 2*np.pi, 100)
x = np.cos(theta)
y = np.sin(theta)

axes.plot(x, y, 'r:')
axes.axis('equal')
```

</div>
</div>

---

<div class="multiple-columns without-title">
<div class="column">

<p align="center">
    <img src="http://localhost:8080/naml/static/1-1-aspect-ratio.png" width="250mm" />
</p>

### More advanced stuff

#### 3D scatterplot

When performing a 3D plot we need to create a `Figure` and add an `Axes` to it in two separate phases. When we add the `Axes` object, the `projection` parameter of the `add_subplot` method allows to specify that we want a 3D plot:

```
fig = plt.figure()
axes = fig.add_subplot(projection = '3d')

np.random.seed(0)
u = np.random.normal(size = (100, 3))
axes.scatter(u[:, 0], u[:, 1], u[:, 2], marker = 'v',
             c = u[:, 0] * u[:, 1] * u[:, 2], s = np.max(u, axis = 1) * 10)
```

<p align="center">
    <img src="http://localhost:8080/naml/static/3d-scatter.png" width="270mm" />
</p>

</div>
<div class="column">

Through the **`view_init`** method, we can move the virtual camera which produces the 3D plot: the `elev` parameter allows to specify the elevation angle in degrees which rotates the camera above the plane pierced by the vertical axis, the `azim` parameter allows to specify the angle in degrees which rotates the camera about the vertical axis, finally the `roll` parameter allows to specify the angle in degrees which rotates the camera about the viewing axis:

```
fig = plt.figure()
axes = fig.add_subplot(projection = '3d')

np.random.seed(0)
u = np.random.normal(size = (100, 3))
axes.scatter(u[:, 0], u[:, 1], u[:, 2], marker = 'v',
             c = u[:, 0] * u[:, 1] * u[:, 2],
             s = np.max(u, axis = 1) * 10)
axes.view_init(45, 45, 0)
```

<p align="center">
    <img src="http://localhost:8080/naml/static/3d-scatter-different-view.png" width="270mm" />
</p>

#### Plotting shapes

##### Plotting circles

We can create a `Circle` `Patch` through the constructor provided in the `patches` package. Then we can add it to the `Axes` through the **`add_patch`** method (_when plotting circles, remember to set the aspect ration of the `Axes` to 1:1_):

</div>
</div>

---

<div class="multiple-columns without-title">
<div class="column">

```
fig, axes = plt.subplots()

import matplotlib.patches as patches

np.random.seed(0)
n = 20
r = np.random.uniform(1, 6, n) / 100
c = np.random.uniform(size = (n, 2))

for i in range(n):
    axes.add_patch(patches.Circle(c[i, :], radius = r[i],
                                  color = 'r', alpha = 0.5))

axes.axis('equal')
```

<p align="center">
    <img src="http://localhost:8080/naml/static/circles.png" width="450mm" />
</p>

##### Plotting vectors

- **`arrow`**: allows to plot a vector (an arrow), the parameters `x` and `y` specify the coordinates of the arrow base, the `dx` and `dy` parameters specify the length of the arrow along `x` and `y` direction.

</div>
<div class="column">

```
fig, axes = plt.subplots()

axes.arrow(0, 1, 1, -1,
           head_width = 0.05, head_length = 0.05,
           length_includes_head = True,
           color = 'r')
axes.arrow(1, 0, 1, 1,
           head_width = 0.05, head_length = 0.05,
           length_includes_head = True,
           color = 'b')
```

<p align="center">
    <img src="http://localhost:8080/naml/static/arrows.png" width="450mm" />
</p>

#### Plotting images

- **`imread`**: allows to read an image into a three-dimensional NumPy array. To each pixel correspond three values to represent its color with RGB encoding.

```
A_RGB = plt.imread("colorful-image.jpg")
```

- **`imshow`**: allows to plot images onto an `Axes`. The `cmap` parameter allows us to plot the image in gray scale.

</div>
</div>

---

<div class="multiple-columns without-title">
<div class="column">

```
A = A_RGB.mean(axis = 2)

fig, axes = plt.subplots()

axes.imshow(A, cmap = "gray")
axes.axis('off')
```

<p align="center">
    <img src="http://localhost:8080/naml/static/image.png" width="450mm" />
</p>

</div>
<div class="column">

#### Add colorbar

- **`colorbar`**: allows to add a color bar for a certain plot on an `Axes`. For example, it can add colorbars to images:

```
A_RGB = plt.imread("colorful-image.jpg")

fig, axes = plt.subplots()
img = axes.imshow(A_RGB)
axes.axis('off')

fig.colorbar(img, ax = axes)
```

<p align="center">
    <img src="http://localhost:8080/naml/static/colorbar.png" width="450mm" />
</p>

</div>
</div>

---

<div class="multiple-columns without-title">
<div class="column">



</div>
<div class="column">



</div>
</div>